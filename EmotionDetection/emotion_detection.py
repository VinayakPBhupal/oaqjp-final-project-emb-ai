import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = input, headers = header)
    response = response.json()
    formatted_response = {'emotion':i['emotion'] for y in response.values() for i in y if isinstance(i,dict) if 'emotion' in i.keys() }
    formatted_response = dict(formatted_response['emotion'])
    for i,j in formatted_response.items():
        if j == max(formatted_response.values()):
            formatted_response['dominant_emotion'] = i
            break
    return formatted_response        