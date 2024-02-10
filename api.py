from flask import Flask, render_template, request
import smtplib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # You may add additional validation and sanitation here

        # Send email
        to_email = "your@email.com"  # Replace with your email address
        subject = "New Contact Form Submission"
        email_body = f"Name: {name}\nEmail: {email}\n\n{message}"

        with smtplib.SMTP('your_smtp_server.com', 587) as server:
            server.starttls()
            server.login('your_email_username', 'your_email_password')
            server.sendmail(email, to_email, email_body)

        # You can also store the data in a database if needed

        # Respond to the client-side
        return "success"

    return render_template('contact_form.html')  # Create an HTML template for the form

if __name__ == '__main__':
    app.run(debug=True)
