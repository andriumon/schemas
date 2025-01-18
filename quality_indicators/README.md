# RS Quality indicators

This repository describes the RS quality indicators vocabulary used in the EVERSE project, in a machine-readable manner.

The `dev` folder contains the latest version under development of the vocabulary.

The folders with numbers refer to the the different available releases.

The latest version of the vocabulary is accessible at [https://w3id.org/everse/rsqi](https://w3id.org/everse/rsqi)

To obtain the JSON-LD context, just perform content negotiation as follows:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqi
```

The vocabulary has versioning enabled. To get a particular version add the version number in the URL:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqi/0.0.1
```