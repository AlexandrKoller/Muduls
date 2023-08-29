import datetime
from task_1.ampplication.sallary import calculate_sallary
from task_1.ampplication.db.people import get_employees
if __name__ == '__main__':
    date = datetime.datetime.today()
    print(date.date())
    calculate_sallary()
    get_employees()
