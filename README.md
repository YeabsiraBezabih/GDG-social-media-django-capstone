# Django Social Media App - Capstone Project

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Project Description

This project is a Django-based social media application designed as a capstone project.  It provides users with a platform to connect, share posts, and interact with each other through features like likes, comments, user profiles, and a follow system. The application is built with a RESTful API backend using Django REST Framework (DRF), making it suitable for consumption by web and mobile frontends in the future.

This project aims to deliver a Minimum Viable Product (MVP) within a two-week timeframe, focusing on core functionalities as defined in the [Software Requirements Specification (SRS) document](https://docs.google.com/document/d/1dHQ8spuqU2ITR3dGEpkIKDXdbOXGj-4HhbJJLwGRxS4/edit?usp=sharing).

## Team Members

**Group Lead:** Yeabsira Bezabih - Project Management, Backend Architecture, API Design, Documentation Oversight

**Team Members:**

*   **Alhamdu Desalegn:** User Authentication & Authorization
*   **Kibrom Nasir:** User Profiles
*   **Sosina Ayele Nega:** Posts Functionality
*   **Natnael Asfaw:** Interactions (Likes & Comments)
*   **Hiruy Habtamu Debalkie:** Follow System & API Documentation

## Table of Contents

1.  [Getting Started](#getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
    *   [Database Setup](#database-setup)
    *   [Running the Development Server](#running-the-development-server)
2.  [Features](#features)
3.  [API Endpoints](#api-endpoints)
4.  [Technology Stack](#technology-stack)
5.  [Project Structure](#project-structure)
6.  [Contributing](#contributing)
7.  [License](#license)
8.  [Contact](#contact)

## Getting Started

Follow these instructions to get the project up and running on your local machine for development and testing.

### Prerequisites

*   **Python:** Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
*   **pip:** Python package installer (usually included with Python installations).
*   **Git:**  Git is required for version control. Install it from [git-scm.com](https://git-scm.com/downloads).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YeabsiraBezabih/GDG-social-media-django-capstone.git
    cd GDG-social-media-django-capstone
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **On Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **On Windows:**
        ```bash
        venv\Scripts\activate
        ```

4.  **Install project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
### Database Setup

This project is initially configured to use SQLite.

1.  **Apply database migrations:**
    ```bash
    python manage.py migrate
    ```
    This command creates the database tables based on your Django models.

### Running the Development Server

1.  **Start the Django development server:**
    ```bash
    python manage.py runserver
    ```

2.  **Access the application:** Open your web browser and go to `http://127.0.0.1:8000/`.  (The API endpoints will be accessible under `/api/` path, as defined in your URL configurations).

## Features

The Django Social Media App MVP includes the following core features:

*   **User Authentication:**
    *   User registration with email and password.
    *   Secure login and logout using JWT authentication.
*   **User Profiles:**
    *   Users can create and edit their profiles (bio and personal details).
    *   Users can view other users' profiles.
*   **Posts:**
    *   Users can create, edit, and delete text-based posts (image support may be added later if time permits).
    *   Posts include timestamps for creation and updates.
*   **Interactions:**
    *   Users can like and unlike posts.
    *   Users can comment on posts.
*   **Follow System:**
    *   Users can follow and unfollow other users.
    *   Users can view lists of followers and users they are following (stretch goal for MVP if time is limited).
*   **API Documentation:**
    *   API documentation will be generated using Swagger or Postman for easy testing and integration.

For detailed feature specifications, please refer to the [SRS document](https://docs.google.com/document/d/1dHQ8spuqU2ITR3dGEpkIKDXdbOXGj-4HhbJJLwGRxS4/edit?usp=sharing).

## API Endpoints

The backend exposes a RESTful API with the following main endpoint categories:

*   **/api/auth/**: User authentication endpoints (register, login, logout).
*   **/api/users/**: User profile management endpoints.
*   **/api/posts/**: Post creation, retrieval, update, and deletion endpoints.
*   **/api/posts/{post_id}/like/**:  Post liking endpoint.
*   **/api/posts/{post_id}/comment/**: Post commenting endpoint.
*   **/api/users/{user_id}/follow/**: User following/unfollowing endpoints.

For detailed API endpoint specifications, including request bodies and response formats, please refer to the [SRS document](https://docs.google.com/document/d/1dHQ8spuqU2ITR3dGEpkIKDXdbOXGj-4HhbJJLwGRxS4/edit?usp=sharing) and the API documentation (Swagger/Postman) that will be generated as part of the project.

## Technology Stack

*   **Backend Framework:** [Django](https://www.djangoproject.com/)
*   **REST API Framework:** [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
*   **Database (Initial MVP):** [SQLite](https://www.sqlite.org/) (Intended to be upgraded to PostgreSQL in future versions)
*   **Authentication:** [JWT (JSON Web Tokens)](https://jwt.io/)
*   **API Documentation:** [Swagger](https://swagger.io/) / [Postman](https://www.postman.com/)
*   **Version Control:** [Git](https://git-scm.com/) & [GitHub](https://github.com/)
*   **Programming Language:** [Python](https://www.python.org/)

## Project Structure

```
django-social-media-app/
├── backend/                # Django project root directory
│   ├── api/                # Django app for API functionalities
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py       # Database models (User, Post, Comment, Like, Follow)
│   │   ├── serializers.py  # DRF serializers for API data transformation
│   │   ├── views.py        # DRF views for API logic
│   │   ├── urls.py         # API endpoint URLs
│   │   └── ...
│   ├── backend/            # Django project settings and core files
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py     # Project settings (database, authentication, etc.)
│   │   ├── urls.py         # Project-level URLs (including API URLs)
│   │   └── wsgi.py
│   ├── manage.py           # Django management script
├── venv/                   # Virtual environment directory (not tracked in Git)
├── requirements.txt        # Project dependencies
├── README.md               # Project README file (this file)
├── .gitignore              # Git ignore file
└── ...
```

## Contributing

We encourage contributions from all team members! Please follow these guidelines when contributing to the project:

1.  **Branching:** Always create a new branch for your work based on the `main` branch. Use descriptive branch names like `feature/user-profiles` or `bugfix/authentication-issue`.  **Never commit directly to the `main` branch.**

2.  **Git Workflow:**
    *   **Sync with `main`:** Before starting any work, sync your local `main` branch with the remote `main` and create your feature branch from the updated `main`.
    *   **Commit Frequently:** Make small, logical commits with clear commit messages.
    *   **Push Regularly:** Push your branch to the remote repository frequently.
    *   **Pull Requests (PRs):** When your feature or bug fix is ready, create a Pull Request on GitHub to merge your branch into `main`.

3.  **Code Review:** All code contributions will be reviewed via Pull Requests by the group lead before being merged into the `main` branch. Please be responsive to feedback and participate in code reviews.

4.  **Coding Standards:**  Follow Python and Django coding best practices. Aim for clean, readable, and well-commented code.

For more detailed Git workflow instructions, please refer to the team communication channels.

## License

This project is licensed under the [MIT License](LICENSE) - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues regarding this project, please contact:

Yeabsira Bezabih (Group Lead) - yeabsirabezabih791@gmail.com

---

**Last Updated:** April 14, 2025 