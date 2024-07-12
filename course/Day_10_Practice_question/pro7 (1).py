# write a python program that uses encapsulation to protect sensitive information in a user class.

class User:
    def __init__(self, username, password):
        self.__username = username  
        self.__password = password 

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password
    def check_password(self, password):
        return self.__password == password

if __name__ == "__main__":
    user = User("Meet", "Admin1234")

    print("Username:", user.get_username())
    user.set_username("Meet_s")
    print("Updated Username:", user.get_username())
    print("Password check:", user.check_password("admin123"))

    user.set_password("admin@123")
    print("Password check:", user.check_password("admin@123"))
