class  employee():
    """docstring for  employee."""

    def __init__(self, first,last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {} '.format(self.first, self.last)

emp1 = employee('Jayesh', 'Suthar', 50000)
emp2 = employee('Khushbu', 'Suthar', 60000)

emp1.fullname()
print(employee.fullname(emp1))
