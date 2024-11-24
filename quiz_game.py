import psycopg2

DB_CONFIG = {
    "dbname": "quiz_game",
    "user": "postgres",
    "password": "your_password",
    "host": "localhost",
    "port": "5432",
}


def fetch_questions():
    connection = psycopg2.connect(**DB_CONFIG)
    cursor = connection.cursor()
    cursor.execute("SELECT id, question, option_a, option_b, option_c, option_d, correct_option FROM questions;")
    questions = cursor.fetchall()
    cursor.close()
    connection.close()
    return questions

def quiz_game():
    questions = fetch_questions()
    score = 0

    print("Welcome to the Quiz Game!\n")
    for question in questions:
        _, q_text, opt_a, opt_b, opt_c, opt_d, correct_option = question
        print(q_text)
        print(f"A: {opt_a}\nB: {opt_b}\nC: {opt_c}\nD: {opt_d}")
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer == correct_option:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_option}.\n")

    print(f"Quiz Over! Your final score is: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
