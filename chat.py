import random
import json
import torch
from pre_process import bag_of_words, tokenize, stem
from models import NeuralNet
import train_test
import torch, torchvision.models
model = torchvision.models.vgg16()
path = 'test.pth'
torch.save(model.state_dict(), path) # nothing else here
model.load_state_dict(torch.load(path))

print("Kundan")

device = torch.device('cpu')

with open(r'C:/Users/glitcher/Desktop/Rj_hackathon_2/venv/intents1.json') as json_data:
    intents = json.load(json_data)

# Use train_test.data as the model state dictionary
model_state = train_test.data

input_size = model_state["input_size"]
hidden_size = model_state["hidden_size"]
output_size = model_state["output_size"]
all_words = model_state['all_words']
tags = model_state['tags']

# Create the NeuralNet model with the correct architecture
model = NeuralNet(input_size, hidden_size, output_size).to(device)

# Load the model state dictionary into the model
model.load_state_dict(model_state)
model.eval()

bot_name = "Police"
print("Let's chat! (type 'quit' to exit)")

while True:
    sentence = input("You: ")
    if sentence == "quit":
        break

    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]

    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                print(f"{bot_name}: {random.choice(intent['responses'])}")
    else:
        print(f"{bot_name}: I do not understand...")
