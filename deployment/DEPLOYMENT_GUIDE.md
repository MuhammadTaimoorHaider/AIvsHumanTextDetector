# 🚀 PythonAnywhere Deployment Guide

## Step-by-Step Instructions for Deploying Your AI vs Human Text Classifier

---

## 📋 Prerequisites

- PythonAnywhere account (Free or Paid)
- Your trained model files (best_model.pkl, tfidf_vectorizer.pkl)
- Flask application files (app.py, templates/, static/)

---

## 🎯 Deployment Steps

### Step 1: Create PythonAnywhere Account

1. Go to [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Click "Pricing & signup"
3. Choose "Create a Beginner account" (Free tier)
4. Complete the registration process
5. Verify your email address
6. Log in to your account

---

### Step 2: Upload Project Files

#### Option A: Using the Files Tab (Recommended for beginners)

1. Click on the **"Files"** tab in the dashboard
2. Navigate to your home directory (e.g., `/home/yourusername/`)
3. Create a new directory called `ai_classifier`:
   ```
   Click "New directory" → Enter "ai_classifier" → Click Create
   ```
4. Enter the `ai_classifier` directory
5. Create the following subdirectories:
   - `models/`
   - `templates/`
   - `static/`

6. Upload files to respective directories:
   - Upload `app.py` to `/home/yourusername/ai_classifier/`
   - Upload `best_model.pkl` to `/home/yourusername/ai_classifier/models/`
   - Upload `tfidf_vectorizer.pkl` to `/home/yourusername/ai_classifier/models/`
   - Upload `index.html` to `/home/yourusername/ai_classifier/templates/`
   - Upload `style.css` to `/home/yourusername/ai_classifier/static/`
   - Upload `requirements.txt` to `/home/yourusername/ai_classifier/`

#### Option B: Using Git (Advanced)

1. Push your project to GitHub
2. Open a Bash console from the **"Consoles"** tab
3. Clone your repository:
   ```bash
   git clone https://github.com/yourusername/your-repo.git ai_classifier
   cd ai_classifier
   ```

---

### Step 3: Set Up Virtual Environment

1. Open a **Bash console** (Consoles tab → New console → Bash)

2. Create a virtual environment:
   ```bash
   cd ~/ai_classifier
   python3.10 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

4. Upgrade pip:
   ```bash
   pip install --upgrade pip
   ```

5. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

6. Verify installation:
   ```bash
   pip list
   ```

---

### Step 4: Configure Web App

1. Go to the **"Web"** tab
2. Click **"Add a new web app"**
3. Click **"Next"** (choose your domain)
4. Select **"Manual configuration"**
5. Choose **Python 3.10**
6. Click **"Next"**

---

### Step 5: Configure WSGI File

1. In the **"Web"** tab, scroll down to **"Code"** section
2. Click on the **WSGI configuration file** link (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`)

3. **Delete all the existing content** and replace with:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/yourusername/ai_classifier'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtual environment
activate_this = '/home/yourusername/ai_classifier/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Flask app
from app import app as application
```

**IMPORTANT:** Replace `yourusername` with your actual PythonAnywhere username!

4. Click **"Save"** (top right corner)

---

### Step 6: Set Virtual Environment Path

1. In the **"Web"** tab, scroll to the **"Virtualenv"** section
2. Click **"Enter path to a virtualenv"**
3. Enter: `/home/yourusername/ai_classifier/venv`
4. Click the checkmark ✓

---

### Step 7: Reload Web App

1. Scroll to the top of the **"Web"** tab
2. Click the big green **"Reload yourusername.pythonanywhere.com"** button
3. Wait for the reload to complete

---

### Step 8: Test Your Application

1. Click on the link at the top: `https://yourusername.pythonanywhere.com`
2. Your application should now be live!
3. Test the classifier by entering some text

---

## 🔧 Troubleshooting

### Issue 1: 502 Bad Gateway Error

**Solution:**
- Check the **Error log** in the Web tab
- Verify all file paths in WSGI configuration
- Ensure virtual environment path is correct
- Check that all dependencies are installed

### Issue 2: Module Not Found Error

**Solution:**
```bash
source ~/ai_classifier/venv/bin/activate
pip install -r ~/ai_classifier/requirements.txt
```

### Issue 3: Model File Not Found

**Solution:**
- Verify model files are in `/home/yourusername/ai_classifier/models/`
- Check file names match exactly (case-sensitive)
- Update paths in `app.py` if necessary:
  ```python
  MODEL_PATH = '/home/yourusername/ai_classifier/models/best_model.pkl'
  VECTORIZER_PATH = '/home/yourusername/ai_classifier/models/tfidf_vectorizer.pkl'
  ```

### Issue 4: Static Files Not Loading

**Solution:**
1. Go to **Web** tab
2. Scroll to **"Static files"** section
3. Add mapping:
   - URL: `/static/`
   - Directory: `/home/yourusername/ai_classifier/static/`
4. Click **Reload**

---

## 📊 Monitoring Your App

### View Logs

1. **Error log**: Web tab → Log files → Error log
2. **Server log**: Web tab → Log files → Server log
3. **Access log**: Web tab → Log files → Access log

### Check Resource Usage

1. Go to the **"Dashboard"**
2. Monitor CPU seconds used
3. Free tier: 100 seconds/day CPU limit

---

## 🔄 Updating Your App

When you make changes:

1. Upload new files via **Files** tab
2. Or pull changes from Git:
   ```bash
   cd ~/ai_classifier
   git pull
   ```
3. Restart virtual environment if you updated requirements:
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```
4. **Reload** the web app from Web tab

---

## 💡 Performance Tips

1. **Model Size**: Keep models under 100MB for faster loading
2. **Free Tier Limits**:
   - 100 seconds CPU per day
   - App sleeps after 3 months inactivity
   - One web app allowed
3. **Optimization**:
   - Use model compression if needed
   - Add caching for repeated predictions
   - Consider upgrading to paid plan for production use

---

## 🎉 Success Checklist

- ✅ Account created and verified
- ✅ All files uploaded to correct directories
- ✅ Virtual environment created and activated
- ✅ Dependencies installed
- ✅ Web app configured
- ✅ WSGI file updated with correct paths
- ✅ Virtual environment path set
- ✅ Web app reloaded
- ✅ Application accessible via browser
- ✅ Classification working correctly

---

## 📞 Need Help?

- **PythonAnywhere Help**: [https://help.pythonanywhere.com](https://help.pythonanywhere.com)
- **Forums**: [https://www.pythonanywhere.com/forums/](https://www.pythonanywhere.com/forums/)
- **Email Support**: support@pythonanywhere.com (Paid accounts)

---

## 🔗 Alternative Deployment Options

If PythonAnywhere doesn't work for you, consider:

1. **Heroku**: [https://www.heroku.com](https://www.heroku.com)
2. **Render**: [https://render.com](https://render.com)
3. **Railway**: [https://railway.app](https://railway.app)
4. **Google Cloud Run**: [https://cloud.google.com/run](https://cloud.google.com/run)
5. **AWS Elastic Beanstalk**: [https://aws.amazon.com/elasticbeanstalk/](https://aws.amazon.com/elasticbeanstalk/)

---

## 📝 Notes

- Replace `yourusername` with your actual PythonAnywhere username everywhere
- Keep your model files backed up
- Test locally before deploying
- Monitor your app regularly
- Update dependencies for security patches

---

**Congratulations! Your AI vs Human Text Classifier is now deployed! 🎉**
