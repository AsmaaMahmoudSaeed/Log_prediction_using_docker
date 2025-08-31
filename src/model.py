
import pickle
import joblib
import pandas as pd
import logging
from typing import Optional, Any

# Configure logging
logger = logging.getLogger(__name__)

def predict_dt(model: Any, input_data: pd.DataFrame) -> float:
    """
    Make a DT prediction using the provided model and input data.

    Args:
        model (Any): Loaded machine learning model.
        input_data (pd.DataFrame): Input data with columns ['RHOB', 'GR', 'NPHI', 'PEF'].

    Returns:
        float: Predicted DT value.

    Raises:
        ValueError: If input data is invalid or prediction fails.
    """
    try:
        if not all(col in input_data.columns for col in ["RHOB", "GR", "NPHI", "PEF"]):
            raise ValueError("Input data must contain columns: RHOB, GR, NPHI, PEF")
        prediction = model.predict(input_data)[0]
        return float(prediction)
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise ValueError(f"Failed to make prediction: {str(e)}")