
class Person():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print('Person Created.')
    
    def who_am_i(self):
        print('I am a person.')

    def eat(self):
        print('I am eating.')

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print('Student Created.')

p1 = Person('Ali','Yilmaz')
s1 = Student('Cinar','Turan')

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname)

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()








class Person():
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
        print('Person Created.')
    
    def who_am_i(self):
        print('I am a person.')

    def eat(self):
        print('I am eating.')

class Student(Person):

    def __init__(self, fname, lname,number):
        Person.__init__(self,fname, lname)
        self.studentNumber = number
        print('Student Created.')

        # override (Alttaki who am i usttekini ezer ve yeni deger olur buna override denir.)
    def who_am_i(self):
        print('I am a student.')

    def sayHello(self):
        print('Hello I am a student.')

class Teacher(Person):

    def __init__(self, fname, lname,branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

p1 = Person('Ali','Yilmaz')
s1 = Student('Cinar','Turan',1256)
t1 = Teacher('Serkan','Yilmaz','Math')

print(p1.firstname + ' ' + p1.lastname)
print(s1.firstname + ' ' + s1.lastname + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
t1.who_am_i()

