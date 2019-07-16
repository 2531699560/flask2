# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_mail():
    fromaddr = '2531699560@qq.com'
    password = 'fkmflzyrfftbdhgg'
    toaddrs = ['2531699560@qq.com']
    content = 'hello, this is email content.'
    textApart = MIMEText(content)

    # imageFile = './1.PNG'
    # imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    # imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    #
    # pdfFile = './Django.pdf'
    # pdfApart = MIMEApplication(open(pdfFile, 'rb').read())
    # pdfApart.add_header('Content-Disposition', 'attachment', filename=pdfFile)
    #
    # zipFile = './v1.0.3.zip.zip'
    # zipApart = MIMEApplication(open(zipFile, 'rb').read())
    # zipApart.add_header('Content-Disposition', 'attachment', filename=zipFile)

    m = MIMEMultipart()
    m.attach(textApart)
    # m.attach(imageApart)
    # m.attach(pdfApart)
    # m.attach(zipApart)
    m['Subject'] = 'Auto_mail'

    try:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        # server = smtplib.SMTP('smtp.163.com')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:
        print('error:', e)  # 打印错误


if __name__ == '__main__':
    print (111)
    send_mail()
