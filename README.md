## AI vs Human Text Detector

Production-style NLP project that classifies text as **Human-Written** or **AI-Generated**.

This repository includes the full workflow: EDA, preprocessing, feature engineering, model training/comparison, model persistence, and a Flask web app for real-time inference.

## Why This Project Matters

- AI-generated content is now common in education, publishing, and social media.
- Reliable detection helps with authenticity checks, moderation, and quality control.
- This project demonstrates practical machine learning delivery from notebook to deployed app.

## Highlights

- End-to-end binary text classification pipeline.
- TF-IDF + classic ML models benchmarked across 12 algorithms.
- Best model selected and serialized for inference.
- Flask API + web UI for interactive predictions.
- Deployment-ready structure for PythonAnywhere.

## Model Snapshot

From `models/model_metadata.json` and `models/model_comparison.csv`:

- Best model: `LinearSVC` (Linear SVM)
- Dataset used for saved model: 44,868 samples
- Feature space: 5,000 TF-IDF features (unigrams + bigrams)
- Test accuracy: 0.99298
- Test F1-score: 0.99297
- CV mean F1-score: 0.99398 (+/- 0.00083)

## Tech Stack

- Python
- scikit-learn
- pandas / numpy
- matplotlib / seaborn / wordcloud
- Flask
- joblib

## Repository Structure

```text
.
|- AI_vs_Human_Text_Classification.ipynb   # Main notebook
|- AIvsHuman.csv                           # Dataset
|- models/                                 # Trained artifacts and metadata
|- results/                                # Generated visuals / outputs
|- deployment/
|  |- app.py                               # Flask inference app
|  |- templates/index.html                 # Frontend template
|  |- static/style.css                     # Frontend styles
|  |- requirements.txt
|  `- DEPLOYMENT_GUIDE.md
|- test_deployment.py                      # API smoke test script
`- README.md
```

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

## Train / Reproduce Results

1. Open `AI_vs_Human_Text_Classification.ipynb`.
2. Run cells top to bottom.
3. Confirm model artifacts are produced in `models/`.

## Run the Web App

```bash
cd deployment
pip install -r requirements.txt
python app.py
```

Open: `http://localhost:5000`

### API Endpoints

- `GET /health` -> service and model load status
- `POST /predict` -> classify text

Example payload:

```json
{
  "text": "I wrote this after coming home from work and I am still tired."
}
```

## Deployment

Use `deployment/DEPLOYMENT_GUIDE.md` and `PYTHONANYWHERE_QUICKSTART.md` for PythonAnywhere setup.

## Recruiter Notes

This project demonstrates:

- Applied NLP for a real classification problem.
- Strong experimentation discipline (multi-model comparison + metrics).
- Practical MLOps fundamentals (artifact saving, inference app, deployment path).
- Ability to communicate work through notebooks, documentation, and live demo endpoints.

## License

This project is provided for educational and portfolio use.

### Key Insights

- Text length differences between AI and human text
- Most discriminative features identified
- Performance vs. training time trade-offs
- Cross-validation stability

### Visualizations

All visualizations are saved in the `results/` folder:

- Label distribution charts
- Text length analysis
- Word clouds (Human vs AI)
- Top TF-IDF features
- Model performance comparison
- Confusion matrices
- ROC curves

---

## 🌐 Deployment

### Option 1: PythonAnywhere (Recommended)

Follow the comprehensive guide in `deployment/DEPLOYMENT_GUIDE.md`

**Quick Steps:**

1. Create PythonAnywhere account
2. Upload files
3. Set up virtual environment
4. Configure web app
5. Update WSGI file
6. Reload and test

**Live Demo:** `https://yourusername.pythonanywhere.com`

### Option 2: Local Deployment

```bash
cd deployment
python app.py
# Access at http://localhost:5000
```

### Option 3: Docker (Advanced)

Create `Dockerfile`:

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY deployment/ /app/
COPY models/ /app/models/
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

Build and run:

