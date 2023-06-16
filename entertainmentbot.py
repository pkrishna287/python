import random 
hello = ["hy","hi","is there anyone here??","hello"]
bye = ["see you","bye","tata"]
interest = ["what are options to watch?","give me some options"]
types = ["what are the categories??","available categories"]
print('Welcome to Entertainment bot\n')
while True:
    a = input('User -')
    if a.lower() in hello:
        botans = ["hello","hey","how can i help you?"]
        print('Bot -'+random.choice(botans)+'\n')
    elif a.lower() in bye:
        botans =["bye","have a good day","hope you enjoyed here"]
        print('Bot -'+random.choice(botans)+'\n')
    elif a.lower() in interest:
        botans =["movies","series","TV series"]
        for item in botans:
            print("Bot - " + item)
    elif a.lower() in types:
        botans =["action","comedy","horror","fiction","biography","romance"]
        for item in botans:
            print("Bot - " + item)
    elif a == 'action':
        botans =["Pathan","Black Panther","RRR","Avengers","KGF"]
        for item in botans:
            print("Bot - " + item)
    elif a == 'comedy':
        botans =["Housefull","F.R.I.E.N.D.S","How i met your mother","Phonebooth"]
        for item in botans:
            print("Bot - " + item)
    elif a == 'horror':
        botans =["stranger things","Annabell","Bulbul","Bhoot"]
        for item in botans:
            print("Bot - " + item)
    elif a == 'fiction':
        botans =["Avtar","The adams Project","The Wandering Earth"]
        for item in botans:
            print("Bot - " + item)
    elif a == 'biography':
        botans =["Sardar Udham","Rocketry","Spencer","Jhund"]
        for item in botans:
            print("Bot - " + item)
    elif a == 'romance':
        botans =["Shiddat","Love Story","After","Sita Ramam","Radhe Shyam"]
        for item in botans:
            print("Bot - " + item)
    else :
        print("Sorry I dont Understand...")
    
    
        


    


