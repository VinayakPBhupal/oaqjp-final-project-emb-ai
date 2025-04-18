#importing the required modules
import requests

#function for emotion detection
def emotion_detector(text_to_analyse):
    #initializing the url,header, input which will be sent 
    #as arguments in the post request.
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }

    #post request
    response = requests.post(url, json = input, headers = header)

    #finding the status code
    status = response.status_code

    #if status code is 400 the dictionary is sent in as None for all the keys
    if status == 400:
        formatted_response = { 
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return formatted_response
    
    #if the status code is other than 400 following linesof code are executed
    #for formatting and returning the formatted dictionary
    response = response.json()
    formatted_response = {'emotion':i['emotion'] for y in response.values() for i in y if isinstance(i,dict) if 'emotion' in i.keys() }
    formatted_response = dict(formatted_response['emotion'])
    for i,j in formatted_response.items():
        if j == max(formatted_response.values()):
            formatted_response['dominant_emotion'] = i
            break
    return formatted_response  
