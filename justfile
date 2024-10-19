check:
  @echo "🚀 Checking lock file consistency with 'pyproject.toml'"
  @uv lock --locked
  @echo "🚀 Static type checking: Running pyright"
  @uv run pyright
  @echo "🚀 Checking for obsolete dependencies: Running deptry"
  @uv run deptry src

test:
  @echo "🚀 Testing code: Running pytest"
  @uv run python -m pytest --cov --cov-config=pyproject.toml

examples: examples-alp examples-boiler examples-coffee_machine examples-failure_time_prediction examples-linear_data examples-one_tank examples-ros_offline

examples-alp:
  uv run --directory ./examples/automatic_lashing_platform/ --with-editable ../../ run.py

examples-boiler:
  uv run --directory ./examples/boiler/ --with-editable ../../ run.py

examples-coffee_machine:
  uv run --directory ./examples/coffee_machine/ --with-editable ../../ run.py

examples-failure_time_prediction:
  uv run --directory ./examples/failure_time_prediction/ --with-editable ../../ run.py

examples-linear_data:
  uv run --directory ./examples/linear_data/ --with-editable ../../ run.py

examples-one_tank:
  uv run --directory ./examples/one_tank/ --with-editable ../../ run.py

examples-ros_offline:
  uv run --directory ./examples/ros_offline/ --with-editable ../../ run.py
