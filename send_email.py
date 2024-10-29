import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import sys

def send_email(to_email, subject, body):
  """
  Function to send an email via an SMTP server.
  :param to_email: Recipient's email address
  :param subject: Email subject
  :param body: Email body
  """
  # Get SMTP settings from environment variables
  smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
  smtp_port = int(os.getenv("SMTP_PORT", 465))
  smtp_user = os.getenv("SMTP_USER")
  smtp_password = os.getenv("SMTP_PASSWORD")

  if not smtp_user or not smtp_password:
    raise ValueError("SMTP_USER and SMTP_PASSWORD must be set as environment variables.")

  # Construct the email content
  msg = MIMEMultipart()
  msg["From"] = smtp_user
  msg["To"] = to_email
  msg["Subject"] = subject
  msg.attach(MIMEText(body, "plain"))

  # Send the email using SMTP
  try:
    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    server.login(smtp_user, smtp_password)
    server.sendmail(smtp_user, to_email, msg.as_string())
    server.quit()
    print(f"Email successfully sent to {to_email}")
  except Exception as e:
    print(f"Error sending email: {e}")
    sys.exit(1)

if __name__ == "__main__":
  """
  Main program entry point, gets recipient, subject, and body from command line arguments and sends the email.
  """
  if len(sys.argv) != 4:
    print("Usage: python send_email.py <to_email> <subject> <body>")
    sys.exit(1)

  to_email = sys.argv[1]
  subject = sys.argv[2]
  body = sys.argv[3]

  send_email(to_email, subject, body)
