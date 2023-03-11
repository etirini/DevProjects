class Employee:
    def __init__(self, first_name, last_name, anual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.anual_salary = anual_salary
    
    def give_raise(self, anual_raise=''):
        if anual_raise:
            self.anual_salary = self.anual_salary + anual_raise
        else:
            self.anual_salary = self.anual_salary + 5000 
        print(f'The new salary is {self.anual_salary}')

    def show_employee(self):
        print(f' {self.first_name} {self.last_name} {self.anual_salary}')



