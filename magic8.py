import random

# Generate a random number for the Magic 8-Ball
random_number = random.randint(1, 10)

# Variables for name and question
name = "Jessica"
question = "Do i love Sam?"

# Determine the Magic 8-Ball's answer based on the random number
if random_number == 1:
    answer = "Yes - definitely."
elif random_number == 2:
    answer = "It is decidedly so."
elif random_number == 3:
    answer = "Without a doubt."
elif random_number == 4:
    answer = "Reply hazy, try again."
elif random_number == 5:
    answer = "Ask again later."
elif random_number == 6:
    answer = "Better not tell you now."
elif random_number == 7:
    answer = "My sources say no."
elif random_number == 8:
    answer = "Outlook not so good."
elif random_number == 9:
    answer = "Very doubtful."
elif random_number == 10:
    answer = "Absolutely yes!"
else:
    answer = "Error."

# Check if the question is empty
if question.strip() == "":
    print("The fabric of reality is not safe! Please ask a valid question.")
else:
    # Display the user's question and Magic 8-Ball's answer
    if name.strip() == "":
        print("Question:", question)
    else:
        print(f"{name} asks: {question}")
    print("Magic 8-Ball's answer:", answer)
