# 사용자로부터 두 개의 정수와 연산자를 받아서 
# 정수의 합, 정수의 차, 정수의 곱, 정수의 나누기, 나누기, 나머지를 계산하여 화면에 출력하는 프로그램을 작성하라.

# 입력
num_1 = int(input("첫번째 정수를 입력하시오."))
num_2 = int(input("두번째 정수를 입력하시오."))
Oper_1 = input("연산자를 입력하시오.")

# 출력
if Oper_1 == '+':
    print("\n",num_1, Oper_1, num_2, "=", num_1 + num_2,"\n")
elif Oper_1 == '-':
    print("\n",num_1, Oper_1, num_2, "=", num_1 - num_2,"\n")
elif Oper_1 == '*':
    print("\n",num_1, Oper_1, num_2, "=", num_1 * num_2,"\n")
elif Oper_1 == '/':
    print("\n",num_1, Oper_1, num_2, "=", num_1 / num_2,"\n")
elif Oper_1 == '%':
    print("\n",num_1, Oper_1, num_2, "=", num_1 % num_2,"\n")
else:
    print("\n잘못된 값을 입력하셨습니다.\n")