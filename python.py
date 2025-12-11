result=""
Temp=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def Convert(n):
   bin=""
   global Temp
   global result
   if(n>32767 or n<-32767):
        print("Number is out of Range")  
   N=abs(n)
   while N>0:
       bin=str(N%2)+ bin
       N//=2
#    print(bin)

   for i, char in enumerate(bin):
       Temp[len(Temp)-len(bin)+i]=int(char)
   bin=""
   for i in range(0,len(Temp)):
       result= result+ str(Temp[i])
   N=0   

   if(n<0):
    #  print(f"The Binary form of {n} is {compliment_2()}")
     return compliment_2()
   else:
    #  print(f"The Binary form of {n} is {result}")
     give=result
     result=""
     return give

     
carry=0      
def compliment_2():
    global Temp
    global carry
    for i in range(0,len(Temp)):
     if(Temp[i]==0):
      Temp[i]=1
     else:
      Temp[i]=0

    if(Temp[len(Temp)-1]==1):
     Temp[len(Temp)-1] =0
     carry=1 
     for i in range(len(Temp)-2,-1,-1):
      if(Temp[i]==1 and carry ==1):
         Temp[i]=0
         carry=1
      elif(Temp[i]==0):
         Temp[i]=carry
         carry=0
         break            
    else:
     Temp[len(Temp)-1]=1
    result=""   
    for i in range(0,len(Temp)):
       result= result+ str(Temp[i])   
    return result     
           
       
       
# if __name__ == "__main__":
#    N=input("Enter Number to Convert in Binary: ")
#    try:
#        val = int(N)
#        Convert(val)
#    except ValueError:
#        print("That's not integer")