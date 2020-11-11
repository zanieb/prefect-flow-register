from example_project.bar.bar_flow import flow as bar_flow
from example_project.foo.foo_flow import flow as foo_flow


PROJECT = "example"

bar_flow.register(project_name=PROJECT)
foo_flow.register(project_name=PROJECT)