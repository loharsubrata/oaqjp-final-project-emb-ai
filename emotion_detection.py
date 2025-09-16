import requests
import json

def emotion_detector(text_to_analyze):

    #url for emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    #request header
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    #request payload
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    #send request to emotion detection service
    response = requests.post( url, json=myobj, headers=header)

    #response text
    response_text = response.text

    #formatted json 
    formatted_response = json.loads(response_text)
    
    #list of emotions and scores
    emotion_score = formatted_response['emotionPredictions'][0]['emotion']

    #get the highest score emotion
    highest_score_emotion = max(emotion_score, key=emotion_score.get)
    
    #Add dominant emotion to the emotion score
    emotion_score['dominant_emotion'] = highest_score_emotion
    
    print(emotion_score)
