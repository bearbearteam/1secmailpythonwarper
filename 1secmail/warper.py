import requests

class warper():
    def __init__(self):
        print('Loaded the warper')
    def get_emails(self,amount:int=None):
        if amount==None:amount=1
        self.emails = requests.get(f"https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={str(amount)}").text
        return self.emails

    def domain_list(self):
        return requests.get('https://www.1secmail.com/api/v1/?action=getDomainList').text
    def email_list(self):
        return self.emails
    def check_inbox(self,email):
        user,domain = email.split('@')
        r = requests.get(f'https://www.1secmail.com/api/v1/?action=getMessages&login={user}&domain={domain}')
        return r.text
