# AI vs Human Text Detector

A production-style NLP project that classifies text as **Human-Written** or **AI-Generated** using machine learning.

Built end-to-end: from exploratory data analysis and feature engineering, through multi-model benchmarking, to a deployed Flask web application for real-time inference.

---

## Problem Statement

AI-generated content is increasingly common in education, publishing, and social media. Reliable detection helps with academic integrity checks, content moderation, and quality control. This project delivers a practical, deployable solution.

---

## Results

| Metric | Score |
|---|---|
| Best Model | LinearSVC (Linear SVM) |
| Test Accuracy | 99.30% |
| Test F1-Score | 0.99297 |
| CV Mean F1 | 0.99398 ± 0.00083 |
| Dataset Size | 44,868 samples |
| Feature Space | 5,000 TF-IDF features (unigrams + bigrams) |

---

## Pipeline Overview

1. **EDA & Preprocessing** — label distribution, text length analysis, cleaning
2. **Feature Extraction** — TF-IDF vectorization (unigrams + bigrams, max 5,000 features)
3. **Model Training** — 12 algorithms benchmarked: Logistic Regression, Random Forest, LinearSVC, RBF SVM, Naive Bayes, KNN, Decision Tree, Gradient Boosting, AdaBoost, Extra Trees, XGBoost, LightGBM
4. **Evaluation** — accuracy, F1-score, confusion matrix, ROC curve, cross-validation
5. **Model Persistence** — best model serialized with joblib
6. **Deployment** — Flask API + web UI for live predictions

---

## Tech Stack

- **Python 3.8+**
- **scikit-learn** — ML algorithms, TF-IDF, evaluation
- **pandas / numpy** — data processing
- **matplotlib / seaborn / wordcloud** — visualization
- **xgboost / lightgbm** — gradient boosting
- **Flask** — inference web app
- **joblib** — model persistence

---

## Repository Structure

```
.
├── AI_vs_Human_Text_Classification.ipynb   # Main notebook (all 7 steps)
├── AIvsHuman.csv                           # Dataset
├── models/
│   ├── best_model.pkl                      # Serialized LinearSVC
│   ├── tfidf_vectorizer.pkl                # Fitted vectorizer
│   ├── model_comparison.csv                # All 12 model scores
│   └── model_metadata.json                 # Model info
├── results/                                # Generated visualizations
│   ├── label_distribution.png
│   ├── text_length_analysis.png
│   ├── wordclouds.png
│   ├── top_tfidf_features.png
│   ├── model_comparison.png
│   ├── confusion_matrix.png
│   └── roc_curve.png
├── deployment/
│   ├── app.py                              # Flask inference app
│   ├── templates/index.html                # Web UI
│   ├── static/style.css                    # Styles
│   ├── requirements.txt
│   └── DEPLOYMENT_GUIDE.md
├── test_deployment.py                      # API smoke test
└── requirements.txt
```

---

## Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/MuhammadTaimoorHaider/AIvsHumanTextDetector.git
cd AIvsHumanTextDetector

# 2. Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## Reproduce Results

1. Open `AI_vs_Human_Text_Classification.ipynb` in Jupyter.
2. Run all cells top to bottom (`Kernel → Restart & Run All`).
3. Trained artifacts will be saved to `models/` and plots to `results/`.

---

## Run the Web App

```bash
cd deployment
pip install -r requirements.txt
python app.py
```

Open `http://localhost:5000` in your browser.

### API

**Health check**
```
GET /health
```

**Classify text**
```
POST /predict
Content-Type: application/json

{
  "text": "Paste any text here and the model will classify it."
}
```

---

## Deployment

See `deployment/DEPLOYMENT_GUIDE.md` for full PythonAnywhere setup.

Quick Docker option:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY deployment/ /app/
COPY models/ /app/models/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

```bash
docker build -t ai-text-classifier .
docker run -p 5000:5000 ai-text-classifier
```

---

## Key Visualizations

All plots are saved in `results/`:

- Label distribution
- Text length distribution (Human vs AI)
- Word clouds for each class
- Top TF-IDF discriminative features
- 12-model performance comparison bar chart
- Confusion matrix
- ROC curve

---

## Author

**Muhammad Taimoor Haider**
GitHub: [@MuhammadTaimoorHaider](https://github.com/MuhammadTaimoorHaider)

---

## License

MIT License — free for educational and portfolio use.
