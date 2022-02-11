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

_VARIANTS = ["all", "r_legaladvice"]

_DATA_URL = {
    "r_legaladvice" : 
    {
        "train" : "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/train.r_legaldvice.jsonl.xz",
        "validation" : "https://huggingface.co/datasets/pile-of-law/pile-of-law/resolve/main/data/validation.r_legaldvice.jsonl.xz"
    }
}


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
            data_urls[split] = [
                _DATA_URL[source][split] for source in data_sources
            ]
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
            with xz.open(filepath, "rt", encoding="utf-8") as f:
                for line in f:
                    if line:
                        example = json.loads(line)
                        yield id_, example
                        id_ += 1
