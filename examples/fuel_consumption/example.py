import logging

import flowcean.util
from flowcean.environments.csv import CsvDataLoader
from flowcean.environments.train_test_split import TrainTestSplit
from flowcean.learners.regression_tree import RegressionTree
from flowcean.metrics.evaluate import evaluate
from flowcean.metrics.regression import MeanAbsoluteError, MeanSquaredError
from flowcean.strategies.offline import learn_offline


logger = logging.getLogger(__name__)

flowcean.util.initialize_logging()

environment = CsvDataLoader("data.csv")
environment.load()
stream = environment.as_stream(batch_size=10)

train, test = TrainTestSplit(
    ratio=0.8,
    shuffle=True,
    seed=42,
).split(environment)

learner = RegressionTree(
    dot_graph_export_path="graph.dot",
    max_depth=2,
    random_state=42,
)

inputs = ["Cylinders", "Displacement", "Weight"]
outputs = ["MPG"]

model = learn_offline(
    train,
    learner,
    inputs,
    outputs,
)

report = evaluate(
    model,
    test,
    inputs,
    outputs,
    [MeanAbsoluteError(), MeanSquaredError()],
)
print(report)
