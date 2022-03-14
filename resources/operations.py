import argparse
from functools import reduce, wraps
import os
import pandas as pd
import sys
from resources.shape import Shape
from resources.errors import *
parse = argparse.ArgumentParser(description="Operationsal operations program",usage="math_proccess.py [SOURCE] [OPERATION] [OUTPUT(optional)] [ANALYZE STYLE()]")
operation_list = ["sum","sub","multiply","div","fact","mean","mod","sdeviation"]
operations = parse.add_argument_group("Operations")
operations.add_argument("-+","--sum",help="You can sum the given numbers",action="store_true")
operations.add_argument("-_","--sub",help="You can subtract the given numbers if given numbers is not 2 you cannot get a result ",action="store_true")
operations.add_argument("-*","--multiply",help="You can multiply the given numbers",action="store_true")
operations.add_argument("-/","--div",help="You can divide given 2 numbers if given numbers is not 2 you cannot get a result",action="store_true")
operations.add_argument("-!","--fact",help="you can get the factorial of each given numbers",action="store_true")
operations.add_argument("-=","--mean",help="You can get the mean of numbers",action="store_true")
operations.add_argument("->","--mod",help="You can get the mod of numbers",action="store_true")
operations.add_argument("-(","--sdeviation",help="You can get the standart deviation of numbers",action="store_true")
operations.add_argument("--all",help="You can apply all operations",action="store_true")
operations.add_argument("--excl",choices=operation_list,help="if you apply all arguments, you can select exclude operations, you have to type argument names",nargs="+")
source = parse.add_argument_group("Source")
source.add_argument("-n","--nums",nargs="+",type=float,metavar="number input",help="Numbers")
source.add_argument("--txt",help="You can get numbers from .txt files. if you type just file name searchs in input directory as default. if you don't want to use input directory you have to type your desired file path",metavar=".txt input")
output = parse.add_argument_group("Output")
output.add_argument("--wtxt",help="You can output to a file. if you type just file name searchs in output directory as default.if you don't want to use output directory you have to type your file's path",metavar=".txt output")
analyze =parse.add_argument_group("Analyze Style")
analyze.add_argument("--table",help="You can see all the data from the data frame",action="store_true")
args= parse.parse_args()
methods ={"txt":args.txt,"nums":args.nums}

class Decorators():
 def control(func):
     @wraps(func)
     def wrap():
        if args.excl!=None and args.all: 
         if not func.__name__ in args.excl:
             func()
        else:
            func()       
     return wrap 
 def src(methods=None):  
  def decorator(func):
    @wraps(func)           
    def wrap():
          if list(methods.values()).count(None)==1:  
            if methods["txt"] and methods["txt"].endswith(".txt"):
                try:
                    condition = os.path.basename(methods["txt"])==methods["txt"]
                    with open(os.curdir+"/input/"+methods["txt"] if condition else methods["txt"],"r") as file:
                     resul= file.readlines()
                     resul =[*map(float,resul)]
                     if resul:   
                      Operations.result = resul 
                      func()
                     else:
                         print("File is empty!") 
                except:
                    print("File doesn't exists!")     
            elif methods["nums"]:
                    Operations.result = methods["nums"]
                    func()       
          else:
              raise MultiSelectedError("You cannot select more than one option!")
                                                                                   
    return wrap
  return decorator

 def out(func):
    @wraps(func) 
    def wrap():
      if args.wtxt and args.wtxt.endswith(".txt"):
        condition = os.path.basename(args.wtxt)==args.wtxt  
        f= open(os.curdir+"/output/"+args.wtxt if condition else args.wtxt,"a")
        sys.stdout = f
        func()
      else:
          func() 
        
    return wrap  
