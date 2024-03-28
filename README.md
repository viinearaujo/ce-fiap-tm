# Cognitive Environments MBA Project: Topic Modeling

## Description
This repository contains my MBA project for the Cognitive Environments class, focusing on Topic Modeling Subject (NLP Text Classification) using GCP Vertex AI, Python, and Streamlit. The project showcases the implementation of a text classification model trained and deployed on GCP Vertex AI, with an interactive front-end built using Streamlit.

## Project Structure
- **gcp_artifacts/**: Contains screenshots presenting all GCP artifacts required to create this project, including Service Account, Storage Bucket, Model, Endpoint, and Dataset.
- **convert_authjson_b64string.ipynb**: A Jupyter notebook responsible for encoding the GCP authentication JSON file to a base64 string for secure storage in Streamlit Cloud app secret management.
- **front_app.py**: The main Streamlit file that handles the web app's front-end and invokes code from `gcp.py` for model interaction.
- **gcp.py**: Interacts with GCP through its SDK, performs text data prediction, and picks the best label (category) to be displayed in the Streamlit app.
- **preprocess_dataset.ipynb**: A Jupyter notebook for retrieving, preprocessing the dataset using the SPACY library for Brazilian Portuguese text, lemmatizing, cleaning up the dataset, and formatting it for Vertex AI.
- **requirements.txt**: Lists all the dependencies required to run the project.
- **tm-fiap-predict.ipynb**: A sandbox notebook for testing and ensuring the envisioned functionalities work correctly.
- - **tm-fiap-createGCPArtifactsUsingGoogleSDK-sandbox.ipynb**: A sandbox notebook for testing and playing around with the Google SDK - created with the purpose of testing SDK's functionalities of creating some of the required artifacts for the project.

## Getting Started

https://ce-fiap-tm.streamlit.app/
