def Get_Winnings(m, s):
    try:
        if int(m) <= 5 and int(m) > 0:
            prize = (int(m) * 75000) + int(s)
        else:
            prize = "Invalid"
    except:
        prize = "Invalid"
    return(prize)
    
inp = str(input("Enter Gold Medals Won: "))
inp2 = str(input("For how many dollars was your event sponsored?: "))
print("Your prize money is: "+str(Get_Winnings(inp,inp2)))

