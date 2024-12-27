import requests
def emotion_detector(text_to_analyze):
    #Define endpoint URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Define the API key and the authentication credentials
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    #define the text to analyze
    input_json = { "raw_document": { "text": text_to_analyze } }
    #Send the post request
    
    try:
        #send the POST request
        response = requests.post(url, headers=headers, json=input_json)
        #check response
        if response.status_code ==200:
            return response.json()
        else:
            return {"error": f"request failed with status code: {response.status_code}", "details": response.text}
        # handle exceptions
    except Exception as e:
        return {'error': "An exception has occured", "details": str(e)}

