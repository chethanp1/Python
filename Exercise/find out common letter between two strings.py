def common_letter():
    str1=input("Enter first String : ")
    str2 = input("Enter first String : ")
    s1=set(str1)
    s2=set(str2)
    lst=s1 & s2
    print(lst)
common_letter()