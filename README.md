# LaunderEase - Laundry Management System 

Laundry Management System (LMS) is a Python-based application. It helps manage laundry services for students living in hostels.

## Overview

The project aims to create a user-friendly system for students to place laundry orders and for administrators to manage these orders efficiently. It provides separate dashboards for both students and administrators with different functionalities.

## Features

- **Login:**
  - Separate login interfaces for administrators and students.
  - Separate authentication process for accessing respective dashboards.

- **Admin Dashboard:**
  - View and manage student requests.
  - Mark requests as completed.
  - View student contact details.

- **Student Dashboard:**
  - Place laundry orders.
  - View order status.
  - Access support and instructions.

## Technologies Used

- **Python:** The core programming language used for backend logic.
- **Tkinter:** Python's standard GUI (Graphical User Interface) library used for building the application's interface.
- **MySQL:** Relational database management system used for storing application data.
- **Pillow:** Python Imaging Library used for image processing and displaying images in the application.
- **GitLab:** Version control platform used for collaboration and project management.

## File Structure
- **Main Script (main.py):** The main Python script for running the application.
- **SQL Queries (sql_queries.txt):** Contains SQL queries for creating database tables.
- **Images:**
  - **admin_logo.jpg:** Image used for the admin interface.
  - **student_logo.png:** Image used for the student interface.

## Installation

- Clone the repository
- Run the sql queries provided in sql_queries.txt for creating necessary tables.
- Installing dependencies in terminal after opening the folder: <br> pip install pillow <br> pip install mysql-connector-python.
- Run the application by typing "python main.py" command
