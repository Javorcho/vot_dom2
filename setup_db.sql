CREATE TABLE questions(
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_option CHAR(1) NOT NULL
)

SELECT * FROM questions;

DELETE FROM questions;

INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_option)
VALUES 
    ('What is the capital of France?', 'Paris', 'Berlin', 'Madrid', 'Rome', 'A'),
    ('What is 2 + 2?', '3', '4', '5', '6', 'B'),
    ('Which planet is known as the Red Planet?', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'B');