list_num = []
first = list_num.append(int(input()))
second = list_num.append(int(input()))
third = list_num.append(int(input()))

count_first = list_num.count(list_num[0])
count_second = list_num.count(list_num[1])
count_third = list_num.count(list_num[2])

if (count_first + count_second + count_third) == 3:
    print(0)
elif (count_first + count_second + count_third) == 9:
    print(3)
else:
    print(2)
