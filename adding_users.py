import requests
import re
import pandas as pd
usersheet = pd.read_excel('new.xlsx')
usernames = usersheet['username'].values.tolist()
emails = usersheet['email'].values.tolist()
passwords = usersheet['password'].values.tolist()
LOGIN_URL = "https://link.com/login"
ENDPOINT_URL = 'https://link.com/api/v1/users'
client = requests.session()
csrftoken = re.search("var\s+csrf_nonce\s+=\s+(.*);", client.get(LOGIN_URL).text).group(0)[18:-2]
login_data = {"name":"abc", "password":"xyz", "nonce":csrftoken}
r1 = client.post(LOGIN_URL, data=login_data)
for i in range(len(usernames)):
    csrftoken = re.search("var\s+csrf_nonce\s+=\s+(.*);", client.get("https://link.com/admin/users").text).group(0)[18:-2]
    sessioncookies = client.cookies['session']
    headers = {"CSRF-Token":csrftoken,"Content-Type": "application/json","Cookies":sessioncookies}
    payload = '{"name":"'+usernames[i]+'","email":"'+emails[i]+'","password":"'+passwords[i]+'","type":"user","verified":true,"hidden":false,"banned":false}'
    r2 = client.post(ENDPOINT_URL, data=payload,headers=headers)
    print(r2.text)
