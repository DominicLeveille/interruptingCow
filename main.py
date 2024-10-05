

import speech_recognition as sr
import pyttsx3
import pyaudio


# recognizor
r = sr.Recognizer()

# text to speech
def speakText(cmd):
    
    # initialize the engne
    eng = pyttsx3.init()
    eng.say(cmd)
    eng.runAndWait()
    

# Loop infinite for user to speak

def main():
    running = True
    while(running):
        try:
            # use the mic as input
            with sr.Microphone() as source2:
                # wait for the regocnizor to adjust
                r.adjust_for_ambient_noise(source2, duration=0.2)

                # listen
                audio2 = r.listen(source2)
                
                # use google to recognize audiio
                mytext = r.recognize_google_cloud(audio2)
                mytext - mytext.lower()
                
                print("&quot;Did you say &quot;", mytext)
                print(f"{mytext}")
                speakText(mytext)
        except sr.RequestError as e:
            print(f"could not requdst results {0}".format(e))
        except sr.UnknownValueError:
            print(f"Unknown error {e} has occurred")
        running = False

if __name__ == "__main__":
    # print(main())
    main()