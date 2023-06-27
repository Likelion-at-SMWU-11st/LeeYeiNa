print("================================")
print("회원가입")
print("================================")

register = False
users = []
while not register:

    print("회원가입을 진행하시겠습니까?")
    print("y : 진행      n : 취소")
    answer = input(">>   ")
    answer = answer.lower()

    if answer == "y":
        user = {}
        register = True
        print("================================")
        print("회원가입이 진행됩니다.")
        username = input("ID : ")
        while True:
            pwd = input("PWD : ")
            pwd2 = input("Check PWD : ")
            if pwd == pwd2:
                break
            else:
                print("비밀번호가 일치하지 않습니다")
        name = input("이름 : ")
        while True:
            birth = input("생년월일(6자리) : ")
            if len(birth) == 6:
                break
            else:
                print("생년월일을 6자리로 다시 입력해주세요")
        email = input("이메일 : ")
        print("================================")
        user["username"] = username
        user["password"] = pwd
        user["name"] = name
        user["birth"] = birth
        user["email"] = email
        users.append(user)
        print(users)
        print("================================")
        print(user["name"], "님 가입을 환영합니다!")

        print("회원가입을 추가로 진행하시겠습니까?")
        print("y : 진행      n : 취소")
        answer = input(">>   ")
        answer = answer.lower()

        if answer == "y":
            pass
        else:
            exit()

    elif answer == "n":
        print("================================")
        print("회원가입이 취소됩니다.")
        print("================================")
    else:
        print("입력 값을 확인해주세요.")
