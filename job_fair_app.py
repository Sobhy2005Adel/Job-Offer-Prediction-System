import streamlit as st
import pandas as pd
import joblib
import base64

# ========== إعداد واجهة الصفحة ==========
st.set_page_config(
    page_title="نظام التنبؤ بعرض العمل",
    page_icon="🧠",
    layout="centered",
)

# ========== خلفية مخصصة ==========
def set_background(image_path):
    with open(image_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    background_css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(background_css, unsafe_allow_html=True)

set_background("D:/job_offer_model/484563071_1050021197152845_3604579975566674094_n.jpg")  # ضع اسم صورة الخلفية هنا (يجب أن تكون في نفس المجلد)

st.markdown("""
    <style>
    h1, h2, h3, h4, h5, h6, p, label, .stTextInput > label, .stSlider > label, .stCheckbox > label, .stSelectbox > label {
        color: black !important;
    }
    .stMetricLabel {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)
# طبقة تغطية شفافة فوق الخلفية لتحسين وضوح الكلام
st.markdown("""
    <style>
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(255,255,255,0.6); /* غطاء أبيض شفاف */
        z-index: 0;
    }

    .stApp > * {
        position: relative;
        z-index: 1;
    }
    </style>
""", unsafe_allow_html=True)


# ========== تحميل النموذج والخصائص ==========
@st.cache_resource
def load_model():
    try:
        model = joblib.load('job_offer_model.joblib')
        features = pd.read_csv('model_features.csv')['feature'].tolist()
        return model, features
    except Exception as e:
        st.error(f"خطأ في تحميل النموذج: {str(e)}")
        return None, None

model, model_features = load_model()

# ========== العنوان والشعار ==========
st.markdown("<h1 style='text-align: center; color: white;'>🎓 نظام التنبؤ بعروض العمل</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #cccccc;'>ادخل بيانات الطالب لمعرفة احتمالية حصوله على عرض عمل</p>", unsafe_allow_html=True)

# ========== النموذج ==========
if model is not None:
    with st.form("student_form"):
        st.subheader("📌 البيانات الأساسية")
        col1, col2 = st.columns(2)
        with col1:
            experience = st.slider("سنوات الخبرة", 0, 10, 2)
            grades = st.slider("متوسط الدرجات (%)", 50, 100, 75)
        with col2:
            projects = st.slider("عدد المشاريع", 0, 20, 5)
            extracurriculars = st.slider("الأنشطة اللامنهجية", 0, 10, 2)

        st.subheader("🧰 المهارات التقنية")
        col3, col4, col5 = st.columns(3)
        with col3:
            python = st.checkbox("Python")
            java = st.checkbox("Java")
        with col4:
            sql = st.checkbox("SQL")
            ml = st.checkbox("Machine Learning")
        with col5:
            data_analysis = st.checkbox("Data Analysis")
            cpp = st.checkbox("C++")

        submitted = st.form_submit_button("🔍 تنبأ")

    if submitted:
        input_data = {
            'experience_years': experience,
            'course_grades': grades,
            'projects_completed': projects,
            'extracurriculars': extracurriculars,
            'Python': int(python),
            'Java': int(java),
            'SQL': int(sql),
            'Machine Learning': int(ml),
            'Data Analysis': int(data_analysis),
            'C++': int(cpp)
        }

        input_df = pd.DataFrame([input_data], columns=model_features)
        prediction = model.predict(input_df)[0]
        proba = model.predict_proba(input_df)[0]

        st.subheader("📊 النتيجة")

        if prediction == 1:
            st.success(f"✅ محتمل الحصول على عرض عمل\n\n📈 الاحتمالية: {proba[1]*100:.1f}%")
        else:
            st.error(f"❌ غير محتمل الحصول على عرض عمل\n\n📉 الاحتمالية: {proba[1]*100:.1f}%")

        st.markdown("### ⚙️ تفاصيل الاحتمالية")
        st.progress(proba[1])
        st.metric("عرض عمل", f"{proba[1]*100:.1f} %")
        st.metric("لا عرض عمل", f"{proba[0]*100:.1f} %")

        st.info("🔧 نصائح لتحسين الفرص:")
        if grades < 75:
            st.write("- حاول رفع معدلك الأكاديمي")
        if experience < 2:
            st.write("- احرص على اكتساب خبرة عملية")
        if not (python or java):
            st.write("- تعلم لغة برمجة أساسية مثل Python أو Java")

else:
    st.warning("⚠️ تعذر تحميل النموذج، تأكد من وجود الملفات المطلوبة.")

