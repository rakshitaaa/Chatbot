# -*- coding: utf-8 -*-
"""BotMusk.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sZI19pNYLrv9VETe6VtEz6CeVq14KcHP

##BotMusk
"""

# pip install nltk

# pip install newspaper3k

"""##Importing The Libraries"""

from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Downloading the punkt package
nltk.download('punkt', quiet=True)

#Get the Article
article = Article('https://www.biography.com/business-figure/elon-musk')
article.download()
article.parse()
article.nlp()
corpus = article.text

#Print the article's text
print(corpus)

#Tokenization
text = corpus
sentence_list = nltk.sent_tokenize(text) #A list of sentences

#Print the list of snetences
print(sentence_list)

#Creating a function tp return a random response to a user's greeting.
def greeting_response(text):
  text = text.lower()

  #Bot's Greeting response
  bot_greetings = ['howdy', 'hi', 'hello', 'hey', 'namaste', 'hola']

  #User's greetings
  user_greetings = ['hi', 'hola', 'hello', 'greetings', 'wassup']


  for word in text.split():
    if word in user_greetings:
      return random.choice(bot_greetings)

def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0, length))

  x = list_var
  for i in range(length):
    for j in range(length):
      if x[list_index[i]] > x[list_index[j]]:
      #Swap
        temp = list_index[i]
        list_index[i] = list_index[j]
        list_index[j] = temp

  return list_index

#Create the Bot's response
def bot_response(user_input):
  user_input = user_input.lower()
  sentence_list.append(user_input)
  bot_response = ''
  cm = CountVectorizer().fit_transform(sentence_list)
  similarity_scores = cosine_similarity(cm[-1], cm)
  similarity_scores_list = similarity_scores.flatten()
  index = index_sort(similarity_scores_list)
  index = index[1:]
  response_flag = 0

  j = 0
  for i in range(len(index)):
    if similarity_scores_list[index[i]] > 0.0:
      bot_response = bot_response+' '+sentence_list[index[i]]
      response_flag = i
      j += 1
    if j > 2:
      break

  if response_flag == 0:
    bot_response = bot_response+' '+"I apologize, I don't understand"

  sentence_list.remove(user_input)

  return bot_response

'''
user_input = 'Hello World'
sentence_list.append(user_input)
bot_response = ''
cm = CountVectorizer().fit_transform(sentence_list)
similarity_scores = cosine_similarity(cm[-1], cm)
similarity_scores_list = similarity_scores.flatten()
index = index_sort(similarity_scores_list)
'''

#Start Chat
print("Hi I am BotMusk! I will answer your queries about my Boss. If you want to exit type: Bye")

exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']

while(True):
  user_input = input()
  if user_input.lower() in exit_list:
    print('BotMusk: Chat with you later !')
    break
  else:
    if greeting_response(user_input) != None :
      print('BotMusk: '+greeting_response(user_input))
    else:
      print('BotMusk: '+bot_response(user_input))