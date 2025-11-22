Gaurav Pandey: Laptop Price Predictor
Predict the market price of a laptop based on its specifications using an interactive Streamlit application.

✨ Overview
This project provides a clean, user-friendly interface for inputting various laptop features (Brand, RAM, Storage, Screen Size, etc.). The inputs are fed into a machine learning model, resulting in a predicted price.

Model: Scikit-learn Regressor (Trained and saved as pipe.pkl).

Framework: Built entirely with Streamlit.

Deployment: Hosted on Streamlit Community Cloud.

🚀 Local Setup
Follow these steps to get the app running on your machine:

Clone the Repository:

Bash

git clone https://github.com/userGauravPandey/Laptop_Price_Prediction.git
cd Laptop_Price_Prediction
Install Dependencies: A virtual environment is recommended. This command installs all required packages, including the necessary version of scikit-learn (1.7.2).

Bash

pip install -r requirements.txt
Run the App:

Bash

streamlit run app.py
The application will automatically launch in your default web browser.

📂 Project Structure
File	Purpose
app.py	Main application script (UI and prediction logic).
pipe.pkl	Trained ML model file.
df.pkl	Data source for dropdown menus.
requirements.txt	List of Python dependencies (streamlit, scikit-learn==1.7.2, etc.).

👤 Author
Gaurav Pandey
Live Demo: https://usergauravpandey-laptop-price-prediction-app-zn2y7k.streamlit.app/
