import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Press Enter to stop...")

    # Adjust for ambient noise for better recognition
    recognizer.adjust_for_ambient_noise(source)

    # Continuous listening until Enter key is pressed
    while True:
        audio = recognizer.listen(source)

        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            print("You said: " + text)

            # Check for Enter key press to stop listening
            if input("Press Enter to stop...") == "":
                break

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
