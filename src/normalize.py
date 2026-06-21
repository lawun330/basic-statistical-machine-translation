import contextlib
import io
import sys
from pathlib import Path

from config import SYL_DIR, SYL_DICT

sys.path.insert(0, str(SYL_DIR))
from syl_normalizer import process_input  # noqa: E402


def normalize_myanmar_line(text: str) -> str:
    line = text.strip()
    if not line:
        return ""

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(io.StringIO()):
        process_input(
            input_stream=io.StringIO(line + "\n"),
            output_file=None,
            error_output_file=None,
            dictionary_file=str(SYL_DICT),
            min_frequency=2,
            fuzzy_distance=0,
        )

    return buf.getvalue().strip()

