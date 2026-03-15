"""
Script to complete the Jupyter notebook by adding remaining cells
Run this after the basic notebook structure is created
"""

import nbformat as nbf
import sys

# Load existing notebook
notebook_path = 'AI_vs_Human_Text_Classification.ipynb'
print(f"Loading notebook: {notebook_path}")

try:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbf.read(f, as_version=4)
    print(f"✅ Loaded notebook with {len(nb.cells)} cells")
except Exception as e:
    print(f"❌ Error loading notebook: {e}")
    sys.exit(1)

# Define cells to add for Step 3 (continued)
step3_cells = [
    # Train-Test Split
    ('code', '''# Sub-step 3.9: Split data into train and test sets
print("\\nSub-step 3.9: Splitting data into train and test sets...")
print("="*60)

# Prepare X and y
X = df['cleaned_text']
y = df['label']

# Split with stratification
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42, 
    stratify=y
)

print(f"✅ Data split completed!")
print(f"\\nTraining set size: {len(X_train):,} ({len(X_train)/len(df)*100:.1f}%)")
print(f"Test set size: {len(X_test):,} ({len(X_test)/len(df)*100:.1f}%)")
print(f"\\nTraining label distribution:")
print(y_train.value_counts())
print(f"\\nTest label distribution:")
print(y_test.value_counts())'''),
    
    ('markdown', '### Sub-step 3.3-3.4: Fit and Transform TF-IDF'),
    
    ('code', '''# Sub-step 3.3-3.4: Fit TF-IDF and transform data
print("\\nSub-step 3.3-3.4: Fitting TF-IDF on training data...")
print("This may take a few minutes...")
print("="*60)

start_time = time.time()

# Fit on training data
tfidf.fit(X_train)

# Transform both train and test
X_train_tfidf = tfidf.transform(X_train)
X_test_tfidf = tfidf.transform(X_test)

elapsed_time = time.time() - start_time

print(f"✅ TF-IDF transformation completed in {elapsed_time:.2f} seconds!")
print(f"\\nTraining feature matrix shape: {X_train_tfidf.shape}")
print(f"Test feature matrix shape: {X_test_tfidf.shape}")
print(f"Total features extracted: {X_train_tfidf.shape[1]:,}")'''),
    
    ('markdown', '### Sub-step 3.5-3.7: Analyze TF-IDF Features'),
    
    ('code', '''# Sub-step 3.5-3.7: Analyze TF-IDF features
print("\\nSub-step 3.5-3.7: Analyzing TF-IDF features...")
print("="*60)

# Get feature names
feature_names = tfidf.get_feature_names_out()

# Calculate feature importance (mean TF-IDF scores)
feature_importance = np.array(X_train_tfidf.mean(axis=0)).flatten()
top_indices = feature_importance.argsort()[-20:][::-1]

print("\\nTop 20 TF-IDF Features:")
print("-"*60)
for idx in top_indices:
    print(f"{feature_names[idx]:20s} : {feature_importance[idx]:.6f}")

# Visualize top features
plt.figure(figsize=(12, 6))
top_features = [feature_names[i] for i in top_indices]
top_scores = [feature_importance[i] for i in top_indices]
plt.barh(range(len(top_features)), top_scores, color='steelblue')
plt.yticks(range(len(top_features)), top_features)
plt.xlabel('Mean TF-IDF Score', fontsize=12, fontweight='bold')
plt.title('Top 20 TF-IDF Features', fontsize=14, fontweight='bold')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('results/top_tfidf_features.png', dpi=300, bbox_inches='tight')
plt.show()

print("\\n✅ Feature visualization saved to 'results/top_tfidf_features.png'")'''),
    
    ('markdown', '### Sub-step 3.8: Save TF-IDF Vectorizer'),
    
    ('code', '''# Sub-step 3.8: Save TF-IDF vectorizer
print("\\nSub-step 3.8: Saving TF-IDF vectorizer...")
joblib.dump(tfidf, 'models/tfidf_vectorizer.pkl')
print("✅ TF-IDF vectorizer saved to 'models/tfidf_vectorizer.pkl'")
print("\\n" + "="*60)
print("✅ STEP 3: Feature Extraction completed successfully!")
print("="*60)'''),
]

