CREATE TABLE  questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL
);

INSERT INTO questions (question)
VALUES
('What is the capital of France?'),
('What is 2 + 2?'),
('Which planet is known as the Red Planet?');
