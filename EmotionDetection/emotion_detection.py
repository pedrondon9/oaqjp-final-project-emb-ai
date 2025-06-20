
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

    if response.status_code == 200:

        # obtenet el objeto de emociones
        obj_emotion =  formatted_response['emotionPredictions'][0]['emotion']

        # Inicializacion de variable de la emocion con mas puntaje
        emotion_score = 0
        emotion_name = ""

        # Bucle para buscar la emocion con mayor puntaje
        for key, val in obj_emotion.items():

            if val > emotion_score:
                emotion_name = key
                emotion_score = val
        
        obj_emotion['dominant_emotion'] = emotion_name

    # Si el código de estado de la respuesta es 500, establece label y score en None
    elif response.status_code == 400:

        obj_emotion = {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion":None
            }
    
    return obj_emotion