```bash
docker build -t ai-text-classifier .
docker run -p 5000:5000 ai-text-classifier
```

---

## 🛠️ Technologies Used

### Data Processing & Analysis

- **pandas** - Data manipulation
- **numpy** - Numerical computing
- **matplotlib** - Visualization
- **seaborn** - Statistical visualization
- **wordcloud** - Word cloud generation

### Machine Learning

- **scikit-learn** - ML algorithms and tools
- **xgboost** - Gradient boosting
- **lightgbm** - Fast gradient boosting
- **joblib** - Model persistence

### Web Development

- **Flask** - Web framework
- **HTML/CSS** - Frontend
- **JavaScript** - Interactivity

### Development Tools

- **Jupyter Notebook** - Interactive development
- **Git** - Version control
- **Python 3.8+** - Programming language

---

## 🔮 Future Improvements

### Model Enhancements

- [ ] Implement deep learning models (LSTM, BERT)
- [ ] Add ensemble voting classifier
- [ ] Experiment with other embedding methods (Word2Vec, GloVe)
- [ ] Fine-tune transformer models

### Feature Engineering

- [ ] Add stylometric features
- [ ] Include sentence complexity metrics
- [ ] Analyze punctuation patterns
- [ ] Extract syntactic features

### Application Features

- [ ] Batch file processing
- [ ] API endpoint for integration
- [ ] Confidence threshold adjustment
- [ ] Explanation of predictions (LIME/SHAP)
- [ ] Multi-language support
- [ ] User authentication
- [ ] Usage analytics dashboard

### Performance

- [ ] Model quantization for faster inference
- [ ] Caching mechanism
- [ ] Load balancing for multiple requests
- [ ] Database integration for logging

---

## 👥 Contributors

**Muhammad Taimoor Haider**

- GitHub: [@MuhammadTaimoorHaider](https://github.com/MuhammadTaimoorHaider)
- Repository: [Multi-Task-Computer-Vision-Model-for-Demographic-Prediction-using-Deep-Learning](https://github.com/MuhammadTaimoorHaider/Multi-Task-Computer-Vision-Model-for-Demographic-Prediction-using-Deep-Learning)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Dataset source: Kaggle
- Instructor guidance and requirements
- Open-source community for libraries and tools
- PythonAnywhere for free hosting

---

## 📞 Contact

For questions, suggestions, or collaboration:

- **Email:** [Your Email]
- **GitHub Issues:** [Create an issue](https://github.com/MuhammadTaimoorHaider/Multi-Task-Computer-Vision-Model-for-Demographic-Prediction-using-Deep-Learning/issues)
- **LinkedIn:** [Your LinkedIn]

---

## 🎓 Academic Use

This project was developed as a semester project for [Course Name]. It demonstrates:

- ✅ Complete ML pipeline implementation
- ✅ Best practices in data science
- ✅ Model evaluation and selection
- ✅ Production-ready deployment
- ✅ Comprehensive documentation

---

## 📚 References

1. scikit-learn documentation: https://scikit-learn.org/
2. Flask documentation: https://flask.palletsprojects.com/
3. TF-IDF explanation: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
4. Machine Learning best practices
5. Python packaging guidelines

---

## 🎉 Project Completion Status

- [X] Step 1: Problem Definition
- [X] Step 2: Dataset Selection & Preprocessing
- [X] Step 3: Feature Extraction (TF-IDF)
- [X] Step 4: Train 12+ ML Algorithms
- [X] Step 5: Model Evaluation & Optimization
- [X] Step 6: Save Best Model
- [X] Step 7: Deployment Preparation
- [X] Documentation Complete
- [ ] PPT Presentation (To be created)
- [ ] Live Demo & Feedback (Pending)

---

**⭐ If you find this project helpful, please give it a star!**

**🐛 Found a bug? Open an issue!**

**💡 Have suggestions? We'd love to hear them!**

---

*Last Updated: November 2025*

*Made with ❤️ and ☕ by Muhammad Taimoor Haider*
