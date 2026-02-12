
💳 UPI Fraud Detection Using Machine Learning
📌 Overview

Unified Payments Interface (UPI) is a real-time digital payment system widely used in India. With the rapid growth of digital transactions, detecting fraudulent activities has become increasingly important.

This project focuses on building a machine learning model to detect fraudulent UPI transactions using classification techniques.

🎯 Objective

To develop a robust fraud detection system that can accurately classify transactions as:

✅ Legitimate (0)

🚨 Fraudulent (1)

📊 Dataset & Preprocessing

The following steps were performed:

Removed duplicate records

Checked and handled missing values

Converted date column to datetime format

Extracted time-based features (Year, Month)

Applied One-Hot Encoding for categorical variables

Removed unnecessary ID-based columns

Handled class imbalance using SMOTE (Synthetic Minority Over-sampling Technique)

🤖 Models Implemented

The following machine learning models were trained and compared:

Decision Tree

Random Forest

Gradient Boosting

XGBoost (Best Performing Model)

⚙️ Model Optimization

Applied SMOTE to balance the training dataset

Performed Hyperparameter Tuning using GridSearchCV

Re-trained XGBoost using optimal hyperparameters

Although RandomizedSearchCV is more computationally efficient, GridSearchCV was used for exhaustive parameter tuning.

📈 Final Model Performance (XGBoost)

Accuracy: 96.9%

ROC-AUC Score: 93.75%

F1 Score: ~0.93

These results indicate strong classification performance and effective fraud detection capability.

🧠 Key Insights

XGBoost outperformed other models due to its boosting mechanism and ability to handle complex feature interactions.

Handling class imbalance significantly improved recall and overall model robustness.

ROC-AUC and F1-score were prioritized over accuracy due to the nature of fraud detection problems.

🛠 Technologies Used

Python

Pandas

NumPy

Scikit-learn

XGBoost

Imbalanced-learn (SMOTE)

Matplotlib / Seaborn
