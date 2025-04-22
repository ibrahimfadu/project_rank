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

🧪 Testing Summary

Feature	Status
Input validation	✅ Success
Accurate prediction (85–90%)	✅ Success
Fast response time (1–3 sec)	✅ Success
Mobile compatibility	❌ Needs work
Error handling	✅ Success
🔮 Future Enhancements
Mobile-friendly UI

AI-based career path suggestions

Chatbot for admission guidance

Real-time application tracking

Interactive college explorer

Integration with scholarship databases

👨‍🎓 Target Users
DCET students & parents

Coaching institutes

Education counselors & researchers

📜 License & Credits
Built with ❤️ by Ibrahim Khaleel

Open-source under MIT License

Data sourced from official DCET records and educational platforms

🌐 Live Demo
👉 https://project-xhyg.onrender.com/recommend
