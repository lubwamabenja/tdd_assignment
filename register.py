import re

class User_Accounts:
    """ class User_accounts aunthenticates user credentials"""

    
    def __init__(self):
        self.users = []

    def verify_email(self, email):
        if email and not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
            raise ValueError("Bad syntax in "+ email)
        else:
            return True

        if email =="" and email ==" ":
            raise ValueError("Email cant be empty")
        else:
            return True

    def verify_password(self, password):
        """ checks for password complexity """
        l_case = re.search(r"[a-z]", password)
        u_case = re.search(r"[A-Z]", password)
        number = re.search(r"[0-9]", password)
        character = re.search(r"[@_!#$%^&*()<>?/\|}{~:]",password)

        if  l_case and u_case and number  and character and len(password) >= 4:
            return True
        else:
            return False

    def verify_username(self, username, name):
        """ checks if the username is different from name """

        if username and name and username != name\
            and len(username) >= 4:
            return True
        else:
            return False

    def verify_age(self, age):
        if isinstance(age, int) and age > 0:
            return True
        else:
            return False

    def register_user(self, name,**kwargs):
        """ Allows the user to signup """
        username = kwargs["username"]
        email = kwargs["email"]
        age = kwargs["age"]
        password = kwargs["password"]
          

    
        account = dict(
            name = name,
            username = self.verify_username(username, name),
            email = self.verify_email(email),
            age = self.verify_age(age),            
            password = self.verify_password(password)
        )

        if account not in self.users:
            self.users.append(account)
        else:
            print("User already exists")
            return False
    
    def login(self, username, password):
        """ Checks if the username and password already exist 
            and returns true it they do
        """
        for account in self.users:
            name = account['name']
            if username and self.verify_username(username, name) == account['username'] and \
                self.verify_password(password) == account['password']:
                print("You're logged in")
                return True
            else:
                return False

    def change_password(self,username,password):
        """ Changes password if user opts to change it"""
        if self.login == True:
            new_password = input("Enter new Password: ")
            self.users['password'] = new_password
            print("password changed")
            return True
        else: 
            return False
    
    def change_email(self,username,password):
        """ changes email if user opts to change it"""
        if self.login == True:
            new_email = input("Enter new email: ")
            self.users['email'] = new_email
            print("Email Successfully changed")
            return True
        else:
            return False
        
        


                