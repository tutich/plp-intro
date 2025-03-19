import random

# Personalised greeting
myName = input("Enter your name:")

favColor = input("Enter favorite color:")

print(f"Hello, {myName}! Your favorite color, {favColor}, is awesome!")



# Simple quiz game

def quiz_game():
    score = 0

    questions = [
        {
            "question": "What is the correct python file extension?",
            "options": ["A) .py", "B) .pt", "C) .pyt"],
            "answer": "A",
        },

        {
            "question": "Who played Iron Man in the Marvel movies?",
            "options": ["A) Tutich", "B) Robert Downey Jr.", "C) pk"],
            "answer": "B",
        },

        {
            "question": "Which keyword is used to define a function in python?",
            "options": ["A) func", "B) function", "C) def"],
            "answer": "C",
        },
    ]

    print("\n🎮 Welcome to the Quiz Game! 🎮\n")

    for q in questions:
        print(q["question"])
        for option in q["options"]:
           print(option)


        answer = input("\nEnter your answer (A, B, or C): ").strip().upper()

        if answer == q["answer"]:
           print("✅ Correct!\n")
           score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}\n")
    print(f"You got {score}/{len(questions)} correct!")

while True:
     quiz_game()
     play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
     if play_again != "yes":
         print("Thanks for playing! 👋")
         break



# Random joke generator
def random_jokes():
    jokes = [
        "How do you comfort a javascript bug? you console it",
        "Why do devs prefer dark mode? because light attracts bugs",
        "Why did the developer go broke? He used up all his cache",
        "Why did the Python programmer break up with Java? Because he didn’t like the class system! 😆",
    ]

    joke = random.choice(jokes)

    print("\n🤣Random jokes🤣\n")
    print(joke)

random_jokes()