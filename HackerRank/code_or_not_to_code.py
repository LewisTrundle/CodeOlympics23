import sys
import itertools

# find all possible subsets of holidays
def find_power_set(s):
    power_set = []
    for i in range(1, len(s)//2+1):
        power_set += itertools.combinations(s, i)
    return set(power_set)


def calc_prod(n, week, holidays):
    total_prod = 0
    last_holiday = max(holidays)
    next_holiday = min(holidays)
    starting_holiday = next_holiday
    
    for i in range(0, n):
        #print("\nwe're now on day", i)
        if i in holidays:
            holidays.remove(i)
            last_holiday = i
            if len(holidays) >= 1:
                next_holiday = min(holidays)
            else:
                next_holiday = starting_holiday
            #print("The last holiday is now day ", last_holiday)
            #print("The next holiday is now day ", next_holiday)
        else:
            if last_holiday <= i:            # if there has already been a holiday this week
                x = i - last_holiday
            else:                            # if the last holiday was last week
                x = n - last_holiday + i
            
            if next_holiday > i:             # if the next holiday is still in this week
                y = next_holiday - i
            else:                            # if the next holiday is next week
                y = n - i + starting_holiday
            
            total_prod += week[min(x, y)-1]
            
            
    return total_prod

        
def productivity(n, ps):
    power_set = find_power_set(range(n))
    max_prod = 0
    for holidays in power_set:
        prod = calc_prod(n, ps, list(holidays))
        if prod > max_prod:
            max_prod = prod
    return max_prod
        

args = []
for line in sys.stdin:
    args.append(line.strip("\n"))
prod = productivity(int(args[0]), [eval(i) for i in args[1].split(" ")])
print(prod)