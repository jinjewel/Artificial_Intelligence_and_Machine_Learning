# 사용자로부터 학년 반, 국어, 영어, 수학, 물리 점수를 입력 받아 총점, 
# 평균, 학점을 계산하여 화면에 출력하는 프로그램을 작성하라. 

# 입력
num = int(input("번호를 입력하시오."))
korean = float(input("국어 점수를 입력하시오."))
english = float(input("영어 점수를 입력하시오."))
math = float(input("수학 점수를 입력하시오."))
physics = float(input("물리 점수를 입력하시오."))

# 계산
sum = korean + english + math + physics
avg = sum / 4
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 90:
    grade = 'D'
else:
    grade = 'F'

# 출력
print("="*50)
print("번호","국어"," 영어"," 수학"," 물리"," 총점","  평균  "," 학점")
print("="*50)
print("%3d %3.2f %3.2f %3.2f %3.2f %3.2f %3.2f     %c " % (num, korean, english, math, physics, sum, avg, grade))
