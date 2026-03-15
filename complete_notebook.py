"""
Script to add Steps 5, 6, and 7 to the notebook
"""

import nbformat as nbf
import sys

notebook_path = 'AI_vs_Human_Text_Classification.ipynb'
print(f"Loading notebook: {notebook_path}")

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
    print(f"✅ Loaded notebook with {len(nb.cells)} cells")
except Exception as e:
    print(f"❌ Error loading notebook: {e}")
    sys.exit(1)

# Step 5: Model Evaluation & Optimization
step5_cells = [
    ('markdown', '''## 📌 STEP 5: MODEL EVALUATION & OPTIMIZATION

### Sub-step 5.1-5.6: Create Model Comparison Table'''),
    
    ('code', '''# Sub-step 5.1-5.6: Create comprehensive comparison table
print("\\nCreating model comparison table...")
print("="*60)

# Create DataFrame from results
results_df = pd.DataFrame(results_list)

# Sort by F1-Score
results_df = results_df.sort_values('F1-Score', ascending=False).reset_index(drop=True)

print("\\nMODEL PERFORMANCE COMPARISON")
print("="*60)
print(results_df.to_string(index=False))

# Save to CSV
results_df.to_csv('models/model_comparison.csv', index=False)
print("\\n✅ Results saved to 'models/model_comparison.csv'")'''),
    
    ('markdown', '### Sub-step 5.7-5.9: Visualize Model Comparison'),
    
    ('code', '''# Sub-step 5.7-5.9: Create comparison visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Sort by accuracy for consistent visualization
plot_df = results_df.sort_values('Accuracy', ascending=True)

# Plot 1: Accuracy comparison
axes[0, 0].barh(plot_df['Model'], plot_df['Accuracy'], color='skyblue')
axes[0, 0].set_xlabel('Accuracy', fontsize=12, fontweight='bold')
axes[0, 0].set_title('Model Accuracy Comparison', fontsize=14, fontweight='bold')
axes[0, 0].set_xlim([0, 1])
for i, v in enumerate(plot_df['Accuracy']):
    axes[0, 0].text(v + 0.01, i, f'{v:.4f}', va='center')

# Plot 2: F1-Score comparison
axes[0, 1].barh(plot_df['Model'], plot_df['F1-Score'], color='lightcoral')
axes[0, 1].set_xlabel('F1-Score', fontsize=12, fontweight='bold')
axes[0, 1].set_title('Model F1-Score Comparison', fontsize=14, fontweight='bold')
axes[0, 1].set_xlim([0, 1])
for i, v in enumerate(plot_df['F1-Score']):
    axes[0, 1].text(v + 0.01, i, f'{v:.4f}', va='center')

# Plot 3: Precision vs Recall
axes[1, 0].scatter(plot_df['Recall'], plot_df['Precision'], s=100, alpha=0.6, c='green')
for i, model in enumerate(plot_df['Model']):
    axes[1, 0].annotate(model, (plot_df['Recall'].iloc[i], plot_df['Precision'].iloc[i]), 
                        fontsize=8, alpha=0.7)
axes[1, 0].set_xlabel('Recall', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Precision', fontsize=12, fontweight='bold')
axes[1, 0].set_title('Precision vs Recall', fontsize=14, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# Plot 4: Training Time comparison
axes[1, 1].barh(plot_df['Model'], plot_df['Training Time (s)'], color='orange')
axes[1, 1].set_xlabel('Training Time (seconds)', fontsize=12, fontweight='bold')
axes[1, 1].set_title('Model Training Time Comparison', fontsize=14, fontweight='bold')
for i, v in enumerate(plot_df['Training Time (s)']):
    axes[1, 1].text(v + 0.5, i, f'{v:.2f}s', va='center')

plt.tight_layout()
plt.savefig('results/model_comparison.png', dpi=300, bbox_inches='tight')
plt.show()

print("✅ Visualizations saved to 'results/model_comparison.png'")'''),
    
    ('markdown', '### Sub-step 5.10: Identify Best Model'),
    
    ('code', '''# Sub-step 5.10: Identify the best model
print("\\n" + "="*60)
print("BEST MODEL IDENTIFICATION")
print("="*60)

best_model_row = results_df.iloc[0]
best_model_name = best_model_row['Model']
best_model = models_dict[best_model_name]

print(f"\\n🏆 BEST MODEL: {best_model_name}")
print(f"\\nPerformance Metrics:")
print(f"  - Accuracy:  {best_model_row['Accuracy']:.4f}")
print(f"  - Precision: {best_model_row['Precision']:.4f}")
print(f"  - Recall:    {best_model_row['Recall']:.4f}")
print(f"  - F1-Score:  {best_model_row['F1-Score']:.4f}")
if best_model_row['ROC-AUC']:
    print(f"  - ROC-AUC:   {best_model_row['ROC-AUC']:.4f}")
print(f"  - Training Time: {best_model_row['Training Time (s)']:.2f}s")

print("\\n" + "="*60)'''),
    
    ('markdown', '### Sub-step 5.11-5.12: Detailed Evaluation of Best Model'),
    
    ('code', '''# Sub-step 5.11-5.12: Generate detailed classification report
print("\\nDetailed Classification Report for Best Model:")
print("="*60)

# Get predictions
y_pred_best = best_model.predict(X_test_tfidf)

# Classification report
print(classification_report(y_test, y_pred_best, target_names=['Human (0)', 'AI (1)']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred_best)

# Visualize confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Human (0)', 'AI (1)'],
            yticklabels=['Human (0)', 'AI (1)'])
plt.title(f'Confusion Matrix - {best_model_name}', fontsize=14, fontweight='bold')
plt.ylabel('True Label', fontsize=12)
plt.xlabel('Predicted Label', fontsize=12)
plt.tight_layout()
plt.savefig(f'results/confusion_matrix_{best_model_name.replace(" ", "_")}.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"\\n✅ Confusion matrix saved")'''),
    
    ('markdown', '### Sub-step 5.13-5.19: Hyperparameter Optimization'),
    
    ('code', '''# Sub-step 5.13-5.19: Hyperparameter tuning for best model
print("\\n" + "="*60)
print("HYPERPARAMETER OPTIMIZATION")
print("="*60)
print(f"\\nOptimizing {best_model_name}...")

# Define parameter grid based on best model type
if best_model_name == 'Logistic Regression':
    param_grid = {
        'C': [0.1, 1, 10],
        'penalty': ['l2'],
        'solver': ['lbfgs', 'liblinear']
    }
    base_model = LogisticRegression(max_iter=1000, random_state=42)
    
elif best_model_name == 'Random Forest':
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5]
    }
    base_model = RandomForestClassifier(random_state=42, n_jobs=-1)
    
elif best_model_name == 'Naive Bayes':
    param_grid = {
        'alpha': [0.1, 0.5, 1.0, 2.0]
    }
    base_model = MultinomialNB()
    
elif best_model_name == 'Extra Trees':
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20, None],
        'min_samples_split': [2, 5]
    }
    base_model = ExtraTreesClassifier(random_state=42, n_jobs=-1)
    
else:
    # Default: use existing best model
    print(f"Using existing {best_model_name} without additional tuning")
    optimized_model = best_model
    param_grid = None

if param_grid:
    print(f"\\nParameter grid: {param_grid}")
    print("\\nPerforming Grid Search (this may take several minutes)...")
    
    # Perform grid search
    grid_search = GridSearchCV(
        base_model, 
        param_grid, 
        cv=3, 
        scoring='f1_weighted',
        n_jobs=-1,
        verbose=1
    )
    
    grid_search.fit(X_train_tfidf, y_train)
    
    print(f"\\n✅ Grid Search completed!")
    print(f"\\nBest parameters: {grid_search.best_params_}")
    print(f"Best cross-validation F1-score: {grid_search.best_score_:.4f}")
    
    # Use optimized model
    optimized_model = grid_search.best_estimator_
else:
    optimized_model = best_model

print("\\n" + "="*60)'''),
    
    ('markdown', '### Sub-step 5.20-5.22: Cross-Validation & Final Evaluation'),
    
    ('code', '''# Sub-step 5.20-5.22: Perform cross-validation
print("\\nPerforming 5-Fold Cross-Validation...")
cv_scores = cross_val_score(optimized_model, X_train_tfidf, y_train, cv=5, scoring='f1_weighted', n_jobs=-1)

print(f"\\nCross-Validation F1-Scores: {cv_scores}")
print(f"Mean CV F1-Score: {cv_scores.mean():.4f} (+/- {cv_scores.std() * 2:.4f})")

# Final training on full training set
print("\\nFinal training on full training set...")
start_time = time.time()
optimized_model.fit(X_train_tfidf, y_train)
final_training_time = time.time() - start_time

# Final evaluation
y_pred_final = optimized_model.predict(X_test_tfidf)
final_accuracy = accuracy_score(y_test, y_pred_final)
final_f1 = f1_score(y_test, y_pred_final, average='weighted')

print(f"\\n" + "="*60)
print("FINAL OPTIMIZED MODEL PERFORMANCE")
print("="*60)
print(f"Model: {best_model_name} (Optimized)")
print(f"Accuracy:  {final_accuracy:.4f}")
print(f"F1-Score:  {final_f1:.4f}")
print(f"Training Time: {final_training_time:.2f}s")
print(f"\\n✅ STEP 5: Model Evaluation & Optimization completed!")
print("="*60)'''),
]

