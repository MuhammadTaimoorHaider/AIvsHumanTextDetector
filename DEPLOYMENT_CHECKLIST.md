# ✅ PythonAnywhere Deployment Checklist

## 📦 What You Have Ready

✅ **Deployment Package**: `ai_classifier_deploy.zip` (0.25 MB)
✅ **Includes**:
- Flask app (app.py)
- Trained model (best_model.pkl)
- TF-IDF vectorizer (tfidf_vectorizer.pkl)
- Web interface (templates/index.html)
- Styling (static/style.css)
- Requirements (requirements.txt)

---

## 🚀 Deployment Steps (15 minutes)

### ✅ Step 1: Login to PythonAnywhere (2 min)
1. Go to: https://www.pythonanywhere.com
2. Login with your free beginner account
3. You should see the Dashboard

### ✅ Step 2: Upload Your Files (3 min)
1. Click **"Files"** tab at the top
2. You're in: `/home/yourusername/`
3. Click **"Upload a file"** button
4. Select `ai_classifier_deploy.zip` from your Desktop folder
5. Wait for upload to complete (file appears in list)
6. Click on **"ai_classifier_deploy.zip"** filename
7. At the top, you'll see "Would you like to unzip it?" - Click the link
8. Files are now extracted!

### ✅ Step 3: Install Dependencies (4 min)
1. Click **"Consoles"** tab at the top
2. Under "Start a new console", click **"$ Bash"**
3. A terminal window opens - type these commands:

```bash
cd ai_classifier_deploy
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Wait 2-3 minutes for installation. You'll see lots of "Successfully installed..." messages.

### ✅ Step 4: Create Your Web App (2 min)
1. Click **"Web"** tab at the top
2. Click green **"Add a new web app"** button
3. Click **"Next"** (your domain shows: yourusername.pythonanywhere.com)
4. Select **"Manual configuration"** (important!)
5. Choose **"Python 3.10"**
6. Click **"Next"**

### ✅ Step 5: Configure WSGI File (2 min)
1. On the Web page, scroll to **"Code"** section
2. Click the blue link: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
3. **SELECT ALL** (Ctrl+A) and **DELETE**
4. **COPY AND PASTE** this code (replace `yourusername` with YOUR actual username):

```python
import sys
import os

# Add project directory
project_home = '/home/yourusername/ai_classifier_deploy'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Activate virtual environment
activate_this = '/home/yourusername/ai_classifier_deploy/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Import Flask app
from app import app as application
```

5. Click green **"Save"** button (top right)

### ✅ Step 6: Set Virtual Environment Path (1 min)
1. Go back to **"Web"** tab (close the WSGI editor)
2. Scroll to **"Virtualenv"** section
3. Click the text: "Enter path to a virtualenv"
4. Type: `/home/yourusername/ai_classifier_deploy/venv`
5. Click the blue ✓ checkmark

### ✅ Step 7: Add Static Files (1 min)
1. Scroll to **"Static files"** section
2. Click **"Enter URL"**: Type `/static/`
3. Click **"Enter path"**: Type `/home/yourusername/ai_classifier_deploy/static/`
4. Click the blue ✓ checkmark

### ✅ Step 8: Launch! 🚀 (1 min)
1. Scroll to the **TOP** of the Web page
2. Click the BIG GREEN button: **"Reload yourusername.pythonanywhere.com"**
3. Wait 10-15 seconds
4. Click the link at the top: `https://yourusername.pythonanywhere.com`

**Your app is now LIVE!** 🎉

---

## 🧪 Test Your App

Try these sample texts:

**Human Text:**
```
I absolutely loved visiting Paris last summer! The Eiffel Tower was breathtaking, 
and the croissants were to die for. Can't wait to go back next year!
```

**AI Text:**
```
Machine learning algorithms utilize mathematical models to process data and make 
predictions based on patterns identified during the training phase. These systems 
can be applied to various domains including natural language processing.
```

---

## 🔍 Troubleshooting

### Problem: 502 Bad Gateway
**Solution:** Check error log
1. Web tab → Click "error log" link
2. Look at last few lines
3. Usually: wrong username in WSGI or virtualenv path

### Problem: Import Error
**Solution:** Reinstall packages
```bash
cd ~/ai_classifier_deploy
source venv/bin/activate
pip install -r requirements.txt
```
Then reload web app.

### Problem: Static files not loading
**Solution:** Check Step 7 again, make sure paths are exact.

---

## 📋 Important Reminders

**ALWAYS replace `yourusername`** with your actual PythonAnywhere username in:
- WSGI configuration file (Step 5)
- Virtual environment path (Step 6)
- Static files path (Step 7)

**Example:** If your username is `john123`, use:
- `/home/john123/ai_classifier_deploy/venv`
- `/home/john123/ai_classifier_deploy/static/`

---

## 📊 Your App URL

**Your live app will be at:**
```
https://yourusername.pythonanywhere.com
```

Share this link with anyone to demo your AI classifier! 🌟

---

## 💡 Free Account Limits

✅ You get:
- 1 web app (you're using it!)
- 512 MB storage (your app uses ~0.25 MB)
- 100 CPU seconds/day (enough for demos)
- App stays live forever (as long as you login every 3 months)

---

## 🎯 Quick Check Before Going Live

Before clicking "Reload" in Step 8:

- [ ] Uploaded and extracted ZIP file
- [ ] Installed all requirements in virtual environment
- [ ] Created web app with Python 3.10
- [ ] Updated WSGI file with MY username (not "yourusername")
- [ ] Set virtualenv path with MY username
- [ ] Added static files mapping with MY username

**All checked?** You're ready to deploy! 🚀

---

## 📞 Need Help?

If something goes wrong:
1. Check the **error log** (Web tab)
2. Verify all paths have YOUR username
3. Check PythonAnywhere forums: https://www.pythonanywhere.com/forums/
4. Email support: support@pythonanywhere.com

---

**Good luck with your deployment! You've got this! 💪**

Your AI vs Human Text Classifier will be live in just 15 minutes! 🎉
