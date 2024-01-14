class Class:
    def __init__(self, identification, room):
        self.__identification = identification
        self.__room = room
        self.student_list = []

    def get_identification(self):
        return self.__identification

    def set_identification(self, value):
        __identification = value

    def get_room(self):
        return self.__room

    def set_room(self, value):
        self.__room = value

    def get_student_list(self):
        return self.student_list

    def set_student_list(self, value):
        student_list = value