# Add Step 5 cells
for cell_type, content in step5_cells:
    if cell_type == 'markdown':
        nb.cells.append(nbf.v4.new_markdown_cell(content))
    else:
        nb.cells.append(nbf.v4.new_code_cell(content))

print(f"✅ Added {len(step5_cells)} cells for Step 5")

# Step 6: Save Best Model
step6_cells = [
    ('markdown', '''## 📌 STEP 6: SAVE BEST MODEL

### Sub-step 6.1-6.8: Save Model, Vectorizer, and Metadata'''),
    
    ('code', '''# Sub-step 6.1-6.8: Save all necessary files
print("\\n" + "="*60)
print("SAVING BEST MODEL AND COMPONENTS")
print("="*60)

# Save the optimized model
model_filename = 'models/best_model.pkl'
joblib.dump(optimized_model, model_filename)
print(f"\\n✅ Model saved: {model_filename}")

# TF-IDF vectorizer already saved earlier, verify it exists
vectorizer_filename = 'models/tfidf_vectorizer.pkl'
if not os.path.exists(vectorizer_filename):
    joblib.dump(tfidf, vectorizer_filename)
    print(f"✅ Vectorizer saved: {vectorizer_filename}")
else:
    print(f"✅ Vectorizer exists: {vectorizer_filename}")

# Save model metadata
metadata = {
    'model_name': best_model_name,
    'model_type': str(type(optimized_model).__name__),
    'training_date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    'dataset_size': len(df),
    'training_size': len(X_train),
    'test_size': len(X_test),
    'features': X_train_tfidf.shape[1],
    'performance': {
        'accuracy': float(final_accuracy),
        'f1_score': float(final_f1),
        'cv_mean_f1': float(cv_scores.mean()),
        'cv_std_f1': float(cv_scores.std())
    },
    'parameters': str(optimized_model.get_params()) if hasattr(optimized_model, 'get_params') else 'N/A',
    'training_time_seconds': float(final_training_time)
}

metadata_filename = 'models/model_metadata.json'
with open(metadata_filename, 'w') as f:
    json.dump(metadata, f, indent=4)
print(f"✅ Metadata saved: {metadata_filename}")

# Test loading the saved model
print("\\nVerifying saved model...")
loaded_model = joblib.load(model_filename)
loaded_vectorizer = joblib.load(vectorizer_filename)
print("✅ Model and vectorizer loaded successfully!")

# Test prediction with loaded model
sample_text = df['cleaned_text'].iloc[0]
sample_vectorized = loaded_vectorizer.transform([sample_text])
sample_prediction = loaded_model.predict(sample_vectorized)
print(f"\\nTest prediction with loaded model: {sample_prediction[0]}")
print(f"Actual label: {df['label'].iloc[0]}")

print("\\n" + "="*60)
print("✅ STEP 6: Model Saving completed successfully!")
print("="*60)

# Display all saved files
print("\\nSaved Files:")
print(f"  1. {model_filename}")
print(f"  2. {vectorizer_filename}")
print(f"  3. {metadata_filename}")
print(f"  4. models/model_comparison.csv")'''),
]

