class Student:
    total_students = 0
    total_age = 0
    GENDER = ["Male", "Female"]

    # keep track of all the instance that are created
    all_students = []

    def __init__(self, first_name, last_name, age, gender, phone_number=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        Student.total_students += 1
        Student.total_age += age
        Student.all_students.append(self)

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@student.moringaschool.com"

    # getter method for the first name
    @property
    def first_name(self):
        return self._first_name

    # setter methods
    @first_name.setter
    def first_name(self, fname):
        if isinstance(fname, str):
            self._first_name = fname
        else:
            raise ValueError("Firstname has to be a string")

    # getter method
    @property
    def last_name(self):
        return self._last_name

    # setter methods
    @last_name.setter
    def last_name(self, lname):
        if isinstance(lname, str):
            self._last_name = lname
        else:
            raise ValueError("Lastname has to be a string")

    # get the gender
    # check to see if the gender exists in our list
    # if it does, we successfully create a gender attribute.
    # else we throw/ raise a value error
    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, value):
        if value not in Student.GENDER:
            raise ValueError(f"Gender value must either be {','.join(Student.GENDER)}")
        else:
            self._gender = value

    # phone number property
    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, number):
        if number is None:
            self._phone_number = None
        elif isinstance(number, str) and number.isdigit() and (7 <= len(number) <= 15):
            self._phone_number = number
        else:
            raise ValueError("Phone number must be a string of digits (7-15 characters) or None.")

    # class methods
    @classmethod
    def total_student_tally(cls):
        return f"Total Students: {cls.total_students}"

    @classmethod
    def average_age(cls):
        average = cls.total_age / cls.total_students
        return f"Average age : {round(average)}"

    # class method to get all student firstnames
    @classmethod
    def student_first_names(cls):
        student_fns = []

        for student in cls.all_students:
            student_fns.append(student.first_name)

        return student_fns

    @classmethod
    def get_specific_gender_students(cls, gender: str):
        gendered_list = []

        for student in cls.all_students:
            if student.gender == gender:
                gendered_list.append(student.first_name)

        return gendered_list

    # string representation
    def __repr__(self):
        return str(self.__dict__)


student_1 = Student("John", "True", 23, "Male", "0712345678")
student_2 = Student("Jane", "Doe", 25, "Female", "0723456789")
student_3 = Student("Alex", "Hormozi", 30, "Male", "0734567890")
student_4 = Student("Mary", "Magdalene", 20, "Female", "0745678901")
student_5 = Student("Fred", "Kilowatt", 35, "Male", "0756789012")
student_6 = Student("Ruth", "Naomi", 26, "Female", "0767890123")

# class variables and Methods
print(Student.total_students)
print(Student.total_student_tally())

# print the total age
print(Student.total_age)

# get the average age
print(Student.average_age())

# get access to the list of students
# print(Student.all_students)

# get student first names
print(Student.student_first_names())

# get all male students
print(Student.get_specific_gender_students(gender="Male", ))

# get all female students
print(Student.get_specific_gender_students(gender="Female"))

# ...existing code...

# print all students' phone numbers
print("Student Phone Numbers:")
for student in Student.all_students:
    print(f"{student.first_name} {student.last_name}: {student.phone_number}")

# ...existing code...
# inheritance