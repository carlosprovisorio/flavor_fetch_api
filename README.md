# Recipe REST API - # flavor_fetch_api

This project is a backend REST API built using **Python**, **Django (3.2)**, **Django REST Framework (3.12)**, **Docker**, and **Postgres**, following **Test Driven Development (TDD)** principles. The API allows users to manage recipes, including features like filtering, uploading images, and more.

## Features

The goal of this project is to create a recipe management system that can be leveraged by both web and mobile applications, offering functionalities such as:

- **User Authentication**: Secure sign-up and login functionality for users.
- **Recipe Management**: Add recipes with titles, price points, cooking times, ingredients, and tags such as “comfort food”, “vegan”, or “dessert”.
- **Filtering and Sorting**: Sort and filter recipes based on various fields (e.g., price, tags).
- **Image Uploading**: Upload and view images related to recipes.
- **Django Admin Customization**: Leverage the built-in Django admin interface for managing users and recipes.

## Tech Stack

- **Python**
- **Django & Django REST Framework**
- **Docker & Docker-Compose**
- **PostgreSQL**
- **GitHub Actions** for CI/CD
- **Test Driven Development (TDD)** using Django's test framework

## Objectives

To develop a fully functional REST API that includes:

- **User Authentication**: A fully implemented authentication system using Django's built-in user management.
- **Creating Objects**: Users can create and manage recipes.
- **Filtering and Sorting**: Implement filters and sorting on recipe attributes (e.g., price, tags).
- **Image Uploading**: Handle media files for recipe images.
- **Unit Testing**: All major functionalities are covered by unit tests.

## Key Points

- Setting up a project with **Docker** and **Docker-Compose** for development and production environments.
- Configuring **GitHub Actions** for Continuous Integration (CI), including linting and running unit tests automatically.
- Writing unit tests using the **Django Test Framework** and applying **Test Driven Development** principles.
- Handling media files (e.g., images) with Django’s file upload system.
- Configuring and connecting to a **PostgreSQL** database.
- Customizing the **Django Admin** interface for better management of recipes and users.

## Setup Instructions

### Prerequisites

- **Docker** and **Docker-Compose** installed on your system.
- **Git** for version control.

### Clone the repository

```bash
git clone https://github.com/yourusername/flavor_fetch_api.git
```
