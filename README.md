# Fox_Paper - Research Portal


## Project Overview
Welcome to Fox Paper, a cutting-edge platform designed for the management and discovery of research papers, articles, and academic resources. Tailored for researchers, students, educators, and enthusiasts, Fox Paper offers a centralized, user-friendly interface for accessing a wide range of scholarly materials.

## Key Features
* User Registration:  Sign up with essential information such as email, phone number, and password.

* Secure User Authentication: Utilizes JWT (JSON Web Tokens) to ensure secure access.

* User Role Management: Supports predefined roles including 'User' and 'Moderator', allowing for differentiated access and functionalities.

* Profile Management: Users can update personal information such as phone number, name, date of birth.

* Research Management: Create, update, view, and delete research entries, enhancing academic collaboration and resource sharing.

* File Upload: Allows for independent file uploads with the ability to link these files to research entries post-upload.

* Advanced Search: Filter and search for research papers by title, author, publication date, or category.

* Commenting System: Engage with the community by adding comments to research papers.

* Ratings and Reviews: Rate and review research papers to aid in quality assurance and community engagement.

* Favorites: Bookmark research papers for easy access and reference.

* Categorized Browsing: Navigate through research papers sorted into categories like Science, Technology, Medicine, and more.

* Moderator Dashboard: Specialized dashboard for moderators to approve, reject, and manage submissions ensuring content quality and relevance.

## Technology Stack
* FastAPI: Utilizes this modern, fast web framework for building APIs with Python 3.11, emphasizing on speed and the use of standard Python type hints.

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
│   ├── script.py.mako
│   └── versions
│       ├── 4b8c0642a303_created_all_tables.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── src
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── annotates.py
│   │   │   ├── category.py
│   │   │   ├── comment.py
│   │   │   ├── enums.py
│   │   │   ├── file.py
│   │   │   ├── mixins.py
│   │   │   ├── research.py
│   │   │   ├── role.py
│   │   │   └── user.py
│   │   ├── routers
│   │   │   ├── __init__.py
│   │   │   ├── repositories
│   │   │   │   ├── __init__.py
│   │   │   │   ├── categories.py
│   │   │   │   ├── comments.py
│   │   │   │   ├── file.py
│   │   │   │   ├── researches.py
│   │   │   │   └── users.py
│   │   │   ├── schemas
│   │   │   │   ├── __init__.py
│   │   │   │   ├── auth.py
│   │   │   │   ├── comments.py
│   │   │   │   ├── researches.py
│   │   │   │   └── users.py
│   │   │   ├── services
│   │   │   │   ├── __init__.py
│   │   │   │   ├── category.py
│   │   │   │   ├── comment.py
│   │   │   │   ├── db.py
│   │   │   │   ├── file.py
│   │   │   │   ├── researches.py
│   │   │   │   └── users.py
│   │   │   └── views
│   │   │       ├── __init__.py
│   │   │       ├── auth.py
│   │   │       ├── comments.py
│   │   │       ├── moderators.py
│   │   │       ├── researches.py
│   │   │       └── users.py
│   │   └── uploads
│   └── test
│       ├── __init__.py
│       ├── config
│       │   ├── __init__.py
│       │   └── database_test_config.py
│       ├── templates
│       │   └── __init__.py
│       ├── test_api
│       │   └── __init__.py
│       └── test_jwt.py
├── docker-compose.yml
├── requirements.txt
└── scripts
    ├── entrypoint.sh
    └── wait-for-it.sh
```

## Environment Setup
Before running the application, you need to set up the environment variables which are crucial for connecting to the database and securing the application. Create a .env file in the root directory of the project and populate it with the following keys:

```plaintext
DB_HOST=localhost
DB_PORT=5432
DB_USER=your_username
DB_PASS=your_password
DB_NAME=fox_paper
SECRET_KEY=your_secret_key
ALGORITHM=HS256
```
* Important:
    - `DB_HOST`: The hostname where your database is running.
    - `DB_PORT`: The port on which your database server is listening.
    - `DB_USER`: The username used to access the database.
    - `DB_PASS`: The password for the database user.
    - `SECRET_KEY`: A secret key used for securely signing the JWTs.
    - `ALGORITHM`: The algorithm used for encoding the JWTs.

## Installation Instructions

* Clone the repository and navigate to the project directory:
    ```bash
    git clone https://github.com/Bayashat/fox_paper_api
    cd fox_paper_api
    ```

* Set up a virtual environment (recommended):
    - windows
        ```bash
        python -m venv .venv
        .venv\Scripts\activate
        ```
    - macOS/Linux
        ```bash
        python3 -m venv .venv
        source .venv/bin/activate
        ```

* Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Database Setup
Apply migrations with Alembic:

```bash
alembic upgrade head
```

## Running the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```
Access the API at: http://127.0.0.1:8000.

## Docker Usage

Build and run using Docker Compose:

```bash
docker compose up -d --build
```
The API will be available at [http://0.0.0.0:8080.](http://127.0.0.1:8000/docs) (Auto-generated Swagger documentation)

## Author
[Tokmukamet Bayashat](https://t.me/bayashat)
