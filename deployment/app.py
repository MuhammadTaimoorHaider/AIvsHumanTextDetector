"""
Flask Web Application for AI vs Human Text Classification
"""

from flask import Flask, render_template, request, jsonify
import joblib
import re
import os

app = Flask(__name__)

# Load model and vectorizer
# For PythonAnywhere, use absolute paths
# Update 'yourusername' with your actual PythonAnywhere username
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'best_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'tfidf_vectorizer.pkl')

# Alternative: If models are in parent directory
if not os.path.exists(MODEL_PATH):
    MODEL_PATH = os.path.join(os.path.dirname(BASE_DIR), 'models', 'best_model.pkl')
    VECTORIZER_PATH = os.path.join(os.path.dirname(BASE_DIR), 'models', 'tfidf_vectorizer.pkl')

print("Loading model and vectorizer...")
print(f"Model path: {MODEL_PATH}")
print(f"Vectorizer path: {VECTORIZER_PATH}")
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    print("✅ Model and vectorizer loaded successfully!")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    model = None
    vectorizer = None

def clean_text(text):
    """
    Clean and preprocess text data
    """
    # Convert to string
    text = str(text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    
    # Remove email addresses
    text = re.sub(r'\S+@\S+', '', text)
    
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    
    # Remove extra whitespaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

@app.route('/')
def home():
    """Home page"""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Prediction endpoint"""
    try:
        # Get text from request
        data = request.get_json()
        text = data.get('text', '')
        
        if not text or len(text.strip()) == 0:
            return jsonify({
                'error': 'Please provide some text to classify'
            }), 400
        
        # Check if model is loaded
        if model is None or vectorizer is None:
            return jsonify({
                'error': 'Model not loaded. Please check server configuration.'
            }), 500
        
        # Preprocess text
        cleaned_text = clean_text(text)
        
        if len(cleaned_text.strip()) == 0:
            return jsonify({
                'error': 'Text contains no valid words after preprocessing'
            }), 400
        
        # Vectorize text
        text_vectorized = vectorizer.transform([cleaned_text])
        
        # Make prediction
        prediction = model.predict(text_vectorized)[0]
        
        # Get probability if available
        if hasattr(model, 'predict_proba'):
            probabilities = model.predict_proba(text_vectorized)[0]
            confidence = float(max(probabilities) * 100)
            prob_human = float(probabilities[0] * 100)
            prob_ai = float(probabilities[1] * 100)
        else:
            confidence = 100.0
            prob_human = 100.0 if prediction == 0 else 0.0
            prob_ai = 100.0 if prediction == 1 else 0.0
        
        # Prepare response
        result = {
            'prediction': int(prediction),
            'label': 'Human-Written' if prediction == 0 else 'AI-Generated',
            'confidence': round(confidence, 2),
            'probabilities': {
                'human': round(prob_human, 2),
                'ai': round(prob_ai, 2)
            },
            'text_length': len(text),
            'word_count': len(text.split()),
            'cleaned_text_preview': cleaned_text[:100] + '...' if len(cleaned_text) > 100 else cleaned_text
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({
            'error': f'Prediction error: {str(e)}'
        }), 500

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'vectorizer_loaded': vectorizer is not None
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
