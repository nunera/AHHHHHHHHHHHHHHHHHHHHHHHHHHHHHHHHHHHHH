def Get_Winnings(m):
    try:
        if int(m) <= 5 and int(m) > 0:
            prize = int(m) * 75000
        else:
            prize = "Invalid"
    except:
        prize = "Invalid"
    return(prize)
    
inp = input("Enter Gold Medals Won: ")
print("Your prize money is: "+str(Get_Winnings(inp)))

