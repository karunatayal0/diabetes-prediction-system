import os
import gradio as gr
import joblib

model = joblib.load("diabetes_prediction_model.pkl")

def predict_diabetes(pregnancies, glucose, bmi, age):
    try:
        input_data = [[pregnancies, glucose, bmi, age]]
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            return "High Risk of Diabetes (Positive)"
        else:
            return "Low Risk of Diabetes (Negative)"

    except Exception as e:
        return str(e)
        
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
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )
