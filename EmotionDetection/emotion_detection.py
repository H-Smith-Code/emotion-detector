import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detection(text_to_analyse):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'  # URL of the sentiment analysis service
    inputobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = inputobj, headers=header)  # Send a POST request to the API with the text and headers
    response_dict = json.loads(response.text)

    #Create dictionary to store emotion values
    emotions_dict = {}
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