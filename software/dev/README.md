# EVERSE Research Software metadata schema
- Version: 0.0.1
- Identifier: https://w3id.org/everse/rs#
- Version identifier: https://w3id.org/everse/rs/0.0.1
- Date: Jan 20th, 2025


A repository to describe the Research Software metadata, for the tools described within the EVERSE project.
This metadata schema relies heavily on [CodeMeta](https://codemeta.github.io/terms/) and [Schema.org](http://schema.org/)), extending them when needed to 
acommodate the project needs. The requirements for this vocabulary come from the D3.1 (Technology Watch) and
the RSQKit collection of tools.

Namespaces used in this document:

| Namespace prefix | Namespace URI |
|---|---|
|schema|[http://schema.org/](http://schema.org/)|
|codemeta|[https://codemeta.github.io/terms/](https://codemeta.github.io/terms/)|
|rsqd|[https://w3id.org/everse/rsqd#](https://w3id.org/everse/rsqd#)|
|rsqi|[https://w3id.org/everse/rsqi#](https://w3id.org/everse/rsqi#)|
|rs|[https://w3id.org/everse/rs#](https://w3id.org/everse/rs#)|

The following attributes describe a RS tool (please note that not all are mandatory): 

| Attribute | Vocabulary term | Expected value |
|---|---|---|
| Application category | schema:applicationCategory | rsqd:SoftwareQualityDimension (URL) |
| Applies to Programming language | rs:appliesToProgrammingLanguage | schema:Text (string)|
| Author | schema:author | schema:Person or schema:Organization (URL) |
| Description | schema:description | schema:Text (string)|
| How to use the tool? (service, CI/CD, etc.) | rs:howToUse | schema:URL (string)|
| Name of the tool | schema:name | schema:Text (string)|
| Identifier | schema:identifier | schema:URL (string)|
| Is accessible for free? | schema:isAccessibleForFree | schema:Boolean|
| Quality indicator(s) the tool addresses | rs:hasQualityIndicator | schema:Text (string)|
| Quality dimension(s) the tool addresses | schema:hasQualityDimension | schema:Text (string)|
| License | schema:license | schema:License (URL)|
| Maintainer | codemeta:maintainer | schema:URL (string)|
| URL | schema:url | schema:URL (string)|
| Cluster/Community using the tool | rs:usedBy | schema:Text (string)|



The type of appplications categories recognized are:
- `AnalysisCode`: Software tier type used to categorize scripts and tools designed to support a research publication or investigation, with a low level of maturity
- `PrototypeTool`: Software tier type used to categorize tools designed to support a research publication or investigation that have reached a level of maturity and reuse among the community
- `ResearchInfrastructureSoftware`: Software tier type used to categorize mature tools that are used by one or several Research Infrastructures and/or science communities

Each of the categories have an identifier: `https://w3id.org/everse/rs#{id}` where the id is one of the keys used in the list above (e.g., `https://w3id.org/everse/rs#PrototypeTool`)

The dimensions recognized so far are:
- `FAIRness`: Quality dimension related to the compliance of a software tool with the Findable, Accessible, Interoperable and Reusable (FAIR) principles.
- `Sustainability`: Quality dimension related to the compliance of a software tool with aspects related to Functional sustainability, Reproducibility, Long-term usability, Portability, Maintainability, Documentation, Usability, Code analysis, Security, Community and Resource efficiency. 
- `Openness`: Quality dimension related to the compliance of a software tool with best practices for Open Source.

Each of the dimensions have an identifier: `https://w3id.org/everse/rs#{id}` where the id is one of the keys used in the list above (e.g., `https://w3id.org/everse/rs#FAIRness`)


To see an example of a tool, see [the example JSON-LD file](./example.json) in this repository.

The latest version of the vocabulary is accessible at [https://w3id.org/everse/rs](https://w3id.org/everse/rs).

To obtain the JSON-LD context, just perform content negotiation as follows:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rs
```

The vocabulary has versioning enabled. To get a particular version add the version number in the URL:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rs/0.0.1
```

