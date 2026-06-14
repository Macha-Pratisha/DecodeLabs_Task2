"""
Iris Flower Classification using Machine Learning
A beginner-friendly supervised learning project demonstrating data classification.

Author: Pratisha Macha
Project: DecodeLabs Internship - Project 2
Date: June 2026
"""

# ============================================================================
# STEP 1: IMPORT LIBRARIES
# ============================================================================

# Data manipulation and analysis
import pandas as pd
import numpy as np

# Machine learning models and utilities
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

# Model evaluation metrics
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Visualization libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)


# ============================================================================
# STEP 2: LOAD DATASET
# ============================================================================

def load_dataset():
    """
    Load the Iris dataset from scikit-learn.

    The Iris dataset contains measurements of iris flowers from three species:
    - Setosa
    - Versicolor
    - Virginica

    Returns:
        tuple: (features_df, target_df, target_names, feature_names)
    """
    print("=" * 70)
    print("LOADING IRIS DATASET")
    print("=" * 70)

    # Load iris dataset
    iris = load_iris()

    # Create DataFrame for features
    features_df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    # Create DataFrame for target
    target_df = pd.DataFrame(
        iris.target,
        columns=['species']
    )

    print("[OK] Dataset loaded successfully!")
    print()

    return features_df, target_df, iris.target_names, iris.feature_names


# ============================================================================
# STEP 3: EXPLORE DATASET
# ============================================================================

def explore_dataset(features_df, target_df, target_names):
    """
    Perform exploratory data analysis on the dataset.

    Args:
        features_df: DataFrame containing feature data
        target_df: DataFrame containing target labels
        target_names: Names of target classes
    """
    print("=" * 70)
    print("EXPLORATORY DATA ANALYSIS")
    print("=" * 70)

    # Display dataset information
    print("\n1. DATASET OVERVIEW")
    print("-" * 70)
    print(f"Number of samples: {len(features_df)}")
    print(f"Number of features: {features_df.shape[1]}")
    print(f"Number of classes: {len(target_names)}")
    print(f"Class names: {', '.join(target_names)}")

    # Display first few records
    print("\n2. FIRST 5 RECORDS")
    print("-" * 70)
    combined_df = pd.concat([features_df, target_df], axis=1)
    print(combined_df.head())

    # Display dataset shape
    print("\n3. DATASET SHAPE")
    print("-" * 70)
    print(f"Features shape: {features_df.shape}")
    print(f"Target shape: {target_df.shape}")

    # Display data types
    print("\n4. DATA TYPES")
    print("-" * 70)
    print(features_df.dtypes)

    # Check for missing values
    print("\n5. MISSING VALUES CHECK")
    print("-" * 70)
    missing_values = features_df.isnull().sum()
    print(missing_values)
    if missing_values.sum() == 0:
        print("[OK] No missing values found!")

    # Display statistical summary
    print("\n6. STATISTICAL SUMMARY")
    print("-" * 70)
    print(features_df.describe())

    # Display class distribution
    print("\n7. CLASS DISTRIBUTION")
    print("-" * 70)
    class_counts = target_df['species'].value_counts()
    for idx, count in class_counts.items():
        print(f"Class {idx} ({target_names[idx]}): {count} samples")

    print()


# ============================================================================
# STEP 4: DATA PREPROCESSING
# ============================================================================

def preprocess_data(features_df, target_df):
    """
    Preprocess the data (already clean for Iris dataset).

    Args:
        features_df: DataFrame containing feature data
        target_df: DataFrame containing target labels

    Returns:
        tuple: (X, y) preprocessed features and target
    """
    print("=" * 70)
    print("DATA PREPROCESSING")
    print("=" * 70)

    # Convert to numpy arrays
    X = features_df.values
    y = target_df.values.ravel()

    print("[OK] Data converted to numpy arrays")
    print(f"[OK] Features shape: {X.shape}")
    print(f"[OK] Target shape: {y.shape}")
    print()

    return X, y


# ============================================================================
# STEP 5: SPLIT DATASET
# ============================================================================

def split_dataset(X, y, test_size=0.2):
    """
    Split dataset into training and testing sets.

    Args:
        X: Feature matrix
        y: Target vector
        test_size: Proportion of dataset for testing (default: 0.2)

    Returns:
        tuple: (X_train, X_test, y_train, y_test)
    """
    print("=" * 70)
    print("SPLITTING DATASET")
    print("=" * 70)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=42,
        stratify=y  # Maintain class distribution
    )

    print(f"Training set size: {len(X_train)} samples ({(1-test_size)*100:.0f}%)")
    print(f"Testing set size: {len(X_test)} samples ({test_size*100:.0f}%)")
    print()

    return X_train, X_test, y_train, y_test


