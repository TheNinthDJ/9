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
- **Paper:** Under review.

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

We curate a large corpus of legal and administrative data. The utility of this data is twofold: (1) to aggregate legal and administrative data sources that demonstrate different norms and legal standards for data filtering; (2) to collect a dataset that can be used in the future for pretraining legal-domain language models, a key direction in access-to-justice initiatives. As such, data sources are curated to inform: (1) legal analysis, knowledge, or understanding; (2) argument formation; (3) privacy filtering standards. Sources like codes and laws tend to inform (1). Transcripts and court filings tend to inform (2). Opinions tend to inform (1) and (3).

### Source Data

#### Initial Data Collection and Normalization

We do not normalize the data, but we provide dataset creation code and relevant urls in https://github.com/Breakend/PileOfLaw

#### Who are the source language producers?

Varied (see sources above).

### Personal and Sensitive Information

This dataset may contain personal and sensitive information. However, this has been previously filtered by the relevant government and federal agencies that weigh the harms of revealing this information against the benefits of transparency. If you encounter something particularly harmful, please file a takedown request with the upstream source and notify us in the communities tab. We will then remove the content. We cannot enable more restrictive licensing because upstream sources may restrict using a more restrictive license. However, we ask that all users of this data respect the upstream licenses and restrictions. Per the standards of CourtListener, we do not allow indexing of this data by search engines and we ask that others do not also. Please do not turn on anything that allows the data to be easily indexed.

## Considerations for Using the Data

### Social Impact of Dataset

We hope that this dataset will provide more mechanisms for doing data work. As we describe in the paper, the internal variation allows contextual privacy rules to be learned. If robust mechanisms for this are developed they can applied more broadly. This dataset can also potentially be used for legal language model pretraining. As discussed in [other work](https://arxiv.org/abs/2108.07258), legal language models can help improve access to justice in various ways. But they can also be used in potentially harmful ways. While such models are not ready for most production environments and are the subject of significant research, we ask that model creators using this data, particularly when creating generative models, consider the impacts of their model and make a good faith effort to weigh the benefits against the harms of their method. Our license and many of the sub-licenses also restrict commercial usage.

### Discussion of Biases

The data reflects the biases of governments and courts. As we discuss in our work, these can be significant, though more recent text will likely be less overtly toxic. Please see the above statement and embark on any model uses responsibly.

### Other Known Limitations

We mainly focus on U.S. and English-speaking legal sources, though we include some European and Canadian resources.

## Additional Information

### Licensing Information

 CreativeCommons Attribution-NonCommercial-ShareAlike 4.0 International. But individual sources may have other licenses. See paper for details.

### Citation Information

For a citation to this work:

```
TODO:
```

Since this dataset also includes several other curations, if you cite this work please also cite:

```

```