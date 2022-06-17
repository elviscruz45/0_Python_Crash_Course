def sum_two_smallest_numbers(numbers):
    numbers.sort()
    sum_lowers=[]
    for i in numbers:
        if i >0 and i%1==0:
            sum_lowers.append(i)
    
    return (sum_lowers[0]+sum_lowers[1])


print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))