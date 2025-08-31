import streamlit as st
import pandas as pd
import logging
from typing import Optional
from model import load_model, predict_dt

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Constants
INPUT_FEATURES = ["RHOB", "GR", "NPHI", "PEF"]
DEFAULT_VALUES = {
    "RHOB": 2.5,  # g/cm³
    "GR": 50.0,   # API
    "NPHI": 0.2,  # v/v
    "PEF": 5.0    # b/e
}
VALID_RANGES = {
    "RHOB": (1.0, 3.0),  # Typical density range
    "GR": (0.0, 200.0),  # Typical gamma ray range
    "NPHI": (0.0, 1.0),  # Typical neutron porosity range
    "PEF": (0.0, 10.0)   # Typical photoelectric factor range
}

def validate_input(feature: str, value: float) -> bool:
    """Validate if the input value is within the acceptable range."""
    min_val, max_val = VALID_RANGES[feature]
    return min_val <= value <= max_val

def setup_page():
    """Configure the Streamlit page layout and description."""
    st.set_page_config(page_title="Well Log DT Prediction App", layout="wide")
    st.title("Well Log DT Prediction App")
    st.markdown("""
        This application predicts the sonic log (DT) value based on well log measurements: 
        Density (RHOB), Gamma Ray (GR), Neutron Porosity (NPHI), and Photoelectric Factor (PEF).
        Enter the values below and click 'Predict DT' to get the prediction.
    """)

def render_input_form() -> tuple[dict, bool]:
    """Render the input form and collect user inputs."""
    st.subheader("Input Well Log Parameters")
    inputs = {}
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        with col1:
            inputs["RHOB"] = st.number_input(
                "RHOB (Density, g/cm³)",
                min_value=VALID_RANGES["RHOB"][0],
                max_value=VALID_RANGES["RHOB"][1],
                value=DEFAULT_VALUES["RHOB"],
                step=0.01
            )
            inputs["GR"] = st.number_input(
                "GR (Gamma Ray, API)",
                min_value=VALID_RANGES["GR"][0],
                max_value=VALID_RANGES["GR"][1],
                value=DEFAULT_VALUES["GR"],
                step=0.1
            )
        with col2:
            inputs["NPHI"] = st.number_input(
                "NPHI (Neutron Porosity, v/v)",
                min_value=VALID_RANGES["NPHI"][0],
                max_value=VALID_RANGES["NPHI"][1],
                value=DEFAULT_VALUES["NPHI"],
                step=0.01
            )
            inputs["PEF"] = st.number_input(
                "PEF (Photoelectric Factor, b/e)",
                min_value=VALID_RANGES["PEF"][0],
                max_value=VALID_RANGES["PEF"][1],
                value=DEFAULT_VALUES["PEF"],
                step=0.1
            )
        submitted = st.form_submit_button("Predict DT")
    return inputs, submitted

def main():
    """Main function to run the Streamlit app."""
    setup_page()
    
    # Load the model
    model = load_model()
    if model is None:
        st.error("Failed to load the model. Please check the logs and ensure 'cmodel.pkl' is available in the 'models' directory.")
        logger.error("Model loading failed, stopping the app.")
        st.stop()

    # Render input form and handle submission
    inputs, submitted = render_input_form()
    
    if submitted:
        # Validate inputs
        for feature, value in inputs.items():
            if not validate_input(feature, value):
                st.error(f"Invalid value for {feature}: {value}. Must be between {VALID_RANGES[feature][0]} and {VALID_RANGES[feature][1]}.")
                logger.warning(f"Invalid input for {feature}: {value}")
                return

        # Prepare input data
        input_data = pd.DataFrame([inputs], columns=INPUT_FEATURES)
        
        # Make prediction
        try:
            predicted_dt = predict_dt(model, input_data)
            st.success(f"Predicted DT: {predicted_dt:.2f} µs/ft")
            logger.info(f"Prediction successful: DT={predicted_dt:.2f} for inputs {inputs}")

            # Display results in a table
            result_df = pd.DataFrame({
                **inputs,
                "Predicted DT (µs/ft)": [predicted_dt]
            })
            st.table(result_df)
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            logger.error(f"Prediction failed: {str(e)}")

if __name__ == "__main__":
    main()