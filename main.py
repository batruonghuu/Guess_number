import random

print("Xin chao")
name = input()
print("Xin chao " + name +", toi dang nghi toi mot con so, hay thu doan xem do la so gi?")
choose_number = random.randint(1,20)
#pick a default random number
print(choose_number)
for i in range(1,4):
    print("So ban dang nghi toi la ")
    guess_i = int(input())
    n = i
    guess = guess_i
    if guess_i < choose_number:
        print("So ban dang nghi nho hon so toi nghi")
    elif guess_i > choose_number:
        print("So ban dang nghi lon hon so toi nghi")
    else:
        break

if guess == choose_number:
    print("Ban da doan dung, va doan dung sau ", n , " lan")
else:
    print("Ban da doan sai, ban khong con co hoi")

