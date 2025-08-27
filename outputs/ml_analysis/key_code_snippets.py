"""
ML Model Visualization & Interpretability - Key Code Snippets
Generated from comprehensive analysis pipeline
"""

# 1. Basic Model Training and Evaluation
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# 2. SHAP Interpretability
import shap

# Create explainer and get SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)
shap.summary_plot(shap_values, X_test, feature_names=feature_names)

# 3. Interactive Visualization with Plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create interactive performance dashboard
fig = make_subplots(rows=2, cols=2)
fig.add_trace(go.Bar(x=model_names, y=accuracies), row=1, col=1)
fig.show()

# 4. Yellowbrick Integration
from yellowbrick.classifier import ClassificationReport
from yellowbrick.model_selection import LearningCurve

# Classification report visualization
visualizer = ClassificationReport(model)
visualizer.fit(X_train, y_train)
visualizer.score(X_test, y_test)
visualizer.show()
