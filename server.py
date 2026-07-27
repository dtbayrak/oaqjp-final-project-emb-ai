"""
This Flask module provides a web endpoint that takes text input, 
runs emotion analysis using `emotion_detector` function, and 
returns an emotion report.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_emotion_analysis():
    """
    This function handles emotion analysis requests.
    Takes the 'textToAnalyze' query parameter, processes it, 
    and returns a emotion report.
    If the text is invalid or no emotion can be detected, 
    an error message is returned.
    Returns str: Emotion analysis report or an error message.
    """
        # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract data from the response
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion is None:
        emotion_report = "Invalid text! Please try again!"
    else:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']

        emotion_report = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
            )
    return emotion_report

@app.route("/")
def index():
    """
    Render the main page of the application.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "localhost", port = "5000")
