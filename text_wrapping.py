
def manipulate(str):
    if(len(str) == (0)):
        return str
    else:
        
        print(str[:4])
        str = str[4:]
        return manipulate(str)
        
    

string  = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
w= 4
#res = 
print(manipulate(string))
