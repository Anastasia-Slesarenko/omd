def read_data(file_name: str) -> list:
    """
    Function for reading and parsing csv files

    Args:
        file_name (str): original file in csv format

    Returns:
        list: list containing file data without a header
    """
    data = []
    with open(file=file_name, mode='r', encoding='utf-8') as fp:
        for line in fp.readlines():
            data += [line.replace('\n', '').split(';')]
    return data[1::]


def department_structure(file_name: str) -> dict:
    """
    Function that writes the structure of departments to the dictionary

    Args:
        file_name (str): original file in csv format

    Returns:
        dict: department names are keys and team sets are values
    """
    dict_departments = {}
    for row in read_data(file_name):
        if row[1] not in dict_departments:
            dict_departments[row[1]] = set()
        dict_departments[row[1]].add(row[2])
    return dict_departments


def print_department_structure(file_name: str) -> None:
    """
    Function for nice output of the structure of departments

    Args:
        file_name (str): original file in csv format
    """
    for department, teams in department_structure(file_name).items():
        print(f'* {department}:')
        for team in teams:
            print(f' - {team}')


def create_report(file_name: str) -> str:
    """
    Function for creating a report on departments

    Args:
        file_name (str): original file in csv format

    Returns:
        str: Size and salary fork for each department separated by semicolons
    """
    report = ('Департамент;' +
              'Численность;' +
              'Минимальная заплата;' +
              'Максимальная зарплата;' +
              'Средняя зарплата'
              )
    for department in department_structure(file_name).keys():
        department_salary = []
        department_size = 0
        for row in read_data(file_name):
            if department in row:
                department_size += 1
                department_salary += [int(row[5])]
        report += (f'\n{department};' +
                   f'{department_size};' +
                   f'{min(department_salary)};' +
                   f'{max(department_salary)};' +
                   f'{round(sum(department_salary)/len(department_salary))}'
                   )
    return report


def print_report(file_name: str) -> None:
    """
    Function for nice output of the report on departments

    Args:
        file_name (str): original file in csv format
    """
    for row in create_report(file_name).split('\n'):
        print('|'.join([el.center(25) for el in row.split(';')]))


def write_report(file_name: str, report_name: str) -> None:
    """
    Function for writing a report on departments to a csv file

    Args:
        file_name (str): original file in csv format
        report_name (str): name of the report by department
    """
    with open(file=report_name, mode='w', encoding='utf-8') as fp:
        fp.write(create_report(file_name))
        print('Отчет по департаментам записан записан в файл Report.csv')


def initialization(file_name: str, report_name: str = 'Report.csv') -> None:
    """
    Depending on the choice, the function outputs the department structure,
    the department report or writes the report to csv

    Args:
        file_name (str): original file in csv format
        report_name (str, optional): defaults to 'Report.csv'

    Returns:
        _type_: _description_
    """
    print(
        '1. Вывести иерархию команд'
        '\n2. Вывести сводный отчёт по департаментам'
        '\n3. Сохранить сводный отчёт по департаментам'
    )
    option = ''
    options = ['1', '2', '3']
    while option not in options:
        print(f'Выберите пункт меню: {options[0]}/{options[1]}/{options[2]}')
        option = input()
    if option == '1':
        return print_department_structure(file_name)
    if option == '2':
        return print_report(file_name)
    if option == '3':
        return write_report(file_name, report_name)


if __name__ == '__main__':
    initialization(file_name='Corp_Summary.csv')
