for i  in range(11,0,-1):
    for k in range(1,11-i): 
        print(" ", end=" ")
    for j in range(1, i+1):
        print("*", end=" ")
    print("\n")
