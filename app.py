from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from send_words import send_daily_word_to_all
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])

def subscribe():
    email = request.form['email']

    try:
        conn = sqlite3.connect('daily_word.db')
        c = conn.cursor()
        c.execute("INSERT INTO emails (email) VALUES (?)", (email,))
        conn.commit()
        flash("Your subscription was successful! Your word of the day will be sent to your email every morning at 9.30.")
    except sqlite3.IntegrityError:
        flash("You already subscribed!")

    return redirect(url_for('index'))

scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_word_to_all, 'cron', hour=9, minute=30)
scheduler.start()

if __name__ == '__main__':
    app.run(debug=True)
