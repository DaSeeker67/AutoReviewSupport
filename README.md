# AutoReviewSupport

# Customer Review Sentiment Analyzer

This project provides a simple web interface using Streamlit that takes customer reviews as input, analyzes their sentiment, and generates an appropriate response. This tool can be useful for businesses looking to automate responses to customer feedback based on sentiment (positive, negative, or neutral).

## Overview

The application:
1. Takes a customer review as input.
2. Analyzes the sentiment of the review using a sentiment analysis model.
3. Returns a sentiment-based response, tailoring responses to positive, negative, and neutral feedback.

## Approach

The project leverages the following approach:

1. **Sentiment Analysis**: 
   - We use Hugging Face's `transformers` library to load a pre-trained sentiment analysis pipeline.
   - Each review is passed through this pipeline, which returns a sentiment label (positive, negative, or neutral) and a confidence score for the prediction.

2. **Response Generation**:
   - Based on the detected sentiment, the app generates a tailored response:
     - **Positive Sentiment**: Returns a message of appreciation.
     - **Negative Sentiment**: Returns an apologetic response and an offer to improve.
     - **Neutral Sentiment**: Returns a thank-you message for the feedback.
   
3. **Frontend**: 
   - Built using Streamlit, allowing users to interact with the model by entering reviews and receiving real-time feedback responses.

## Project Structure

- **app.py**: Main application file containing code to load the sentiment model, analyze input reviews, generate responses, and display them on the Streamlit interface.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd customer-review-sentiment-analyzer
2. **Install Required Libraries & Access the App**:

Ensure that Python is installed on your machine. Then, install the required libraries using pip:
   ```bash
    pip install -r requirenments.txt
    streamlit run app.py

![image](https://github.com/user-attachments/assets/fc771467-30b4-45fa-874e-3523978c0204)


![image](https://github.com/user-attachments/assets/9c6c7d5f-bc2a-4b2a-98d1-fbfab1abb50e)


![image](https://github.com/user-attachments/assets/b3efac1d-b417-4700-9c43-2f3ac53b34e6)


![image](https://github.com/user-attachments/assets/e05f2628-60b6-41e4-9f0a-fa0df870f1c8)

