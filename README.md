# Flask Web Application

This repository contains a simple Flask web application with multiple functionalities, including string reversal, addition of numbers, and updating user details in a JSON file.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)

---

## Features

- **String Reversal**: Reverse a given string and display the result.
- **Addition of Numbers**: Input two numbers and get their sum.
- **User Management**: Add or update user details (name, age, and city) in a JSON file.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/string-reverse.git
   ```

2. Navigate to the project directory:
   ```bash
   cd string-reverse
   ```

3. Install the required dependencies:


4. Ensure the `data.json` file exists in the project root directory with initial user data.

---

## Usage

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open a browser and go to `http://localhost:3011` to access the application.

---

## Project Structure

```
.
├── app.py          # Main Flask application
├── models.py       # Contains helper functions for string reversal, addition, and JSON update
├── templates/      # HTML templates for the web application
│   ├── index.html  # Homepage
│   ├── results.html # Display results for string reversal
│   ├── add.html    # Form and results for addition
│   ├── user.html   # Form and success message for user update
├── data.json       # JSON file to store user details
├── static/         # Directory for static files (CSS, JS, images, etc.)
├── requirements.txt # Dependencies
└── README.md       # Documentation
```

---

## API Endpoints

### 1. `/`
- **Method**: `GET`
- **Description**: Displays the homepage.

### 2. `/reverse`
- **Method**: `POST`
- **Description**: Reverses the input string.
- **Form Input**:
  - `my_name`: String to be reversed.
- **Response**: Displays the original and reversed strings.

### 3. `/add`
- **Method**: `GET`
- **Description**: Displays the form for number addition.

### 4. `/add-result`
- **Method**: `POST`
- **Description**: Calculates and displays the sum of two numbers.
- **Form Inputs**:
  - `input1`: First number.
  - `input2`: Second number.

### 5. `/new-user`
- **Method**: `GET`
- **Description**: Displays the form to add or update user details.

### 6. `/user-detail`
- **Method**: `POST`
- **Description**: Updates the `data.json` file with new user details.
- **Form Inputs**:
  - `name`: User's name.
  - `age`: User's age.
  - `city`: User's city.

---
