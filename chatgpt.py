# Quiz questions and answers
questions = [
    "1. What is the capital of France?",
    "2. Who wrote 'Romeo and Juliet'?",
    "3. What is the chemical symbol for water?",
    "4. What is the largest planet in our solar system?",
    "5. Who painted the Mona Lisa?"
]

options = [
    ["A. London", "B. Paris", "C. Rome", "D. Berlin"],
    ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Mark Twain"],
    ["A. Wa", "B. Wo", "C. WaH", "D. H2O"],
    ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
    ["A. Leonardo da Vinci", "B. Vincent van Gogh", "C. Pablo Picasso", "D. Michelangelo"]
]

answers = ["B", "A", "D", "B", "A"]

# Function to ask questions and calculate score
def conduct_quiz():
    score = 0
    for i in range(len(questions)):
        print(questions[i])
        for option in options[i]:
            print(option)
        user_answer = input("Your answer (A, B, C, or D): ").upper()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print()  # Empty line for spacing between questions
    return score

# Function to display final score
def display_score(score):
    print("Quiz ended. Your score is:", score, "out of", len(questions))

# Main function
def main():
    print("Welcome to the Quiz!")
    print("You will be asked 5 multiple-choice questions. Choose the correct option.")
    input("Press Enter to start the quiz...")

    score = conduct_quiz()
    display_score(score)

if __name__ == "__main__":
    main()
