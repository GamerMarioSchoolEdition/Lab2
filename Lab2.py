import statistics
def main():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    num = get_user_input()
    avg = calc_average_temp(num)
    minmax = calc_minmax_temp(num)
    median = calc_median_temp(num)
    print("Average temp is : ", end='')
    print(avg, "C")
    print("minimun and maximum temp is ", minmax)
    print("median is : ", median)

def get_user_input():
    inp = input("Enter : ")
    x = inp.split(",")
    float_num = []
    for item in x:
        float_num.append(float(item))
    return float_num

def calc_average_temp(num):
    elements = len(num)
    total = 0
    for x in num:
        total = total + x
    avg = total / elements
    avg = str(round(avg, 2))
    return avg

def calc_minmax_temp(num):
    min = 1000000
    max = 0
    for x in num:
        if(x < min):
            min = x

        elif(x > max):
            max = x
    return min, max

def calc_median_temp(num):
    z = statistics.median(num)
    return z

if __name__ == "__main__":
    main()