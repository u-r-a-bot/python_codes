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

def left_shift(x:str, bits:int):
    # print(f"Value of x is now {x}")
    x = x[1:]
    x = x+'?'
    # print(f"Value of x is now {x}")
    A = x[:bits+1]
    q = x[bits+1:2*bits+1]
    # print(f'A = {A} and q = {q}')
    return A , q

def Restoring(m:str ,q:str):
    M = to_binary(m)
    Q = to_binary(q)
    negM = complement_2(M)
    bits = max(len(M),len(Q), len(negM))
    print(f"M = {M} and Q = {Q} and negM = {negM}")
    dig = bits
    A = ''.zfill(bits+1)
    Q= Q.zfill(bits-1)
    M= M.zfill(bits)
    negM = negM.rjust(len(A) , "1")
    n= bits
    # print(f"The value of A is {A} and Q  is {Q} before while loop")
    while n!= 0:
        A , Q = left_shift(A+Q,bits)
        print(f"The value of A is {A} and Q  is {Q} after left shift")
        lenA = len(A)
        resA = A
        A = add_bin(A,negM)
        lenAlat = len(A)
        if lenA != lenAlat:
            A = A[1:]
        print(f"The value of A is {A} after addition")
        if A[0] == "0":
            Q = Q[:len(Q)-1]
            print(f"Q = {Q}")
            Q += '1'
            print(f"A =  {A}  Q = {Q}")
        elif A[0] == "1":
            Q = Q[:len(Q)-1]
            Q += '0'
            A = resA
            print(f" this is after restoring A =  {A}  Q = {Q}")
        n-=1
        print(f"The value A = {A} and Q = {Q}")
    return A ,Q
y = input("Enter the value of dividend")
x = input("Enter the value of divisor")
A, q = Restoring(x,y)
print(f"Remainder is {A} and quotient is {q}")
