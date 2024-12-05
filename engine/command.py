import speech_recognition as sr
import time
import eel
from feature import openCommand

@eel.expose
def take_command():
    """Listens to the microphone and returns the recognized speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = r.listen(source, timeout=10, phrase_time_limit=6)  # Listen for audio

    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en-IN')  # Recognize speech
        print(f'User said: {query}')
        eel.DisplayMessage(query)
        time.sleep(2)
        response = openCommand(query)  # Call the command function

        # Show the response from openCommand if applicable
        if response:
            eel.DisplayMessage(response)  # Optionally display response in UI
        eel.ShowHood()  # Call to update UI (ensure this is correctly implemented)
    except sr.UnknownValueError:
        print("Sorry, I did not catch that.")
        eel.DisplayMessage("Sorry, I did not catch that.")  # Feedback for the user
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service.")
        eel.DisplayMessage("Could not request results from the speech recognition service.")
    except Exception as e:
        print(f"An error occurred: {e}")
        eel.DisplayMessage("An error occurred. Please try again.")

    return query.lower()  # Return the recognized query

@eel.expose
def allCommands(message=1):
    if message == 1:
        query = take_command()  # Get the command
        print(query)  # Debugging output
    else:
        query = message  # Handle the message from UI

    try:
        if "open" in query or "how are you" in query:  # Handle the command
            response = openCommand(query)
            return response  # Return the response for the UI # Optionally return a response from chatBot

    except Exception as e:
        print(f"Error in command processing: {e}")

