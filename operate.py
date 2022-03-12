from resources.operations import Operations,operation_list,args
from resources.errors import MultiSelectedError
                     
if __name__ == "__main__":
    if args.all:  
      if sum([1 if vars(args)[i]== True else 0 for i in operation_list])==0:
        Operations.sum()
        Operations.div() 
        Operations.multiply()  
        Operations.mod()  
        Operations.mean() 
        Operations.sub() 
        Operations.fact() 
        Operations.sdeviation()
        if args.table:
          Operations.analysist()
      else: raise MultiSelectedError("You have already actived all parameter!")
          
    else:    
      if args.sum:
        Operations.sum()
      if args.div:
        Operations.div()
      if args.multiply:
        Operations.multiply()
      if args.mod:
        Operations.mod()
      if args.mean:
        Operations.mean()
      if args.sub:
        Operations.sub()
      if args.fact:
        Operations.fact()               
      if args.sdeviation:
        Operations.sdeviation()
      
    