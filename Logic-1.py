def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed > 65 and speed <= 85:
            return 1
        if speed >= 85:
            return 2
        if speed <= 65:
            return 0
    else:
        if speed > 60 and speed <= 80:
            return 1
        if speed > 80:
            return 2
        if speed <= 60:
            return 0


def sorta_sum(a, b):
    sumVal = a+b
    if sumVal >= 10 and sumVal <= 19:
        return 20
    else:
        return sumVal


def alarm_clock(day, vacation):
    if vacation:
        if not day == 0 and not day == 6:
            return "10:00"
        else:
            return "off"
    else:
        if not day == 0 and not day == 6:
            return "7:00"
        else:
            return "10:00"


def love6(a, b):
    if a == 6 or b == 6:
        return True
    if abs(a-b) == 6 or a+b == 6:
        return True
    return False


def in1to10(n, outside_mode):
    if outside_mode:
        return (n <= 1 or n >= 10)
    else:
        return (n >= 1 and n <= 10)


def near_ten(num):
    vale = num % 10
    if 10-vale <= 2 or abs(vale-10) <= 2 or vale <= 2:
        return True
    return False


def lone_sum(a, b, c):
    if not a == b and not a == c and not b == c:
        return a+b+c
    if a == b:
        if not a == c:
            return c
    if a == c:
        if not a == b:
            return b
    if b == c:
        if not a == b:
            return a
    return 0


def lucky_sum(a, b, c):
    # if a != 13 and b != 13 and c!=13:
    #     return a+b+c
    if a != 13:
        if b != 13:
            if c != 13:
                return a+b+c
            else:
                return a+b
        else:
            return a
    return 0


def no_teen_sum(a, b, c):
    sumVal = 0
    if a >= 13 and a <= 19:
        if a != 15 and a != 16:
            sumVal += 0
        else:
            sumVal += a
    else:
        sumVal += a

    if b >= 13 and b <= 19:
        if b != 15 and b != 16:
            sumVal += 0
        else:
            sumVal += b
    else:
        sumVal += b
    if c >= 13 and c <= 19:
        if c != 15 and c != 16:
            sumVal += 0
        else:
            sumVal += c
    else:
        sumVal += c
    return sumVal

def round_sum(a, b, c):
    if (a+b+c)%10 == 0:
        return a+b+c
    else:
        return round10(a) + round10(b) + round10(c)

def round10(num):
    vale = num % 10
    diff = 10 - vale
    if 10-vale <= 5 or abs(vale-10) <= 5:
        return num + diff
    return num - vale

def close_far(a, b, c):
    close = 0
    far = 0
    if abs(c-a)<=1:
        close = c
    elif abs(b-a)<=1:
        close = b
    else:
        return False
    if abs(b-a)>=2:
        far = b
    elif abs(c-a)>=2:
        far = c
    else:
        return False
    if close-a<=1 and abs(far-a)>=2 and abs(far-close)>=2:
        return True
    return False

def make_chocolate(small, big, goal):  
    if goal-big*5<=small and goal%5<=small:
        if goal-big*5<0:
            return goal%5
        return goal-big*5
    else:
        return -1
print(make_chocolate(6,2,7))
