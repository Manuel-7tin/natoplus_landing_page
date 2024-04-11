# Import required libraries and packages
from flask import Flask, render_template, request
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_sqlalchemy import SQLAlchemy

import smtplib
from email.message import EmailMessage
import ssl

# Pseudo-constants
MAIL_ADDRESS = "natoplus.co@gmail.com"
MAIL_APP_PW = "ixrusxxetfjhwfxm"
# MAIL_APP_PW = "lozqjciqzvsibxza"

# Create flask application
app = Flask(__name__)
app.secret_key = "nato123plus"


# Create database
class Base(DeclarativeBase):
    pass


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///email-addrs.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Create and configure Table
class Emails(db.Model):
    __tablename__ = "Email_addresses"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    address: Mapped[str] = mapped_column(String, unique=True)


with app.app_context():
    db.create_all()
email_list = []


def read_data(llist, class_):
    with app.app_context():
        all_mails = db.session.execute(db.select(class_).order_by(class_.id)).scalars()
        llist.clear()
        llist.extend(all_mails)


def send_welcome_mail(name, email, new=True):
    message = EmailMessage()
    message["From"] = MAIL_ADDRESS
    message["To"] = email
    message["Subject"] = "Newsletter signup confirmation"
    message.add_header("Reply-To", "noreply@natomail.com")
    if new:
        message.set_content(f"Welcome dear {name}\n\nYou have succesfully signed up for our newsletter😊")
    else:
        message.set_content(f"Welcome dear {name}\n\nYou were signed up for our newsletter before now😊")

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host="smtp.gmail.com", port=465, context=context) as connection:
        connection.login(user=MAIL_ADDRESS, password=MAIL_APP_PW)
        connection.sendmail(from_addr=MAIL_APP_PW, to_addrs=email, msg=message.as_string())


# Create flask routes
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        read_data(email_list, Emails)
        data = request.form
        user_email = data["email"]
        email_saved = next((True for email in email_list if email.address == user_email), None)
        if not email_saved:
            new_email = Emails(address=user_email)
            with app.app_context():
                db.session.add(new_email)
                db.session.commit()
            send_welcome_mail(name="customer", email=user_email)
        else:
            send_welcome_mail(name="customer", email=user_email, new=False)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