# Add Step 6 cells
for cell_type, content in step6_cells:
    if cell_type == 'markdown':
        nb.cells.append(nbf.v4.new_markdown_cell(content))
    else:
        nb.cells.append(nbf.v4.new_code_cell(content))

print(f"✅ Added {len(step6_cells)} cells for Step 6")

# Step 7: Deployment Preparation
step7_cells = [
    ('markdown', '''## 📌 STEP 7: DEPLOYMENT PREPARATION

### Create Deployment Files

All deployment files have been created in the `deployment/` folder:
- `app.py` - Flask web application
- `templates/index.html` - Web interface
- `static/style.css` - Styling
- `requirements.txt` - Dependencies
- `DEPLOYMENT_GUIDE.md` - Step-by-step deployment instructions

The deployment files are ready for PythonAnywhere or any other cloud platform!'''),
    
    ('code', '''# Display project summary
import os

print("\\n" + "="*60)
print("PROJECT COMPLETION SUMMARY")
print("="*60)

print("\\n✅ ALL STEPS COMPLETED SUCCESSFULLY!")
print("\\n📁 Project Structure:")
print("="*60)

def print_tree(directory, prefix="", max_depth=3, current_depth=0):
    if current_depth >= max_depth:
        return
    
    try:
        items = sorted(os.listdir(directory))
        dirs = [item for item in items if os.path.isdir(os.path.join(directory, item)) and not item.startswith('.')]
        files = [item for item in items if os.path.isfile(os.path.join(directory, item)) and not item.startswith('.')]
        
        for i, d in enumerate(dirs):
            is_last = (i == len(dirs) - 1 and len(files) == 0)
            print(f"{prefix}{'└── ' if is_last else '├── '}{d}/")
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(os.path.join(directory, d), new_prefix, max_depth, current_depth + 1)
        
        for i, f in enumerate(files):
            is_last = (i == len(files) - 1)
            print(f"{prefix}{'└── ' if is_last else '├── '}{f}")
    except PermissionError:
        pass

print_tree(".")

print("\\n" + "="*60)
print("📊 MODEL PERFORMANCE")
print("="*60)
print(f"Best Model: {best_model_name}")
print(f"Accuracy: {final_accuracy:.4f}")
print(f"F1-Score: {final_f1:.4f}")

print("\\n" + "="*60)
print("🚀 NEXT STEPS")
print("="*60)
print("1. Review the results/ folder for all visualizations")
print("2. Check models/ folder for saved model and metadata")
print("3. Go to deployment/ folder for Flask app")
print("4. Read DEPLOYMENT_GUIDE.md for PythonAnywhere deployment")
print("5. Test the Flask app locally before deploying")

print("\\n" + "="*60)
print("🎉 PROJECT COMPLETED!")
print("="*60)'''),
]

