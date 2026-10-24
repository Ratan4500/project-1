# class student:
#     pass

#     def sleep(self):
#      print("i am sleeping")

#     def writing(self):
#        print("i am writing")

#     def studying(self):
#        print("i am studying")    


# s1=student()
# s2=student()
# s1.name='rishu'
# s1.age=20
# s1.sleep()
# s1.writing()
# s1.studying()
# s2.books="pythonbook"
# s2.study="all subjects"


# # print(s1.name)

# class student:
#     def set_name(self,name):
#         self.name=name

#     def get_name(self):
#         print('name',"-",self.name)

# s1=student()
# s2=student()

# s1.set_name("mr ratan")
# s2.set_name("mr rishu")

# s1.get_name()
# s2.get_name()



# class student:
#     def get_data(self):
#         self.name=input("enter the name -")
#         self.age=input("enter the age -")
#         self.rollno=input("enter the roll number-")
#     def display(self):
#         print(self.name,self.age,self.rollno)
# s1=student()
# s1.get_data()
# s1.display()
# s2=student()
# s2.get_data()
# s2.display()


class student():
    collage="BBDIT"
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def display(self):
        print(self.name,self.age)


s1=student("ratan",23)
s1.display()
print(student.collage)