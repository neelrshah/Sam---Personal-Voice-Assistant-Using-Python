# Sam---Personal-Voice-Assistant-Using-Python

A virtual assistant is a software agent that can perform tasks or services for an individual. Virtual Assistant (VA) is a term that applies to computer-simulated
environments that can simulate physical presence in places in the real world, as well as in imaginary worlds.

	
### Objectives
- To Create an interface to provide voice instructions.
- To implement a speech recognition module to convert speech into text.
- To implement Python Dictionary to find synonyms
- To understand the context and give the user response accordingly. 

### Features
- Get current date & time.
- Interact with Google Search , Wikipedia & YouTube (Play videos or songs).
- Shutdown, logout and Restart PC.
- Open photos, videos, documents & downloads.
- Take Screenshot.
- Get CPU, Ram & Battery usage.
- Get Jokes.
- Search online and get related information which user is searching for.
- Interacting with OS using voice commands.
- Perform Mathematical calculation and solving equations using voice command.
- Get local and Global news.
- Get weather information.


### Description
   We are going to use python and google text to speech API for this project, speech recognition module can be used to recognize the voice of the user, and based on its query 
will be fired. Initially, the user will give a voice command to the assistant then that voice command is sent to google engine and voice is converted to text, then keywords are 
extracted from it, then the synonyms are searched for those keywords in Dictionary so that the assistant can understand the user easily. Based on those keywords and synonyms 
appropriate query is fired and the task is performed then the output is again converted to voice and the user gets a response in the form of voice. Many different modules i.e., 
web browser, YouTube, Wikipedia, etc. are used to interact with the internet. the os module is used to interact with operating system related queries. For Learning purposes, users can search any information related to a certain topic on Wikipedia, Google, or in text documents.
  
To gain a deeper knowledge of this topic we have referred to many websites and YouTube videos. These helped us to gain the basic knowledge of the topic. The articles helped us in getting an overview of various technologies that can be used in this project. A computer-primarily based approach for performing a voice command to perform a certain task.

1. Speech recognition 
Link:  https://pypi.org/project/SpeechRecognition/

   Speech recognition has a long history with several waves of major innovations. Speech recognition for dictation, search, and voice commands has become a standard feature on desktop and wearable devices. Design of a compact large vocabulary speech recognition system that can run efficiently on desktop, accurately, and with low latency. As more data becomes available for a given speech recognition task, the natural way to improve recognition accuracy is to train larger acoustic models. 

2. Pyttsx3
Link: https://pypi.org/project/pyttsx3/

   Pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries, it works offline and is compatible with both Python 2 and 3.  An application invokes the pyttsx3. init() factory function to get a reference to a pyttsx3. We referred to the documentation and many videos on YouTube to understand the concept of text-to-speech.

3. Python Dictionary 
Link: https://pypi.org/project/PyDictionary/

   PyDictionary is a Dictionary Module for Python 2/3 to get meanings, translations, synonyms, and Antonyms of words. It uses WordNet for getting meanings, Google for translations, and synonym.com for getting synonyms and antonyms. PyDictionary can be utilized in 2 ways, either by creating a dictionary instance that can take words as arguments or by creating a dictionary instance with a fixed number of words.


