import time
import contant.contants as CONTENT


def str_time(date):
    return str(time.strftime(CONTENT.YYYY_MM_DD_HHMMSS,date))


# if __name__ == '__main__':
print(str_time(time.localtime()))

