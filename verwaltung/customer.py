class Customer:
    def __init__(self, forename, name, id_customer, email):
        self.__forename = forename
        self.__name = name
        self.__id_customer = id_customer
        self.__email = email

    def get_forename(self):
        return self.__forename

    def set_forename(self, value):
        self.__forename = value

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_id_customer(self):
        return self.__id_customer

    def set_id_customer(self, value):
        self.__id_customer = value

    def get_email(self):
        return self.__email

    def set_email(self, value):
        self.__email = value
