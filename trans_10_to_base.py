# программа по переводу числа из десятичной системы исчисления в любую другую
def trans_10_to_base(num, base=2):
    res = ''
    while num:
        num, d = divmod(num, base)
        sd = str(d) if d < 10 else str(chr(ord('A')+d-10))
        res = sd + res
    return res
print(trans_10_to_base(255, 16))


def trans_num_to_base(num, base):   #из 10ой системы в любую до 16й вкл
    s=""
    vol=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    while num != 0:
        ch = num % base
        s = s + str(vol[ch])
        num //= base
    return s
print(trans_num_to_base(num, base))  # num - десятичное число,
                                     # base - система исчисления которую хотим



