import smtplib
from email.mime.text import MIMEText

sender_email = "abinaya12.tech@gmail.com"
app_password = "zwqd qhrv vyvx wrxn"

receiver_email = "abinaya12.tech@gmail.com"

subject = "🚨 Linux Self-Healing Monitor Alert"

body = """
Hello,

Your Linux Self-Healing Monitor detected a service failure.

The cron service was DOWN.

The monitor attempted an automatic restart.

Please check your dashboard for more details.

Regards,
Linux Self-Healing Monitor
"""

msg = MIMEText(body)

msg["Subject"] = subject
msg["From"] = sender_email
msg["To"] = receiver_email

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(sender_email, app_password)

    server.sendmail(sender_email, receiver_email, msg.as_string())

    server.quit()

    print("Email sent successfully!")

except Exception as e:

    print("Error:", e)

