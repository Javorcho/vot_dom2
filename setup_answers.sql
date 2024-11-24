CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    question_id INT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_option CHAR(1) NOT NULL
);

INSERT INTO answers (question_id, option_a, option_b, option_c, option_d, correct_option)
VALUES
(1, 'Paris', 'Berlin', 'Madrid', 'Rome', 'A'),
(2, '3', '4', '5', '6', 'B'),
(3, 'Earth', 'Mars', 'Jupiter', 'Saturn', 'B');
