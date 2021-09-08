import smtplib
from django.core.mail import send_mail
from www.logger import log_crunch

app_logger = log_crunch()

def contactmailnotify(message_dict):

    message = "Subject: contact received from seven stones site\n"
    message += "Contact mail received from " + str(message_dict['name']) + " (" + str(message_dict['email']) + ")\n"
    message += "IP address: " + str(message_dict['ip']) + "\n"
    message += "Message: " + str(message_dict['message'])

    sender = 'netdelta@netdelta.io'
    receivers = ['info@netdelta.io', 'ian.tibble@netdelta.io']

    try:
        send_mail('contact received from www.seven-stones.biz',
                  message,
                  sender,
                  receivers,
                  fail_silently=False)
        app_logger.info("Successfully sent notification email, contact form mail received",
                         contact=message_dict)
    except smtplib.SMTPException as err:
        app_logger.critical("Error: unable to send notification email, contact form mail received from {0}, with error {1}"
                            .format(message_dict['email'], err), contact=message_dict)
        return False
    except ConnectionRefusedError as error:
        app_logger.critical("Error: ConnectionRefusedError - unable to send notification email, contact form mail received from {0}"
                            "with error {1}"
                            .format(message_dict['email'], error), contact=message_dict)
        return False
    except ConnectionError:
        app_logger.critical("Error: Connection Error - unable to send notification email, contact form mail received from {0}".
                            format(message_dict['email']), contact=message_dict)
        return False
    return True
