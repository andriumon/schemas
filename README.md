# EVERSE schemas

This repository contains JSON schemas for the EVERSE project

> [!NOTE]
> This is a work in progress. The schemas of this repository will eventually be merged with [RSQuality_indicators](https://github.com/EVERSE-ResearchSoftware/RSQuality_indicators).


## Current compliance with [RSQuality_indicators](https://github.com/EVERSE-ResearchSoftware/RSQuality_indicators)

|Status| RS Quality attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|---|
| &check; | RS Quality Indicator Identifier | identifier | dcterms:identifier | String |
| &cross; | Contact (person or organization) | contactPoint | dcat:contactPoint | Person/Organization (URL) |
| &check; | Name of the indicator | title | dcterms:title | String |
| &check; | Description | description | dcterms:description | String |
| &cross; | Keywords | keyword | dcat:keyword | String |
| &cross; | RS Quality Dimension  | inDimension | dqv:inDimension | URL (category) |
| &check; | Version | version | dcat:version | String |
| &cross; | Source (e.g., standard/tool where it came from) | source | dcterms:source | URL |


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
