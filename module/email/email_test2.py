import yagmail

# 连接邮箱服务器
yag = yagmail.SMTP(user = '1083554260@qq.com',password = 'rtdhlpzmuyzpjafa',host = 'smtp.qq.com')

# 邮件正文
contents = ('This is the body,and here is just text http://somedomain/image.png',
            'You can find an audio file attaches.',
            'C://Users//12//Desktop//file//python_draft//selenium3//unittest//email_test//log.txt')

# 发送邮件
# yag.send('13814067913@163.com','subject',contents)
# 如果想给多个用户发送邮件，那么只需把收件人放到一个 list 中即可，如：
# yag.send(['aa@126.com','bb@qq.com','cc@gmail.com'], 'subject', contents)

# 发送带附件的邮件,如果想发送带附件的邮件，那么只需指定本地附件的路径即可,需要在contents中加入，附件路径
yag.send('13814067913@163.com', 'subject', contents)
# yag.send('aa@126.com', 'subject', contents, ["d://log.txt","d://baidu_img.jpg"])