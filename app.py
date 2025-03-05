from flask import Flask, request, render_template
import pandas as pd
import math
import numpy as np

app = Flask(__name__)

# Load dataset (ensure the path is correct)
df = pd.read_csv('data/data_allv3.csv')

# Get unique categories and branches from the dataset for dropdowns
unique_categories = sorted(df['CATEGORIES'].unique())
unique_branches = sorted(df['BRANCH'].unique())
unique_branches.insert(0, "Any")  # Add an "Any" option

def calculate_probability(user_rank, cutoff, scale=50):
    if cutoff == 0 or cutoff == 99999:
        return 0
    probability = 1 / (1 + math.exp((user_rank - cutoff) / scale))
    return probability * 100

def safe_polyfit(x, y, degree):
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(y)):
        raise ValueError("Input contains NaN or infinite values")
    try:
        return np.polyfit(x, y, degree)
    except np.linalg.LinAlgError as e:
        print("Polyfit failed:", e)
        return None

def predict_cutoff_2025(row):
    years = np.array([2019, 2020, 2021, 2022, 2023, 2024])
    cutoffs = np.array([
        row['Cutoff_2019'], row['Cutoff_2020'], row['Cutoff_2021'],
        row['Cutoff_2022'], row['Cutoff_2023'], row['Cutoff_2024']
    ])
    valid_mask = (cutoffs != 0) & (cutoffs != 99999)
    if np.sum(valid_mask) < 2:
        return row['Cutoff_2024']
    filtered_years = years[valid_mask]
    filtered_cutoffs = cutoffs[valid_mask]
    coeffs = safe_polyfit(filtered_years, filtered_cutoffs, 1)
    if coeffs is None:
        return row['Cutoff_2024']
    slope, intercept = coeffs
    predicted = slope * 2025 + intercept
    return max(predicted, row['Cutoff_2024'])

df['Predicted_Cutoff_2025'] = df.apply(predict_cutoff_2025, axis=1)

def recommend_colleges(user_rank, user_category, user_branch, use_ai=False):
    reference_year = 'Predicted_Cutoff_2025' if use_ai else 'Cutoff_2024'
    recommendations = []
    
    for _, row in df.iterrows():
        cutoff = row[reference_year]
        if cutoff == 0 or cutoff == 99999:
            continue
        if row['CATEGORIES'].strip().lower() != user_category.strip().lower():
            continue
        if user_branch.strip().lower() != "any":
            if user_branch.strip().lower() not in row['BRANCH'].strip().lower():
                continue
        
        if user_rank <= cutoff:
            chance = calculate_probability(user_rank, cutoff)
            recommendations.append({
                'College': row['COLLEGE'],
                'Branch': row['BRANCH'],
                'Cutoff': int(round(cutoff)),
                'Chance (%)': round(chance, 2)
            })
    
    sorted_recommendations = sorted(recommendations, key=lambda rec: rec['Cutoff'])
    return sorted_recommendations

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', 
                           categories=unique_categories, 
                           branches=unique_branches,
                           rank="",
                           selected_category="",
                           selected_branch="Any",
                           cutoff_type="2024",
                           error=None,
                           recommendations=None)

@app.route('/recommend', methods=['POST'])
def recommend_route():
    try:
        user_rank = int(request.form.get('rank'))
    except (ValueError, TypeError):
        return render_template('index.html', 
                               error="Invalid rank input.",
                               categories=unique_categories, 
                               branches=unique_branches,
                               rank="",
                               selected_category=request.form.get('category'),
                               selected_branch=request.form.get('branch'),
                               cutoff_type=request.form.get('cutoff_type'),
                               recommendations=None)
    
    if user_rank <= 0:
        return render_template('index.html', 
                               error="DCET rank cannot be 0 or negative. Please enter a valid rank.",
                               categories=unique_categories, 
                               branches=unique_branches,
                               rank="",
                               selected_category=request.form.get('category'),
                               selected_branch=request.form.get('branch'),
                               cutoff_type=request.form.get('cutoff_type'),
                               recommendations=None)
    
    user_category = request.form.get('category')
    user_branch = request.form.get('branch')
    cutoff_type = request.form.get('cutoff_type')
    use_ai = cutoff_type == "ai"
    
    recommendations = recommend_colleges(user_rank, user_category, user_branch, use_ai)
    
    return render_template('index.html', 
                           recommendations=recommendations, 
                           categories=unique_categories, 
                           branches=unique_branches,
                           rank=user_rank,
                           selected_category=user_category,
                           selected_branch=user_branch,
                           cutoff_type=cutoff_type,
                           error=None)

if __name__ == '__main__':
    app.run(debug=True)
