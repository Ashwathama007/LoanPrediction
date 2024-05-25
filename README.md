---
# Loan Prediction Application in Django

This is a simple web application built with Django for predicting loan eligibility based on user inputs. The application takes into consideration various factors such as education status, employment status, annual income, loan amount, loan terms, CIBIL score, and total assets. 

## Features

- **User-Friendly Interface**: Clean and intuitive form layout for easy data input.
- **Data Validation**: Ensures all inputs are provided and within specified ranges (e.g., CIBIL score between 300 and 900).
- **Real-time Predictions**: Provides instant feedback on loan eligibility based on the input data.

## Form Fields

- **Graduate**: Indicates if the user is a graduate.
- **Employed**: Indicates if the user is currently employed.
- **Annual Income**: User's annual income.
- **Loan Amount**: Desired loan amount.
- **Loan Terms**: Duration of the loan in months.
- **CIBIL Score**: User's CIBIL credit score (ranging from 300 to 900).
- **Total Assets**: Total assets owned by the user.

## Usage

1. Clone the repository.
2. Install dependencies.
3. Run the Django development server.
4. Navigate to the application in your web browser and fill out the form to predict loan eligibility.

## Installation

1. Clone this repository:
    ```sh
    git clone https://github.com/yourusername/loan-prediction-app.git
    ```
2. Navigate to the project directory:
    ```sh
    cd loan-prediction-app
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Django development server:
    ```sh
    python manage.py runserver
    ```
5. Open your web browser and go to `http://127.0.0.1:8000` to use the application.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

---
