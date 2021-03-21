class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 5000, "bonus": 10000}


class Position(Worker):
    def get_full_name(self):
        return f"Employee: {self.name} {self.surname}: {self.position}"

    def get_total_income(self):
        return f"\nIncome: {self._income['wage'] + self._income['bonus']} rub."


if __name__ == '__main__':
    employee = Position('Ivan', 'Ivanov', 'driver')
    print(employee.get_full_name(), employee.get_total_income())

