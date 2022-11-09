# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 发送邮件主题
# subject = 'Python email test'
#
# # 编写HTML类型的邮件正文
# msg = MIMEText('<html><h1>你好！</h1></html>','html','utf-8')  # 定义发送邮件的正文、格式，以及编码
# msg['Subject'] = Header(subject,'utf-8')    # 定义邮件的主题和编码类型
#
# # 发送邮件
# smtp = smtplib.SMTP()
# smtp.connect("smtp.qq.com") # 指定连接的邮箱服务
# smtp.login("1083554260@qq.com","rtdhlpzmuyzpjafa")
# smtp.sendmail("1083554260@qq.com","13814067913@163.com",msg.as_string())    # 指定发件人、收件人，以及邮件的正文
# smtp.quit()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 邮件主题
subject = 'Python send email test'

# 发送的附件
with open('log.txt','rb') as f:
    send_att = f.read()

att = MIMEText(send_att,'text','utf-8')  # 定义发送邮件的正文、格式，以及编码
att["Content-Type"] = 'application/octet-stream'    # Content-Type 指定附件内容类型,application/octet-stream 表示二进制流
att["Content-Disposition"] = 'attachment;filename="log.txt"'    #Content-Disposition指定显示附件的文件；attachment; filename="log.txt"指定附件的文件名

msg = MIMEMultipart()   # MIMEMultipart 类定义邮件的主题
msg['Subject'] = subject
msg.attach(att) # attach()指定附件信息

# 发送邮件
smtp = smtplib.SMTP()
smtp.connect("smtp.qq.com") # 指定连接的邮箱服务
smtp.login("1083554260@qq.com","rtdhlpzmuyzpjafa")
smtp.sendmail("1083554260@qq.com","13814067913@163.com",msg.as_string())    # 指定发件人、收件人，以及邮件的正文
smtp.quit()