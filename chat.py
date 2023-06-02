import random

#Lager en funksjon med greetings og svar til greetings hvis botten leser at man skriver en av greetings
def get_response(question):
    greetings = ["Hei", "Hallo", "God dag"]
    answers = ["Det kan jeg ikke svare på", "Beklager, jeg vet ikke", "Jeg er ikke sikker"]

    #Lager if loop der hvis vi skriver en av de spørsmålene så retunerer den ut svar enten random fra liste eller et svar, dersom den leser at jeg skriver spørsmålen så printer den ut svaret, hvis ikke så printer den ut random "jeg vet ikke"
    if "hei" in question.lower():
        return random.choice(greetings)
    elif "hvordan har du det" in question.lower():
        return "Jeg er en bot, så jeg har det alltid bra!"
    elif "hva heter du" in question.lower():
        return "Jeg heter ChatterBot"
    elif "hvordan fungerer du" in question.lower():
        return "Jeg fungerer ved å analysere tekst og generere svar basert på mønstre jeg har lært"
    elif "er du ekte" in question.lower():
        return "Nei det er jeg faktisk ikke, jeg er en robot som er lagd for å snakke med folk som deg"
    else:
        return random.choice(answers)

#Hvis alt over er true så lager den en input som brukeren kan skrive i for å kunne skrive de spørsmålene også svarer botten med navnvet sitt og svar fra loop
while True:
    user_input = input("Bruker: ")
    response = get_response(user_input)
    print("ChatterBot:", response)