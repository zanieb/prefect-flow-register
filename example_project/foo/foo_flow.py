from prefect import Flow, Parameter

from example_project.tasks.math import add_some_numbers


with Flow("foo") as flow:
    x = Parameter("x", 3)
    y = Parameter("y", 10)
    add_some_numbers(x, y)
