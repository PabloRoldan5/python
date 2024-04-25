import pyttsx3 as voice
import speech_recognition as s #Google Speech API in Python

#Functional programming Model

def text_to_speech(text):
    #engine connects us to hardware in this case 
    eng= voice.init()
    #Engine created 
    eng.say(text)
    #Runs for small duration of time ohterwise we may not be able to hear
    eng.runAndWait()

    
def speech_to_text():
    r=s.Recognizer()# an object r which recognises the voice
    with s.Microphone() as source:
        #when using with statement. The with statement itself ensures proper acquisition and release of resources
        audio = r.listen(source)
        text_to_speech(r.recognize_google(audio, language='es')) 
        
def speech_to_text(audio_path: str) -> str:   
        r = s.Recognizer()
        with s.AudioFile(audio_path) as source:
            audio = r.record(source)

        return r.recognize_sphinx(audio)

def test_sphinx_spanish(self):
        r = s.Recognizer()
        with s.AudioFile(self.AUDIO_FILE_EN) as source: audio = r.record(source)
        self.assertEqual(r.recognize_sphinx(audio), "one two three")


