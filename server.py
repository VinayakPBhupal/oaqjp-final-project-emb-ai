#importing the required modules
from flask import Flask,render_template,request
from EmotionDetection.emotion_detection import emotion_detector

#initiating the application by initializing the flask object 
app = Flask("Emotion Detection")


#decorator mapping the analysis url to the respective function
@app.route('/emotionDetector')
def emotion_detetction():
    
    #getting the text from the request
    text_to_analyze = request.args.get('textToAnalyze')

    #calling the emotion_detector function with the text recieved from text
    response = emotion_detector(text_to_analyze)

    #if no text has been passed the dictionary recieved will have values as None
    #if such cases encountered returning a normal text as invalid
    if response['dominant_emotion'] == None:
        return "Invalid text! Please try again!."

    #if no errors the recieved dictionary is further subjected to modification
    #to return desired output
    res = [f"'{e}': {j}" for e,j in response.items() if e != 'dominant_emotion']
    formatted_resp = ', '.join(res)
    return (f"For the given statement, the system response is "
    f"{formatted_resp}.The dominant emotion is {response['dominant_emotion']}. " )



#root directory rendering the html page
@app.route('/')
def render_function():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)
