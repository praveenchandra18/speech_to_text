from flask import Flask, render_template, request
import speech_recognition as sr

app = Flask(__name__)
r = sr.Recognizer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/text', methods=['POST'])
def function():
    audio=request.files['audio']
    with sr.AudioFile(audio) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
    lst=[text]
    return render_template('final_output.html',list=lst)

if __name__ == '__main__':
    app.run(debug=True)

