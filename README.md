[![Python](https://img.shields.io/badge/Python-v3.11.13-3776AB?style=plastic&logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-image-2496ED?style=plastic&logo=docker&logoColor=white)](https://www.docker.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-v1.45.1-FF4B4B?style=plastic&logo=streamlit&logoColor=white)](https://docs.streamlit.io/)
[![joblib](https://img.shields.io/badge/joblib-v1.5.1-9C27B0?style=plastic)](https://joblib.readthedocs.io/)
[![NumPy](https://img.shields.io/badge/NumPy-v2.2.3-013243?style=plastic&logo=numpy&logoColor=white)](https://numpy.org/)
[![pandas](https://img.shields.io/badge/pandas-v2.2.3-150458?style=plastic&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.7.1-F7931E?style=plastic&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/stable/)
[![gdown](https://img.shields.io/badge/gdown-v5.2.0-4CAF50?style=plastic)](https://github.com/wkentaro/gdown)



### Well Log DT Prediction App
Overview\
This is a Streamlit-based web application that predicts the sonic log (DT) value based on well log measurements: Density (RHOB), Gamma Ray (GR), Neutron Porosity (NPHI), and Photoelectric Factor (PEF). The app uses a pre-trained machine learning model (cmodel.pkl) and is deployed using Docker .

###  live demo 
https://logpredictionwebapp2-qs3gkpoatwjppsfqxfwcdl.streamlit.app/

### Features

Interactive UI: Input well log parameters via a Streamlit form and get instant DT predictions.
Modular Design: Code is organized into separate modules for UI (app/main.py) and model logic (app/model.py).
Error Handling: Robust validation and logging for user inputs and model operations.
Docker Deployment: Configured for easy deployment on Render using Gunicorn and Uvicorn.


### Project Structure
###  well-log-app/
#### ├── src/
#### │------------├── __init__.py
#### │------------├── main.py              # Streamlit UI and app logic
#### │------------├── model.py             # Model loading and prediction logic
#### ├── models/
#### │------------├── cmodel.pkl           # Pre-trained machine learning model
#### ├── notebooks/
#### │------------├── Prediction of Continuous Well Logs.ipynb  
#### ├── input/
#### │------------├──volve_wells.csv       #dataset  
#### ├── requirements.txt                  # Python dependencies
#### ├── Dockerfile                        # Docker configuration for Render
#### ├── README.md                         # Project documentation

### Prerequisites

python:3.11.13
Docker: For building and deploying the app
Git: For version control

###  Installation

Clone the Repository:
  ```
git clone https://github.com/your-username/well-log-app.git
cd well-log-app
  ```

Install Dependencies:
  ```
pip install -r requirements.txt
  ```

Run Locally:
  ```
streamlit run src/main.py
  ```
Access the app at http://localhost:8501.

Troubleshooting

Model Loading Errors: Ensure cmodel.pkl is in the models/ directory and compatible with scikit-learn==1.7.1.
Deployment Failures: Check Render logs for issues like missing dependencies or memory limits.
Performance Issues: Optimize cmodel.pkl size if it exceeds 100 MB to fit within free tier constraints.

### Run the App with Docker
Pull the Docker Image

You can pull the latest version of the image directly from Docker Hub:
  ```
docker pull asmaamahmoudsaeed/log-app:v3
  ```
Run the Container
Run the app locally by mapping port 8501 (default for Streamlit):
  ```
docker run -p 8501:8501 -e PORT=8501 asmaamahmoudsaeed/log-app:v3
  ```


### Contributing

Fork the repository.
Create a feature branch (git checkout -b feature/your-feature).
Commit changes (git commit -m "Add your feature").
Push to the branch (git push origin feature/your-feature).
Open a pull request.

### License
MIT License
