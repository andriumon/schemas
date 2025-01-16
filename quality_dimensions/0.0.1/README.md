# RS Quality dimensions
- Version: 0.0.1
- Identifier: https://w3id.org/everse/rsqd#
- Version identifier: https://w3id.org/everse/rsqd/0.0.1
- Date: Dect 17th, 2024

This repository describes the RS quality dimensions used in the EVERSE project.

Namespaces used in this document:

| Namespace prefix | Namespace URI |
|---|---|
|dcterms|[http://purl.org/dc/terms/](http://purl.org/dc/terms/)|

The following metadata attributes define a Research Quality dimension:

| Attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|
|persistent identifier|identifier|dcterms:identifier|rdfs:Literal (String)|
|Dimension name|name|dcterms:title|rdfs:Literal (String)|
|Brief description|description|dcterms:description|rdfs:Literal (String)|
|definition source|source|dcterms:source|rdfs:Literal (URL)|

To see an example of a dimension, see [the template YAML file](dimensions_template.yaml) stored in this repository.