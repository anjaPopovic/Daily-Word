# Daily Word

## Simple Project for CS230 - Distributed Systems

This project implements a direct subscription system in Python.

## Project Proposal

The project titled "Daily Word" allows users to subscribe via a website and receive an email with the daily word every morning at 9:30 AM.

## Application Structure

The application uses the Flask framework for web communication. Entered email addresses are stored in an SQLite database, and emails are sent using the SMTP protocol with MIME extension. The BackgroundScheduler triggers the email-sending function every morning at 9:30 AM.

### Functionalities

The application is divided into several Python files:

- `database.py`: Creates the connection to the database and forms the `daily_words` table (for storing daily words) and the `emails` table (for storing subscribed emails).
- `add_words.py`: Defines the `add_daily_word` function to insert words into the database.
- `send_words.py`: Contains the functions `send_daily_word` for sending the daily word to a specific email address and `send_daily_word_to_all` for sending the word to all subscribers. These functions use the SMTP server to send the emails.
- `app.py`: Establishes the foundation for the web application using Flask, including routes for displaying the homepage and handling user sign-ups. It also uses BackgroundScheduler to schedule the daily email dispatch.

### Application Interface

The homepage of the application:

![image](https://github.com/user-attachments/assets/a71af1f7-0660-439d-a84e-35cdb80b7b0b)

## Conclusion

The "Daily Word" project demonstrates the successful use of the Flask framework, SQLite database, SMTP protocol, and BackgroundScheduler. The created application enables subscriptions and the daily sending of new English words via email.
