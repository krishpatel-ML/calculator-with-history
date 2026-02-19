import operator
ops = {
  "+": operator.add,
  "-": operator.sub,
  "*": operator.mul,
  "/": operator.truediv,
}

def show_history():
 try:
  with open("HISTORY_FILE.text","r") as f:
    lines = f.readlines()
    if not lines:
      print("HISTORY IS NOT FOUND")
    else:
       for line in lines:
         print(line.strip()) 
 except FileNotFoundError:
   print("NO HISTORY IS FOUND")       

def clear_history():
  with open("HISTORY_FILE.text","r") as f:
   lines = f.readlines()
   if(len(lines)==0):
    print("HISTORY IS ALLREADY EMPTY")
   else:  
    with open("HISTORY_FILE.text","w") as f:
      f.write("")
      print("YOUR HISTORY IS CLEARED")

def save_to_history(equation,result):
  with open("HISTORY_FILE.text","a")as f:
    f.write(equation + " = " + str(result) + "\n")

def calculate(user_input):
  parts = user_input.split()
  if(len(parts)!=5):
    print("INVALID INPUT.USE FORMAT LIKE THIS : 8 + 8 + 8 ")
    return    
  num1 = float(parts[0])
  op1 = parts[1]
  num2 = float(parts[2])
  op2 = parts[3]
  num3 = float(parts[4])
  try:
    if op2 in ("*","/") and op1 in ("+","-"):
      temp = ops[op2](num2,num3)
      result = ops[op1](num1,temp)
    else:  
     result1 = ops[op1](num1,num2)
     result = ops[op2](result1,num3)
    if(result == int(result)):
      result = int(result)
    print("RESULT OF",num1,op1,num2,op2,num3,"IS",result)  
    save_to_history(user_input,result)

  except ZeroDivisionError:
    print("YOU CANNOT DEVIDE BY ZERO")
  except Exception:
    print("INVALID INPUT.Example:8 + 8 * 2")  
def main():
  print("---SIMPLE CALCULATOR (type history,clear or exit)")
  while True:
    user_input = input("ENTER CALCULATION (+,-,*,/) OR COMMAND(history,clear and exit) : ")
    if(user_input.lower().strip()=="exit"):
      print("GOODBYE...")
      break
    elif(user_input.lower().strip()=="history"):
      show_history()
    elif(user_input.lower().strip()=="clear"):
      clear_history()
    else:
      calculate(user_input)  

if __name__ == "__main__":
 main()