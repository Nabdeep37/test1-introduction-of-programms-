s =float(input("Enter the salary in germany:"))
c =input("Enter the migrate country:")
c = c.lower()
ca ="canada"
com ="combodia"
usa ="united state america"
uk ="united kingdom"
def convertsalary(s,c):
  if(c== ca):
    total_salary = s * 1.55
    if(total_salary>64000):
      print("you will be rich in canada with a salary of",total_salary,"CAD")
    else:
      print("you will be poor in canada with a salary of",total_salary,"CAD")
  if(c== com):
    total_salary = s * 4555
    if(total_salary>5649856):
      print("you will be rich in com with a salary of" ,total_salary,"Cambodian Riel")
    else:
      print("you will bw poor in com with a salary of",total_salary,"Cambodian Riel")
    if(c== usa):
      total_salary = s * 2.5
      if(total_salary>56516):
        print("you will be rich in usa with a salary of" ,total_salary,"US Dollars")
      else:
        print("you will bw poor in usa with a salary of",total_salary,"US Dollars")
        if(c== uk):
          total_salary = s * 1.2
          if(total_salary>35423):
            print("you will be rich in uk with a salary of" ,total_salary,"Pound Sterling")
          else:
            print("you will bw poor in uk with a salary of",total_salary,"Pound Sterling")
        

convertsalary(s, c)



