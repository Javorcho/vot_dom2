Containerized Quiz Game
This project is a simple Python-based quiz game that retrieves questions and answers from two separate PostgreSQL databases running in Docker containers. The questions and answers databases are isolated into separate containers for modularity.

Features
Containerized Databases: Questions and answers are stored in two different PostgreSQL containers.
Python Integration: The Python script fetches questions and answers from their respective databases and runs a text-based quiz game.
Dockerized Setup: Uses docker-compose to manage database containers.
Prerequisites
Python 3.8+
Docker and Docker Compose
DBeaver (optional, for database management)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/containerized-quiz-game.git
cd containerized-quiz-game
Install Python dependencies:

bash
Copy code
pip install psycopg2-binary
Ensure Docker is installed and running on your machine.

Setup Instructions
1. Start the Containers
Run the following command to set up and start the questions and answers database containers:

bash
Copy code
docker-compose up -d
This will:

Create a PostgreSQL container for the questions database, exposed on port 5433.
Create a PostgreSQL container for the answers database, exposed on port 5434.
2. Initialize the Databases
Populate the questions Database
Run the following commands to copy and execute the setup_questions.sql script inside the questions_db container:

bash
Copy code
docker cp setup_questions.sql questions_db:/setup_questions.sql
docker exec -it questions_db psql -U postgres -d questions_db -f /setup_questions.sql
Populate the answers Database
Run the following commands to copy and execute the setup_answers.sql script inside the answers_db container:

bash
Copy code
docker cp setup_answers.sql answers_db:/setup_answers.sql
docker exec -it answers_db psql -U postgres -d answers_db -f /setup_answers.sql
3. Run the Quiz Game
Run the Python script to start the quiz:

bash
Copy code
python quiz_game.py
The script will:

Fetch questions from the questions database container.
Fetch answers and options for each question from the answers database container.
Prompt the user to answer questions and display the score at the end.
