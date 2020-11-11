from prefect import task


@task
def add_some_numbers(a, b):
    return a + b