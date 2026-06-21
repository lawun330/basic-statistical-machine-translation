from pathlib import Path

APP_ROOT = Path(__file__).resolve().parents[1]
MOSES_BIN = APP_ROOT / "moses" / "bin" / "moses"
MODELS_DIR = APP_ROOT / "models"
SYL_DIR = APP_ROOT / "syl-normalizer"
SYL_DICT = SYL_DIR / "filtered_dictionary.txt"

MOSES_ARGS = [
    "-search-algorithm", "1",
    "-cube-pruning-pop-limit", "5000",
    "-s",
    "5000",
]

DIRECTIONS = {
    "my-ph": {
        "title": "Grapheme to Phoneme",
        "config": MODELS_DIR / "my-ph" / "moses.tuned.ini.5",
        "normalize": True,
        "placeholder": "တက် တက် ပြောင်",
        "help": "Burmese graphemes tokens, space-separated.",
    },
    "ph-my": {
        "title": "Phoneme to Grapheme",
        "config": MODELS_DIR / "ph-my" / "moses.tuned.ini.5",
        "normalize": False,
        "placeholder": "te' te' pjauN",
        "help": "Roman phoneme tokens, space-separated.",
    },
}
