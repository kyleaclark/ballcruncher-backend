from dataclasses import asdict, dataclass, is_dataclass
from typing import Type


def generate_log_extra(metadata: dict | Type[dataclass]) -> dict:
    if is_dataclass(metadata):
        metadata = asdict(metadata)

    result = {"metadata": metadata}

    return result
