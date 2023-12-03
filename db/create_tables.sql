CREATE TABLE questions (
    id INT PRIMARY KEY,
    subject VARCHAR(255),
    type VARCHAR(255),
    difficulty VARCHAR(255),
    description TEXT
);

CREATE TABLE question_options (
    id INT PRIMARY KEY,
    question_id INT,
    description VARCHAR(255),
    FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE question_answers (
    id INT PRIMARY KEY,
    question_id INT,
    option_id INT,
    FOREIGN KEY (question_id) REFERENCES questions(id),
    FOREIGN KEY (option_id) REFERENCES question_options(id)
);

CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

