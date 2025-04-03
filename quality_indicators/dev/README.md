# RS Quality indicators metadata schema
- Version: 0.0.2
- Identifier: https://w3id.org/everse/rsqi#
- Version identifier: https://w3id.org/everse/rsqi/0.0.2
- Date: April 3rd, 2025
- Author: Daniel Garijo, Faruk Biden, Thomas Vuillaume, EVERSE Consortium


A repository to describe the RS quality indicators used in the EVERSE project, as well as a template for the RSQKit.

Namespaces used in this document:

| Namespace prefix | Namespace URI |
|---|---|
|dcat|[http://www.w3.org/ns/dcat#](http://www.w3.org/ns/dcat#)|
|dcterms|[http://purl.org/dc/terms/](http://purl.org/dc/terms/)|
|ftr|[https://w3id.org/ftr#](https://w3id.org/ftr#)|
|dqv|[http://www.w3.org/ns/dqv#](http://www.w3.org/ns/dqv#)|
|vcard|[http://www.w3.org/2006/vcard/ns#](http://www.w3.org/2006/vcard/ns#)|
|rsqd|[https://w3id.org/everse/rsqd#](https://w3id.org/everse/rsqd#)|

### Definitions
#### Research Software Indicator
A software quality indicator represents a specific aspect software that can be measured (e.g., FAIRness, test coverage, documentation coverage, etc.)

This definition is inspired by the W3C Data Quality Vocabulary (https://www.w3.org/TR/vocab-dqv/#dqv:Dimension), where a “metric” reads as “Represents a standard to measure a quality dimension".

The figure below show an example on how indicators and dimensions are related to each other:
![overview indicators](img/overview.png)

In the example, let's assume we have a tool `howFairIs` (taken as an illustrative example) that measures two indicators, one about licenses being present in a repository, and another one about software metadata. Both indicators would be associated with their respective quality dimension (`R1.1` and `F2` respectively), which in this case are part of another higher level quality dimension (`FAIRness`).

The following metadata attributes define a Research Software Quality indicator:

| Attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|
| Contact (person or organization) for the indicator | contact | dcat:contactPoint | [schema:Person](https://schema.org/Person) or [schema:Organization](https://schema.org/Organization) |
| Author | author | schema:author | [schema:Person](https://schema.org/Person) or [schema:Organization](https://schema.org/Organization) |
| Creation date | created | schema:dateCreated | [schema:DateTime](https://schema.org/DateTime) (String) |
| Name of the indicator | name | schema:name | [schema:Text](https://schema.org/Text) (String)|
| Description | description | schema:description | schema:Text (String)|
| Indicator Status (active, deprecated, etc.) | status | [schema:creativeWorkStatus](https://schema.org/creativeWorkStatus) | xsd:Literal (String)|
| Keywords | keywords | schema:keywords | rdfs:Literal (String)|
| RS Quality Dimension  | qualityDimension | dqv:inDimension | rsqd:SoftwareQualityDimension (URL) |
| RS Quality Indicator Identifier | identifier | schema:identifier | rdfs:Literal (String) |
| Source (e.g., standard/tool where it came from) | source | dcterms:source | xsd:anyURI (URL) |
| Version | version | [schema:version](https://schema.org/version) | [schema:Text](https://schema.org/Text) (String)|

The indicator `description` should address:
```
### What is being measured?
    Explain what you are measuring
### Why should we measure it?
    Explain why
### What must be provided for the measurement? 
    For example, a zenodo record, or a GitHub id.
### How is the measurement executed?
    Explain the exact process for assessing the indicator
### What is/are considered valid result(s)?
    What outcomes are pass/fail
```

To see an example of an indicator, see [the template YAML file](./indicators_template.yaml) stored in this repository.

The latest version of the vocabulary is accessible at [https://w3id.org/everse/rsqi](https://w3id.org/everse/rsqi)

To obtain the JSON-LD context, just perform content negotiation as follows:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqi
```

The vocabulary has versioning enabled. To get a particular version add the version number in the URL:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqi/0.0.1
```

