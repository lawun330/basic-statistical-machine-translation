import subprocess
import tempfile
from pathlib import Path

from config import MOSES_ARGS, MOSES_BIN


class MosesDecodeError(RuntimeError):
    pass


def _check_setup(config_path: Path) -> None:
    if not MOSES_BIN.is_file():
        raise MosesDecodeError(f"Moses binary not found: {MOSES_BIN}")
    if not config_path.is_file():
        raise MosesDecodeError(f"Moses config not found: {config_path}")


def translate_line(line: str, config_path: Path) -> str:
    text = line.strip()
    if not text:
        return ""

    _check_setup(config_path)

    cmd = [str(MOSES_BIN), *MOSES_ARGS, "-f", str(config_path)]
    proc = subprocess.run(
        cmd,
        input=(text + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )

    if proc.returncode != 0:
        err = proc.stderr.decode("utf-8", errors="replace").strip()
        raise MosesDecodeError(err or f"moses exited with code {proc.returncode}")

    return proc.stdout.decode("utf-8").strip()
