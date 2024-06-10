# Use Case

The three main use cases in the AGenC research project will be described in the following sections.

## Data-Driven Monitoring for Autonomous Mobile Robots

Mobile robots and autonomous vehicles are key technological developments in logistics that can significantly improve the efficiency, cost reduction and flexibility of production and logistics processes. The autonomous navigation of these vehicles depends largely on reliable localization systems. Various environmental influences such as uneven ground, dust, direct sunlight or extreme weather conditions can disrupt localization systems and jeopardize process reliability.

Data-driven monitoring software is to be developed and evaluated using Flowcean in order to detect and monitor these faults. The aim is to control the localization quality during operation, identify errors and make adjustments to ensure the safety and efficiency of the robots. This includes the collection of relevant environmental data, the creation of models to estimate the uncertainty of the robot pose and the use of synthetic and real sensor data for modeling. The models are validated experimentally to ensure their transferability to real application scenarios.


## Monitoring for Energy Systems

With an increasing number of volatile participants, like photovoltaic, wind energy, or electric vehicles, operating the power grid becomes more and more challenging.
Keeping the voltage level within the allowed limits requires manual effort by operators, which mostly decide based on experience, what actions to take.
Those include changing the position of switches, increasing or descreasing the amount of generation or load from a few controllable units or using the tap changer.
In the worst case, some units or parts of the grid have to be disconnected but, generally, this is a situation that is to be avoided.

Monitoring the state of the power grid with AI can help the operator to keep an overview what is going on in the power grid.
With Flowcean, an Reinforcement Learning agent will be developed that utilizes a power grid simulation to monitor the power grid state.
The future actions of the RL agent will be used as recommmendations for an operator.
The operator can decide which of those actions will be applied.
With those information, the power grid environment of the agent can be updated and the process repeated.