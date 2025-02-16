from dataclasses import asdict, dataclass, is_dataclass


def generate_log_extra(metadata: dict | dataclass) -> dict:
    if is_dataclass(metadata):
        metadata = asdict(metadata)

    result = {"metadata": metadata}

    return result
