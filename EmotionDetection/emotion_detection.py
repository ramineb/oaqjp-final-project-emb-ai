import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": { "ext": text_to_analyse }}

    try:
        response = requests.post(url, json=myobj, headers=headers)
        status_code = response.status_code

        if status_code != 200:
            return {
                'anger': None,
                'disgust': None,
                'fear': None,
                'joy': None,
                'sadness': None,
                'dominant_emotion': None
            }

        res = response.json()
        emotions = res['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=lambda x: emotions[x])
        emotions['dominant_emotion'] = dominant_emotion
        return emotions

    except Exception as e:
        # Log or print the exception if needed
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
