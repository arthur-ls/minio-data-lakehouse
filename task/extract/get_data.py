import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

class ImportData:
    def __init__(self, kaggle_project:str):
        self._kaggle_project = kaggle_project

    def get_kaggle_data(self, file_path:str) -> pd.DataFrame:
        df = kagglehub.dataset_load(
            KaggleDatasetAdapter.PANDAS,
            self._kaggle_project,
            file_path,
        )
        return df

