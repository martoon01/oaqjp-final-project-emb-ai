import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": {"text": text_to_analyse}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    #  print(formatted_response)

    emotions = formatted_response['emotionPredictions'][0]['emotion']
    #  print(emotions)

    max_score = 0
    dominant_emotion = None
    for emotion, score in emotions.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion

    result = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

    return result