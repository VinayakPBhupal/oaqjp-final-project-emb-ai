from flask import Flask,render_template,requests

app = Flask("Emotion Detection")

@app.route('\emotionDetector')
def emotion_detetction(textToAnalyze):
    
