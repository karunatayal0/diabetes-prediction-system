# 🩺 Diabetes Prediction System (Deployment Repository)

## 📖 About the Project
The **Diabetes Prediction System** is a machine learning application designed to predict the likelihood of diabetes in patients based on medical diagnostic measurements (such as Glucose, BMI, Age, Insulin, etc.). It utilizes a **Decision Tree Classifier** to analyze the data and categorize the patient's risk level.

⚠️ **Important Note:** This repository is specifically structured and configured for **Render Deployment/Hosting**. 

If you are looking for the complete machine learning workflow—including data exploration, feature selection, outlier removal, model training, and the raw dataset—please visit the Google Colab Notebook linked below:
👉 **[Full Source Code & Dataset (Google Colab)](https://colab.research.google.com/drive/1ZEitm2I-HxMkSzjSPVODiFR1kan1rFGs?usp=sharing)**

## 🛠️ Tools & Technologies Used
* **Machine Learning:** Scikit-learn (Decision Tree Classifier)
* **Data Processing:** Pandas, NumPy
* **Model Serialization:** Joblib
* **Web UI Framework:** Gradio
* **Cloud Hosting:** Render
* **Development Environment:** Google Colab / Jupyter

---

## 🚀 How to Host Your Own Model on Render
You can use this repository as a template to host your own machine learning models on the web for free. Follow these step-by-step instructions:

### Step 1: Prepare Your Code
1. **Clone this repository** to your local machine.
2. **Push the code** to a new, public repository on your personal GitHub account.
3. **Train your model** (you can use the provided Colab link above) and export it as a `.pkl` file using `joblib`.
4. Place your `.pkl` file into the root of your cloned repository.
5. **Configure `app.py`**: Open the `app.py` file and update it so that the input parameters match the exact features your model was trained on. Ensure you also update the code to load your specific `model_name.pkl` file.

### Step 2: Deploy on Render
1. Go to [Render.com](https://render.com/) and Log In or Sign Up.
2. Click on the **New** button in the dashboard and select **Web Service**.
3. Connect your GitHub account and select the repository you just created.
4. Fill in the deployment details:
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `python app.py`
5. Scroll down and select the **Free** instance type.
6. Click **Create Web Service**. 

Boom! 💥 Render will build your environment and give you a live URL. Your machine learning project is now live on the internet!

---

## 🌐 Live Demo
Check out the live, working version of this project hosted on Render:
👉 **[Diabetes Prediction System - Live App](https://diabetes-prediction-system-cxme.onrender.com/)**
