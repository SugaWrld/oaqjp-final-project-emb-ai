"""
Flask server for the Emotion Detection application.

This module provides an API endpoint that processes text input
and returns the predicted emotion scores using the Watson NLP service.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import detect_emotion

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the home page.

    Returns:
        str: The HTML content of the homepage.
    """
    return render_template("index.html")

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector():
    """
    Process user input and return the detected emotions.

    Returns:
        JSON: A JSON response containing the detected emotions
        and their respective scores, or an error message if input is invalid.
    """
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text_to_analyze = data["text"]
    emotion_data = detect_emotion(text_to_analyze)

    if emotion_data.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    response_text = (f"For the given statement, the system response is "
                     f"'anger': {emotion_data['anger']}, "
                     f"'disgust': {emotion_data['disgust']}, "
                     f"'fear': {emotion_data['fear']}, "
                     f"'joy': {emotion_data['joy']}, "
                     f"and 'sadness': {emotion_data['sadness']}. "
                     f"The dominant emotion is {emotion_data['dominant_emotion']}.")

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=True)
