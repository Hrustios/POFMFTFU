def main():
    _str = list(map(str,input("Введите массив:\n")))
    _str.remove('[')
    _str.remove(']')
    _list = list(("".join(_str)).split(','))
    _int_list = list(map(int, _list))
    _m = _int_list.pop(_int_list.index(min(_int_list)))
    print(int(_m) + int(min(_int_list)))
    print(_m)
    print(min(_int_list))
    print(_int_list)

main()