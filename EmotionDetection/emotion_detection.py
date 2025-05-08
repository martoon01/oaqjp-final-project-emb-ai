import requests
import json

def emotion_detector(text_to_analyse):
    # Initialize default response dictionary
    emotions = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }

    # Check for empty input first
    if not text_to_analyse:
        return emotions

    try:
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        myobj = {"raw_document": {"text": text_to_analyse}}
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        
        response = requests.post(url, json=myobj, headers=header)
        
        # Handle non-200 status codes
        if response.status_code != 200:
            return emotions
            
        formatted_response = json.loads(response.text)
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        
        # Find dominant emotion
        max_score = 0
        dominant_emotion = None
        for emotion, score in emotion_data.items():
            if score > max_score:
                max_score = score
                dominant_emotion = emotion

        # Update the response dictionary
        emotions.update({
            'anger': emotion_data['anger'],
            'disgust': emotion_data['disgust'],
            'fear': emotion_data['fear'],
            'joy': emotion_data['joy'],
            'sadness': emotion_data['sadness'],
            'dominant_emotion': dominant_emotion
        })
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        # emotions dictionary will retain its default values
        
    return emotions