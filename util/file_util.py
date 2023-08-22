import logging
def print_file_info(file_name):
    file = None
    try:
        file = open(file_name , mode="r" , encoding="UTF-8")
        return file.read()
    except Exception as e:
        logging.debug(e)
    finally:
        logging.info("close success !")
        if file:
            file.close

def append_to_file(file_name,data):
    file = None
    try:
        file = open(file_name , mode="a" , encoding="UTF-8")
        file.write(data)
    except Exception as e:
        logging.debug(e)
    finally:
        if file:  # 如果变量是None，表示为false ， 否则就是true
            file.close


if __name__ == "__main__":
    file_name = '/home/kali/Downloads/bill.text1'
    print(print_file_info(file_name=file_name))
    content = "\n-------------------分割线----------------------"
    append_to_file(file_name,content)