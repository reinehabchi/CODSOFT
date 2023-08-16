#Reinehabchi
#habchyreine@gmail.com
#https://www.linkedin.com/in/reine-habchi-716272234/
class Question:
    def __init__(self, question, choices=None, correct_answer=None):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

def load_questions():
    questions = [
        Question("What is the capital of France?", ["A. London", "B. Paris", "C. Rome", "D. Madrid"], "B"),
        Question("Which planet is known as the Red Planet?", ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "B"),
        Question("What is 7 x 8?",[None, "56","49","15"], "56"), 
        Question("Fill in the blank: The tallest mountain in the world is Mount ______.",[ None, "A. Everest","B. Qurnat al sawda","C. alpes","D. ukpeek"], "A")
    ]
    return questions

def display_question(question):
    print(question.question)
    if question.choices:
        for choice in question.choices:
            print(choice)
        user_answer = input("Enter your answer: ").upper()
    else:
        user_answer = input("Enter your answer: ")
    return user_answer

def main():
    questions = load_questions()
    score = 0

    print("Welcome to the Advanced Quiz Game!")
    print("Answer the following questions:")
    
    for question in questions:
        user_answer = display_question(question)
        if user_answer == question.correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question.correct_answer}\n")

    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Congratulations! You got all the answers correct.")
    elif score >= len(questions) / 2:
        print("Good job! You did well.")
    else:
        print("Keep practicing! You can do better next time.")

if __name__ == "__main__":
    main()
