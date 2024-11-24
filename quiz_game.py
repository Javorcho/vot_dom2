import psycopg2
from psycopg2 import connect

QUESTIONS_DB_CONFIG = {
    "dbname": "questions_db",
    "user": "postgres",
    "password": "questions_pass",
    "host": "localhost",
    "port": "5433",
}

ANSWERS_DB_CONFIG = {
    "dbname": "answers_db",
    "user": "postgres",
    "password": "answers_pass",
    "host": "localhost",
    "port": "5434",
}

def fetch_questions():
    conn = psycopg2.connect(**QUESTIONS_DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, question FROM questions;")
    questions = cursor.fetchall()
    conn.close()
    return questions

def fetch_answers(question_id):
    conn = psycopg2.connect(**ANSWERS_DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT option_a, option_b, option_c, option_d, correct_option FROM answers WHERE question_id = %s;",
        (question_id,),
    )
    answers = cursor.fetchone()
    conn.close()
    return answers

def play_quiz():
    questions = fetch_questions()
    score = 0
    for q_id, question in questions:
        print(f"\n{question}")
        options = fetch_answers(q_id)
        print(f"A: {options[0]}")
        print(f"B: {options[1]}")
        print(f"C: {options[2]}")
        print(f"D: {options[3]}")
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == options[4]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {options[4]}")
    print(f"\nQuiz Over! Your score is {score}/{len(questions)}")

if __name__ == "__main__":
    play_quiz()
