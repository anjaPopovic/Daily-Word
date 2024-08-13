import sqlite3
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_daily_word(email, word, meaning, example):
    email_from = 'popovicanja200@gmail.com'
    email_password = 'pmzlryvkspochdka'

    html_content = f"""
    <html>
    <body>
        <p>Today's word is <strong>{word}</strong></p>
        <p><b>Meaning:</b> {meaning}</p>
        <p><b>Example:</b> <i>{example}</i></p>
    </body>
    </html>
    """
    msg = MIMEMultipart("alternative")
    msg['Subject'] = 'Your Daily Word'
    msg['From'] = email_from
    msg['To'] = email

    part2 = MIMEText(html_content, "html")
    msg.attach(part2)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_from, email_password)
            text = msg.as_string()
            server.sendmail(email_from, email, text)
            logging.info(f"Email sent to {email}")
    except Exception as e:
        logging.error(f"Failed to send email to {email}. Error: {e}")

def send_daily_word_to_all():
    conn = sqlite3.connect('daily_word.db')
    c = conn.cursor()

    c.execute("SELECT email FROM emails")
    users = c.fetchall()

    c.execute("SELECT word_id, word, meaning, example FROM daily_words WHERE sent = 0 ORDER BY word_id ASC LIMIT 1")
    word_data = c.fetchone()

    if word_data:
        word_id, word, meaning, example = word_data
        for user in users:
            email = user[0]
            send_daily_word(email, word, meaning, example)
        c.execute("UPDATE daily_words SET sent = 1 WHERE word_id = ?", (word_id,))
        conn.commit()
    else:
        logging.info("No words in the database.")

    conn.close()


