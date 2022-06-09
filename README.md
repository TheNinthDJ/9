---
annotations_creators:
- no-annotation
language_creators:
- found
languages:
- en
licenses:
- cc-by-nc-sa-4.0
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

**r_legaladvice** : Filtered data from the r/legaladvice and r/legaladviceofftopic subreddits in the format. 
Title: [Post Title]
Topic: [Post Flair]
Answer \#[N]: [Top Answers]...

**courtListener_docket_entry_documents** : Docket entries in U.S. federal courts, including filed briefs from CourtListener RECAP archive.

**courtListener_opinions** : U.S. court opinions from CourtListener.

**atticus_contracts**: Unannotated contracts from the Atticus Project.

**federal_register**: The U.S. federal register where agencies file draft rulemaking.

**bva_opinions**: Bureau of Veterans Appeals opinions.

**us_bills**: Draft Bills from the United States Congress.

**cc_casebooks**: Educational Casebooks released under open CC licenses.

**tos**: Unannotated Terms of Service contracts.

**euro_parl**: European parliamentary debates.

**nlrb_decisions**: Decisions from the U.S. National Labor Review Board.

**scotus_oral_arguments**: U.S. Supreme Court Oral Arguments

**cfr**: U.S. Code of Federal Regulations

**state_codes**: U.S. State Codes

**scotus_filings**: Briefs and filings with the U.S. Supreme Court.

**bar_exam_outlines**: Bar exam outlines available openly on the web.

**edgar**: Contracts filed with the SEC and made available on the SEC's Edgar tool.

**cfpb_creditcard_contracts**: Credit Card Contracts compiled by the U.S. Consumer Finance Protection Bureau.

**constitutions** : The World's constitutions.

**congressional_hearings** : U.S. Congressional hearing transcripts and statements.

**oig**: U.S. Office of Inspector general reports.

**olc_memos**: U.S. Office of Legal Counsel memos.

**uscode**: The United States Code (laws).

**founding_docs**: Letters from U.S. founders.

**ftc_advisory_opinions**: Advisory opinions by the Federal Trade Commission.

**echr** : European Court of Human Rights opinions.

**eurlex**: European Laws.

**tax_rulings**: Rulings from U.S. Tax court.

**un_debates**: U.N. General Debates

**fre**: U.S. Federal Rules of Evidence

**frcp** : U.S. Federal Rules of Civil Procedure

**canadian_decisions**: Canadian Court Opinions from ON and BC.

**eoir**: U.S. Executive Office for Immigration Review Immigration and Nationality Precedential Decisions

**dol_ecab**: Department of Labor Employees' Compensation Appeals Board decisions after 2006

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

For a citation to this work:

```
TODO:
```

Since this dataset also includes several other curations, if you cite this work please also cite:

```

```