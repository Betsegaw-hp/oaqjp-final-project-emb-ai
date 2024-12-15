"""
Flask application for emotion detection.

This application provides a web interface to detect emotions in text
using the `emotion_detector` function from the EmotionDetection module.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyzes the emotion of the given text.

    Args:
        None (expects a 'textToAnalyze' parameter in the request).

    Returns:
        str: A message containing the emotion analysis result or an error message.
        int: HTTP status code.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)
    if result:
        if result['dominant_emotion'] is None:
            return "Invalid text! Please try again!"
        return (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
            f"'fear': {result['fear']}, 'joy': {result['joy']}, and "
            f"'sadness': {result['sadness']}. The dominant emotion is "
            f"{result['dominant_emotion']}.", 
            200
        )

    return "The input provided is invalid.", 400

@app.route("/")
def render_index_page():
    """
    Renders the index page.

    Returns:
        Response: The rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
