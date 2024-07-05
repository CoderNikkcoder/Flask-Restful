Flask RESTful API with MongoDB
=============================

This is a Flask application that provides a RESTful API for CRUD operations on a User resource. The application uses MongoDB as the database and is containerized using Docker.

Features
--------

* RESTful API endpoints for CRUD operations on a User resource
* MongoDB database for storing user data
* Dockerized application for easy deployment

API Endpoints
-------------

### GET /users

Returns a list of all users.

### GET /users/:id

Returns the user with the specified ID.

### POST /users

Creates a new user with the specified data.

### PUT /users/:id

Updates the user with the specified ID with the new data.

### DELETE /users/:id

Deletes the user with the specified ID.

Getting Started
---------------

### Prerequisites

* Docker installed on your system

### Running the Application

1. Clone the repository: git clone https://github.com/CoderNikkcoder/Flask-Restful
2. Navigate to the project directory: cd Flask-Restful
3. Build the Docker image: docker-compose build
4. Start the application: docker-compose up
5. Access the API endpoints using a tool like Postman

### Environment Variables

* MONGO_URI: the MongoDB connection URI (default: mongodb://mongo:27017/mydatabase)


[Nikhil Tiwari] ([CoderNikkcoder])
