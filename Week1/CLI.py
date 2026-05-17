print("당신은 이번 카테부 4기에서 많이 배워갈 수 있으시죠?")
print("대답 : 당연하지 / 자신없어 ")


while True:
    answer = input("\nQ. 할 수 있지?!! \nA. ")
   
    if answer == "당연하지":
        print("\n굿굿 더 열심히하자~")
        break
   
    elif answer == "자신없어":
        print("\nㄴㄴ 답은 정해져 있어 다시 대답해")

    else:
        print("\n내가 묻잖아 (당연하지 / 자신없어) 중에서 대.답")

