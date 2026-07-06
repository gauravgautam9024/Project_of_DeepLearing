import streamlit as st
import requests

st.title("🧠 Deepfake Detection App")

uploaded_file = st.file_uploader("Upload Face Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            # "http://127.0.0.1:8000/predict",
            # files=files
    "https://your-fastapi-url.onrender.com/predict",
    files=files
        )

        result = response.json()

        st.success(f"Prediction: {result['prediction']}")
        st.info(f"Confidence: {result['confidence']}")
# import streamlit as st
# import joblib

# # Load model
# model = joblib.load("resume_model.pkl")

# st.set_page_config(page_title="Resume Screening System")

# st.title("📄 Resume Screening System")
# st.write("Enter resume skills/text and predict the job role.")

# resume_text = st.text_area(
#     "Paste Resume Text",
#     height=200,
#     placeholder="Example: Python SQL Pandas Machine Learning Data Analysis"
# )

# if st.button("Predict Role"):

#     if resume_text.strip() == "":
#         st.warning("Please enter resume text.")
#     else:
#         prediction = model.predict([resume_text])[0]

#         st.success(f"Predicted Role: {prediction}")
# import streamlit as st
# import pandas as pd
# import joblib

# # load model
# model = joblib.load("car_model.pkl")

# # title
# st.title("🚗 Car Mileage Prediction App")

# st.write("Enter car details:")

# # dropdown options (training data ke hisaab se)
# brand = st.selectbox("Brand", ["Tesla", "BMW", "Audi", "Ford"])
# fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "Electric"])
# trans = st.selectbox("Transmission", ["Manual", "Automatic"])
# model_name = st.selectbox("Model", ["Model X", "5 Series", "A4", "Model Y", "Mustang"])

# # numerical inputs
# year = st.number_input("Year", min_value=2000, max_value=2025, value=2015)
# engine = st.number_input("Engine Size", value=2.0)
# price = st.number_input("Price", value=50000.0)
# car_age = st.number_input("Car Age", value=5)
# mpy = st.number_input("Mileage per year", value=10000.0)

# # prediction button
# if st.button("Predict Mileage"):

#     # create dataframe (IMPORTANT)
#     input_df = pd.DataFrame([{
#         "Brand": brand,
#         "Year": year,
#         "Engine Size": engine,
#         "Fuel Type": fuel,
#         "Transmission": trans,
#         "Price": price,
#         "Model": model_name,
#         "Car_Age": car_age,
#         "Mileage_per_year": mpy
#     }])

#     try:
#         prediction = model.predict(input_df)
#         st.success(f"Estimated Mileage: {prediction[0]:.2f}")
#     except Exception as e:
#         st.error(f"Error: {e}")# import streamlit as st
# st.title("Test App")

# st.write("App working hai ✅")