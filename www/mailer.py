import smtplib
import logging
from django.core.mail import send_mail
from pprint import pprint

app_logger = logging.getLogger('sevenstones_app')

def contactmailnotify(message_dict):

    pprint(message_dict, indent=4)

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
                         extra={'sender_name': message_dict['name'], 'email': message_dict['email'],
                                'sender_ip': message_dict['ip'], 'sender_message': message_dict['message']})
    except smtplib.SMTPException as err:
        app_logger.critical("Error: unable to send notification email, contact form mail received from {0}, "
                            "with error {1}".format(message_dict['email'], err),
                            extra={'sender_name': message_dict['name'], 'email': message_dict['email'],
                                   'sender_ip': message_dict['ip'], 'sender_message': message_dict['message']})
        return False
    except ConnectionRefusedError as error:
        app_logger.critical("Error: ConnectionRefusedError - unable to send notification email, contact form mail "
                            "received from {0} with error {1}".format(message_dict['email'], error),
                            extra={'sender_name': message_dict['name'], 'email': message_dict['email'],
                                   'sender_ip': message_dict['ip'], 'sender_message': message_dict['message']})
        return False
    except ConnectionError:
        app_logger.critical("Error: Connection Error - unable to send notification email, contact form mail "
                            "received from {0}".format(message_dict['email']),
                            extra={'sender_name': message_dict['name'], 'email': message_dict['email'],
                                   'sender_ip': message_dict['ip'], 'sender_message': message_dict['message']})
        return False
    return True
