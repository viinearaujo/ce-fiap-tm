from google.cloud import aiplatform
from google.oauth2 import service_account
import base64
import json
import streamlit as st

# GCP SERVICE ACCOUNT UNIQUE ID 
SAC_UNIQUEID = "115532493627132210234"

# GCP ENDPOINT ID
ENDPOINT_ID = "6120385296526737408"

def predict(text):
    """
    Realiza o Predict utilizando o Modelo criado/treinado utilizando o dataset
    fornecido pelo professor. O dataset foi preprocessado pelo notebook
    preprocess_dataset.ipynb - que tambem o adequou para o formato de dataset
    esperado pelo GCP Vertex AI - seguindo a documentacao vigente.

    Parâmetros:
        text (str): Texto que será analisado pelo modelo.

    Retorna:
        dict: Dicionario com Labels (Categorias) reconhecidas pelo modelo
        e seus Scores.
    """

    # Cria dado para ser analisado pelo modelo treinado utilizando o servico GCP Vertex AI
    # Como o dataset de treino utiliza apenas a coluna 'descricao_reclamacao_processed'
    # para classificar o texto com uma Categoria de chamado, apenas este dado e fornecido.
    data = [
        {   
            "descricao_reclamacao_processed": 
            text
        },
    ]   

    # Get encoded authentication info from Streamlit Secret Management
    encoded_string = st.secrets["gcp_b64encoded_gcp_auth_json"]

    # Decode the string back to JSON
    decoded_auth_bytes = base64.b64decode(encoded_string)
    decoded_auth_json = json.loads(decoded_auth_bytes.decode('utf-8'))

    # Creating credentials using the key file (encoded as b64 string)
    my_credentials = service_account.Credentials.from_service_account_info(
        decoded_auth_json
    )

    aiplatform.init(
        # Google Cloud Project ID
        project='topic-modelling-fiap-417601',

        # Vertex AI region
        location='us-central1',

        # Google Cloud Storage bucket in same region as location
        # used to stage artifacts (artifacts = processed_file.csv)
        # processed_file.csv --> Contem dados do dataset fornecido
        # pelo professor (vide output do notebook preprocess_dataset.ipynb)
        staging_bucket='gs://tm-fiap-bucket',

        # custom google.auth.credentials.Credentials
        credentials=my_credentials,

        # GCP Service Account Unique ID
        encryption_spec_key_name=SAC_UNIQUEID
    )

    # Instantiate endpoint providing Endpoint Unique ID
    endpoint = aiplatform.Endpoint(ENDPOINT_ID)

    # Make the prediction passing list of data (of a single value)
    response = endpoint.predict(instances=data)

    # Process the response
    prediction = response.predictions[0]

    return prediction

def get_top_confidence_category(text):
    """
    Realiza a predição das categorias com base no texto fornecido, 
    selecionando a categoria com maior nível de confiança ('Confidence')
    gerada pelo modelo. Este método destina-se a identificar a 
    categoria mais provável para apresentação no aplicativo web Streamlit.

    Parâmetros:
        text (str): Texto que será analisado pelo modelo.

    Retorna:
        str: O label da categoria com maior confiança prevista pelo modelo.
    """

    # Make prediction
    prediction = predict(text)

    # Find the index of the highest score
    max_score_index = prediction['scores'].index(max(prediction['scores']))

    # Use the index to find the corresponding class (Categoria)
    categoria = prediction['classes'][max_score_index]

    return categoria