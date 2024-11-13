# EVERSE schemas

This repository contains JSON schemas for the EVERSE project

## Setup

Install `pipenv`:

```
python -m pip install --upgrade pipenv wheel
```

Install the dependencies:

```
pipenv install --system --deploy --dev
```

Install `pre-commit`:

```
pre-commit install
```

To test the schemas run:

```
pytest
```