from email.message import EmailMessage
import os
import smtplib
import psutil as ps
email_address = os.environ.get('EMAIL_USER')
email_password = os.environ.get('EMAIL_PASSWORD')
D = []
url = 'The disk usage is about to be exhausted'
partitions = ps.disk_partitions()
for partition in partitions:
    usage = ps.disk_usage(partition.mountpoint)
    percent = usage.percent
    D.append(percent)
    if percent > 80:
        msg = EmailMessage()
        msg['Subject'] = 'disk usage'
        msg['From'] = 'adeosunabdulsamad25@gmail.com'
        msg['To'] = 'adeosunabdulsamad26@gmail.com'
        msg.set_content(f'The disk percentage of {partition.mountpoint} of your server is {percent}%.\nPls try and change the disk soon')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(email_address, email_password)
            smtp.send_message(msg) 
