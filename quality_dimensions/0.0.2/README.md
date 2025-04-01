# RS Quality dimensions
- Version: 0.0.2
- Identifier: https://w3id.org/everse/rsqd#
- Version identifier: https://w3id.org/everse/rsqd/0.0.2
- Previus version: https://w3id.org/everse/rsqd/0.0.1
- Date: April 1st, 2025
- Author: Daniel Garijo, Thomas Vuillaume, EVERSE Consortium

This repository describes the RS quality dimensions used in the EVERSE project.

Namespaces used in this document:

| Namespace prefix | Namespace URI |
|---|---|
|schema|[http://schema.org/](http://schema.org/)| 
|dcterms|[http://purl.org/dc/terms/](http://purl.org/dc/terms/)|

### Definitions
#### Research Software Quality Dimension
A research software quality dimension represents criteria relevant for assessing software quality (e.g., Documentation, Performance, etc.). Each quality dimension must have one or more indicator to measure it. Dimensions may be defined in a hierarchy.

This definition inspired by W3C Data Quality Vocabulary (https://www.w3.org/TR/vocab-dqv/#dqv:Dimension) 

The following metadata attributes define a Research Software Quality dimension:

| Attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|
|Persistent identifier |identifier|schema:identifier|schema:Text (String)|
|Name|name|schema:name|schema:Text (String)|
|Brief description|description|schema:description|schema:Text (String)|
|Definition source (in case the quality dimension is defined elsewhere, e.g., ISO standard)|source|dcterms:source|schema:URL|

To see an example of a dimension, see the [JSON file](example.json) or the [the YAML file](example.yaml) stored in this repository.

The latest version of the vocabulary is accessible at [https://w3id.org/everse/rsqd](https://w3id.org/everse/rsqd)

To obtain the JSON-LD context, just perform content negotiation as follows:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqd
```

The vocabulary has versioning enabled. To get a particular version add the version number in the URL:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqd/0.0.2
```