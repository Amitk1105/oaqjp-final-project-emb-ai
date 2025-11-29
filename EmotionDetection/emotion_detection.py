import requests
import json

def emotion_detector(text_to_analyze):
    none_response = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    if not text_to_analyze or text_to_analyze.strip() == "":
        return none_response

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_data = { "raw_document": { "text": text_to_analyze } }
    try:
        response = requests.post(URL, headers=headers, json=input_data)
        response.raise_for_status()
        if response.status_code == 400:
            return none_response
            
        response_dict  = response.json()
        emotions = response_dict["emotionPredictions"][0]['emotion']
        
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        return emotion_scores

    except:
        print("Some error occured")
        return None

