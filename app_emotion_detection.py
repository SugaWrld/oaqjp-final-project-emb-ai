from flask import Flask, request, jsonify
from emotion_detection import detect_emotion

app = Flask(__name__)

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion_route():
    """
    Receives JSON input with a 'text' field, calls the detect_emotion function,
    and returns the predicted emotion in JSON format.
    """
    # Parse the incoming JSON payload
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "No 'text' field provided in JSON"}), 400
    
    text_to_analyze = data["text"]
    
    # Call the Watson NLP detection function
    emotion_label = detect_emotion(text_to_analyze)

    # Return the emotion label in a JSON response
    return jsonify({"emotion": emotion_label})

if __name__ == '__main__':
    # Start the Flask development server
    app.run(debug=True)
