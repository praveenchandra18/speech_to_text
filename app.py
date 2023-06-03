import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Try saying something...")
    audio = r.listen(source)
    try:
        var=r.recognize_google(audio)
        print(type(var))
    except sr.UnknownValueError:
        print("Could not understand audio")
