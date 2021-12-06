
"""Python Text o Audio Conveter / Text to Speech .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JCc9VRwESfFINWYSAMttgPqCnD6ldsA3
"""

#pip install gTTS

from gtts import gTTS
import os

fh = open("TextToSpeech.txt", 'r')
myText = fh.read().replace('\n', ' ')
language = 'en'
output = gTTS(text = myText, lang = language, slow = False)
output.save('Output.mp3')
fh.close()
os.system('start Output.mp3')

