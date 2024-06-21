import os
import pandas as pd
from io import StringIO  # Import StringIO for working with JSON strings


class Extractor:
    def __init__(self, itbi_report_path):
        """
        Initialize the Extractor class with a data directory.

        Args:
        - itbi_report_path (str): Itbi report path containing data files.
        """
        self.itbi_report_path = itbi_report_path

    def load_itbi_report(self):
        """
        Load itbi report data from a CSV file in the specified directory.

        Returns:
        - pd.DataFrame: DataFrame containing itbi report data.
        """
        try:
            if not os.path.isfile(self.itbi_report_path):
                raise FileNotFoundError(f"File not found: {self.itbi_report_path}")

            return pd.read_csv(self.itbi_report_path)
        except FileNotFoundError as e:
            print(f"Error loading payment lookup file: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error loading payment lookup data: {e}")
            raise

   