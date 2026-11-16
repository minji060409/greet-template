"""{{ cookiecutter.package_description }}."""


def greet(name: str) -> str:
    name = name.strip() or "world"
    return f"Hello, {name}!"

