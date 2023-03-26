import random
responses = {
    "hi": ["Hello!How may I help you??", "Hi there!How may I help you??", "Hi!How may I help you??"],
    "i have an issue":["Please tell us about your issue \n i.  transaction issue\n ii. Account creation issue\n iii.Hostel fee\n iv. stocks purchase/sale\n v.  credit \n vi. FD \n vii.other(please specify)" ],
    "transaction issue" : ["i.payment failure \n ii.Money debited but not reached receiver \n iii.Money debited two times \n iv.Money sent to other number by mistake \n v.other(please specify)"],
    "Account creation issue":["i.Details not verified \n ii.Forgot your password \n iii.Account not found \n iv.forgot my username \n v. Other(please specify) "],
    "Hostel Fee":["i.payment failed \n ii.Fee paid but not updated \n iii. Refund not received \n iv. Other"],
    "stocks purchase":["i.Order was not placed within time \n ii.Order was placed twice by mistake \n iii.Money not received after selling the stock \n iv.Other"],
    "credit": ["i.What are the documents required \n ii.How can i increase my limit \n iii.Why is my credit limit not increasing \n iv.I need more time to repay \n v.Other"],
    "FD":["i.What are the interest rates \n ii. i am unable to create a FD account \n iii.How to withdraw money from FD"],
    "payment failure":["i.payment processing \n ii.Network issue \n iii.Other"],
    "Details not verified ": ["i.Documents pending \n ii. Submitted other documents \n iii. Other"],
    "default": ["Sorry, I didn't understand your message.", "Can you please rephrase that?", "I'm not sure what you're trying to say."]

}


def chatbot_response(message):
    
    message = message.lower()

    
    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])

while True:
    message = input("You: ")
    if message == "bye":
        print("Chatbot: Thank you!")
        break
    else:
        response = chatbot_response(message)
        print("Chatbot: " + response)