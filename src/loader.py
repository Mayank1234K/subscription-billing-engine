import pandas as pd
import logging

logger = logging.getLogger(__name__)

def load_csv(file_path):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        logger.error(f"Error loading {file_path}: {e}")
        return pd.DataFrame()