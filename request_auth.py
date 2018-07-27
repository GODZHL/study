import requests

from requests.auth import HTTPBasicAuth

r = requests.get('http://mail.163.com/js6/main.jsp?sid=rByuXLlVlBmqlfnPIaVVoPQkrVqfcnxV#module=welcome.WelcomeModule%7C%7B%7D',auth=HTTPBasicAuth('zhanghanlinhs@163.com','13956668172'))

print(r.status_code)

