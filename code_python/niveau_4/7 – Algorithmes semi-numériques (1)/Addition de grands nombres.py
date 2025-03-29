import sys
def add_in_base_b(number1, number2, base):
    max_len = max(len(number1), len(number2))
    number1 = [0] * (max_len - len(number1)) + number1
    number2 = [0] * (max_len - len(number2)) + number2
    
    result = []
    carry = 0
    
    for i in range(max_len - 1, -1, -1):
        total = number1[i] + number2[i] + carry
        result.append(total % base) 
        carry = total // base 
              
    if carry > 0:
        result.append(carry)
    return result[::-1]
def main():
    B, N1, N2 = map(int, input().split())
    number1 = list( map(int, input().split()))
    number2 =  list( map(int, input().split()))
    result = add_in_base_b(number1, number2, B)
    sys.stdout.write(" ".join(map(str, result)) + "\n")
main()