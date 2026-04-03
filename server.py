from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector')
def detector(): 
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detection(text_to_analyze)

    if response['dominant_emotion'] == None:
        return 'Invalid text! Please try again!'

    out_string = f"""For the given statement, the system response is
                    'anger': {response['anger']}, 
                    'disgust': {response['disgust']}, 
                    'fear': {response['fear']}, 
                    'joy': {response['joy']}, 
                    and 'sadness': {response['sadness']}. 
                    The dominant emotion is {response['dominant_emotion']}."""

    return out_string

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)