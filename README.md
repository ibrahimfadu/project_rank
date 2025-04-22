# 🎓 Engineering College Prediction System (DCET-Based)

A web-based application that helps students predict potential engineering colleges based on their **DCET rank**, **category**, and **preferred branch**, using machine learning and historical cutoff data.

🔗 **Live Demo**: [https://project-xhyg.onrender.com/recommend](https://project-xhyg.onrender.com/recommend)

---

## 🚀 Features

- ✅ Predicts college admission chances based on DCET rank, category, and branch
- 📊 Uses historical cutoff data from 2019–2023
- 🧠 Built with a Linear Regression ML model for accurate prediction
- 🌐 Web interface using Flask + Jinja2 templates
- 📁 Data stored in CSV files (no external database required)
- 📦 Deployed on Render
- ⚡ Fast predictions within 1–3 seconds

---

## 🧠 Machine Learning

- **Algorithm**: Linear Regression  
- **Data**: Cleaned and preprocessed CSV files from 2019–2023  
- **Preprocessing**:
  - Label Encoding for categorical features
  - Removed invalid entries (e.g., 0, 99999)
- **Evaluation**:
  - MAE (Mean Absolute Error): ~812
  - Accuracy within 5–10% in real-world cases
- **Model Storage**: `joblib`

---

## 🛠️ Technology Stack

| Component        | Technology               |
|------------------|---------------------------|
| Language         | Python                    |
| Web Framework    | Flask                     |
| Frontend         | HTML, CSS                 |
| ML Libraries     | scikit-learn, pandas, numpy |
| Model Storage    | joblib                    |
| Hosting          | Render                    |

---

## 📷 Website Preview

- **Input Form**: Accepts Rank, Category, Branch  
- **Output Table**: Displays predicted cutoff & college suggestions  
- **Responsive**: Desktop UI ready (mobile support in progress)

---

## 🛠️ Installation & Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/college-prediction-system.git
cd college-prediction-system

# 2. Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py

# 5. Visit in browser
http://localhost:5000

```
## ✅ Testing Summary

- **MAE (Mean Absolute Error)** on test data: **812**  
  _Calculated based on the model’s performance on test data._
- **Prediction accuracy**: **85–90%**  
  _This is the model's accuracy within real-world use cases._
- **Response time**: **1–3 seconds**  
  _The time it takes for the model to provide predictions._
- **Desktop UI**: ✅ **Smooth and responsive**
- **Mobile UI**: ❌ **Needs improvement**

---

## 🧪 Model Evaluation & Testing

The performance of the model is evaluated using the following metrics:

1. **Mean Absolute Error (MAE)**: This metric helps us understand the average difference between the predicted and actual values. A lower value indicates better model performance.
2. **Prediction Accuracy**: Represents the percentage of correct predictions the model makes.
3. **Response Time**: Time taken to generate a
