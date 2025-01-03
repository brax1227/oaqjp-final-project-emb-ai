"""
Flask application for emotion detection using the EmotionDetection package.
"""
from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    """
    API endpoint to detect emotions in a given statement.

    Returns:
        JSON response with emotion scores and the dominant emotion.
    """
    # Get the input statement from the request
    input_data = request.get_json()
    statement = input_data.get("statement", "")

    if not statement.strip():
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    # Process the statement using emotion_detector
    result = emotion_detector(statement)

    if result['dominant_emotion'] is None:
        return jsonify({'response': "Invalid text! Please try again!"}), 400

    # Format the output response
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
