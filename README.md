# EVERSE schemas
<!-- Styling related -->
<style>
    r { color: Red }
    o { color: Orange }
    g { color: Green }
</style>
<!-- -->

This repository contains JSON schemas for the EVERSE project

> [!NOTE]
> This is a work in progress. The schemas of this repository will eventually be merged with [RSQuality_indicators](https://github.com/EVERSE-ResearchSoftware/RSQuality_indicators).


## Current compliance with [RSQuality_indicators](https://github.com/EVERSE-ResearchSoftware/RSQuality_indicators)

|Status| RS Quality attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|---|
| <g>&check;</g> | RS Quality Indicator Identifier | identifier | dcterms:identifier | String |
| <r>&cross;</r> | Contact (person or organization) | contactPoint | dcat:contactPoint | Person/Organization (URL) |
| <g>&check;</g> | Name of the indicator | title | dcterms:title | String |
| <g>&check;</g> | Description | description | dcterms:description | String |
| <r>&cross;</r> | Keywords | keyword | dcat:keyword | String |
| <r>&cross;</r> | RS Quality Dimension  | inDimension | dqv:inDimension | URL (category) |
| <g>&check;</g> | Version | version | dcat:version | String |
| <r>&cross;</r> | Source (e.g., standard/tool where it came from) | source | dcterms:source | URL |


## Project setup

Below is the list of the files and the top-level folders.

```
|-- .github
|-- .gitignore
|-- .pre-commit-config.yaml
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- examples
|-- generate_yaml.py
|-- schemas
|-- static
`-- tests
```

**.github:** CI workflows to validate the schemas and update the github.io page

**examples:** examples using the schemas

**schemas:** the JSON schemas

**static:** automatically generated files of the

**tests:** tests for the schemas and the examples


## Developer notes

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
