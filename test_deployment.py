"""
Test Script for AI vs Human Text Classifier Deployment
Run this locally to test if your deployment is working
"""

import requests
import json

# Replace with your PythonAnywhere URL
BASE_URL = "https://muhammadtaimoorhaider.pythonanywhere.com"

def test_health():
    """Test the health endpoint"""
    print("=" * 60)
    print("Testing Health Endpoint...")
    print("=" * 60)
    try:
        response = requests.get(f"{BASE_URL}/health", timeout=10)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_prediction(text, label):
    """Test the prediction endpoint"""
    print("\n" + "=" * 60)
    print(f"Testing: {label}")
    print("=" * 60)
    print(f"Text: {text[:100]}...")
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json={"text": text},
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n✅ Prediction: {result['label']}")
            print(f"   Confidence: {result['confidence']}%")
            print(f"   Human Probability: {result['probabilities']['human']}%")
            print(f"   AI Probability: {result['probabilities']['ai']}%")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

# Test samples
HUMAN_TEXT = """
Hey everyone! I just got back from an amazing trip to Japan. The food was 
absolutely incredible - I must have eaten my weight in sushi and ramen! 
Tokyo was so busy and energetic, but Kyoto was peaceful and beautiful. 
The cherry blossoms were in full bloom and it was just magical. I can't 
wait to go back next year. Has anyone else been to Japan? What were your 
favorite spots?
"""

AI_TEXT = """
Artificial intelligence represents a transformative technology that has 
fundamentally altered numerous aspects of modern society. Machine learning 
algorithms process vast quantities of data to identify patterns and generate 
predictions with remarkable accuracy. These systems utilize neural networks 
that mimic human cognitive processes, enabling them to perform complex tasks 
such as natural language processing, computer vision, and predictive analytics. 
The implementation of AI technologies continues to expand across various 
industries, including healthcare, finance, and transportation.
"""

ANOTHER_HUMAN_TEXT = """
OMG, I can't believe what just happened! I was at the grocery store, minding 
my own business, when I ran into my high school crush. We haven't seen each 
other in like 10 years! We ended up talking for almost an hour in the cereal 
aisle. He seems really nice and gave me his number. Should I text him? I'm so 
nervous lol. My friends think I should definitely reach out, but I don't want 
to seem too eager. What would you guys do?
"""

def main():
    print("\n" + "=" * 60)
    print("AI vs HUMAN TEXT CLASSIFIER - DEPLOYMENT TEST")
    print("=" * 60)
    print(f"Testing URL: {BASE_URL}")
    print("=" * 60)
    
    # Test health endpoint
    health_ok = test_health()
    
    if not health_ok:
        print("\n❌ Health check failed. App may not be running.")
        print("   Check your PythonAnywhere error logs.")
        return
    
    print("\n✅ Health check passed!")
    
    # Test predictions
    results = []
    results.append(test_prediction(HUMAN_TEXT, "Human Text Sample 1"))
    results.append(test_prediction(AI_TEXT, "AI Text Sample"))
    results.append(test_prediction(ANOTHER_HUMAN_TEXT, "Human Text Sample 2"))
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print(f"Total Tests: {len(results)}")
    print(f"Passed: {sum(results)}")
    print(f"Failed: {len(results) - sum(results)}")
    
    if all(results):
        print("\n🎉 All tests passed! Your deployment is working perfectly!")
    else:
        print("\n⚠️  Some tests failed. Check the error messages above.")
    
    print("\n" + "=" * 60)
    print(f"Visit your app: {BASE_URL}")
    print("=" * 60)

if __name__ == "__main__":
    main()
