from datetime import timedelta, date


def daterange(start_date, end_date):
    for i in range(int((end_date - start_date).days)):
        yield start_date + timedelta(i)

def counting_sundays():
    start_date = date(1901,1,1)
    end_date = date(2000,12,31)
    count = 0
    for now_date in daterange(start_date, end_date):
        if now_date.isoweekday() == 7 and now_date.day == 1:
            count += 1

    print count


if __name__ == '__main__':
    counting_sundays()
