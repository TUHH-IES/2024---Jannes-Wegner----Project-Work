import os
import platform
from typing import TYPE_CHECKING, Any

import lightning
import polars as pl
import torch
from lightning.pytorch.callbacks.early_stopping import EarlyStopping
from torch import Tensor
from torch.optim.adam import Adam
from torch.utils.data import DataLoader
from typing_extensions import override

from flowcean.core import SupervisedLearner

from .dataset import TorchDataset
from .model import PyTorchModel

if TYPE_CHECKING:
    from torch.nn import Module


class LightningLearner(SupervisedLearner):
    """A learner that uses PyTorch Lightning."""

    def __init__(
        self,
        module: lightning.LightningModule,
        num_workers: int | None = None,
        batch_size: int = 32,
        max_epochs: int = 100,
        accelerator: str = "auto",
    ) -> None:
        """Initialize the learner.

        Args:
            module: The PyTorch Lightning module.
            num_workers: The number of workers to use for the DataLoader.
            batch_size: The batch size to use for training.
            max_epochs: The maximum number of epochs to train for.
            accelerator: The accelerator to use.
        """
        self.module = module
        self.num_workers = num_workers or os.cpu_count() or 0
        self.max_epochs = max_epochs
        self.batch_size = batch_size
        self.optimizer = None
        self.accelerator = accelerator

    @override
    def learn(
        self,
        inputs: pl.LazyFrame,
        outputs: pl.LazyFrame,
    ) -> PyTorchModel:
        dfs = pl.collect_all([inputs, outputs])
        collected_inputs = dfs[0]
        collected_outputs = dfs[1]
        dataset = TorchDataset(collected_inputs, collected_outputs)
        dataloader = DataLoader(
            dataset,
            batch_size=self.batch_size,
            num_workers=self.num_workers,
            persistent_workers=platform.system() == "Windows",
        )
        trainer = lightning.Trainer(
            accelerator=self.accelerator,
            max_epochs=self.max_epochs,
            callbacks=[
                EarlyStopping(
                    monitor="train_loss",
                    patience=10,
                    mode="min",
                ),
            ],
        )
        trainer.fit(self.module, dataloader)
        return PyTorchModel(self.module, collected_outputs.columns)


class MultilayerPerceptron(lightning.LightningModule):
    """A multilayer perceptron."""

    def __init__(
        self,
        learning_rate: float,
        input_size: int,
        output_size: int,
        hidden_dimensions: list[int] | None = None,
        *,
        activation_function: type[torch.nn.Module] | None = None,
    ) -> None:
        """Initialize the model.

        Args:
            learning_rate: The learning rate.
            input_size: The size of the input.
            output_size: The size of the output.
            hidden_dimensions: The dimensions of the hidden layers.
            activation_function: The activation function to use.
                Defaults to ReLU if not provided.
        """
        super().__init__()
        if hidden_dimensions is None:
            hidden_dimensions = []
        self.save_hyperparameters()
        self.learning_rate = learning_rate

        layers: list[Module] = []
        hidden_size = input_size
        for dimension in hidden_dimensions:
            layers.extend(
                (
                    torch.nn.Linear(hidden_size, dimension),
                    activation_function()
                    if activation_function
                    else torch.nn.ReLU(),
                ),
            )
            hidden_size = dimension
        layers.append(torch.nn.Linear(hidden_size, output_size))
        self.model = torch.nn.Sequential(*layers)

    @override
    def forward(self, *args: Any, **kwargs: Any) -> Tensor:
        y: Tensor = self.model(*args, **kwargs)
        return y

    @override
    def training_step(self, batch: Any) -> Tensor:
        inputs, targets = batch
        outputs = self(inputs)
        loss = torch.nn.functional.mse_loss(outputs, targets)
        self.log(
            "train_loss",
            loss,
            prog_bar=True,
        )
        return loss

    @override
    def configure_optimizers(self) -> Any:
        optimizer = Adam(
            self.parameters(),
            lr=self.learning_rate,
        )
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer,
            T_max=40,
        )
        return {
            "optimizer": optimizer,
            "lr_scheduler": scheduler,
        }
