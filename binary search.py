doomsday=[11, 12, 25, 45, 85, 99, 169, 189]
t=189
start=0
end=len(doomsday)-1
mid=len(doomsday)//2
while mid > 0 and mid <= end:
    if doomsday[mid]==t:
        print("found", mid)
        break
    elif t < doomsday[mid]:
        end = mid -1
        mid = (start + end)//2 
    elif t > doomsday[mid]:
        start = mid + 1
        mid = (start + end)//2 