def to_binary(x:str):
    x = bin(int(x))
    if x[0] == '-':
        return complement_2('0'+x[3:])
    else:
        return '0'+x[2:]

def complement_1(x: str):
    result = ""
    for i in range(len(x)):
        if x[i] == '1':
            result += '0'
        elif x[i] == '0':
            result += '1'
    return result
def add_bin(x:str, y:str):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    carry =0
    result = []
    for i in range(max_len-1,-1,-1 ):
        x_bit = int(x[i])
        y_bit = int(y[i])

        sum = x_bit + y_bit + carry
        res_bit = sum %2
        carry = sum//2
        result.insert(0,str(res_bit))
    if carry:
        result.insert(0, str(carry))
    return ''.join(result)



def complement_2(x:str):
    x = complement_1(x)
    x = add_bin(x, '1')
    return x

# def RightShift(res, bits):
#     print(f"bits are: {bits}")
#     res = list(res)
#     if res[0] == 1:
#         res = res[1:]
#         res.insert(0,'1')
#     elif res[0] == 0:
#         res = res[1:]
#         res.insert(0,'0')
#     A = ''.join(res[:bits])
#     Q = ''.join(res[bits:2*bits])
#     q0 = ''.join(res[-1])
#     return A , Q ,q0
def RightShift(res, bits):
    if len(res) > 2*bits +1 :
        res = res[1:]
    if res[0] == '1':
        res = '1'+ res[:-1]
    elif res[0] == '0':
        res = '0' + res[:-1]
    A = res[:bits]
    Q = res[bits:2 * bits]
    q0 = res[-1]
    return A, Q, q0

def booths(m:str, q:str):
    M = to_binary(m)
    Q = to_binary(q)
    negM = complement_2(M)
    bits = max(len(M),len(Q), len(negM))
    dig = bits
    A = ''.zfill(bits)
    Q= Q.zfill(bits)
    M= M.zfill(bits)
    negM = negM.zfill(bits)
    q0 ='0'
    print(f"A = {A} and Q = {Q} q0 = {q0}")
    while dig != 0:
        if Q[-1] == '1' and q0 == '0':
            A =add_bin(A,negM)
            print(f"after substraction A = {A} and Q = {Q} q0 = {q0}")
        elif Q[-1] == '0' and q0 == '1':
            A = add_bin(A,M)
            print(f"after addition A = {A} and Q = {Q} q0 = {q0}")
        print(f"Before Right shift: {A+Q+q0}")
        print(f"A = {A} and Q = {Q} q0 = {q0}")
        A , Q , q0 = RightShift(A+Q+q0,bits)
        print(f"AFter Right shift: {A + Q + q0}")
        print(f"A = {A} and Q = {Q} q0 = {q0}")
        dig-=1
    return A+Q





x = input("Enter the Multiplicand:")
y = input("Enter the Multiplier: ")
print(f"Binary of x = {to_binary(x)} and binary of y  = {to_binary(y)}")
res = booths(x,y)
print(f"Result in A and Q = {res}")
if res[0] == '1':
    print(f"The {x} * {y}  = -{int(complement_2(res), 2)}")
else:
    print(f"The {x} * {y}  = {int(res, 2)}")
