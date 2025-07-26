# Job-Offer-Prediction-System
🎓 Job Offer Prediction System
This is a Streamlit-based web application that predicts whether a student is likely to receive a job offer based on their academic performance, technical skills, and other activities.

🚀 Features
Predicts job offer likelihood using a trained machine learning model

Simple user interface with sliders and checkboxes

Provides probability scores and actionable recommendations

Arabic UI and styling with custom background

📁 Project Structure
bash
نسخ
تحرير
.
├── job_fair_app.py               # Streamlit web application
├── job_fair_model.ipynb         # Notebook used to train and export the model
├── job_offer_model.joblib       # Trained machine learning model
├── model_features.csv           # Feature list used by the model
├── background.jpg               # Background image (used in app)
└── README.md                    # Project description
🧪 Model Inputs
سنوات الخبرة (Years of Experience)

متوسط الدرجات (Average Grades)

عدد المشاريع (Projects Completed)

الأنشطة اللامنهجية (Extracurricular Activities)

Technical skills (Python, Java, SQL, Machine Learning, Data Analysis, C++)

🛠️ How to Run
Clone the repository or copy the project files.

Install the required libraries:

bash
pip install streamlit pandas joblib
نسخ
تحريpip install streamlit pandas joblib
Make sure the following files exist in the same directory:

job_offer_model.joblib

model_features.csv

Your background image (e.g. background.jpg) and update the path in job_fair_app.py

Run the Streamlit app:

bash
نسخ
تحرير
streamlit run job_fair_app.py
📌 Notes
The app uses a fixed background image. Ensure the path in set_background() is valid.

The model must match the input features exactly as listed in model_features.csv.

📚 Language
The application is in Arabic, making it accessible to Arabic-speaking students and educators.

🧠 Model Training
For training or modifying the model, refer to job_fair_model.ipynb. It includes the code to train a classifier and export it using joblib.
