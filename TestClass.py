def Welcome():
    return print("This is going to be an amazing adventure!")

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

def sum_double(a, b):
    if not a == b:
        return a+b
    else:
        return 2*(a+b)

def diff21(n):
    if n<=21:
        return 21-n
    else:
        return -2*(21-n)

def parrot_trouble(talking, hour):
    if talking and (hour<7 or hour>20):
        return True
    else:
        return False

def makes10(a, b):
    if a ==10 or b == 10:
        return True
    elif a+b==10:
        return True
    else:
        return False

def near_hundred(n):
    if abs(100-n)<=10:
        return True
    elif abs(200-n)<=10:
        return True
    else:
        return False     

def pos_neg(a, b, negative):
    if negative and a<=0 and b<=0:
        return True
    elif not negative and ((a>0 and b<=0) or (a<=0 and b>0)):
        return True
    else:
        return False
        
def not_string(str):
    if str.startswith("not"):
        return str
    else:
        return "not "+str

def array_front9(nums):
    index = len(nums)
    if index > 4:
        index = 4
    for i in range(index):
      if nums[i]==9:
        return True
    return False
    
def array123(nums):
    for i in range(len(nums)):
        if i+2<len(nums):
            if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
                return True
    return False
            
def string_match(a, b):
    index = 0
    counter = 0
    if len(a)>len(b):
        index = len(b)
    else:
        index = len(a)
    for i in range(index):
        if i+1 < index:
            if a[i]==b[i] and a[i+1]==b[i+1]:
                counter = counter+1
    return counter

### STRING 1 ###
def hello_name(name):
    return "Hello "+name+"!"

def make_abba(a,b):
    return a+b+b+a

def make_tags(tag, word):
    return "<"+tag+">"+word+"</"+tag+">"

def make_out_word(out, word):
    return out[0]+out[1]+word+out[2]+out[3]

def extra_end(str):
    end = str[-2:]
    return 3*end

def first_two(str):
    if len(str)>2:
        return str[:2]
    else:
        return str    

def first_half(str):
    mid = int(len(str)/2)
    return str[:mid]

def without_end(str):
    mid = str[1:]
    mid = mid[:-1]
    return mid

def combo_string(a,b):
    if len(a)>0 and len(b)>0:
        if len(a)>len(b):
            return b+a+b
        else:
            return a+b+a
    elif len(a)==0:
        return b
    elif len(b)==0:
        return a

def non_start(a, b):
    return a[1:]+b[1:]

def left2(str):
    starts = str[:2]
    return str[2:]+starts
##Call the method
print(combo_string("to","test"))
