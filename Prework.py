name = input("Welcome to ChatBot! My name is Chatty, what's your name? ")
print("Nice to meet you, " + name +"!")
age = input("And remind me, how old are you again")
print("Ah! I remember when I was " + age +" years old. Good times...\nAnyways!\n--------------------------\nHow Can I Help You Today, " + name +"?\n--------------------------\n")
menu = print("[1] View All Order\n[2] Provide Joke Ideas\n[4] Fortune of the Day\n[5] EXIT")
chat_topic = int(input("Chat Topic Number: "))

if chat_topic == 5:
    print("Thanks for talking to me, " + name +"! I'll see you next time :)")
