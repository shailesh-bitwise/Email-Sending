from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS


@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()

    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_address = data['from_address']
    to_address = data['to_address']
    password = data['password']
    subject = data['subject']
    body = data['body']

    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(from_address, password)
        server.send_message(msg)
        server.quit()
        return jsonify({'message': 'Email sent successfully!'}), 200
    except Exception as e:
        return jsonify({'message': f'Failed to send email. Error: {e}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
