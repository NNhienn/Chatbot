# Chatbot
Prosjektet mitt handler om å lage en kort chatbot i python som kan svare på noen spørsmål som man implementerer i botten. Chatbotten fungerer slik at den lager en funksjon som har spørsmål og svar, også deretter bruker man en loop som har mange ulike spørsmål som har en spesifik svar til den hvis brukeren skriver en av spøsrmålene. Hvis brukeren ikke skriver en av spørsmålene eller noe som er implementert i botten så vil den printe ut at den ikke vet. 

Man trenger en kode editor og python 3(helst nyeste versjon) for å kunne kjøre koden.

Hvordan lage en chatbot med openai model
Man trenger å betale på openai sin nettside for å bruke api key deres som git tigang til en ordentlig model som f.eks. GPT 3.5, deretter må man installere visual studio code og python. Man må også installere openai i CMD ved å skrive inn pip install openai

Bruk denne eksempel koden for å lage en chatbot med openai

import openai

openai.api_key = 'Your_Api_Key'

content = input("User: ")
completion = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages =[
        {"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate"}
    ]
)

chat_response = completion.choices[0].message.content
print(f'ChatGPT: {chat_response}')
