"""
Script to prepare deployment package for PythonAnywhere
This will copy all necessary files to a deployment-ready folder
"""

import os
import shutil
from pathlib import Path

print("=" * 60)
print("PREPARING PYTHONANYWHERE DEPLOYMENT PACKAGE")
print("=" * 60)

# Define source and destination paths
base_dir = Path(__file__).parent
deploy_dir = base_dir / "ai_classifier_deploy"

# Create deployment directory structure
print("\n1. Creating deployment folder structure...")
deploy_dir.mkdir(exist_ok=True)
(deploy_dir / "models").mkdir(exist_ok=True)
(deploy_dir / "templates").mkdir(exist_ok=True)
(deploy_dir / "static").mkdir(exist_ok=True)

# Copy files
print("2. Copying files...")

files_to_copy = [
    # Source -> Destination
    ("deployment/app.py", "app.py"),
    ("deployment/requirements.txt", "requirements.txt"),
    ("models/best_model.pkl", "models/best_model.pkl"),
    ("models/tfidf_vectorizer.pkl", "models/tfidf_vectorizer.pkl"),
    ("deployment/templates/index.html", "templates/index.html"),
    ("deployment/static/style.css", "static/style.css"),
]

copied_files = []
missing_files = []

for src, dst in files_to_copy:
    src_path = base_dir / src
    dst_path = deploy_dir / dst
    
    if src_path.exists():
        shutil.copy2(src_path, dst_path)
        copied_files.append(dst)
        print(f"   ✅ {dst}")
    else:
        missing_files.append(src)
        print(f"   ❌ Missing: {src}")

print("\n3. Deployment package ready!")
print("=" * 60)
print(f"\n📁 Location: {deploy_dir.absolute()}")
print(f"\n✅ Copied {len(copied_files)} files successfully")

if missing_files:
    print(f"\n⚠️  Missing {len(missing_files)} files:")
    for f in missing_files:
        print(f"   - {f}")
    print("\nPlease ensure all files exist before deployment.")
else:
    print("\n🎉 All files copied successfully!")

print("\n" + "=" * 60)
print("NEXT STEPS:")
print("=" * 60)
print("1. Compress the 'ai_classifier_deploy' folder into a ZIP file")
print("2. Upload the ZIP to PythonAnywhere")
print("3. Follow the steps in PYTHONANYWHERE_QUICKSTART.md")
print("\nFolder contents:")
print("-" * 60)

for root, dirs, files in os.walk(deploy_dir):
    level = root.replace(str(deploy_dir), '').count(os.sep)
    indent = ' ' * 2 * level
    print(f"{indent}{os.path.basename(root)}/")
    sub_indent = ' ' * 2 * (level + 1)
    for file in files:
        file_path = Path(root) / file
        size = file_path.stat().st_size / (1024 * 1024)  # MB
        print(f"{sub_indent}{file} ({size:.2f} MB)")

print("\n✅ Ready for deployment!")
