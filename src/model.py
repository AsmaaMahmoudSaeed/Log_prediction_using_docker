
       #1) __file__:
       # __file__ is a special variable in Python that holds the path to the current Python script file (e.g., /path/to/app/model.py or C:\path\to\app\model.py).
       #In your case, this code is in app/model.py, so __file__ refers to the path of model.py.


       #2)os.path.dirname(__file__):
       #This function returns the directory containing the script file.
       #If model.py is located at /path/to/well-log-app/app/model.py, then os.path.dirname(__file__) returns /path/to/well-log-app/app.


      #3)  os.path.join(os.path.dirname(__file__), '..'):
     #os.path.join combines path components using the appropriate separator (/ for Linux, \ for Windows).
     #The .. means "go up one directory level."
     #Starting from /path/to/well-log-app/app:

     #First .. moves to /path/to/well-log-app.
      #Second .. moves to /path/to.
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