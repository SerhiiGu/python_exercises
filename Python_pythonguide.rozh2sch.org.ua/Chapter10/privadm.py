import user

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        #print(self.first_name, self.last_name, ':', end=' ')
        #[print(i, end=', ') for i in self.privileges]
        print(*self.privileges)


class Admin(user.User):
    def __init__(self, first_name, last_name, privileges, login_attempts = 0):
        super().__init__(first_name, last_name, login_attempts)
        self.privileges = Privileges(privileges)







    