
def AND(values):                            # Логическая операция И
    for i in values:                        # Если среди всех значений
        if i == False:                      # есть хотя бы одно ложное
            return False                    # возвращаем ложь
    return True                             # иначе вернется истина


def OR(values):                             # Логическая операция ИЛИ
    for i in values:                        # Если среди всех значений
        if i:                               # есть хотя бы одно истинное
            return True                     # возвращаем истину
    return False                            # иначе вернется ложь


def NOT(value):                             # Логическая операция НЕ
    if value:                               # Если истина
        return False                        # возвращаем ложь
    return True                             # иначе истина


def XOR(values):                            # Логическая операция исключающее или
    if values[0] != values[1]:              # если выражения различны
        return True                         # возвращаем истину
    return False                            # иначе ложь


def IMP(values):                            # Логическая операция импликация
    if values[0] <= values[1]:              # если первое значение меньше или равно второму
        return True                         # возвращаем истину
    return False                            # иначе ложь


def EQV(values):                            # Логическая операция эквивалентность
    if values[0] == values[1]:              # если значения одинаковы
        return True                         # возвращаем истину
    return False                            # иначе ложь


def NAND(values):                           # Логическая операция Штрих Шеффера
    if AND(values):                         # Если оба истинны
        return False                        # возвращаем ложь
    return True                             # иначе истина


def NOR(values):                            # Логическая операция Стрелка Пирса
    if OR(values):                          # если хотябы один истинен
        return False                        # возвращаем ложь
    return True                             # иначе истина
