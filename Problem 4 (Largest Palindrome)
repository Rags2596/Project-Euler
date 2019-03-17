palindrome_list_1 = []
palindrome_list_2 = []
palindrome = []

def check_palindrome(a, x, y):
    a_six = int(a/100000)
    a_five = (int(a/10000))%10
    a_four = (int(a/1000))%10
    a_three = (int(a/100))%10
    a_two = (int(a/10))%10
    a_unit = a%10
    b = a_six + a_five *10 + a_four *100 + a_three*1000 + a_two *10000 + a_unit *100000
    if a == b:
        palindrome_list_1.append(x)
        palindrome_list_2.append(y)
        palindrome.append(x*y)


for i in range(900,999):
    for j in range(900,999):
        product = i*j
        check_palindrome(product, i, j)

print(max(palindrome))

