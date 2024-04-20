# Fox_Paper - Research Portal


## Project Overview
Welcome to the Fox Paper! This portal is designed to serve as a platform for managing and accessing research papers, articles, and related resources. Whether you are a researcher, student, or enthusiast, this portal aims to provide a centralized and user-friendly interface for discovering and organizing research materials.

## Features
1. User Registration: Users can register on the platform by providing essential details like email, phone number, password, name.

2. User Authentication: Utilizing JWT (JSON Web Tokens), the project ensures secure and seamless authentication for registered users.

3. User Profile Management: Authenticated users can update their personal information, including phone number, name, and city.

4. Research Paper Management: Users can create, update, and delete research papers, including details like title, author, publication date, and category.

5. Research Paper Search: Users can search for research papers based on title, author, publication date, and category.

6. Research Paper Comments: Users can add comments to research papers, providing feedback, insights, and additional information.

7. Research Paper Ratings: Users can rate research papers based on their quality, relevance, and significance.

8. Research Paper Favorites: Users can add research papers to their favorites list for easy access and reference.

9. Research Paper Categories: Users can browse research papers based on categories like Computer Science, Mathematics, Physics, and more.

10. Moderator Role: Moderators can review, approve, reject, and flag research papers based on quality, relevance, and compliance.

11. Moderator Dashboard: Moderators have access to a dedicated dashboard for managing research papers, comments, ratings, and user activity.


## Technology Stack
* FastAPI: A modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.

* SQLAlchemy: A powerful and flexible SQL toolkit and Object-Relational Mapping (ORM) library for Python.

* Alembic: A lightweight database migration tool for usage with SQLAlchemy.

* Docker: Containerization for easy deployment and consistent environments.


## Project Structure
```bash
.
├── Dockerfile
├── README.md
├── alembic
│   ├── README
│   ├── env.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   ├── src
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── category.py
│   │   │   ├── comment.py
│   │   │   ├── file.py
│   │   │   ├── id_abc.py
│   │   │   ├── research.py
│   │   │   ├── role.py
│   │   │   └── user.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   │   ├── repositories
│   │   │   │   ├── __init__.py
│   │   │   │   ├── categories.py
│   │   │   │   ├── comments.py
│   │   │   │   ├── researches.py
│   │   │   │   └── users.py
│   │   │   ├── schemas
│   │   │   │   ├── __init__.py
│   │   │   │   ├── comments.py
│   │   │   │   ├── researches.py
│   │   │   │   └── users.py
│   │   │   ├── services
│   │   │   │   ├── __init__.py
│   │   │   │   ├── moderators.py
│   │   │   │   ├── researches.py
│   │   │   │   └── users.py
│   │   │   └── views
│   │   │       ├── __init__.py
│   │   │       ├── auth.py
│   │   │       ├── comments.py
│   │   │       ├── moderators.py
│   │   │       ├── researches.py
│   │   │       └── users.py
│   │   └── utils.py
├── docker-compose.yml
├── requirements.txt
└── scripts
    └── launch.sh
```


## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Bayashat/fox_paper_api
cd fox_paper_api
```

Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
```

Activate the virtual environment:

* Windows:
```bash
.venv\Scripts\activate
```

* macOS/Linux:
```bash
source .venv/bin/activate
```

Install the project dependencies:
```bash
pip install -r requirements.txt
```

## Database Setup

Migrate the database using Alembic:

```bash
alembic upgrade head
```

## Running the API

Run the FastAPI application:

```bash
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000.

## API Endpoints

### User Authentication
* `POST /auth/signup`: Register a new user.
* `POST /auth/login`: Authenticate a user and generate a JWT token.

### User Management
* `GET /users/`: Get list of users
* `GET /users/{id}`: Retrieve details of a user.
* `PUT /users/{id}`: Modify details of a user.
* `DELETE /users/{id}`: Delete a user.

### Research Paper Management
* `GET /researches/`: Get list of research papers.
* `POST /researches/`: Create a new research paper.
* `GET /researches/{id}`: Retrieve details of a research paper.
* `PUT /researches/{id}`: Modify details of a research paper.
* `DELETE /researches/{id}`: Delete a research paper.

### Research Paper Comments
* `GET /researches/{id}/comments/`: Get list of comments for a research paper.
* `POST /researches/{id}/comments/`: Add a new comment to a research paper.
* `GET /researches/{id}/comments/{comment_id}`: Retrieve details of a comment.  
* `DELETE /researches/{id}/comments/{comment_id}`: Delete a comment.

### Moderator Actions
* `GET /moderators/researches/pending`: Get list of pending research papers.
* `PUT /moderators/researches/{id}/review`: Review a research paper.
* `PUT /moderators/researches/{id}/publish`: Publish a research paper.
* `PUT /moderators/researches/{id}/reject`: Reject a research paper.
* `GET /moderators/researches/published`: Get list of published research papers.

## Docker
Build the Docker image:
```bash
docker-compose up -d --build
```

The API will be available at http://0.0.0.0:8080.

## Author
Tokmukamet Bayashat