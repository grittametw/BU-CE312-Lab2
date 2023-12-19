Array = [["Number ID","Name","Count","Status"],[]]
Item = [[1,"Rubber",0,"Out of stock"],
            [2,"Ruler",5,"In stock"],
            [3,"Pencil",1,"In stock"]]
Array = list(Array)

for i in range (0,len(Item)):
    Array[len(Array)-1] = Item[i].copy()
    if i != len(Item)-1:
        Array.append([ ])
        
for i in range (0,len(Array)):
    print(Array[i])

Array_Length = len(Item)
print("All items =", Array_Length)