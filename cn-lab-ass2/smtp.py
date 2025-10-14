import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(
    filename="email_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Replace with your Ethereal credentials
SMTP_SERVER = "smtp.ethereal.email"
SMTP_PORT = 587
USERNAME = "rafaela.lehner63@ethereal.email"
PASSWORD = "akE6ZenG59ms5VvB7y"

def send_email():
    sender = USERNAME
    receiver = "receiver@example.com" 

    # Create the email
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Test Email from Python"

    body = "Hello! This is a test email sent using Ethereal Email (no phone needed)."
    msg.attach(MIMEText(body, "plain"))

    logging.info("Connecting to SMTP server...")
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    
    logging.info("Starting TLS encryption...")
    server.starttls()
    
    logging.info("Logging in...")
    login_response = server.login(USERNAME, PASSWORD)
    
    if login_response[0] == 235:
        logging.info("Sending email...")
        send_response = server.sendmail(sender, receiver, msg.as_string())
        
        if send_response == {}:
            logging.info("Closing connection...")
            server.quit()
            print("Email sent! Check Ethereal dashboard.")
            logging.info("Email sent successfully!")
        else:
            print("Error: Failed to send email.")
            logging.error("Error: Failed to send email.")
    else:
        print("Error: Login failed.")
        logging.error("Login failed.")

send_email()