# ============================================================================
# STEP 6: TRAIN CLASSIFICATION MODEL
# ============================================================================

def train_models(X_train, y_train):
    """
    Train three different classification models.

    Args:
        X_train: Training features
        y_train: Training labels

    Returns:
        dict: Dictionary of trained models
    """
    print("=" * 70)
    print("TRAINING CLASSIFICATION MODELS")
    print("=" * 70)

    models = {}

    # 1. Decision Tree Classifier
    print("\n1. Training Decision Tree Classifier...")
    dt_model = DecisionTreeClassifier(random_state=42)
    dt_model.fit(X_train, y_train)
    models['Decision Tree'] = dt_model
    print("[OK] Decision Tree trained successfully!")

    # 2. K-Nearest Neighbors
    print("\n2. Training K-Nearest Neighbors (KNN)...")
    knn_model = KNeighborsClassifier(n_neighbors=3)
    knn_model.fit(X_train, y_train)
    models['KNN'] = knn_model
    print("[OK] KNN trained successfully!")

    # 3. Logistic Regression
    print("\n3. Training Logistic Regression...")
    lr_model = LogisticRegression(random_state=42, max_iter=200)
    lr_model.fit(X_train, y_train)
    models['Logistic Regression'] = lr_model
    print("[OK] Logistic Regression trained successfully!")

    print()
    return models


# ============================================================================
# STEP 7: MAKE PREDICTIONS
# ============================================================================

def make_predictions(models, X_test):
    """
    Make predictions using trained models.

    Args:
        models: Dictionary of trained models
        X_test: Testing features

    Returns:
        dict: Dictionary of predictions
    """
    print("=" * 70)
    print("MAKING PREDICTIONS")
    print("=" * 70)

    predictions = {}

    for name, model in models.items():
        y_pred = model.predict(X_test)
        predictions[name] = y_pred
        print(f"[OK] {name} predictions completed")

    print()
    return predictions


# ============================================================================
# STEP 8: EVALUATE MODEL PERFORMANCE
# ============================================================================

def evaluate_models(models, predictions, X_test, y_test, target_names):
    """
    Evaluate model performance using multiple metrics.

    Args:
        models: Dictionary of trained models
        predictions: Dictionary of predictions
        X_test: Testing features
        y_test: True labels
        target_names: Names of target classes
    """
    print("=" * 70)
    print("MODEL EVALUATION")
    print("=" * 70)

    results = {}

    for name in models.keys():
        print(f"\n{'=' * 70}")
        print(f"{name.upper()}")
        print(f"{'=' * 70}")

        y_pred = predictions[name]

        # Calculate accuracy
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy

        print(f"\n1. ACCURACY SCORE")
        print("-" * 70)
        print(f"Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

        # Confusion Matrix
        print(f"\n2. CONFUSION MATRIX")
        print("-" * 70)
        cm = confusion_matrix(y_test, y_pred)
        print(cm)

        # Classification Report
        print(f"\n3. CLASSIFICATION REPORT")
        print("-" * 70)
        print(classification_report(y_test, y_pred, target_names=target_names))

    # Display comparison
    print("\n" + "=" * 70)
    print("MODEL COMPARISON")
    print("=" * 70)
    for name, accuracy in results.items():
        print(f"{name:25s}: {accuracy:.4f} ({accuracy*100:.2f}%)")

    best_model = max(results, key=results.get)
    print(f"\n[BEST] Best Model: {best_model} with {results[best_model]*100:.2f}% accuracy")
    print()

    return results


# ============================================================================
# STEP 9: VISUALIZE RESULTS
# ============================================================================

def visualize_results(models, predictions, y_test, target_names, results):
    """
    Create visualizations for model performance.

    Args:
        models: Dictionary of trained models
        predictions: Dictionary of predictions
        y_test: True labels
        target_names: Names of target classes
        results: Dictionary of accuracy results
    """
    print("=" * 70)
    print("GENERATING VISUALIZATIONS")
    print("=" * 70)

    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Iris Classification - Model Performance', fontsize=16, fontweight='bold')

    # 1. Accuracy Comparison
    ax1 = axes[0, 0]
    model_names = list(results.keys())
    accuracies = list(results.values())
    colors = ['#2ecc71', '#3498db', '#e74c3c']

    bars = ax1.bar(model_names, accuracies, color=colors, alpha=0.7, edgecolor='black')
    ax1.set_ylabel('Accuracy', fontsize=12)
    ax1.set_title('Model Accuracy Comparison', fontsize=14, fontweight='bold')
    ax1.set_ylim(0, 1.1)
    ax1.grid(axis='y', alpha=0.3)

    # Add percentage labels on bars
    for bar, accuracy in zip(bars, accuracies):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{accuracy*100:.2f}%',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # 2. Confusion Matrix for best model
    ax2 = axes[0, 1]
    best_model_name = max(results, key=results.get)
    cm = confusion_matrix(y_test, predictions[best_model_name])

    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=target_names, yticklabels=target_names,
                cbar_kws={'label': 'Count'}, ax=ax2)
    ax2.set_xlabel('Predicted Label', fontsize=12)
    ax2.set_ylabel('True Label', fontsize=12)
    ax2.set_title(f'Confusion Matrix - {best_model_name}', fontsize=14, fontweight='bold')

    # 3. Class-wise accuracy for best model
    ax3 = axes[1, 0]
    report = classification_report(y_test, predictions[best_model_name],
                                  target_names=target_names, output_dict=True)

    class_accuracies = [report[cls]['f1-score'] for cls in target_names]
    bars = ax3.bar(target_names, class_accuracies, color=['#9b59b6', '#f39c12', '#1abc9c'],
                   alpha=0.7, edgecolor='black')
    ax3.set_ylabel('F1-Score', fontsize=12)
    ax3.set_title(f'Per-Class Performance - {best_model_name}', fontsize=14, fontweight='bold')
    ax3.set_ylim(0, 1.1)
    ax3.grid(axis='y', alpha=0.3)

    # Add labels
    for bar, score in zip(bars, class_accuracies):
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height,
                f'{score:.3f}',
                ha='center', va='bottom', fontsize=10, fontweight='bold')

    # 4. Prediction distribution
    ax4 = axes[1, 1]
    unique, counts = np.unique(predictions[best_model_name], return_counts=True)
    pred_labels = [target_names[i] for i in unique]

    ax4.pie(counts, labels=pred_labels, autopct='%1.1f%%', startangle=90,
           colors=['#e74c3c', '#3498db', '#2ecc71'], explode=[0.05]*len(counts))
    ax4.set_title(f'Prediction Distribution - {best_model_name}', fontsize=14, fontweight='bold')

    plt.tight_layout()
    plt.savefig('iris_classification_results.png', dpi=300, bbox_inches='tight')
    print("[OK] Visualization saved as 'iris_classification_results.png'")
    plt.show()
    print()


