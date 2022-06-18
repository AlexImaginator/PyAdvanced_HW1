from datetime import date
from application.salary import calculate_salary
from application.people import get_employees


def main():
    print(f'Текущая дата: {date.today().strftime("%d.%m.%y")}')
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()
