from dataclasses import dataclass
from pathlib import PosixPath, WindowsPath


@dataclass
class AppSettings:
    app_start_datetime_utc: str
    env: str
    deployed_flag: bool
    root_dir: PosixPath | WindowsPath
