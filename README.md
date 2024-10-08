# RS Quality indicators
A repository to describe the RS quality indicators used in the EVERSE project.

RS Quality indicators should be described in both machine-readable and human-readable manner, following the template below:

| RS Quality attribute | Key (YAML) | Term (mapping) | Expected value |
|---|---|---|---|
| RS Quality Indicator Identifier | identifier | dcterms:identifier | String |
| Contact (person or organization) | contactPoint | dcat:contactPoint | Person/Organization (URL) |
| Name of the indicator | title | dcterms:title | String |
| Description | description | dcterms:description | String |
| Keywords | keyword | dcat:keyword | String |
| RS Quality Dimension  | inDimension | dqv:inDimension | URL (category) |
| Version | version | dcat:version | String |
| Source (e.g., standard/tool where it came from) | source | dcterms:source | URL |

The term (mapping) will be used to create a machine-readable version in JSON-LD, following the YAML template provided in the repository.