# Add Step 7 cells
for cell_type, content in step7_cells:
    if cell_type == 'markdown':
        nb.cells.append(nbf.v4.new_markdown_cell(content))
    else:
        nb.cells.append(nbf.v4.new_code_cell(content))

print(f"✅ Added {len(step7_cells)} cells for Step 7")

# Add missing import at the top if needed
import_cell = nb.cells[2]  # Should be the imports cell
if 'import os' not in import_cell.source:
    import_cell.source += "\nimport os"
    print("✅ Added missing 'import os' to imports")

# Save the updated notebook
try:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"\\n✅ Successfully updated notebook!")
    print(f"Total cells now: {len(nb.cells)}")
except Exception as e:
    print(f"❌ Error saving notebook: {e}")
    sys.exit(1)

print("\\n" + "="*60)
print("✅ NOTEBOOK IS COMPLETE WITH ALL 7 STEPS!")
print("="*60)
print("\\nThe notebook now contains:")
print("  - Step 1: Problem Definition")
print("  - Step 2: Data Exploration & Preprocessing")
print("  - Step 3: Feature Extraction (TF-IDF)")
print("  - Step 4: Train 12 ML Models")
print("  - Step 5: Model Evaluation & Optimization")
print("  - Step 6: Save Best Model")
print("  - Step 7: Deployment Preparation")
print("\\nTotal cells: " + str(len(nb.cells)))
