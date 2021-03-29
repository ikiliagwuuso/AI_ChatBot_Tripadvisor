# AI_ChatBot_Tripadvisor (Retrieval Based)

AI ChatBot using Tensorflow, Natural Language ToolKit (NLTK), Tkinter and Pickle.

## What is a ChatBot
A chatbot (also known as a talkbot, chatterbot, Bot, IM bot, interactive agent, or Artificial Conversational Entity) is a computer program or an artificial
intelligence which conducts a conversation through auditory or textual methods. 

## Prerequisites
Downloading and installing modules

Python, Keras, and Natural language processing (NLTK). 
downloading modules with the python-pip command.

pip install tensorflow, keras, pickle, nltk


## Procedure to train model and files

Intents.json – The data file which has predefined patterns and responses.

train_chatbot.py – In this Python file, we wrote a script to build the model and train our chatbot.

Words.pkl – This is a pickle file in which we store the words Python object that contains a list of our vocabulary.

Classes.pkl – The classes pickle file contains the list of categories.

Chatbot_model.h5 – This is the trained model that contains information about the model and has weights of the neurons.

Chatgui.py – This is the Python script in which we implemented GUI for our chatbot. Users can easily interact with the bot.

## Procedure

Import and load the data file
Preprocess data
Create training and testing data
Build the model
Predict the response

## Types of Chatbot

1. Retrieval based Chatbots
A retrieval-based chatbot uses predefined input patterns and responses. It then uses some type of heuristic approach to select the appropriate response. It is widely used in the industry to make goal-oriented chatbots where we can customize the tone and flow of the chatbot to drive our customers with the best experience.

2. Generative based Chatbots
Generative models are not based on some predefined responses.

They are based on seq 2 seq neural networks. It is the same idea as machine translation. In machine translation, we translate the source code from one language to another language but here, we are going to transform input into an output. It needs a large amount of data and it is based on Deep Neural networks.


The chatbot was trained on a dataset which contains categories (intents), pattern and responses using a special recurrent neural network (LSTM) to classify
which category the user’s message belongs to and then we will give a random response from the list of responses.

## Training the model
The model was trained on 3 layers using sing Keras sequential API where the first layer had 64 neutrons, second layer has 128 neutrons. The model was trained for 200 epoch and achieved an 
accuracy of 100%. 

AI ChatBot (Retrieval) using intent for Travellers and Frequently Asked Question

The Dataset was from TripAdvisor Relational Strategies in Customer Service (RSiCS) courtesy of lionbridge.ai 


