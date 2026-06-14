# Quick Start Guide - Iris Classification Project

## ⚡ Get Started in 5 Minutes!

---

## Step 1: Check Python Installation

Open terminal/command prompt and check Python version:

```bash
python --version
```

You should see: `Python 3.7` or higher

**If not installed:**
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

---

## Step 2: Navigate to Project Folder

```bash
cd D:\DecodeLabs\Project-2-Iris-Classification
```

---

## Step 3: Install Required Libraries

### Method 1: Using requirements.txt (Recommended)

```bash
pip install -r requirements.txt
```

### Method 2: Install individually

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

**Note:** Installation may take 2-5 minutes depending on your internet speed.

---

## Step 4: Run the Project

```bash
python iris_classifier.py
```

---

## 🎉 Expected Output

You should see:

```
╔====================================================================╗
║               IRIS FLOWER CLASSIFICATION PROJECT                   ║
║                    Machine Learning Internship                     ║
╚====================================================================╝

======================================================================
LOADING IRIS DATASET
======================================================================
✓ Dataset loaded successfully!

======================================================================
EXPLORATORY DATA ANALYSIS
======================================================================

1. DATASET OVERVIEW
----------------------------------------------------------------------
Number of samples: 150
Number of features: 4
Number of classes: 3
...
```

The program will:
1. Load the dataset
2. Show data exploration results
3. Train 3 models
4. Display accuracy for each model
5. Generate visualization (saves as `iris_classification_results.png`)
6. Make sample predictions

---

## 🖼️ Generated Files

After running, you'll find:
- `iris_classification_results.png` - Visualization of results

---

## ❓ Troubleshooting

### Error: "python is not recognized"

**Solution:** Use `python3` instead:
```bash
python3 iris_classifier.py
```

### Error: "No module named 'pandas'"

**Solution:** Install the libraries:
```bash
pip install -r requirements.txt
```

### Error: "pip is not recognized"

**Solution:** Install pip or use:
```bash
python -m pip install -r requirements.txt
```

### Libraries install but import fails

**Solution:** You might have multiple Python versions. Try:
```bash
python -m pip install pandas numpy scikit-learn matplotlib seaborn
python iris_classifier.py
```

### Visualization doesn't show

**Solution:** The image is saved as `iris_classification_results.png` in the current folder. Check there!

---

## 💡 What to Observe

### 1. Dataset Information
- 150 samples total
- 4 features per sample
- 3 classes (species)
- No missing values

### 2. Model Accuracies
- Decision Tree: Usually 96-100%
- KNN: Usually 96-100%
- Logistic Regression: Usually 96-100%

### 3. Confusion Matrix
- Shows how many predictions were correct/incorrect
- Diagonal values = correct predictions
- Off-diagonal = mistakes

### 4. Sample Predictions
- 3 new samples will be classified
- You'll see which species each belongs to

---

## 📝 Next Steps

After running successfully:

1. **Read the code** - Open `iris_classifier.py` in an editor
2. **Understand each step** - Read `CODE_EXPLANATION.md`
3. **Experiment** - Try changing parameters:
   - Change `test_size` in split_dataset (line 160)
   - Change `n_neighbors` in KNN (line 204)
   - Add your own sample predictions

---

## 🎯 For Your Internship Report

### What to Include:
1. Screenshot of terminal output
2. The generated visualization image
3. Accuracy scores for all three models
4. Sample predictions section

### How to Take Screenshots:
- **Windows**: Win + Shift + S
- **Mac**: Cmd + Shift + 4
- **Linux**: PrtSc or Shift + PrtSc

---

## 🚀 Running in Jupyter Notebook (Optional)

If you prefer Jupyter:

1. Install Jupyter:
   ```bash
   pip install jupyter
   ```

2. Create notebook:
   ```bash
   jupyter notebook
   ```

3. Copy code from `iris_classifier.py` into cells

---

## ⏱️ Time Requirements

- **Install libraries**: 3-5 minutes
- **Run program**: 10-20 seconds
- **Read output**: 5 minutes
- **Total**: ~10 minutes

---

## ✅ Success Checklist

- [ ] Python 3.7+ installed
- [ ] All libraries installed (`pip install -r requirements.txt`)
- [ ] Project runs without errors
- [ ] See all 10 steps in output
- [ ] Visualization image generated
- [ ] Understand the results

---

## 🎓 Understanding the Output

### Training Output
```
✓ Decision Tree trained successfully!
✓ KNN trained successfully!
✓ Logistic Regression trained successfully!
```
This means all 3 models learned from the training data.

### Accuracy Scores
```
Decision Tree            : 1.0000 (100.00%)
```
This means the model got 100% of test predictions correct!

### Confusion Matrix
```
[[10  0  0]
 [ 0  9  0]
 [ 0  0 11]]
```
Perfect diagonal = perfect predictions!

---

## 💬 Need Help?

1. Read `CODE_EXPLANATION.md` for detailed explanations
2. Check `README.md` for project overview
3. Email: pratishamacha@gmail.com

---

**You're ready! Run the project and see machine learning in action! 🚀**
