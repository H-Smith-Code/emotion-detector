"""
Flask server for emotion detection.
Provides a home page and an endpoint that analyzes text
using the Watson NLP emotion detection model.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector')
def detector():
    """
    Analyze the provided text and return emotion scores.
    Expects a 'textToAnalyze' query parameter.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'

    out_string = f"""
    For the given statement, the system response is
        'anger': {response['anger']},
        'disgust': {response['disgust']},
        'fear': {response['fear']},
        'joy': {response['joy']},
        and 'sadness': {response['sadness']}.
    The dominant emotion is {response['dominant_emotion']}.
    """

    return out_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
