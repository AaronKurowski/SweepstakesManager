class Contestant:
    def __init__(self, first_name, last_name, email_address, number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email_address
        self.reg_num = number

    def notify(self, is_winner):
        pass

    # def get_contestant_info(self):
    #     self.first_name = input("What is your first name? >")
    #     self.last_name = input("What is your last name? >")
    #     self.email = input("What is your email? >")
    #     self.reg_num = input("Enter registration number. >")
    #
    # def display_contestant_info(self):
    #     output_text(f"First name: {self.first_name}\nLast name: {self.last_name}"
    #                 f"\nEmail: {self.email}\nRegistration #: {self.reg_num}")
