import sys
def soustraction(number1, number2, base):
    max_len = max(len(number1), len(number2))
    n1 = [0] * (max_len - len(number1)) + number1
    n2 = [0] * (max_len - len(number2)) + number2
    
    result = []
    borrow = 0
    negative = False
    if n2 > n1:
        negative = True
        n1, n2 = n2, n1
   
    for i in range(max_len - 1, -1, -1):
        total = n1[i] - n2[i] + borrow
        if total < 0:
            total += base 
            borrow = -1
        else:
            borrow = 0
        result.append(total)
    
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    result.reverse()
    
    if negative:
        return ["-"] + result
    else:
        return result
def main():
    B, N1, N2 = map(int, input().split())
    number1 = list(map(int, input().split()))
    number2 = list(map(int, input().split()))
    result = soustraction(number1, number2, B)
    sys.stdout.write(" ".join(map(str, result)) + "\n")
main()