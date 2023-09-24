from email.mime.text import MIMEText
from email import parser
import smtplib, ssl, poplib, email.utils, mariadb, os

def convert(j):
    s = []
    for i in j:
        s.append(i.decode())

    return s

def send(hostname: str, port: int, username: str, password: str, subject: str,  emails: list, content: str, sendAs=""):
    if sendAs == "":
        sendAs = username

    msg = MIMEText(content)
    msg['From'] = email.utils.formataddr(('Author', sendAs))
    msg['Subject'] = subject
 
    context = ssl.create_default_context()
    server = smtplib.SMTP(hostname, port)
    server.starttls(context=context)
    server.login(username, password)
    
    for e in emails:
        server.sendmail(username, e, msg.as_string())

def recv(hostnames: list, ports: list, emails: list, passwords: list):
    for i in range(len(emails)):
        try:
            pop_conn = poplib.POP3_SSL(hostnames[i], ports[i])
            pop_conn.user(emails[i])
            pop_conn.pass_(passwords[i])

            messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
            pop_conn.quit()

            messages = ["\n".join(convert(mssg[1])) for mssg in messages]
            messages = [parser.Parser().parsestr(mssg) for mssg in messages]
            
            yield messages
        except Exception as e:
            print(e)

if __name__ == '__main__':
    # user=os.environ.get("USER")
    # password=os.environ.get("PASSWORD")
    # host=os.environ.get("HOST")
    # port=int(os.environ.get("PORT"))
    # database=os.environ.get("DB")

    # conn = mariadb.connect(
    #     user=user,
    #     password=password,
    #     host=host,
    #     port=port,
    #     database=database

    # )
    # cur = conn.cursor()

    send("smtp.gmail.com", 587, os.environ.get("EMAIL_HOST_USER"), os.environ.get("EMAIL_HOST_PASSWORD"), "hi", [os.environ.get("EMAIL_HOST_USER")], "test")

    for messages in recv(["pop.gmail.com"], [995], [os.environ.get("EMAIL_HOST_USER")], [os.environ.get("EMAIL_HOST_PASSWORD")]):
        print(messages)