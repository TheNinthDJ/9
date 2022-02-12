"""C4 dataset based on Common Crawl."""


import gzip
import json

import datasets
try:
    import lzma as xz
except ImportError:
    import pylzma as xz


logger = datasets.logging.get_logger(__name__)


_DESCRIPTION = """\
A living legal dataset.
"""

_CITATION = """
TODO
"""

_URL = ""


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
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlistenerdocketentries.0.jsonl.xz"
        ]
    },
    "courtlistener_opinions" : {
        "train" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.courtlisteneropinions.jsonl.xz"],
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.courtlisteneropinions.jsonl.xz"]
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
        "validation" : ["https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.state_code.jsonl.xz"]
    },
    "bar_exam_outlines" : {
        "train" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.stanfordbarexamoutlines.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.shajnfeldbarexamoutlines.jsonl.xz",
        ],
        "validation" : [
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.stanfordbarexamoutlines.jsonl.xz",
            "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.shajnfeldbarexamoutlines.jsonl.xz",
        ]
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
            logger.info("generating examples from = %s", filepath)
            with xz.open(open(filepath, "rb"), "rt", encoding="utf-8") as f:
                for line in f:
                    if line:
                        example = json.loads(line)
                        yield id_, example
                        id_ += 1
