from pathlib import Path
from typing import Final

ROOT_PATH: Final[Path] = Path(__file__).parents[2]
INPUT_FILES: Final[Path] = ROOT_PATH.joinpath("file_temp")
