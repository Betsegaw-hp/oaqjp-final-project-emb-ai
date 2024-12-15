import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    res = requests.post(url, json = myobj, headers=header)
    formatted_res = json.loads(res.text)
    
    if res.status_code == 200:
        emotions = formatted_res['emotionPredictions'][0]['emotion']
        max_val = emotions['anger']
        dominant_emotion = 'anger'
        for k,v in emotions.items():
            if v > max_val:
                dominant_emotion = k
                max_val = v
        
        result = {
                **emotions,
                'dominant_emotion': dominant_emotion
                }
    elif res.status_code == 400:
        result = { "anger": None, "disgust": None, "fear": None,  "joy": None, 
                "sadness": None, "dominant_emotion": None }
    elif res.status_code == 500:
        result = None

    return result

