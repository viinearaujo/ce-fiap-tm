from google.cloud import aiplatform
from google.oauth2 import service_account
import base64
import json


# GCP SERVICE ACCOUNT UNIQUE ID 
SAC_UNIQUEID = "115532493627132210234"

# GCP ENDPOINT ID
ENDPOINT_ID = "6120385296526737408"


def predict(text):
    """
    
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


    # Read text file with the encoded authentication info
    with open('encoded-auth.txt', 'r') as encoded_file:
        encoded_string = encoded_file.read()

    # Decode the string back to JSON
    decoded_auth_bytes = base64.b64decode(encoded_string)
    decoded_auth_json = json.loads(decoded_auth_bytes.decode('utf-8'))

    # Creating credentials using the key file
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