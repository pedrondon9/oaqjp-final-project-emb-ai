from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emo_detector() :

    # Recupera el texto a analizar de los argumentos de la solicitud
    text_emotion = request.args.get('textToAnalyze')
    # Pasa el texto a la función sentiment_analyzer y almacena la respuesta
    response = emotion_detector(text_emotion)

    if response["dominant_emotion"] == None :

        return "Invalid text! Please try again!."

    else :

        data_return = (
            f"For the given statement, the system response is "
            f"anger: {response['anger']}, "
            f"disgust: {response['disgust']}, "
            f"fear: {response['fear']}, "
            f"joy: {response['joy']} and "
            f"sadness: {response['sadness']}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
        
        return data_return

@app.route("/")
def render_index_page():
    return render_template('index.html')
python3 -m pip install requests

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)