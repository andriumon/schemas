# RS Quality dimensions

This repository describes the RS quality dimensions vocabulary used in the EVERSE project, in a machine-readable manner.

The `dev` folder contains the latest version under development of the vocabulary.

The folders with numbers refer to the the different available releases.

The latest version of the vocabulary is accessible at [https://w3id.org/everse/rsqd](https://w3id.org/everse/rsqd)

To obtain the JSON-LD context, just perform content negotiation as follows:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqd
```

The vocabulary has versioning enabled. To get a particular version add the version number in the URL:

```
curl -sH "accept:application/ld+json" -L https://w3id.org/everse/rsqd/0.0.1
```