import requests

def emotion_detector(text_to_analyze):
    """
    Function to analyze emotions in a given text using Watson NLP.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=input_json)

        if response.status_code == 200:
            response_dict = response.json()
            print("API Response:", response_dict)  # Debugging: Inspect API response

            # Extract emotions
            emotion_predictions = response_dict.get('emotionPredictions', [])
            if not emotion_predictions:
                return {'error': "No emotion predictions found in response"}
            
            emotions = emotion_predictions[0].get('emotion', {})
            print("Extracted Emotions:", emotions)  # Debugging

            anger = emotions.get('anger', 0.0)
            disgust = emotions.get('disgust', 0.0)
            fear = emotions.get('fear', 0.0)
            joy = emotions.get('joy', 0.0)
            sadness = emotions.get('sadness', 0.0)

            # Calculate the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get) if emotions else "unknown"

            return {
                'anger': anger,
                'disgust': disgust,
                'fear': fear,
                'joy': joy,
                'sadness': sadness,
                'dominant_emotion': dominant_emotion
            }
        else:
            return {"error": f"Request failed with status code: {response.status_code}", "details": response.text}

    except Exception as e:
        return {'error': "An exception has occurred", 'details': str(e)}


