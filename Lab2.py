def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    num = get_user_input()
    avg = calc_average_temp(num)
    minmax = calc_minmax_temp(num)
    print("Average temp is : ", end='')
    print(avg, "C")
    print("minimun and maximumtemp is ", minmax)

def get_user_input():
    inp = input("Enter : ")
    x = inp.split(",")
    return x

def calc_average_temp(num):
    elements = len(num)
    total = 0
    for x in num:
        num1 = float(x)
        total = total + num1
    avg = total / elements
    return avg

def calc_minmax_temp(num):
    elements = len(num)
    total = 0
    min = 1000000
    max = 0
    for x in num:
        num1 = float(x)
        if(num1 < min):
            min = num1

        elif(num1 > max):
            max = num1

    return min, max
display_main_menu()