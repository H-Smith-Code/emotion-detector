import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detection(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' 
    inputobj = { "raw_document": { "text": text_to_analyse } }  
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  
    response = requests.post(url, json = inputobj, headers=header) 
    response_dict = json.loads(response.text)

    #Create dictionary to store emotion values
    emotions_dict = {}

    #If status code is 400 set values to None and return dictionary
    if response.status_code == 400:
        emotions_dict['anger'] = None
        emotions_dict['disgust'] = None
        emotions_dict['fear'] = None
        emotions_dict['joy'] = None
        emotions_dict['sadness'] = None
        emotions_dict['dominant_emotion'] = None
        return emotions_dict

    #if submission is not empty assign values to dictionary
    emotions_dict['anger'] = response_dict['emotionPredictions'][0]['emotion']['anger']
    emotions_dict['disgust'] = response_dict['emotionPredictions'][0]['emotion']['disgust']
    emotions_dict['fear'] = response_dict['emotionPredictions'][0]['emotion']['fear']
    emotions_dict['joy'] = response_dict['emotionPredictions'][0]['emotion']['joy']
    emotions_dict['sadness'] = response_dict['emotionPredictions'][0]['emotion']['sadness']
    emotions_dict['dominant_emotion'] = 0.0

    #Determine which emotion is dominant
    emotion_list = list(emotions_dict.values())
    emotion_list.sort()
    dominant = emotion_list[-1]

    for emotion in emotions_dict:
        if emotions_dict[emotion] == dominant:
            emotions_dict['dominant_emotion'] = emotion

    return emotions_dict # Return the response text from the API