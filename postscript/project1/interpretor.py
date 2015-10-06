#!/usr/bin/python3
import re
import sys



#globle varibles
opStack=[]
dictStack=[]

#input
demoProg = '''
/fact {
   1 dict begin
   /x exch def
      x 0 eq
      {1}
      {x 1 sub fact x mul}
   ifelse
   end
} def
5 fact
'''

#parse input
pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'
# Given a string, return the tokens it contains
def parse(s):
   tokens = re.findall(pattern, s)
   return tokens

# Given an open file, return the tokens it contains
def parseFile(f):
   tokens = parse(''.join(f.readlines()))
   return tokens



#main function
#interprete parsed postScript code in python
def running(l):
   l=helperFun(l)
   for el in l:
      # push /name on the stack
      if (el[0]=='/'):
         opStack.append(el)

      # adjuct bool varible
      elif(el=='true'):
         opStack.append(True)
      elif(el=='false'):
         opStack.append(False)
         
      #push procedure--{},
      #which have been translated into a list
      #onto the stack
      elif (type(el)==list):
         opStack.append(el)

      #push #s onto the stack
      elif (el.isdigit()==True):
         opStack.append(int(el))

      #find the operators in operations dictionary
      elif (el in operations):
         operations[el]()

      #find names in dictStack
      else:
         lookDict(el)



# helperFun translate thing within the first pair of {} into list
def helperFun(prog):
   count=0
   left=False
   right=False
   holer=[]
   fun=[]
   for el in prog:
      if(el!='\r'):
         if (el=='{'):
            count=count+1
         elif (el=='}'):
            count=count-1
            if (count==0):
               holer=holer[1:]
               fun.append(holer)
               holer=[]
         if(count==0 ):
            if( el!='}'):
               fun.append(el)
         else:
            holer.append(el)
   return fun
      
#find names on dictStack
def lookDict(name):
   i=len(dictStack)-1
   while(i>=0):
      if( name in dictStack[i]):
         if (type(dictStack[i][name])==list):
            running(dictStack[i][name])
         else:
            opStack.append(dictStack[i][name])
         return
      i=i-1
   print('name undefined')

#print contains of dictStack from top to bottom
#seperating by "============="
def printDict():
   i=len(dictStack)-1
   while(i>=0):
      print(dictStack[i])
      print("======================")
      i=i-1



#operations on stack

def stack():
   i=len(opStack)-1
   while(i>=0):
      print(opStack[i])
      i=i-1
   
def clear():
	del opStack[:]
	       
def exch():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1)
        opStack.append(op2)
     
def dup():
        op1=opStack[-1]
        opStack.append(op1)
      
def pop():
        op1=opStack.pop()
            
def p_p():
        op1=opStack.pop()
        print (op1)
       
  

#operations on dictStack
def dictionary():
   if(type(opStack[-1])!=int):
      print("dict takes argument: int")
   else:
        arg=opStack.pop()
        newDict={}
        opStack.append(newDict)
       
        
def begin():
   if(opStack[-1]=={}):
        arg=opStack.pop()
        dictStack.append(arg)
   else:
       print("begin takes argument:{}")
       

def end():
   dictStack.pop()
   dictStack.pop()
                    
def deF():
   if(opStack[-2][0]!='/'):
      print("dict takes argument: /name")
   else:
      op1=opStack.pop()
      op2=opStack.pop()     
      newDict={op2[1:]:op1}
      dictStack.append(newDict)



#boolean operators
      
def iF():
   if(type(opStack[-1])!=list):
      print("if takes procedure as argument")
   elif(type(opStack[-2])!=bool):
      print("if takes bool as argument")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      if(op2==True):
         running(op1)

def ifelse():
   if((type(opStack[-1])!=list) or (type(opStack[-2])!=list)):
      print("ifelse takes argument procedue: {...}")
   elif(type(opStack[-3])!=bool):
      print("ifelse takes bool as argument")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      op3=opStack.pop()
      if (op3==True):
         running(op2)
      else:
         running(op1)

def AND():
   if((type(opStack[-1])!=bool) or (type(opStack[-2])!=bool)):
      print("and takes argument:bool")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op2 and op1)
      
def OR():
   if((type(opStack[-1])!=bool) or (type(opStack[-2])!=bool)):
      print("or takes argument:bool")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op2 or op1)

def NOT():
   if((type(opStack[-1])!=bool) or (type(opStack[-2])!=bool)):
      print("not takes argument:bool")
   else:
      op1=opStack.pop()
      opStack.append(not op1)
            
            
# logical operations

def eq():
   if((type(opStack[-1])!=int )or (type(opStack[-2])!=int) ):
      print("eq takes argument: int")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op1==op2)

   
def lt():
   if((type(opStack[-1])!=int )or (type(opStack[-2])!=int) ):
      print("lt takes argument: int")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op2<op1)
        
def gt():
   if((type(opStack[-1])!=int )or (type(opStack[-2])!=int) ):
      print("gt takes argument: int")
   else:
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op2>op1)


# Arithmetic operators
def add():
   if ((type(opStack[-1])!=int ) or (type(opStack[-2]) != int)):
      print("add takes argument: int")
   else:        
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op1+op2)

def sub():
   if ((type(opStack[-1])!=int ) or (type(opStack[-2]) != int)):
      print("sub takes argument: int")
   else:  
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op2-op1)

def mul():
   if ((type(opStack[-1])!=int ) or (type(opStack[-2]) != int)):
      print("mul takes argument: int")
   else:  
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op1*op2)

def div():
   if ((type(opStack[-1])!=int ) or (type(opStack[-2]) != int)):
      print("div takes argument: int")
   else:  
      op1=opStack.pop()
      op2=opStack.pop()
      opStack.append(op2/op1)

#functions in operations
operations={

#6 opStack operators
'stack':stack,
'clear':clear,
'exch':exch,
'pop':pop,
'=':p_p,
'dup':dup,



#4 dictStack Operators
'dict':dictionary,
'begin':begin,
'end':end,
'def':deF,



#5 boolean operators
'if':iF,
'ifelse':ifelse,
'and':AND,
'or':OR,
'not':NOT,



#3 logical operators
'eq':eq,
'gt':gt,
'lt':lt,


# Arithmetic operators
'add':add,
'sub':sub,
'mul':mul,
'div':div,
   }


            





        
        
