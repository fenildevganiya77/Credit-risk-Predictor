# 💳 Credit Risk Prediction System

A Machine Learning web application that predicts whether a loan applicant is at **Low Credit Risk** or **High Credit Risk** based on their financial and personal information.

The project is developed using **Python**, **Scikit-learn**, and **Streamlit** and provides an interactive interface for real-time credit risk prediction.

---

## 📌 Project Overview

Financial institutions use credit risk assessment to determine whether an applicant is likely to repay a loan. This project applies machine learning techniques to automate that prediction process.

The application accepts customer details as input and predicts the applicant's credit risk instantly.

---

## 🚀 Features

- Interactive Streamlit Web Application
- Real-time Credit Risk Prediction
- Machine Learning Classification Model
- User-friendly Interface
- Data Preprocessing using Scikit-learn Pipeline
- Model saved using Joblib

---

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📊 Dataset

The project uses the **Credit Risk Dataset** containing customer information such as:

- Age
- Income
- Home Ownership
- Employment Length
- Loan Amount
- Loan Intent
- Loan Grade
- Interest Rate
- Loan Percent Income
- Historical Defaults
- Credit History Length

Target Variable:

- **0 → Low Credit Risk**
- **1 → High Credit Risk**

---

## 🤖 Machine Learning Model

After comparing different algorithms, the final deployed model is trained using **Scikit-learn** and saved as a serialized `.pkl` file.

---

## 📂 Project Structure

```text
Credit-risk-Predictor/
│
├── app.py
├── README.md
│
├── model/
│   └── model.pkl
│
├── dataset/
│   └── credit_risk_dataset.csv
│
└── notebook/
    └── task1.ipynb
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/fenildevganiya77/Credit-risk-Predictor.git
```

Move into the project directory

```bash
cd Credit-risk-Predictor
```

---

### Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r streamlit pandas numpy scikit-learn joblib pickle
```

---

### Run the Application

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

---

## 👨‍💻 Author

**Fenil Devganiya**

2nd year B.Tech – Data Science & Artificial Intelligence

Indian Institute of Technology Bhilai

GitHub: https://github.com/fenildevganiya77

---

## 📄 License

This project was developed for learning purposes and as part of the **CodeAlpha Machine Learning Internship**.
