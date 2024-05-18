number_list=[11, 12, 25, 45, 85, 99, 169, 189]
t=189
start=0
end=len(number_list)-1
mid=len(number_list)//2
while mid > 0 and mid <= end:
    if number_list[mid]==t:
        print("found", mid)
        break
    elif t < number_list[mid]:
        end = mid -1
        mid = (start + end)//2 
    elif t > number_list[mid]:
        start = mid + 1
        mid = (start + end)//2 