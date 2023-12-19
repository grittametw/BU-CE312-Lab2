Array = [["Number ID","Name","Count","Status"],[]]
Item = [[1,"Rubber",0,"Out of stock"],
            [2,"Ruler",5,"In stock"],
            [3,"Pencil",1,"In stock"],
            [4,"Pen",10,"In stock"],
            [5,"Colour pencil",5,"In stock"],
            [6,"A4 Paper",0,"Out of stock"]]
Array = list(Array)

for i in range (0,len(Item)):
    Array[len(Array)-1] = Item[i].copy()
    if i != len(Item)-1:
        Array.append([ ])
        
for i in range (0,len(Array)):
    print(Array[i])

Array_Length = len(Item)
print("All items =", Array_Length)

print("\nIf buyer buy 1 ruler 1 pencil 2 pens and 1 colour pencil.")
Array[2][2] = Array[2][2]-1
Array[3][2] = Array[3][2]-1
Array[4][2] = Array[4][2]-2
Array[5][2] = Array[5][2]-1
Array[3][3] = 'Out of stock'

print("\n")
print("Remaining items")
for i in range (0,len(Array)):
    print(Array[i])