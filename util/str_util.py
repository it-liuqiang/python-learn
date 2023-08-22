def str_reverse(s):
    """接收传入字符串，将字符串反转返回

    Args:
        s (str): 字符串

    Returns:
        _type_: 字符串
    """

    # s = list(s)
    # s.reverse() # list.reverse() 函数是没有返回值的
    # return ''.join(s)

    # return ''.join(reversed(list(s)))
    #最优解决 -1 表示倒着切
    return s[::-1] 


def substr(s , x ,y):
    s = str(s)
    return s[x:y]

    
a = "abcdefg"
if __name__ == "__main__":
    print(str_reverse(a))
    print(substr(a,2,5))