# 1000〜9999のうち
# 四則演算した結果
# 元の数の桁をが逆から並べた数字と同じ

def get_eval_result(str_eval, num):
    r_num = int(''.join(reversed(str(num))))
    try:
        result = eval(str_eval)
        if result == r_num:
            return True
    except ZeroDivisionError:
        pass
    except SyntaxError:
        pass
    return False

op = ['+', '-', '*', "/"]

answer = []
for num in range(1000, 10000):
    r_num = int(''.join(reversed(str(num))))
    if len(str(r_num)) < 4:
        continue
    #print(r_num)

    list_num = [x for x in str(num)]
    #print(list_num)
    flg = False
    for op1 in op:
        for op2 in op:
            for op3 in op:
                ans = get_eval_result("{n1} {o1} {n2} {o2} {n3} {o3} {n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1, o2=op2, o3=op3), num)
                if ans:
                    answer.append(num)
                    flg = True
                    break
    if not flg:
        for op1 in op:
            for op2 in op:
                ans = get_eval_result("{n1} {o1} {n2} {o2} {n3}{n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1, o2=op2), num)
                if ans:
                    answer.append(num)
                    flg = True
                    break

                ans = get_eval_result("{n1} {o1} {n2}{n3} {o2} {n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1, o2=op2), num)
                if ans:
                    answer.append(num)
                    flg = True
                    break

                ans = get_eval_result("{n1}{n2} {o1} {n3} {o2} {n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1, o2=op2), num)
                if ans:
                    answer.append(num)
                    flg = True
                    break

    if not flg:
        for op1 in op:
            ans = get_eval_result("{n1} {o1} {n2}{n3}{n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1), num)
            if ans:
                answer.append(num)
                flg = True
                break
            ans = get_eval_result("{n1}{n2} {o1} {n3}{n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1), num)
            if ans:
                answer.append(num)
                flg = True
                break

            ans = get_eval_result("{n1}{n2}{n3} {o1} {n4}".format(n1=list_num[0], n2=list_num[1], n3=list_num[2], n4=list_num[3], o1=op1), num)
            if ans:
                answer.append(num)
                flg = True
                break

print(answer)