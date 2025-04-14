# Django Social Media App

A RESTful social media application built with Django and Django REST Framework.

## Features

- User authentication (register, login, logout)
- User profiles
- Create, edit, and delete posts
- Like/unlike posts
- Comment on posts
- Follow/unfollow users
- View feed of followed users' posts

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- POST `/api/auth/register/` - Register a new user
- POST `/api/auth/login/` - Login and get JWT tokens
- POST `/api/auth/logout/` - Logout (invalidate refresh token)

### Users
- GET `/api/users/` - List all users
- GET `/api/users/{id}/` - Get user details
- PUT `/api/users/{id}/` - Update user profile
- POST `/api/users/{id}/follow/` - Follow a user
- POST `/api/users/{id}/unfollow/` - Unfollow a user

### Posts
- GET `/api/posts/` - List posts from followed users
- POST `/api/posts/` - Create a new post
- GET `/api/posts/{id}/` - Get post details
- PUT `/api/posts/{id}/` - Update a post
- DELETE `/api/posts/{id}/` - Delete a post
- POST `/api/posts/{id}/like/` - Like a post
- POST `/api/posts/{id}/unlike/` - Unlike a post

### Comments
- GET `/api/posts/{post_id}/comments/` - List comments on a post
- POST `/api/posts/{post_id}/comments/` - Add a comment to a post
- GET `/api/posts/{post_id}/comments/{id}/` - Get comment details
- PUT `/api/posts/{post_id}/comments/{id}/` - Update a comment
- DELETE `/api/posts/{post_id}/comments/{id}/` - Delete a comment

## Authentication

The API uses JWT (JSON Web Tokens) for authentication. Include the access token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## License

MIT 