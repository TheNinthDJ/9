---
annotations_creators:
- no-annotation
language_creators:
- found
languages:
- en
licenses:
- other-my-license
multilinguality:
- monolingual
pretty_name: pile-of-law
size_categories:
- 10M<n<100M
source_datasets: []
task_categories:
- fill-mask
task_ids:
- masked-language-modeling
---

# Dataset Card for Pile of Law

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
  - [Annotations](#annotations)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

## Dataset Description

- **Homepage:** https://huggingface.co/datasets/pile-of-law/pile-of-law
- **Repository:** https://huggingface.co/datasets/pile-of-law/pile-of-law
- **Paper:** TBD

### Dataset Summary

We curate a large corpus of legal and administrative data. The utility of this data is twofold: (1) to aggregate legal and administrative data sources that demonstrate different norms and legal standards for data filtering; (2) to collect a dataset that can be used in the future for pretraining legal-domain language models, a key direction in access-to-justice initiatives.

### Supported Tasks and Leaderboards

This is meant as an analysis corpus, but may be used for masked language model pretraining.

### Languages

English

## Dataset Structure

### Data Instances

[More Information Needed]

### Data Fields

- text: the document text
- created_timestamp: If the original source provided a timestamp when the document was created we provide this as well. Note, these may be inaccurate. For example CourtListener case opinions provide the timestamp of when it was uploaded to CourtListener not when the opinion was published. We welcome pull requests to correct this field if such inaccuracies are discovered.
- downloaded_timestamp: When the document was scraped.
- url: the source url

### Data Splits

There is a train/validation split for each subset of the data. 75%/25%

## Dataset Creation

### Curation Rationale

[More Information Needed]

### Source Data

#### Initial Data Collection and Normalization

[More Information Needed]

#### Who are the source language producers?

[More Information Needed]

### Personal and Sensitive Information

[More Information Needed]

## Considerations for Using the Data

### Social Impact of Dataset

[More Information Needed]

### Discussion of Biases

[More Information Needed]

### Other Known Limitations

[More Information Needed]

## Additional Information

### Dataset Curators

[More Information Needed]

### Licensing Information

[More Information Needed]

### Citation Information

[More Information Needed]

### Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.
