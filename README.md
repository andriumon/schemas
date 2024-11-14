# EVERSE schemas

This repository contains JSON schemas for the EVERSE project

> [!NOTE]
> This is a work in progress. The schemas of this repository will eventually be merged with <https://github.com/EVERSE-ResearchSoftware/RSQuality_indicators>.


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

To test the schemas after changes:

```
pytest
```


## Remove the virtualenv and clear the cache

```
pipenv --rm
pipenv --clear
```


## Useful links

- https://json-schema.org
