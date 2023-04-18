class TransactionRole(Enum):
    
    ADMIN = "Admin"
    LECTURER = "Lecturer"
    STUDENT = "Student"

    @classmethod
    def choices(cls):
        # print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)