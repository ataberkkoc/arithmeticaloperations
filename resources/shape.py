from .errors import *
class Shape():
    def __init__(self,name=None,text=None):
        self.NAME = name
        self.TEXT = text
    class Field():
        def __init__(self,width=34,pos=34,content_margin=2):
            self.content_margin = content_margin
            self.pos= pos
            self.width = width
            self.FIELD_POS = " "*self.pos +"-".center(self.width,"-")
            self.TEXT_POS = None
            self.LABEL_POS = None

        def label_position(self,name,hpos=14,vpos=0):
          assert vpos>=0  
          pos= [(" "*(hpos+self.pos+1)+"-"*(len(name)+2)),(" "*(hpos+self.pos)+"| " + name + " |"),(" "*(hpos+self.pos+1)+"-"*(len(name)+2)),"\n"*vpos]
          self.LABEL_POS ="\n".join(pos)
        
        def multiple(self,name,text,hpos):
             a=  zip(name,text)
             b= ["\n"*self.content_margin]
             for n,t in a:
                b.append(" "*(hpos+self.pos)+n +" : " +t)
             b.append("\n"*self.content_margin)
             self.TEXT_POS = "\n".join(b)                   
                  
        def text_position(self,name,text,hpos,multirow=False):
         if  multirow:
             return self.multiple(name,text,hpos)    
         assert self.content_margin >=0
         self.TEXT_POS = "\n"*self.content_margin+" "*(hpos+self.pos)+str(name) +  " : " + str(text) + "\n"*self.content_margin
        def shape(self):
            
          up = self.LABEL_POS 
          bot = self.FIELD_POS +  self.TEXT_POS  + self.FIELD_POS
          return up+bot
    def shape(self):
        if self.NAME and self.NAME != None:
         field = self.Field()
         field.label_position(self.NAME,int(16-len(self.NAME)/2))
         field.text_position(self.NAME,self.TEXT,15-len(self.NAME))
         return field.shape()
        else:
         raise ValidationError("Your given data doesn't validate")
    def move_structure(self,text,hpos,tmargin=0):
        structure_li = str(text).splitlines()
        structure_li =[" "*hpos +i for i in structure_li]
        structure_li.insert(0,"\n"*tmargin)
        return "\n".join(structure_li)