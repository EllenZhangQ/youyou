import pyttsx3
# initialize Text-to-speech engine
engine = pyttsx3.init()
# convert this text to speech
#text = "Hello YOYOU, Mom love you!"
# import the text file
with open("text.txt", "r", encoding='UTF-8') as f:
    text = f.read()
        

# setting new voice rate (faster)
engine.setProperty("rate", engine.getProperty("rate") - 50)

# set another voice
engine.setProperty("voice", engine.getProperty("voices")[1].id)

engine.say(text)

# saving speech audio into a file
engine.save_to_file(text, "speech.mp3")


# play the speech
engine.runAndWait()
