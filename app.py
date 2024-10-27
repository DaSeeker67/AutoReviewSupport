import streamlit as st
import requests

# API configurations
SENTIMENT_API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": "Bearer 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"}

def query_sentiment(text):
    """Query the Cardiff NLP RoBERTa model for sentiment analysis"""
    try:
        if not text.strip():
            return None
            
   
        response = requests.post(
            SENTIMENT_API_URL,
            headers=headers,
            json={"inputs": text}
        )
        
        if response.status_code != 200:
            st.error(f"API Error: Status code {response.status_code}")
            return None

        result = response.json()
        
        st.write("Raw API Response:", result)
        
        if not result or not isinstance(result, list) or len(result) == 0:
            st.error("Invalid response format from API")
            return None
            
        scores = result[0]
        sentiment_scores = {'NEGATIVE': 0.0, 'NEUTRAL': 0.0, 'POSITIVE': 0.0}
        max_score = 0.0
        max_label = 'NEUTRAL'
        
        for item in scores:
            if 'label' in item and 'score' in item:
                label = item['label']
                score = float(item['score'])
                
                sentiment_scores[label] = score
                
                if score > max_score:
                    max_score = score
                    max_label = label
        
        return {
            'label': max_label,
            'score': max_score,
            'scores': sentiment_scores
        }
        
    except Exception as e:
        st.error(f"Error in sentiment analysis: {str(e)}")
        return None

def generate_response(sentiment, confidence):
    """Generate appropriate response based on sentiment and confidence"""
    responses = {
        'positive': [
            "Thank you for your wonderful feedback! We're delighted to hear about your positive experience.",
            "We truly appreciate your kind words! Thank you for choosing our services.",
            "Your positive review makes our day! We're glad you had a great experience."
        ],
        'negative': [
            "We apologize for not meeting your expectations. Please let us know how we can improve.",
            "We're sorry about your experience. This isn't the level of service we aim to provide.",
            "Thank you for bringing this to our attention. We'd like to make things right."
        ],
        'neutral': [
            "Thank you for your feedback. We appreciate your balanced perspective.",
            "We value your input and are committed to continuous improvement.",
            "Thank you for taking the time to share your thoughts."
        ]
    }
    
    response_index = 0 if confidence > 0.9 else 1 if confidence > 0.7 else 2
    return responses.get(sentiment.lower(), responses['neutral'])[response_index]

def analyze_review(review):
    """Analyze the review and generate appropriate response"""
    sentiment_result = query_sentiment(review)
    
    if sentiment_result is None:
        return {
            'reply': "Unable to analyze the review. Please try again.",
            'sentiment': "ERROR",
            'scores': {'NEGATIVE': 0.0, 'NEUTRAL': 0.0, 'POSITIVE': 0.0},
            'confidence': 0.0
        }
    
    sentiment = sentiment_result['label']
    confidence = sentiment_result['score']
    response = generate_response(sentiment, confidence)
    
    return {
        'reply': response,
        'sentiment': sentiment,
        'scores': sentiment_result['scores'],
        'confidence': confidence
    }

st.title("Advanced Customer Review Sentiment Analyzer")
st.write("Using Cardiff NLP RoBERTa model for enhanced sentiment analysis")

user_review = st.text_area("Enter customer review:", "")

if st.button("Analyze and Generate Response"):
    if user_review.strip():
        with st.spinner("Analyzing sentiment..."):
            result = analyze_review(user_review)
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Sentiment Analysis")
                sentiment_color = {
                    'positive': 'green',
                    'negative': 'red',
                    'neutral': 'blue'
                }.get(result['sentiment'].lower(), 'black')
                
                st.markdown(f"<p style='color: {sentiment_color}'><b>Detected Sentiment:</b> {result['sentiment']}</p>", 
                          unsafe_allow_html=True)
                st.write(f"**Overall Confidence:** {result['confidence']:.2%}")
                
                st.write("**Detailed Sentiment Scores:**")
                for label, score in result['scores'].items():
                    st.progress(score)
                    st.write(f"{label}: {score:.2%}")
            
            with col2:
                st.subheader("Response Preview")
                st.info(result['reply'])
                confidence_level = "High" if result['confidence'] > 0.9 else "Medium" if result['confidence'] > 0.7 else "Low"
                st.write(f"**Confidence Level:** {confidence_level}")
    else:
        st.error("Please enter a review to analyze.")


st.subheader("Try these example reviews:")
example_reviews = {
    "😊 Positive": "The service was excellent! The staff was very friendly and helpful.",
    "😐 Neutral": "The service was okay. Nothing special but it worked.",
    "😟 Negative": "Very disappointed with the service. Many issues to fix."
}

for label, review in example_reviews.items():
    if st.button(label):
        st.text_area("Review text:", review, key=f"example_{label}")

# Sidebar information
with st.sidebar:
    st.header("About this App")
    st.write(""" 
    This sentiment analyzer uses:
    - Cardiff NLP RoBERTa model
    - Custom response templates
    - Confidence-based responses
    
    Sentiment Labels:
    - 🔴 Negative
    - 🔵 Neutral
    - 🟢 Positive
    """)

