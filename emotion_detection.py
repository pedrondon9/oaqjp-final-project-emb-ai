

import requests
import json

def emotion_detector(text_to_analyse):

    # Definimos la URL para la API de análisis de sentimientos
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Creamos la carga útil con el texto a analizar
    mydata = { "raw_document": { "text": text_to_analyse } }

    # Establecemos los encabezados con el ID de modelo requerido para la API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Realizamos una solicitud POST a la API con la carga útil y los encabezados
    response = requests.post(url, json=mydata, headers=header)

        # Analiza la respuesta de la API
    formatted_response = json.loads(response.text)


    # Devuelve el label y el score en un diccionario
    return formatted_response