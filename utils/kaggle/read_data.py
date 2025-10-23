import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

def get_kaggle_data(kaggle_project: str, file_path:str) -> pd.DataFrame:
    return kagglehub.dataset_load(
        KaggleDatasetAdapter.PANDAS,
        kaggle_project,
        file_path,
    )

