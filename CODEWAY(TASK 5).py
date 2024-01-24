import random

class QuizGame:
    def __init__(self):
        self.score = 0
        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['London', 'Paris', 'Berlin', 'Rome'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'Which planet is known as the Red Planet?',
                'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
                'correct_answer': 'Mars'
            },
            {
                'question': 'What is the largest mammal on Earth?',
                'options': ['Elephant', 'Blue Whale', 'Giraffe', 'Hippopotamus'],
                'correct_answer': 'Blue Whale'
            },
            # Add more questions as needed
        ]

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Answer multiple-choice or fill-in-the-blank questions on a specific topic.")
        print("Let's see how much you know!\n")

    def present_quiz_questions(self):
        for i, question in enumerate(self.questions, 1):
            print(f"Question {i}: {question['question']}")
            for j, option in enumerate(question['options'], 1):
                print(f"{j}. {option}")

            user_answer = input("Your answer: ").strip()

            # Evaluate the user's answer
            self.evaluate_user_answer(user_answer, question['correct_answer'])

    def evaluate_user_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            self.score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}\n")

    def display_final_results(self):
        print(f"Quiz completed! Your final score is: {self.score}/{len(self.questions)}")

    def play_again(self):
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        return play_again_input == 'yes'

def main():
    while True:
        quiz_game = QuizGame()
        quiz_game.display_welcome_message()
        quiz_game.present_quiz_questions()
        quiz_game.display_final_results()

        if not quiz_game.play_again():
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
