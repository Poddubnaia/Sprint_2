class EmployeeSalary:
    hourly_payment = 400
    def __init__(self, name, hours = None, rest_days = 2, email = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, rest_days):
        return (7 - rest_days) * 8

    @classmethod    
    def get_email(cls,name):
        return f"{name}@email.com"

    @classmethod
    def set_hourly_payment(cls,new_payment):
        cls.hourly_payment = new_payment
    
    def salary(self,hours):
        return hours * self.hourly_payment
