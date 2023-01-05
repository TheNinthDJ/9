"""Pile of Law"""


import gzip
import json

import datasets
try:
    import lzma as xz
except ImportError:
    import pylzma as xz


datasets.logging.set_verbosity_info()
logger = datasets.logging.get_logger(__name__)


_DESCRIPTION = """
We curate a large corpus of legal and administrative data. The utility of this data is twofold: (1) to aggregate legal and administrative data sources that demonstrate different norms and legal standards for data filtering; (2) to collect a dataset that can be used in the future for pretraining legal-domain language models, a key direction in access-to-justice initiatives.
"""

_CITATION = """
@misc{hendersonkrass2022pileoflaw,
  url = {https://arxiv.org/abs/2207.00220},
  author = {Henderson, Peter and Krass, Mark S. and Zheng, Lucia and Guha, Neel and Manning, Christopher D. and Jurafsky, Dan and Ho, Daniel E.},
  title = {Pile of Law: Learning Responsible Data Filtering from the Law and a 256GB Open-Source Legal Dataset},
  publisher = {arXiv},
  year = {2022}
}
"""

_URL = "https://huggingface.co/datasets/pile-of-law/pile-of-law"


_DATA_URL = {
    "r_legaladvice" : 
    {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.r_legaldvice.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.r_legaldvice.jsonl.xz"]
    },
    "courtlistener_docket_entry_documents" : {
        "train" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlistenerdocketentries.0.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlistenerdocketentries.1.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlistenerdocketentries.2.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlistenerdocketentries.3.jsonl.xz"
        ],
        "validation" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlistenerdocketentries.0.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlistenerdocketentries.1.jsonl.xz"
        ]
    },
    "atticus_contracts" : {
        "train" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.atticus_contracts.0.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.atticus_contracts.1.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.atticus_contracts.2.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.atticus_contracts.3.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.atticus_contracts.4.jsonl.xz"            
        ],
        "validation" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.atticus_contracts.0.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.atticus_contracts.1.jsonl.xz"
        ]
    },
    "courtlistener_opinions" : {
        "train" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.0.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.1.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.2.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.3.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.4.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.5.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.6.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.7.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.8.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.9.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.10.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.11.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.12.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.13.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.14.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.15.jsonl.xz"

        ],
        "validation" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.0.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.1.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.2.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.3.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.4.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.5.jsonl.xz"
        ]
    },
    "federal_register" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.federal_register.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.federal_register.jsonl.xz"]
    },
    "bva_opinions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.bva.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.bva.jsonl.xz"]
    },
    "us_bills" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.us_bills.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.us_bills.jsonl.xz"]
    },
    "cc_casebooks" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.cc_casebooks.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.cc_casebooks.jsonl.xz"]
    },
    "tos" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.tos.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.tos.jsonl.xz"]
    },
    "euro_parl" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.euro_parl.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.euro_parl.jsonl.xz"]
    },
    "nlrb_decisions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.nlrb_decisions.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.nlrb_decisions.jsonl.xz"]
    },
    "scotus_oral_arguments" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.scotus_oral.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.scotus_oral.jsonl.xz"]
    },
    "cfr" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.cfr.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.cfr.jsonl.xz"]
    },
    "state_codes" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.state_code.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.state_code.jsonl.xz"]
    },
    "scotus_filings" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.scotus_docket_entries.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.scotus_docket_entries.jsonl.xz"]
    },
    "exam_outlines" : {
        "train" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.examoutlines.jsonl.xz",
        ],
        "validation" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.examoutlines.jsonl.xz",
        ]
    },
    "edgar" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.edgar.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.edgar.jsonl.xz"]        
    },
    "cfpb_creditcard_contracts" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.cfpb_cc.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.cfpb_cc.jsonl.xz"]        
    },
    "constitutions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.constitutions.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.constitutions.jsonl.xz"]        
    },
    "congressional_hearings" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.congressional_hearings.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.congressional_hearings.jsonl.xz"]        
    },
    "oig" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.oig.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.oig.jsonl.xz"]        
    },
    "olc_memos" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.olcmemos.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.olcmemos.jsonl.xz"]        
    },
    "uscode" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.uscode.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.uscode.jsonl.xz"]        
    },
    "founding_docs" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.founding_docs.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.founding_docs.jsonl.xz"]        
    },
    "ftc_advisory_opinions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.ftc_advisory_opinions.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.ftc_advisory_opinions.jsonl.xz"]        
    },
    "echr" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.echr.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.echr.jsonl.xz"]        
    },
    "eurlex" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.eurlex.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.eurlex.jsonl.xz"]        
    },
    "tax_rulings" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.taxrulings.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.taxrulings.jsonl.xz"]        
    },
    "un_debates" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.undebates.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.undebates.jsonl.xz"]        
    },
    "fre" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.fre.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.fre.jsonl.xz"]      
    },
    "frcp" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.frcp.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.frcp.jsonl.xz"]      
    },
    "canadian_decisions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.canadian_decisions.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.canadian_decisions.jsonl.xz"]     
    },
    "eoir" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.eoir.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.eoir.jsonl.xz"]     
    },
    "dol_ecab" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.dol_ecab.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.dol_ecab.jsonl.xz"]     
    },
    "icj-pcij" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.ijc.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.ijc.jsonl.xz"]
    },
    "uspto_office_actions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.uspto_oab.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.uspto_oab.jsonl.xz"]
    },
    "ed_policy_guidance" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.ed_policy_guidance.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.ed_policy_guidance.jsonl.xz"]
    },
    "acus_reports" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.acus_reports.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.acus_reports.jsonl.xz"]
    }
}

_VARIANTS = ["all"] + list(_DATA_URL.keys())


class PileOfLaw(datasets.GeneratorBasedBuilder):
    """TODO"""

    BUILDER_CONFIGS = [datasets.BuilderConfig(name) for name in _VARIANTS]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "text": datasets.Value("string"),
                    "created_timestamp": datasets.Value("string"),
                    "downloaded_timestamp": datasets.Value("string"),
                    "url": datasets.Value("string"),
                }
            ),
            supervised_keys=None,
            homepage=_URL,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        data_urls = {}
        if self.config.name == "all":
            data_sources = list(_DATA_URL.keys())
        else:
            data_sources = [self.config.name]
        for split in ["train", "validation"]:
            data_urls[split] = []
            for source in data_sources:
                for chunk in _DATA_URL[source][split]:
                    data_urls[split].append(chunk)

        train_downloaded_files = dl_manager.download(data_urls["train"])
        validation_downloaded_files = dl_manager.download(data_urls["validation"])
        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepaths": train_downloaded_files}),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION, gen_kwargs={"filepaths": validation_downloaded_files}
            ),
        ]

    def _generate_examples(self, filepaths):
        """This function returns the examples in the raw (text) form by iterating on all the files."""
        id_ = 0
        for filepath in filepaths:
            logger.info("Generating examples from = %s", filepath)
            try:
                with xz.open(open(filepath, "rb"), "rt", encoding="utf-8") as f:
                    for line in f:
                        if line:
                            example = json.loads(line)
                            if example is not None and isinstance(example, dict):
                                yield id_, {
                                    "text": example.get("text", ""),
                                    "created_timestamp": example.get("created_timestamp", ""),
                                    "downloaded_timestamp": example.get("downloaded_timestamp", ""),
                                    "url": example.get("url", "")
                                }
                                id_ += 1
            except:
                print("Error reading file:", filepath)
