# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development

```bash
python -m pip install -e .
```

## Run the tests

```bash
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```

Output:
Hello, Hee!

## Send a change

- Create a branch from main and commit.
- Push branch and open a PR to main.