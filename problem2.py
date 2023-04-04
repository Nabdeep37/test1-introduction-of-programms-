RED = "red"
BLUE = "blue"
YELLOW = "yellow"
color1 =input("Enter the color1:")
color2 =input("Enter the color2:")
if(color1== 'RED', 'BLUE', 'YELLOW'):
 print("input are valid")
else:
 print("Error: Invalid Color1")
if(color2== 'RED', 'BLUE', 'YELLOW'):
  print("input are valid")
else:
  print("Error: Invalid Color2")
if(color1== color2):
  print("Error: The two colors you entered are same")
if(color1== "RED" and color2== "BLUE"):
  print("RED+BLUE" + "=" + "PURPLE")
elif(color2== 'YELLOW'):
    print("RED+YELLOW" + "=" + "ORANGE")
if(color1== "BLUE" and  color2== "RED"):
  print("BLUE + RED" + "="+ "PURPLE")
elif(color2== "YELLOW"):
 print("BLUE+YELLOW" + "=" + "GREEN")
if(color1== "YELLOW" and  color2== "RED"):
  print("YELLOW+RED" + "=" + "ORANGE")
elif(color2== "BLUE"):
  print("YELLOW+BLUE" + "=" + "GREEN")

