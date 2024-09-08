# Exercise-Data-Analyzer

## Table of Contents
1. [Introduction](#introduction)
2. [System Architecture](#system-architecture)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Prerequisites](#prerequisites)
6. [Installation](#installation)
7. [Configuration](#configuration)
8. [Usage](#usage)
9. [Code Structure](#code-structure)
10. [API Integration](#api-integration)
11. [Data Flow](#data-flow)
12. [Security Considerations](#security-considerations)
13. [Error Handling](#error-handling)
14. [Testing](#testing)
15. [Performance Considerations](#performance-considerations)
16. [Deployment](#deployment)
17. [Maintenance and Logging](#maintenance-and-logging)
18. [Future Enhancements](#future-enhancements)
19. [Troubleshooting](#troubleshooting)
20. [Contributing](#contributing)
21. [License](#license)
22. [Acknowledgements](#acknowledgements)

## 1. Introduction

The Exercise Tracking API Project is a sophisticated Python-based application designed to seamlessly integrate natural language processing of exercise data with automated logging capabilities. This system leverages the power of the Nutritionix API for exercise analysis and the Sheety API for data persistence in Google Sheets, providing users with a streamlined method to maintain comprehensive exercise records.

## 2. System Architecture

The project follows a client-server architecture, where our Python script acts as the client interfacing with two external APIs:

1. Nutritionix API (Server 1): Processes natural language exercise inputs and returns structured exercise data.
2. Sheety API (Server 2): Interfaces with Google Sheets to persist the processed exercise data.

The system operates in a linear flow: User Input → Nutritionix Processing → Data Structuring → Sheety API → Google Sheets Storage.

## 3. Features

- Natural Language Processing (NLP) of exercise inputs
- Automatic exercise duration and calorie expenditure calculation
- Personalized calculations based on user metrics (gender, weight, height, age)
- Precise datetime stamping of exercise entries
- Secure API authentication using environment variables
- Automated data logging to Google Sheets
- Extensible codebase for future enhancements

## 4. Technologies Used

- Python 3.6+
- Requests library for HTTP operations
- OS module for environment variable management
- Datetime module for timestamp generation
- Nutritionix API v2 for exercise processing
- Sheety API for Google Sheets integration

## 5. Prerequisites

To successfully deploy and run this project, ensure you have the following:

- Python 3.6 or higher installed on your system
- pip package manager
- A Nutritionix API account with API ID and Key
- A Sheety account with API access configured
- A Google account with a prepared Google Sheet for data logging
- Basic understanding of RESTful APIs and JSON data structures

## 6. Installation

Follow these steps to set up the project environment:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/exercise-tracking-api.git
   ```

2. Navigate to the project directory:
   ```
   cd exercise-tracking-api
   ```

3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the required dependencies:
   ```
   pip install requests python-dotenv
   ```

## 7. Configuration

The application relies on environment variables for secure configuration. Set up your environment by creating a `.env` file in the project root with the following structure:

```
API_ID=your_nutritionix_api_id
API_KEY=your_nutritionix_api_key
EX_END=https://trackapi.nutritionix.com/v2/natural/exercise
SHT_END=your_sheety_endpoint_url
BEAR_AUTH=Bearer your_sheety_bearer_token
```

Ensure to replace the placeholder values with your actual API credentials and endpoints.

## 8. Usage

To utilize the Exercise Tracking API:

1. Ensure your virtual environment is activated (if used).
2. Verify all environment variables are correctly set.
3. Execute the script:
   ```
   python exercise_tracker.py
   ```
4. When prompted, input your exercise details in natural language. For example:
   ```
   Which exercise you did today: Ran 5 kilometers in 30 minutes and did 3 sets of 15 pushups
   ```
5. The script will process your input, calculate relevant metrics, and log the data to your configured Google Sheet.

## 9. Code Structure

The main script, `exercise_tracker.py`, is organized into several logical sections:

1. Import statements
2. Environment variable loading
3. Configuration constants
4. API endpoint and header setup
5. User input collection
6. Nutritionix API request construction and execution
7. Response parsing and data extraction
8. Datetime generation for logging
9. Sheety API request construction and execution for each exercise
10. Response printing for verification

## 10. API Integration

### Nutritionix API
- Endpoint: `https://trackapi.nutritionix.com/v2/natural/exercise`
- Method: POST
- Headers: 
  - `x-app-id`: Your Nutritionix App ID
  - `x-app-key`: Your Nutritionix API Key
- Body: JSON object containing query and user metrics

### Sheety API
- Endpoint: Your specific Sheety endpoint
- Method: POST
- Headers:
  - `Authorization`: Bearer token for authentication
- Body: JSON object containing exercise data to be logged

## 11. Data Flow

1. User inputs exercise information
2. Input is sent to Nutritionix API along with user metrics
3. Nutritionix API returns structured exercise data
4. Script processes the response and extracts relevant information
5. Extracted data is formatted with current date and time
6. Formatted data is sent to Sheety API
7. Sheety API logs the data in the specified Google Sheet

## 12. Security Considerations

- All sensitive data (API keys, endpoints) are stored as environment variables
- Bearer token authentication is used for Sheety API requests
- HTTPS is used for all API communications
- User metrics are hardcoded in this version but could be moved to environment variables or user input for increased security

## 13. Error Handling

The current implementation includes basic error handling:

- API response status is checked implicitly by the `requests` library
- Nutritionix API errors will result in an empty or error response
- Sheety API errors are printed to the console for debugging

Future versions should implement more robust error handling and logging.

## 14. Testing

While the current version doesn't include formal tests, here are recommended testing strategies:

1. Unit tests for individual functions (e.g., date formatting, data extraction)
2. Integration tests for API interactions
3. End-to-end tests simulating user input and verifying Google Sheet entries
4. Error case testing with invalid inputs and simulated API failures

## 15. Performance Considerations

- The script processes exercises sequentially, which is suitable for individual use
- For handling larger volumes of data, consider implementing batch processing
- API rate limits should be taken into account for high-frequency usage

## 16. Deployment

This script is designed to run locally. For production deployment, consider:

1. Containerization using Docker for consistent environments
2. Scheduling regular runs using cron jobs or a task scheduler
3. Implementing a simple web interface for easier user interaction
4. Setting up CI/CD pipelines for automated testing and deployment

## 17. Maintenance and Logging

To facilitate ongoing maintenance:

1. Implement comprehensive logging using Python's `logging` module
2. Set up automated alerts for critical errors
3. Regularly update dependencies to patch security vulnerabilities
4. Monitor API usage to stay within rate limits and budget constraints

## 18. Future Enhancements

Potential areas for future development include:

1. User interface (web or mobile app) for easier interaction
2. Support for multiple users with individual profiles
3. Integration with fitness tracking devices for automated input
4. Data visualization and analytics features
5. Expanded error handling and input validation

## 19. Troubleshooting

Common issues and their solutions:

1. API Authentication Errors: Verify environment variables are set correctly
2. Module Import Errors: Ensure all dependencies are installed (`pip install -r requirements.txt`)
3. JSON Parsing Errors: Check API response format and handle potential changes
4. Network Errors: Verify internet connection and API endpoint availability

## 20. Contributing

Contributions to this project are welcome. Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 21. License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 22. Acknowledgements

- [Nutritionix API](https://www.nutritionix.com/business/api) for exercise data processing
- [Sheety](https://sheety.co/) for Google Sheets integration
- All contributors and users of this project
