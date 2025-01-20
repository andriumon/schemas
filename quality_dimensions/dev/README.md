# RS Quality dimensions
- Version: 0.0.1
- Identifier: https://w3id.org/everse/rsqd#
- Version identifier: https://w3id.org/everse/rsqd/0.0.1
- Date: Dect 17th, 2024

This repository describes the RS quality dimensions used in the EVERSE project.

Namespaces used in this document:

| Namespace prefix | Namespace URI |
|---|---|
|schema|[http://schema.org/](http://schema.org/)| 
|dcterms|[http://purl.org/dc/terms/](http://purl.org/dc/terms/)|

The following metadata attributes define a Research Quality dimension:

| Attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|
|persistent identifier|identifier|schema:identifier|schema:Text (String)|
|Dimension name|name|schema:name|schema:Text (String)|
|Brief description|description|schema:description|schema:Text (String)|
|definition source|source|dcterms:source|rdfs:Literal (URL)|

To see an example of a dimension, see [the template YAML file](dimensions_template.yaml) stored in this repository.

The latest version of the vocabulary is accessible at [https://w3id.org/everse/rsqd](https://w3id.org/everse/rsqd)

To obtain the JSON-LD context, just perform content negotiation as follows:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqd
```

The vocabulary has versioning enabled. To get a particular version add the version number in the URL:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqd/0.0.1
```