# 🚀 Quick PythonAnywhere Deployment Guide (Free Beginner Account)

## ⚡ Fast Track Deployment Steps

### Step 1: Prepare Your Files Locally

First, create a deployment package with the correct structure:

1. **Copy these files to a temporary folder** called `ai_classifier`:
   ```
   ai_classifier/
   ├── app.py (from deployment folder)
   ├── requirements.txt (from deployment folder)
   ├── models/
   │   ├── best_model.pkl
   │   └── tfidf_vectorizer.pkl
   ├── templates/
   │   └── index.html
   └── static/
       └── style.css
   ```

2. **Compress the folder** into a ZIP file: `ai_classifier.zip`

---

### Step 2: Upload to PythonAnywhere

1. **Login to PythonAnywhere**: https://www.pythonanywhere.com
2. Go to **Files** tab
3. Click **"Upload a file"** button
4. Upload your `ai_classifier.zip`
5. Click on the ZIP file name → Click **"Extract here"**
6. You should now have `/home/yourusername/ai_classifier/` folder

---

### Step 3: Install Dependencies

1. Go to **Consoles** tab
2. Click **"Bash"** to open a new Bash console
3. Run these commands:

```bash
cd ~/ai_classifier
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

Wait for installation to complete (2-3 minutes). You should see "Successfully installed..." messages.

---

### Step 4: Create Web App

1. Go to **Web** tab
2. Click **"Add a new web app"**
3. Click **"Next"** at the domain screen
4. Select **"Manual configuration"**
5. Choose **"Python 3.10"**
6. Click **"Next"**

---

### Step 5: Configure WSGI

1. On the Web tab, scroll to **"Code"** section
2. Click on the blue WSGI configuration file link
3. **DELETE ALL CONTENT** in the file
4. **PASTE THIS** (replace `yourusername` with your actual username):

```python
import sys
import os

# Add project directory
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

5. Click **"Save"** button (top right)

---

### Step 6: Set Virtual Environment

1. Still on **Web** tab, scroll to **"Virtualenv"** section
2. Enter this path: `/home/yourusername/ai_classifier/venv`
3. Click the ✓ checkmark

---

### Step 7: Configure Static Files

1. Scroll to **"Static files"** section
2. Click **"Enter URL"** and type: `/static/`
3. Click **"Enter path"** and type: `/home/yourusername/ai_classifier/static/`
4. Click the ✓ checkmark

---

### Step 8: Launch Your App! 🎉

1. Scroll to the TOP of the Web tab
2. Click the big green **"Reload yourusername.pythonanywhere.com"** button
3. Wait 10 seconds
4. Click on your domain link: `https://yourusername.pythonanywhere.com`

Your app should now be live! 🚀

---

## 🔍 Troubleshooting

### Problem: "502 Bad Gateway" Error

**Solution:**
1. Go to Web tab → Error log (click to view)
2. Look for error messages at the bottom
3. Common issues:
   - Wrong username in WSGI file → Fix and reload
   - Virtual environment path wrong → Check Step 6
   - Missing dependencies → Rerun Step 3

### Problem: "ImportError" or "ModuleNotFoundError"

**Solution:**
```bash
cd ~/ai_classifier
source venv/bin/activate
pip install -r requirements.txt
```
Then reload the web app.

### Problem: Can't find model files

**Check file locations:**
```bash
ls -la ~/ai_classifier/models/
```
Should show:
- `best_model.pkl`
- `tfidf_vectorizer.pkl`

If missing, re-upload them to the correct folder.

### Problem: Page loads but prediction fails

1. Check browser console (F12 → Console tab)
2. Test the health endpoint: `https://yourusername.pythonanywhere.com/health`
3. Should return: `{"model_loaded": true, "status": "healthy"}`

---

## 📝 Important Notes for Free Account

✅ **Free Tier Includes:**
- One web app
- 512 MB disk space
- 100 seconds CPU per day
- App URL: `yourusername.pythonanywhere.com`

⚠️ **Limitations:**
- App sleeps if inactive for 3 months (just reload to wake it)
- Cannot use custom domain
- Limited CPU time per day

💡 **Tips:**
- Keep your model file under 100MB
- Free account is perfect for portfolio/demo projects
- Upgrade to paid plan ($5/month) for production use

---

## ✅ Quick Checklist

Before asking for help, verify:

- [ ] Uploaded all files to `/home/yourusername/ai_classifier/`
- [ ] Created virtual environment in Step 3
- [ ] Installed all requirements successfully
- [ ] Created web app (Step 4)
- [ ] Updated WSGI file with YOUR username (Step 5)
- [ ] Set virtualenv path with YOUR username (Step 6)
- [ ] Added static files mapping (Step 7)
- [ ] Clicked "Reload" button (Step 8)
- [ ] Waited 10-15 seconds after reload
- [ ] Checked Error log if something went wrong

---

## 🎯 Testing Your Deployed App

Once live, test with these texts:

**Human Text Example:**
```
Hey everyone! I just wanted to share my experience with the new restaurant downtown. 
The food was absolutely amazing, and the service was top-notch. I highly recommend 
trying their signature dish!
```

**AI Text Example:**
```
Artificial intelligence represents a significant advancement in computational 
technology. Machine learning algorithms can process vast amounts of data and 
identify patterns that would be difficult for humans to detect manually.
```

---

## 📞 Need Help?

- **PythonAnywhere Help**: https://help.pythonanywhere.com/pages/DebuggingImportError/
- **Forums**: https://www.pythonanywhere.com/forums/
- **Check Error Logs**: Web tab → Click on error log link

---

**Your app URL will be: `https://yourusername.pythonanywhere.com`**

Replace `yourusername` with your actual PythonAnywhere username!

Good luck! 🚀