# ============================================================================
# STEP 10: MAKE SAMPLE PREDICTIONS
# ============================================================================

def predict_sample(models, target_names):
    """
    Make predictions on sample input data.

    Args:
        models: Dictionary of trained models
        target_names: Names of target classes
    """
    print("=" * 70)
    print("SAMPLE PREDICTIONS")
    print("=" * 70)

    # Sample inputs (sepal length, sepal width, petal length, petal width)
    samples = [
        [5.1, 3.5, 1.4, 0.2],  # Typical Setosa
        [6.5, 3.0, 5.2, 2.0],  # Typical Virginica
        [5.7, 2.8, 4.1, 1.3],  # Typical Versicolor
    ]

    sample_names = ['Sample 1', 'Sample 2', 'Sample 3']

    best_model_name = 'Decision Tree'  # Use best performing model
    model = models[best_model_name]

    print(f"\nUsing {best_model_name} for predictions\n")

    for i, (sample, name) in enumerate(zip(samples, sample_names), 1):
        print(f"{name}:")
        print(f"  Input: Sepal Length={sample[0]}, Sepal Width={sample[1]}, "
              f"Petal Length={sample[2]}, Petal Width={sample[3]}")

        # Reshape for prediction
        sample_array = np.array(sample).reshape(1, -1)
        prediction = model.predict(sample_array)[0]

        print(f"  Prediction: {target_names[prediction]}")
        print()


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main function to execute the complete classification workflow.
    """
    print("\n")
    print("=" * 70)
    print("           IRIS FLOWER CLASSIFICATION PROJECT")
    print("              Machine Learning Internship")
    print("=" * 70)
    print()

    # Step 2: Load Dataset
    features_df, target_df, target_names, feature_names = load_dataset()

    # Step 3: Explore Dataset
    explore_dataset(features_df, target_df, target_names)

    # Step 4: Preprocess Data
    X, y = preprocess_data(features_df, target_df)

    # Step 5: Split Dataset
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    # Step 6: Train Models
    models = train_models(X_train, y_train)

    # Step 7: Make Predictions
    predictions = make_predictions(models, X_test)

    # Step 8: Evaluate Models
    results = evaluate_models(models, predictions, X_test, y_test, target_names)

    # Step 9: Visualize Results
    visualize_results(models, predictions, y_test, target_names, results)

    # Step 10: Sample Predictions
    predict_sample(models, target_names)

    print("=" * 70)
    print("PROJECT COMPLETED SUCCESSFULLY! [OK]")
    print("=" * 70)
    print()


# ============================================================================
# RUN THE PROGRAM
# ============================================================================

if __name__ == "__main__":
    main()
