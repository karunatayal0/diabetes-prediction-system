import gradio as gr
import joblib

# Load the trained model
model = joblib.load("diabetes_prediction_model.pkl")


def predict_diabetes(pregnancies, glucose, bmi, age):
    input_data = [[pregnancies, glucose, bmi, age]]
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        return "High Risk of Diabetes (Positive)"
    else:
        return "Low Risk of Diabetes (Negative)"


demo = gr.Interface(
    fn=predict_diabetes,
    inputs=[
        gr.Number(label="Pregnancies"),
        gr.Number(label="Glucose"),
        gr.Number(label="BMI"),
        gr.Number(label="Age"),
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Diabetes Prediction System",
    description="Enter the patient's details to predict diabetes risk."
)

demo.launch()
