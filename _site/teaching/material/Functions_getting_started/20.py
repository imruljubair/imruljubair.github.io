def main():
    
    rows = int(input("Enter the number of rows: "))
    
    for i in range (rows,0,-1):
       for j in range(1, i+1):
           print(str(j),end="")
       print(end="\n")

main()
