Containerized Quiz Game
Този проект е контейнеризирано Python приложение за викторини, което използва две PostgreSQL бази данни в отделни контейнери – една за въпроси и друга за отговори. Python приложението е също контейнеризирано, което прави целия проект лесен за настройка и управление с Docker Compose.

Функционалности
Изолирани бази данни: Въпросите и отговорите са разделени в два PostgreSQL контейнера.
Контейнеризирано приложение: Python скриптът работи в собствен Docker контейнер.
Docker Compose: Лесно управление на всички контейнери чрез един команден файл.
Изисквания
Docker и Docker Compose
Python 3.8+ (само ако искаш да стартираш приложението локално)
DBeaver (опционално, за управление на базите данни)
Настройка
1. Клониране на проекта
Клонирай репозиторито и влез в директорията:

bash
Copy code
git clone https://github.com/your-repo/containerized-quiz-game.git
cd containerized-quiz-game
2. Структура на проекта
bash
Copy code
containerized-quiz-game/
├── docker-compose.yml      # Docker Compose файл за настройка на контейнерите
├── Dockerfile              # Dockerfile за Python приложението
├── setup_questions.sql     # SQL файл за създаване и попълване на въпросите
├── setup_answers.sql       # SQL файл за създаване и попълване на отговорите
├── quiz_game.py            # Python скрипт за играта
└── README.md               # Документация на проекта
3. Стартиране на контейнерите
Стартирай всички контейнери (бази данни и Python приложението) с една команда:

bash
Copy code
docker-compose up --build
Това ще:

Създаде и стартира два PostgreSQL контейнера:
questions_db (на порт 5433)
answers_db (на порт 5434)
Изгради и стартира Python приложението в контейнер quiz_app.
4. Инициализиране на базите данни
След стартиране на контейнерите, трябва да изпълниш SQL файловете, за да добавиш въпроси и отговори:

За въпросите:
bash
Copy code
docker cp setup_questions.sql questions_db:/setup_questions.sql
docker exec -it questions_db psql -U postgres -d questions_db -f /setup_questions.sql
За отговорите:
bash
Copy code
docker cp setup_answers.sql answers_db:/setup_answers.sql
docker exec -it answers_db psql -U postgres -d answers_db -f /setup_answers.sql
5. Стартиране на играта
Python приложението ще се стартира автоматично в контейнера quiz_app. За да видиш изхода, можеш да провериш логовете на контейнера:

bash
Copy code
docker logs -f quiz_app
Конфигурация
Файлове на базите данни
setup_questions.sql:
Създава таблицата за въпросите и добавя данни:

sql
Copy code
CREATE TABLE IF NOT EXISTS questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL
);

INSERT INTO questions (question)
VALUES
('What is the capital of France?'),
('What is 2 + 2?'),
('Which planet is known as the Red Planet?');
setup_answers.sql:
Създава таблицата за отговорите и добавя данни:

sql
Copy code
CREATE TABLE IF NOT EXISTS answers (
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
Python Конфигурация
Python приложението се свързва към контейнерите на базите данни чрез следните настройки:

python
Copy code
DB_CONFIG_QUESTIONS = {
    "dbname": "questions_db",
    "user": "postgres",
    "password": "questions_pass",
    "host": "questions_db",  # Името на контейнера
    "port": "5432",
}

DB_CONFIG_ANSWERS = {
    "dbname": "answers_db",
    "user": "postgres",
    "password": "answers_pass",
    "host": "answers_db",  # Името на контейнера
    "port": "5432",
}
Тест и Поддръжка
Проверка на Контейнерите
Увери се, че всички контейнери работят:

bash
Copy code
docker ps
Спиране на Контейнерите
За да спреш всички контейнери:

bash
Copy code
docker-compose down
Бъдещи Подобрения
Добавяне на уеб интерфейс за играта.
REST API за по-лесна комуникация с базите данни.
Логване на резултатите от играта в отделна база данни.