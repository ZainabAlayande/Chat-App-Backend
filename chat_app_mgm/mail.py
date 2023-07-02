import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:

    # @staticmethod
    # def send_mail(bio_data):
    #     port = 465  # For SSL
    #     email = "alayandezainab64@gmail.com"
    #     password = "cmrlvmyxcdgmzqdl"
    #
    #     # Create a secure SSL context
    #     context = ssl.create_default_context()
    #
    #     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    #         server.login(email, password)
    #         # TODO: Send email here
    #
    #         sender_email = "alayandezainab64@gmail.com"
    #         receiver_email = bio_data.email
    #         message = """\
    #               Registration just begin
    #           ."""
    #         server.sendmail(sender_email, receiver_email, message)

    @staticmethod
    def send_mail(bio_data):
        sender_email = "alayandezainab64@gmail.com"
        receiver_email = bio_data.email
        password = "cmrlvmyxcdgmzqdl"

        message = MIMEMultipart("alternative")
        message["Subject"] = "Converse - Complete your registration"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hello,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = f"""\
        <html>
          <body>
            <p>Hello, <br><br>
               Please complete your registration with Converse<br>
               Your OTP: {bio_data.otp} <br><br> 
               <a href="google.com">Click Here</a> 
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        # part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        # message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
