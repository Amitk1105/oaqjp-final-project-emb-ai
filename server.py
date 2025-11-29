"""
Flask server for Emotion Detection application.
This module provides a web interface for analyzing emotions in text.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
        Render the main index page.

        Returns:
            str: Rendered HTML content of the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emotion_detector_route():
    """
        Analyze emotion for the given text and return formatted response.

        This endpoint accepts a text parameter and returns emotion analysis
        results including anger, disgust, fear, joy, sadness scores and
        the dominant emotion.

        Returns:
            str: Formatted emotion analysis results or error message.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "Invalid text! Please try again."

    result = emotion_detector(text_to_analyze)

    if result is None or result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
