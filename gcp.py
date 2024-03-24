from google.cloud import aiplatform
from google.oauth2 import service_account

# Path to your service account key file
SAC_KEY_FP = "topic-modelling-fiap-417601-432750c09ce7.json"
SAC_UNIQUEID = "115532493627132210234"
ENDPOINT_ID = "6120385296526737408"


def predict(text):

    teste = [
        {   # Hipotecas / Empréstimos (Mortgages / Loans)
            "descricao_reclamacao_processed": 
            text
        },
    ]   
    
    # Creating credentials using the key file
    my_credentials = service_account.Credentials.from_service_account_file(
        SAC_KEY_FP
    )

    aiplatform.init(
        # your Google Cloud Project ID or number
        # environment default used is not set
        project='topic-modelling-fiap-417601',

        # the Vertex AI region you will use
        # defaults to us-central1
        location='us-central1',

        # Google Cloud Storage bucket in same region as location
        # used to stage artifacts
        staging_bucket='gs://tm-fiap-bucket',

        # custom google.auth.credentials.Credentials
        # environment default credentials used if not set
        credentials=my_credentials,

        # customer managed encryption key resource name
        # will be applied to all Vertex AI resources if set
        encryption_spec_key_name=SAC_UNIQUEID
    )

    endpoint = aiplatform.Endpoint(ENDPOINT_ID)

    # Make the prediction
    response = endpoint.predict(instances=teste)

    # Process the response
    prediction = response.predictions[0]
    
        # Extract classes and scores from the prediction
    predicted_classes = prediction['classes']
    predicted_scores = prediction['scores']

    # Print each class with its corresponding score
    print("Prediction results:")
    for predicted_class, score in zip(predicted_classes, predicted_scores):
        print(f"{predicted_class}: {score:.2f}")
        print("-------------------")
    
    return prediction