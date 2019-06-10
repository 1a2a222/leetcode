def isValid( s: str) -> bool:
    if not s:  # 判断字符串是否为空
        return True
    temp_str = ""  # 存放临时开括号
    for cha in s:
        if cha == "(" or cha == "[" or cha == "{":  # 如果是开括号就放入temp_str字符串中
            temp_str = temp_str + cha
        else:
            if not temp_str:  # 如果temp_str为空，返回False
                return False
            else:
                temp_cha = temp_str[-1]  # 取出最新压入的开括号
                temp_str = temp_str[0:-1]  # 开括号字符串减一
                if temp_cha == "(" and cha == ")":  # 判断开括号和闭括号是否满足要求
                    pass
                elif temp_cha == "[" and cha == "]":
                    pass
                elif temp_cha == "{" and cha == "}":
                    pass
                else:
                    return False
    if not temp_str:  # 判断是否存在多余开括号
        return True
    else:
        return False
a = isValid(']')
print(a)