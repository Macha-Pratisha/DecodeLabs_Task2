# Installation Guide

## Libraries Installed on D: Drive Only

All libraries are installed in a virtual environment on **D:** drive to save space on C: drive.

---

## What Was Installed

The following packages are installed in:
```
D:\DecodeLabs\Project-2-Iris-Classification\venv\
```

### Packages:
- **pandas** - Data manipulation
- **numpy** - Numerical computations
- **scikit-learn** - Machine learning algorithms
- **matplotlib** - Data visualization
- **seaborn** - Statistical visualizations

---

## How to Run the Project

### Method 1: Using the Batch File (Easiest)

Double-click on:
```
run_project.bat
```

This will:
1. Activate the virtual environment automatically
2. Run the iris classifier
3. Show all results in the terminal

---

### Method 2: Manual Activation

1. **Open Command Prompt**

2. **Navigate to project:**
   ```bash
   cd D:\DecodeLabs\Project-2-Iris-Classification
   ```

3. **Activate virtual environment:**
   ```bash
   venv\Scripts\activate
   ```

4. **Run the project:**
   ```bash
   python iris_classifier.py
   ```

5. **Deactivate when done:**
   ```bash
   deactivate
   ```

---

## Verifying Installation

To check if all libraries are installed correctly:

```bash
cd D:\DecodeLabs\Project-2-Iris-Classification
venv\Scripts\activate
python -c "import pandas, numpy, sklearn, matplotlib, seaborn; print('All libraries OK!')"
```

You should see: `All libraries OK!`

---

## Disk Space Used

Approximate space used on D: drive:
- Virtual environment: ~300-400 MB
- Project code: < 1 MB
- Generated images: < 1 MB

**Total: ~400 MB on D: drive only**

---

## Troubleshooting

### Issue: "Cannot find venv"

**Solution:**
The virtual environment needs to be created. Run:
```bash
cd D:\DecodeLabs\Project-2-Iris-Classification
python -m venv venv
venv\Scripts\pip install -r requirements.txt
```

### Issue: "python is not recognized"

**Solution:**
Add Python to PATH or use full path:
```bash
C:\Python\python.exe -m venv venv
```

### Issue: "Permission denied"

**Solution:**
Run Command Prompt as Administrator

---

## Reinstalling Libraries

If you need to reinstall everything:

```bash
cd D:\DecodeLabs\Project-2-Iris-Classification
rmdir /s venv
python -m venv venv
venv\Scripts\pip install -r requirements.txt
```

---

## Using Different Python Version

If you have multiple Python versions:

```bash
# Use Python 3.9
C:\Python39\python.exe -m venv venv

# Use Python 3.10
C:\Python310\python.exe -m venv venv

# Use Python 3.11
py -3.11 -m venv venv
```

---

## Checking Package Versions

```bash
venv\Scripts\activate
pip list
```

Expected versions:
```
pandas        >= 1.3.0
numpy         >= 1.21.0
scikit-learn  >= 1.0.0
matplotlib    >= 3.4.0
seaborn       >= 0.11.0
```

---

## Uninstalling

To completely remove the virtual environment:

```bash
cd D:\DecodeLabs\Project-2-Iris-Classification
rmdir /s venv
```

This will free up ~400 MB on D: drive.

---

## ✅ Everything is Ready!

Your installation on **D: drive** is complete and ready to use!

Simply run:
```bash
run_project.bat
```

Or manually:
```bash
cd D:\DecodeLabs\Project-2-Iris-Classification
venv\Scripts\activate
python iris_classifier.py
```

**No C: drive space used!** ✓
