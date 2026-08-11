# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API with FastAPI by creating routes, handling JSON data, and using validation to make the service reliable and easy to test.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI App

#### Description
Create a FastAPI application that exposes a simple API for managing items such as products or tasks.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn in the project environment
- Create an app instance and define a root endpoint that returns a welcome message
- Add a `GET /items` endpoint that returns a list of sample items
- Run the app locally and confirm it responds correctly

### 🛠️ Implement CRUD Endpoints

#### Description
Expand the API so it can create, read, update, and delete items through HTTP requests.

#### Requirements
Completed program should:

- Define a request model for item data using Pydantic
- Implement `POST /items` to add a new item
- Implement `GET /items/{item_id}` to retrieve one item by ID
- Implement `PUT /items/{item_id}` to update an existing item
- Implement `DELETE /items/{item_id}` to remove an item
- Return appropriate HTTP status codes for success and not-found cases

### 🛠️ Add Validation and Interactive Docs

#### Description
Improve the API with validation and documentation so it is easier to use and understand.

#### Requirements
Completed program should:

- Use response models to structure API responses clearly
- Add validation rules for required fields and sensible value ranges
- Include helpful endpoint descriptions or docstrings
- Open the generated `/docs` page to verify the interactive documentation works
