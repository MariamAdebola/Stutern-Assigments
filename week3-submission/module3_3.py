"""define the parent class"""
class StuternStudent:

    def __init__(self, first, last):

        """define the class atrributes"""
        self.first = first
        self.last = last
        self.email = first + last + "@stutern.com"

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def get_email(self):
        return self.email

    def set_first(self, first_name):
        self.first = first_name

    def set_last(self, last_name):
        self.last = last_name

    def set_email(self, email):
        self.email = email

    def __str__(self):
        """print the full name"""
        return str(self.first) + " " + str(self.last)

class GroupLeader(StuternStudent):

    """define the subclass"""

    def __init__(self, first, last, student=[]):

        """define the class attributes & methods"""

        super().__init__(first, last)
        self.student = student

        if student is []:
            self.student = []
            print(self.student)

    def add_students(self, new_student):
        self.student.append(new_student)
        print(self.student)

    def remove_students(self, old_student):
        self.student.remove(old_student)
        print(self.student)

    def __str__(self):
        return str(self.student)

# create 5 instances of the parent class
student1 = StuternStudent('Bukola', 'Ajayi')
student2 = StuternStudent("Temitope", "Bamidele")
student3 = StuternStudent("Abubakar", "Adisa")
student4 = StuternStudent("Adedoyin", "Abass")
student5 = StuternStudent("Awonaike", "Tawakalitu")

# get the first name, last and email of student1 in the parent class
print(student1.get_first())
print(student1.get_last())
print(student1.get_email())

# create 2 instances of the subclass
leader1 = GroupLeader("Rasheedat", "Sikiru")
leader2 = GroupLeader("Praise", "Emmanuel")

# add 2 students to leader1
new_student1 = ('Stephen', 'Ogungbile')
new_student2 = ("Theresa", "Karamor")

# add 2 students to leader2
new_student3 = ('Sheriff', 'Azeez')
new_student4 = ("Placidus", "Ali")

# call the add_students method for the 2 instances of the subclass
leader1.add_students(new_student1)
leader1.add_students(new_student2)
leader2.add_students(new_student3)
leader2.add_students(new_student4)

# remove students from the 2 instances of the subclass
leader1.remove_students(new_student2)
leader2.remove_students(new_student4)

# print email of the instances of the subclass
print(leader1.get_email())
print(leader2.get_email())