# Add Step 3 cells
for cell_type, content in step3_cells:
    if cell_type == 'markdown':
        nb.cells.append(nbf.v4.new_markdown_cell(content))
    else:
        nb.cells.append(nbf.v4.new_code_cell(content))

print(f"✅ Added {len(step3_cells)} cells for Step 3")

# Define cells for Step 4 - Model Training
step4_cells = [
    ('markdown', '''## 📌 STEP 4: TRAIN 12 MACHINE LEARNING ALGORITHMS

### Define Evaluation Function'''),
    
    ('code', '''# Sub-step 4.1-4.2: Define evaluation metrics function
def evaluate_model(name, model, X_train, X_test, y_train, y_test, training_time):
    """
    Evaluate a trained model and return performance metrics
    """
    # Predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1] if hasattr(model, 'predict_proba') else None
    
    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    # ROC-AUC (if probability predictions available)
    roc_auc = roc_auc_score(y_test, y_pred_proba) if y_pred_proba is not None else None
    
    results = {
        'Model': name,
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1-Score': f1,
        'ROC-AUC': roc_auc,
        'Training Time (s)': training_time
    }
    
    print(f"\\n{'='*60}")
    print(f"Model: {name}")
    print(f"{'='*60}")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")
    if roc_auc:
        print(f"ROC-AUC:   {roc_auc:.4f}")
    print(f"Training Time: {training_time:.2f}s")
    
    return results

print("✅ Evaluation function defined")'''),
    
    ('markdown', '### Train All Models'),
    
    ('code', '''# Sub-step 4.3-4.15: Train all models
print("\\n" + "="*60)
print("TRAINING 12 MACHINE LEARNING MODELS")
print("="*60)
print("\\nThis will take several minutes...")

# Dictionary to store all models and results
models_dict = {}
results_list = []

# Model 1: Logistic Regression
print("\\n[1/12] Training Logistic Regression...")
start = time.time()
lr = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)
lr.fit(X_train_tfidf, y_train)
lr_time = time.time() - start
models_dict['Logistic Regression'] = lr
results_list.append(evaluate_model('Logistic Regression', lr, X_train_tfidf, X_test_tfidf, y_train, y_test, lr_time))

# Model 2: Random Forest
print("\\n[2/12] Training Random Forest...")
start = time.time()
rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf.fit(X_train_tfidf, y_train)
rf_time = time.time() - start
models_dict['Random Forest'] = rf
results_list.append(evaluate_model('Random Forest', rf, X_train_tfidf, X_test_tfidf, y_train, y_test, rf_time))

# Model 3: Gradient Boosting
print("\\n[3/12] Training Gradient Boosting...")
start = time.time()
gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
gb.fit(X_train_tfidf, y_train)
gb_time = time.time() - start
models_dict['Gradient Boosting'] = gb
results_list.append(evaluate_model('Gradient Boosting', gb, X_train_tfidf, X_test_tfidf, y_train, y_test, gb_time))

# Model 4: XGBoost (if available)
if xgb_available:
    print("\\n[4/12] Training XGBoost...")
    start = time.time()
    xgb_model = XGBClassifier(n_estimators=100, random_state=42, use_label_encoder=False, eval_metric='logloss')
    xgb_model.fit(X_train_tfidf, y_train)
    xgb_time = time.time() - start
    models_dict['XGBoost'] = xgb_model
    results_list.append(evaluate_model('XGBoost', xgb_model, X_train_tfidf, X_test_tfidf, y_train, y_test, xgb_time))
else:
    print("\\n[4/12] XGBoost not available, skipping...")

# Model 5: LightGBM (if available)
if lgbm_available:
    print("\\n[5/12] Training LightGBM...")
    start = time.time()
    lgbm_model = LGBMClassifier(n_estimators=100, random_state=42, verbose=-1)
    lgbm_model.fit(X_train_tfidf, y_train)
    lgbm_time = time.time() - start
    models_dict['LightGBM'] = lgbm_model
    results_list.append(evaluate_model('LightGBM', lgbm_model, X_train_tfidf, X_test_tfidf, y_train, y_test, lgbm_time))
else:
    print("\\n[5/12] LightGBM not available, skipping...")

# Model 6: Linear SVM
print("\\n[6/12] Training Linear SVM...")
start = time.time()
linear_svm = LinearSVC(max_iter=1000, random_state=42)
linear_svm.fit(X_train_tfidf, y_train)
linear_svm_time = time.time() - start
models_dict['Linear SVM'] = linear_svm
# Note: LinearSVC doesn't have predict_proba, so we handle it differently
y_pred = linear_svm.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
results_list.append({
    'Model': 'Linear SVM',
    'Accuracy': accuracy,
    'Precision': precision,
    'Recall': recall,
    'F1-Score': f1,
    'ROC-AUC': None,
    'Training Time (s)': linear_svm_time
})
print(f"\\n{'='*60}")
print(f"Model: Linear SVM")
print(f"{'='*60}")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")
print(f"Training Time: {linear_svm_time:.2f}s")

# Model 7: RBF SVM (with smaller sample for speed)
print("\\n[7/12] Training RBF SVM (on sample)...")
sample_size = min(10000, len(X_train_tfidf.toarray()))
sample_indices = np.random.choice(X_train_tfidf.shape[0], sample_size, replace=False)
X_train_sample = X_train_tfidf[sample_indices]
y_train_sample = y_train.iloc[sample_indices]
start = time.time()
rbf_svm = SVC(kernel='rbf', probability=True, random_state=42)
rbf_svm.fit(X_train_sample, y_train_sample)
rbf_svm_time = time.time() - start
models_dict['RBF SVM'] = rbf_svm
results_list.append(evaluate_model('RBF SVM', rbf_svm, X_train_sample, X_test_tfidf, y_train_sample, y_test, rbf_svm_time))

# Model 8: Naive Bayes
print("\\n[8/12] Training Naive Bayes...")
start = time.time()
nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)
nb_time = time.time() - start
models_dict['Naive Bayes'] = nb
results_list.append(evaluate_model('Naive Bayes', nb, X_train_tfidf, X_test_tfidf, y_train, y_test, nb_time))

# Model 9: K-Nearest Neighbors (on sample for speed)
print("\\n[9/12] Training K-Nearest Neighbors (on sample)...")
start = time.time()
knn = KNeighborsClassifier(n_neighbors=5, n_jobs=-1)
knn.fit(X_train_sample, y_train_sample)
knn_time = time.time() - start
models_dict['K-Nearest Neighbors'] = knn
results_list.append(evaluate_model('K-Nearest Neighbors', knn, X_train_sample, X_test_tfidf, y_train_sample, y_test, knn_time))

# Model 10: Decision Tree
print("\\n[10/12] Training Decision Tree...")
start = time.time()
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train_tfidf, y_train)
dt_time = time.time() - start
models_dict['Decision Tree'] = dt
results_list.append(evaluate_model('Decision Tree', dt, X_train_tfidf, X_test_tfidf, y_train, y_test, dt_time))

# Model 11: AdaBoost
print("\\n[11/12] Training AdaBoost...")
start = time.time()
ada = AdaBoostClassifier(n_estimators=50, random_state=42)
ada.fit(X_train_tfidf, y_train)
ada_time = time.time() - start
models_dict['AdaBoost'] = ada
results_list.append(evaluate_model('AdaBoost', ada, X_train_tfidf, X_test_tfidf, y_train, y_test, ada_time))

# Model 12: Extra Trees
print("\\n[12/12] Training Extra Trees...")
start = time.time()
et = ExtraTreesClassifier(n_estimators=100, random_state=42, n_jobs=-1)
et.fit(X_train_tfidf, y_train)
et_time = time.time() - start
models_dict['Extra Trees'] = et
results_list.append(evaluate_model('Extra Trees', et, X_train_tfidf, X_test_tfidf, y_train, y_test, et_time))

print("\\n" + "="*60)
print("✅ ALL MODELS TRAINED SUCCESSFULLY!")
print("="*60)'''),
]

# Add Step 4 cells
for cell_type, content in step4_cells:
    if cell_type == 'markdown':
        nb.cells.append(nbf.v4.new_markdown_cell(content))
    else:
        nb.cells.append(nbf.v4.new_code_cell(content))

print(f"✅ Added {len(step4_cells)} cells for Step 4")

# Save the updated notebook
try:
    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print(f"\\n✅ Successfully updated notebook!")
    print(f"Total cells now: {len(nb.cells)}")
except Exception as e:
    print(f"❌ Error saving notebook: {e}")
    sys.exit(1)

print("\\n✅ Notebook update completed!")
print("\\nNext: Run the notebook to execute all cells")
