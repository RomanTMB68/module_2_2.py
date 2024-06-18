first=int(input('целое число:'))
second=int(input('целое число:'))
third=int(input('целое число:'))
if first == second and second != third:
    print(2)
elif first == third and second != third:
    print(2)
elif third  == second and second != first:
    print(2)
elif first == second and second == third and first == third:
    print(3)
else:
    print(0)