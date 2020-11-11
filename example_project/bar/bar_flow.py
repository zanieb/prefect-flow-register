from prefect import Flow, Parameter

from example_project.tasks.math import add_some_numbers


with Flow("bar") as flow:
    x = Parameter("x", 1)
    y = Parameter("y", 3)
    add_some_numbers(x, y)