class Operations():
 ADD = None
 DIVIDE = None
 SUBTRACT = None
 FACTORIAL = None
 MULTIPLY = None
 MOD = None
 MEAN = None
 SDEVIATION = None
 result = None
 ACTIVERESULTS = {}
     

 @Decorators.out
 @Decorators.src(methods=methods)
 @Decorators.control
 def sum():
     Operations.ADD = sum(Operations.result)
     Operations.ACTIVERESULTS["sum"] = Operations.ADD
     shape = Shape("Sum",Operations.ADD)
     print(shape.shape())
         
 @Decorators.out
 @Decorators.src(methods=methods)
 @Decorators.control     
 def multiply():
    Operations.MULTIPLY = reduce(lambda x,y: x*y,Operations.result)
    Operations.ACTIVERESULTS["multiply"] =  Operations.MULTIPLY
    shape = Shape("Multiply",Operations.MULTIPLY)
    field=  shape.Field()
    field.label_position("Multiply",12)
    field.text_position("Multiply",Operations.MULTIPLY,10)
    print(field.shape())
 @Decorators.out    
 @Decorators.src(methods=methods)  
 @Decorators.control  
 def div():  

    if len(Operations.result)==2 and not 0 in Operations.result:
        Operations.DIVIDE = Operations.result[0]/Operations.result[1]
        Operations.ACTIVERESULTS["divide"] = Operations.DIVIDE
        shape = Shape("Divide",Operations.DIVIDE)
    else:
        shape = Shape("Divide","You cannot divide these numbers!")
    print(shape.shape())
 @Decorators.out       
 @Decorators.src(methods=methods)
 @Decorators.control          
 def fact():
   
    if [*filter(lambda x: x>=0,Operations.result)]==Operations.result:
      
 
     a= [reduce(lambda a,b: int(a)*int(b),range(1,int(i+1))) for i in Operations.result]

     Operations.FACTORIAL = " ".join([*map(str,a)])
     Operations.ACTIVERESULTS["factorial"] = Operations.FACTORIAL
     shape = Shape("Factorial",Operations.FACTORIAL)
     n,t = [],[]
     for name,text in zip(Operations.result,a):
           n.append(str(int(name))+"!")
           t.append(str(text)) 
     field = shape.Field()
     field.text_position(n,t,13,multirow=True)
     field.label_position("Factorial",11)
     print(field.shape()) 
    
    else:
        shape = Shape("Factorial","You cannot get the factorial of negative numbers!")
        print(shape.shape())   
           
 @Decorators.out          
 @Decorators.src(methods=methods) 
 @Decorators.control          
 def sub():
                
    if(len(Operations.result))==2:
        Operations.SUBTRACT = Operations.result[0]-Operations.result[1] 
        Operations.ACTIVERESULTS["subtract"] = Operations.SUBTRACT
        shape = Shape("Subtract",Operations.SUBTRACT)
        print(shape.shape())         
    else:
        shape = Shape("Subtract","You cannot subtract these numbers!")
        print(shape.shape())
 @Decorators.out       
 @Decorators.src(methods=methods)
 @Decorators.control      
 def mean():
    Operations.MEAN =  sum(Operations.result)/len(Operations.result)
    Operations.ACTIVERESULTS["mean"] = Operations.MEAN
    shape = Shape("Mean",Operations.MEAN)
    print(shape.shape())     
 @Decorators.out    
 @Decorators.src(methods=methods)
 @Decorators.control
 def mod():
   
    count_dict = dict()
    for i in Operations.result:
        count_dict.setdefault(i,0)
        count_dict[i]+=1  
    max_list= [k if v == max(count_dict.values()) else None for k,v in count_dict.items()]
    for i in range(max_list.count(None)):
        max_list.remove(None)
    n = [*map(str,[*range(1,len(max_list)+1)])]
    t = [*map(str,max_list)]   
    Operations.MOD  = " ".join([*map(str,max_list)])   
    Operations.ACTIVERESULTS["mod"] = Operations.MOD
    shape = Shape(n,t)
    field= shape.Field()
    field.text_position(n,t,15,multirow=True)
    field.label_position("Mod",15)
    print(field.shape())       
 @Decorators.out
 @Decorators.src(methods=methods)
 @Decorators.control
 def sdeviation():

    Operations.SDEVIATION = (sum([((sum(Operations.result)/len(Operations.result))-i)**2 for i in Operations.result])/(len(Operations.result)-1))**1/2
    Operations.ACTIVERESULTS["sdeviation"] = Operations.SDEVIATION
    shape = Shape("Standart Deviation",str(Operations.SDEVIATION))
    field = shape.Field()
    field.label_position("Standart deviation",7)
    field.text_position("Standart deviation",str(Operations.SDEVIATION),5)
    print(field.shape())
 @Decorators.out  
 @Decorators.src(methods=methods)   
 def analysist():
     ser= pd.Series(Operations.ACTIVERESULTS)
     shape = Shape()
     
     print(shape.move_structure(ser,41,1))