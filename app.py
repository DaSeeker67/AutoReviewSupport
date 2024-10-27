import streamlit as st
from transformers import pipeline

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_and_reply(review):
    sentiment_result = sentiment_analyzer(review)[0]
    sentiment = sentiment_result['label']
    confidence = sentiment_result['score']
    if sentiment == 'POSITIVE':
        reply = "Thank you for your kind words! We are thrilled to hear you enjoyed your experience. Your satisfaction is our priority!"
    elif sentiment == 'NEGATIVE':
        reply = "We are sorry to hear about your experience. We value your feedback and will work to improve. Please feel free to reach out to discuss further."
    else:
        reply = "Thank you for sharing your experience. We appreciate your feedback and are here to help make your next visit even better."

    return reply, sentiment, confidence
st.title("Customer Review Sentiment Analyzer")
st.write("Enter a customer review below to receive a response based on the sentiment.")

# Input area for review
user_review = st.text_area("Enter customer review:", "")

# Button to process the review
if st.button("Analyze and Reply"):
    if user_review.strip(): 
        reply, sentiment, confidence = analyze_and_reply(user_review)
        
        # Display the results
        st.subheader("Analysis Result")
        st.write(f"**Detected Sentiment:** {sentiment}")
        st.write(f"**Confidence Score:** {confidence:.2f}")
        st.subheader("Generated Reply")
        st.write(reply)
    else:
        st.write("Please enter a review to analyze.")
