'''from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

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
        return jsonify({'message': f'Failed to send email. Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)'''

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    data = request.get_json()

    from_address = data['from_address']
    to_address = data['to_address']
    password = data['password']
    subject = data['subject']
    body = data['body']

    # Determine SMTP server and port based on email provider
    if 'gmail.com' in from_address:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
    elif 'outlook.com' in from_address :
        smtp_server = "smtp.office365.com"
        smtp_port = 587
    else:
        return jsonify({'message': 'Unsupported email provider'}), 400

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
        return jsonify({'message': f'Failed to send email. Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050)
