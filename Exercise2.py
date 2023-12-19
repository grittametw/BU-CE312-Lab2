Array_A = [7,5,10,14,3,9,7]
Array_B = [9,10,3,4,2,5,7,1]

Array_Length_A = len(Array_A)
Array_Length_B = len(Array_B)
print("Length of Array_A =", Array_Length_A)
print("Length of Array_B =", Array_Length_B)

Array_A.insert(0,15)
Location_of_A = Array_A.index(7)
Location_of_B = Array_B.index(7)
Array_A.append(1)
Array_B.append(14)
Array_C = Array_A.copy()
Array_C.extend(Array_B)
Value = Array_C.count(7)
Array_C.sort()
Array_C.remove(7)
Array_D = Array_C.copy()
Array_D.reverse()

print(Array_C)
print(Array_D)