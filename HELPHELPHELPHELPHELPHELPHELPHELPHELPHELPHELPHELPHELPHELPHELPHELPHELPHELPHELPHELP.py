def print_product(x,y,z):
    print(x*y*z)

num = []    
for i in range(1,4):
    inp = input("Enter number "+str(i)+":")
    num.append(int(inp))
print_product(num[0],num[1],num[2])
