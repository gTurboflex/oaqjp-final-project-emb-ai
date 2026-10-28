"""Serve the Emotion Detection interface and the Watson-backed endpoint."""

import requests
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Display the original project interface."""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect_emotion():
    """Format the Watson emotion scores or show a helpful input error."""
    text_to_analyze = request.args.get("textToAnalyze", "")
    try:
        result = emotion_detector(text_to_analyze)
    except requests.RequestException:
        return "Emotion service unavailable. Please try again later."
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
        f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
