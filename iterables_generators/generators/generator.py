def count_up_to(max):
    count = 1
    nums = []

    while count < max:
        nums.append(count)
        count +=1

    return nums

# print(count_up_to(10))

def gen_count_up_to(max):
    count = 1

    while count <= max:
        yield count
        count += 1

counter = gen_count_up_to(10)

# for num in counter:
#     print(num)

def week():
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    count = 0

    for day in days:
        yield day

day_counter = week()

# for day in day_counter:
#     print(day)

def yes_or_no():
    message = 'yes'
    


    while True:
        yield message
        if message == 'yes':
            message = 'no'
        else:
            message = 'yes'


    
    

# gen = yes_or_no()

# for m in gen:
#     print(m)

def current_beat():
    nums = (1,2,3,4)
    i = 0
    
    while True:
        if i == len(nums): 
            i = 0
        yield nums[i]
        i+=1

beat = current_beat()

print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))
print(next(beat))