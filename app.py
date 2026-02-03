from flask import Flask, render_template, request
import os
from topsis_core import topsis
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]
    email = request.form["email"]

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(OUTPUT_FOLDER, "result.csv")

    file.save(input_path)

    topsis(input_path, weights, impacts, output_path)
    send_email(email, output_path)

    return "Result sent to your email successfully!"

def send_email(receiver, attachment_path):
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = "yourgmail@gmail.com"
    msg["To"] = receiver
    msg.set_content("Please find the TOPSIS result attached.")

    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("yourgmail@gmail.com", "APP_PASSWORD")
        server.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)