s = input() #{{{}{})()){[][][[


if 1 <= len(s) <= pow(10,8):

    opened_brackets_list = [] #[({

    possible = True

    for c in s:
        if c == '[' or c == '{' or c == '(':
            opened_brackets_list.append(c)
        elif c == ']':
            if len(opened_brackets_list) > 0 and opened_brackets_list[-1] == '[':
                opened_brackets_list.pop()
            else:
                possible = False
                break
        elif c == '}':
            if len(opened_brackets_list) > 0 and opened_brackets_list[-1] == '{':
                opened_brackets_list.pop()
            else:
                possible = False
                break
        elif c == ')':
            if len(opened_brackets_list) > 0 and opened_brackets_list[-1] == '(':
                opened_brackets_list.pop()
            else:
                possible = False
                break

    if possible and len(opened_brackets_list) == 0:
        print("Yes")
    else:
        print("No")