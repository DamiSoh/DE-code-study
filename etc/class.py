"""
@property, getter, setter
"""

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

fred = Person('Ted', 'Williams')

print(fred.first_name, fred.full_name, end = " ") #attribute 속성처럼 쓸 수 있다 fred_full_name() 으로 안해도 가져올 수 있음


# property 지정을 해주면, 후에 setter사용이 가능하다. 
class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @full_name.setter
    def full_name(self, new_full_name):
        first_name, last_name = new_full_name.split()
        self.first_name = first_name 
        self.last_name = last_name

fred = Person('Ted', 'Williams')
print('변경전', fred.full_name)

fred.full_name = 'Ted Thecutee'
print('변경 후', fred.first_name, fred.last_name, fred.full_name, end = " ")
