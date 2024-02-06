import datetime
from application.salary import calculate_salary
from application.DB.people import get_employees


if __name__ == '__main__':
    print(calculate_salary())
    print(get_employees())