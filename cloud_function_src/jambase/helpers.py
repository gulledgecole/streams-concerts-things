from google.cloud import secretmanager
from google.cloud import storage

def get_key():
    client = secretmanager.SecretManagerServiceClient()
    name = "projects/639888050178/secrets/jambase/versions/1"
    response = client.access_secret_version(request={"name": name})
    payload = response.payload.data.decode("UTF-8")

    return payload