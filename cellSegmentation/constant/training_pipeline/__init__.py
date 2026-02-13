from dataclasses import field
from typing import List



ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_DIR_NAME: str = "data_ingestion"

DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"

DATA_DOWNLOAD_URL: str = "https://drive.google.com/file/d/17vDLJrk4iYtysocirKNCDuDIOAsX0-17/view?usp=sharing"


"""Data Validation related constant start with DATA_VALIDATION VAR NAME
    """

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE = "validation_status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILES : list[str] = field(
        default_factory=lambda: ["train", "valid", "test", "data.yaml"]
    )