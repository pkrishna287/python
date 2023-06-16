import random
greetings = ["Hi", "Hello", "Hey there"]
farewells = ["Hope it was useful", "Travel to the fullest", "Have a nice day"]

user_input = input("Hi, I'm your travel chatbot! Give the name of state you wanna explore.\n")
response = random.choice(greetings) + "! "

if "gujarat" in user_input:
    response += " here are some places to explore in gujarat 1) Statue of Unity 2) Kankaria Lake  3) Jhulta Minar 4) Lothal 5) Gir National Park 6) Somnath Jyotirlinga Temple 7) Tarnetar 8) Gandhi Nagar 9)Dumas Beach 10)Mandvi Beach  11)Rann of Kutch  12) Ahmedabad  13) Saputara  14) Laxmi Vilas Palace 15) Dwarka  16) Sun Temple 17) Dwarkadhish Temple 18) Junagadh"

elif "delhi" in user_input:
    response += "here are some places to explore in delhi 1) India gate 2) Red Fort 3) Qutub minar 4) Lotus temple 5) Humayuns tomb 6) Connaught place 7) Chandni chowk"

elif "maharashtra" in user_input:
    response += "here are some places to explore in maharastra 1) Mumbai 2) Pune 3) Mahabaleshwar 4) Nashik 5) Panchgani 6) Kolhapur 7) Matheran "

elif "kerala" in user_input:
    response += "here are some places to explore in kerala 1) Alleppey 2) Kochi 3) Thekkady 4) Munnar 5) Kovalam 6) Thissur 7) Thiruvananthapuram"

elif "rajasthan" in user_input:
    response += "here are some places to explore in rajasthan 1) Jaipur 2) Jaisalmer 3) Udaipur 4) Jodhpur 5) Bikaner 6) Ranthambore national park 7) Pushkar 8) Chittorgarh"

print(response)
print(random.choice(farewells))
