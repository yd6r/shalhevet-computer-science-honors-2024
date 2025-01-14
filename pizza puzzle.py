"""
Four friends ordered a pizza cut into eight slices. The whole pizza
was eaten, with each friend eating a different number of slices.
If no slice was divided and no friend ate more than the other three
put together, how many slices did each friend eat? Print all
possibilities. 
"""
def pizza(slices):
    for a in range(5):
        for b in range(5):
            for c in range(5):
                for d in range(5):
                    if a+b+c+d==slices:
                        if a<=b+c+d and b<=a+c+d and c<=a+b+d and d<=a+b+c:
                            if a!=b and a!=c and a!=d and b!=c and b!=d and c!=d:
                                print(a, b, c, d)
        
        
pizza(8)
