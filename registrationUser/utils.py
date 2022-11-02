import smtplib
from email.mime.text import MIMEText


def send(massege):
  smtpObj = smtplib.SMTP('smtp.mail.ru', 587) # подключение к почтовому сервесу
  smtpObj.starttls() # вкл шифрования
  smtpObj.login('gto-test@inbox.ru','QUYwhL8buP8r2cyUMJpi') # логин к нему

  title = 'You want?'
  msg_content = f'<h2>{title} > <font color="green">OK</font></h2>\n' # Тут html форма на вкус и цвет
  msg = MIMEText(msg_content, 'html') # Указание что в сообщение есть html

  msg['From'] = 'gto-test@inbox.ru' # От кого
  msg['To'] = 'kirya.shabalin.2014@mail.ru' # Кому
  msg['Subject'] = 'New GTO event' # Тема

  msg_full = msg.as_string()

  smtpObj.sendmail(msg['From'], msg['To'], msg_full)
  smtpObj.quit()