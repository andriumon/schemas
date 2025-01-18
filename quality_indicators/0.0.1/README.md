# RS Quality indicators metadata schema
- Version: 0.0.1
- Identifier: https://w3id.org/everse/rsqi#
- Version identifier: https://w3id.org/everse/rsqi/0.0.1
- Date: Dect 17th, 2024


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


RS Quality indicators should be described in both machine-readable and human-readable manner, following the template below:

| Attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|
| Contact (person or organization) | contact | dcat:contactPoint | vcard:Kind (vcard:Individual or vcard:Organization) |
| Creation date | created | dcterms:created | rdfs:Literal (String) |
| Name of the indicator | name | dcterms:title | rdfs:Literal (String)|
| Description | description | dcterms:description | rdfs:Literal (String)|
| Indicator Status | status | ftr:status | xsd:Literal (String)|
| Keywords | keywords | dcat:keyword | rdfs:Literal (String)|
| RS Quality Dimension  | qualityDimension | dqv:inDimension | rsqd:SoftwareQualityDimension (URL) |
| RS Quality Indicator Identifier | identifier | dcterms:identifier | rdfs:Literal (String) |
| Source (e.g., standard/tool where it came from) | source | dcterms:source | xsd:anyURI (URL) |
| Version | version | dcat:version | String (String)|

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

