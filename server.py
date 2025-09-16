''' To host web page for emotion detector'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def emotion_detect():
    '''This method is used to emotion detector service '''
    #fetch the emotion from input argument
    emotion_to_detect = request.args.get('textToAnalyze')
    #pass the emotion to emotion detector
    response = emotion_detector(emotion_to_detect)

    #error handing
    if response.get('dominant_emotion') is None:
        return 'Invalid text! Please try again!.'

    return f"For the given statement, the system response is 'anger': {response['anger']}, \
    'disgust': {response['disgust']}, \
    'fear': {response['fear']}, \
    'joy': {response['joy']} and \
    'sadness': {response['sadness']} .\
    The dominant emotion is {response['dominant_emotion']} ."

@app.route("/")
def render_index_page():
    '''This moduel is used to render the home page '''
    return render_template('index.html')
#run the application in localhost:5000
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
