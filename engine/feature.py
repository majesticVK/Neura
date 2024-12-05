import os
import webbrowser
import pyttsx3
import wikipedia
import pyjokes
import json
from urllib.request import urlopen

# Initialize the speech engine globally
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)  # Set voice
engine.setProperty('rate', 170)  # Set speaking rate
engine.setProperty('volume', 1)  # Set volume to max (1.0)

def speak(text):
    """Uses the pyttsx3 library to convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def openCommand(query):
    query = query.lower()  # Normalize the query to lowercase

    if "open calculator" in query:
        os.system("calc")  # Opens Calculator
        speak("Opening Calculator")
    elif "open notepad" in query:
        os.system("notepad")  # Opens Notepad
        speak("Opening Notepad")
    elif "open chrome" in query:
        os.system("start chrome")  # Opens Chrome
        speak("Opening Chrome")
    elif "open settings" in query:
        os.system("start ms-settings:")  # Opens Windows Settings
        speak("Opening Settings")
    elif "open microsoft store" in query:
        os.system("start ms-windows-store")  # Opens Microsoft Store
        speak("Opening Microsoft Store")
    elif "open youtube" in query:
        webbrowser.open("https://www.youtube.com")  # Opens YouTube
        speak("Opening YouTube")
    elif "open github" in query:
        webbrowser.open("https://www.github.com")  # Opens GitHub
        speak("Opening GitHub")
    elif 'hello' in query:  # Respond to "how are you?"
        response = "hi i'm neura pleasure to meet you"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response
    elif 'how are you' in query:  # Respond to "how are you?"
        response = "I'm fine, thank you! How are you?"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response
    elif 'who are you' in query:  # Respond to "who are you?"
        response = "I'm Neura, a chatbot to help, assist, and regrow mental stature and stability in one being."
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response
    elif "why do we need you" in query:  # Respond to "why do we need you?"
        response = "Well, we can see that humans often ignore mental discomfort, which can be challenging in different aspects of life. That's why I was created, to assist you."
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response
    elif "can you be my friend" in query:  # Respond to "can you be my friend?"
        response = "Sure, why not? You can discuss anything you want with me, whether it's related to searches or what you want to listen to. I'm very fond of books."
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response
    elif "what is your favorite book" in query:  # Respond to "what is your favorite book?"
        response = "My favorite books are mostly self-help books. One example is 'Atomic Habits.'"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response
    elif "can you dance" in query:  # Respond to "can you dance?"
        response = "Physically, I can't dance, but you can imagine me dancing with you."
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling

    elif 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)
        return results
    elif 'joke' in query:
        result = pyjokes.get_joke()
        speak(result)
        print(result)
        return result
    elif 'news' in query:
        try:
        # Replace 'YOUR_API_KEY' with your actual API key
            api_key = "5d331fde643e40faa2b5c64b0527f12c"
            jsonObj = urlopen(f'https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=top&apiKey={api_key}')
            data = json.load(jsonObj)

            i = 1
            speak('Here are some top news from the Times of India.')
            print('''=============== TIMES OF INDIA ============''' + '\n')

            for item in data['articles']:
                print(str(i) + '. ' + item['title'] + '\n')
                print(item['description'] + '\n')
                speak(str(i) + '. ' + item['title'] + '\n')
                i += 1
        except Exception as e:
            print("An error occurred:", str(e))  # More descriptive error message

    elif 'failed' in query:  # Respond to "can you dance?"
        response = "You have the right to perform your prescribed duties, but you are not entitled to the fruits of your actions.    Meaning: Focus on your actions without being attached to the outcomes"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif 'peace' in query:  # Respond to "can you dance?"
        response = "Seeking solace in spirituality or a higher power can bring about profound mental peace. By directing your focus away from worldly troubles and towards the divine, you cultivate a sense of tranquility that helps heal the mind"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif "how to deal with stress" in query:  # Respond to "can you dance?"
        response = "Mastering one's emotions and maintaining detachment from external influences is crucial for mental wellness. This practice allows individuals to navigate life's challenges without being overwhelmed by stress and anxiety, By focusing on performing your duties without the fear of success or failure, you can alleviate stress and anxiety. This approach encourages a mindset of acceptance, promoting mental healing"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif 'productive' in query:  # Respond to "can you dance?"
        response = " Acknowledging the restless nature of the mind is the first step in managing it, through persistent effort and detachment from distractions, one can achieve mental control, leading to inner peace."
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif 'stressful' in query:  # Respond to "can you dance?"
        response = " Acknowledging the restless nature of the mind is the first step in managing it, through persistent effort and detachment from distractions, one can achieve mental control, leading to inner peace."
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif "how to acheive balance in life" in query:  # Respond to "can you dance?"
        response = "Achieving a balanced perspective towards the dualities of life is key to mental peace. This teaching encourages individuals to remain steady regardless of external circumstances, reducing the emotional turbulence caused by life's fluctuations , One who is not disturbed by the dualities of happiness and distress, who is unbothered by them, is certainly eligible for liberation"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif 'desires' in query:  # Respond to "can you dance?"
        response = " Desire is the root cause of all suffering, Recognizing that unfulfilled desires often lead to emotional pain can help individuals manage anxiety and depression. This understanding promotes mindfulness about desires, encouraging a more peaceful state of mind"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif "how to be happy" in query:  # Respond to "can you dance?"
        response = "  He who is satisfied with his own self, he alone is truly happy , Cultivating self-contentment is crucial for overcoming negative emotions. This quote reminds us that true happiness is derived from within, rather than external circumstances, promoting emotional stability"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif "how to attain happiness" in query:  # Respond to "can you dance?"
        response = "   The one who is free from ego and self-identity can attain true happiness ,  Letting go of ego helps in achieving emotional freedom. This quote suggests that true happiness stems from selflessness and connection with others, promoting a healing mindset"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    elif 'inner peace' in query:  # Respond to "can you dance?"
        response = "  Mastery over the mind is vital for inner peace; an uncontrolled mind can lead to suffering.the importance of mindfulness and self-regulation in achieving emotional well-being"
        print(response)  # Print to console for debugging
        speak(response)  # Speak the response
        return response  # Return the response for further handling
    else:
        print("Application not found or unsupported query")
        speak("I couldn't understand that command.")  # Optional feedback
        return "I couldn't understand that command."

