#!/usr/bin/python3
import re
import sys

################################################################################## 
#  the reader (from class website)
###################################################################################

# A regular expression that matches postscript each different kind of postscript token
pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'

# Given a string, return the tokens it contains
def parse(s):
   tokens = re.findall(pattern, s)
   return tokens

# Given an open file, return the tokens it contains
def parseFile(f):
   tokens = parse(''.join(f.readlines()))
   return tokens

##########################################################################################
# build in functions
# all names are hold in a dictionary: operations at the bottom of dictStack
# Thus rewrite built in functions are allowed
#########################################################################################


#operations on stack

#print contained of opStack from top to bottom
def stack():
   i=len(opStack)-1
   while(i>=0):
      print(opStack[i])
      i=i-1
      
#clear opStack   
def clear():
	del opStack[:]
	
#exchange top two element of opStack	       
def exch():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1)
        opStack.append(op2)
        
#duplicate the top most element of opStack     
def dup():
        op1=opStack[-1]
        opStack.append(op1)
        
#remove the top element of opStack
def pop():
        op1=opStack.pop()
        
#postScript =
#remove and print the top element of opStack
def p_p():
        op1=opStack.pop()
        print (op1)
       
  

#operations on dictStack

#postScript "dict"
#take an int argment from opStack, error if not
#create a empty dictionary, {}
#push it onto opStack
def dictionary():
   if(type(opStack[-1])!=int):
      print("dict takes argument: int")
   else:
        arg=opStack.pop()
        newDict={}
        opStack.append(newDict)
       
#pop {} from opStack, error if not
#push it onto dictStack
#names defined after {} are local
#{} will use as a symbol for end function
def begin():
   if(opStack[-1]=={}):
        arg=opStack.pop()
        dictStack.append(arg)
   else:
       print("begin takes argument:{}")
       
#pop out local variables(defined after begin) from dictStack
#until and include {} 
def end():
   while(dictStack[-1]!={}):
      dictStack.pop()
   dictStack.pop()

#pop /name and its definition from opStack, error if not /name
#create a dictionary {name: defination}
#push this dictonary onto dictStack
#redefine allowed
def deF():
   if(opStack[-2][0]!='/'):
      print("dict takes argument: /name")
   else:
      op1=opStack.pop()
      op2=opStack.pop()     
      newDict={op2[1:]:op1}
      if -1 in dictStack[-1]:
         dictStack[-1][op2[1:]]=op1
      else:
         dictStack.append(newDict)


#boolean operators

#postScript 'if'
#pop out a boolean variable, error if not
#and a procedure (list), error if not
#if boolean is true, exe procedue
def iF():
   if(type(opStack[-1])!=list):
      print("if takes procedure as argument")
   elif(type(opStack[-2])!=bool):
      print("if takes bool as argument")
   else:
      op1=opStack.pop()
      op2=opStack.pop()
      if(op2==True):
         interprete(op1)
         
#pop out a boolean variable, error if not
#and two procedure (list), error if not
#if boolean is true, exe procedue1
#if boolean is false, exe procedue2        
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
         interprete(op2)
      else:
         interprete(op1)


#postScript 'and', 'or', 'not', takes only boolean varibles
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



#adjuct bool varibles
def true():
   opStack.append(True)
def false():
   opStack.append(False)

            
# compare operations
# takes only int argment
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
# takes only int argment
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
      

#operations holds all built in funcitons
#and lies at the bottom of dictStack
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



#7 boolean operators
'if':iF,
'ifelse':ifelse,
'and':AND,
'or':OR,
'not':NOT,


'true':true,
'false':false,


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


#operand stack are impletemented as a list
#list built in function pop and append are used to access
#the top most element
opStack=[]

#dictionary stack, build in funtions at the bottom
#list built in function pop and append are used to access
#the top most element
#interator of the last element are used to search from top to bottom
dictStack=[operations,]

#####################################################################################
#interpreter
######################################################################################

#exe function
#interprete postScript code in python envirment
#input is as list of parsed postScript code
   #e.g. parseFile(filename), parse(stringname)
#or a list, representing a procedure {...} in postScript
#all postScript code are impletement after this function call

def interprete(l):

   #call handling {} function
   l=helperFun(l)
   
   for el in l:

      # push new /name on the stack
      if (el[0]=='/'):
         opStack.append(el)
         
      #push procedure{}, now is a list, onto the stack
      elif (type(el)==list):
         opStack.append(el)

      #push numbers onto the stack
      elif (el.isdigit()==True or (el[0]=='-' and el[1:].isdigit()==True)):
         opStack.append(int(el))

      #call name dictStack search function for names
      else:
         searchDict(el)
       
     

#search names on dictStack from top to bottom
#and push its value or exe its procedure

#input is a string, which could be a existing key
#error if not find

#built in functions are at the bottom of dictStack
#Thus, redefined built in names are allowed

         
def searchDict(name):
   i=len(dictStack)-1
   while(i>=0):
      if( name in dictStack[i]):
        
         #run built in functions
         if(i==0):
            
            operations[name]()

         #self defined dictionary   
         else:
           
            
            # run its procedure, if its value is list
            if (type(dictStack[i][name])==list):
               dictStack.append({-1:i})
               interprete(dictStack[i][name])
	      # dictStack.pop()

            # push its value, if its value is noncode
            else:
               opStack.append(dictStack[i][name])
   
         return 
      else:
         if( rule=='-s') and (-1 in dictStack[i]):
            i=dictStack[i][-1]
         else:
            i=i-1
   print("name undefined")



#handling {}
#translate the first pair of {}, procedure into list
#get ride of \r
#input is a list of parsed postScript code
#or a list of procedures, to handle nested {}
   
def helperFun(prog):

   count=0
   holer=[]
   fun=[]
   for el in prog:
      
      if(el!='\r'):

         if (el=='{'):
            count=count+1

         elif (el=='}'):
            count=count-1
            if (count==0):

               #exclude first "{"
               fun.append(holer[1:])
               
               #clear holer for parallel {}
               holer=[]

         if(count==0 ):
            if( el!='}'):
               fun.append(el)

         else:
            holer.append(el)
   return fun
      

#print contains of dictStack from top to bottom
#except built in functions
def printDict():
   i=len(dictStack)-1
   while(i>0):
      print(dictStack[i])
      print("----------------------")
      i=i-1

###################################################################################
# input
# from command line : python sps.py input_filename -s/ -d
# from windows file :
# program as a string
####################################################################################
#  from file
#  fn=open('filename', 'r')

# Command line use: pass the filename as the first command-line argument
if __name__ == "__main__":
	fn = sys.argv[1]
	rule='-d'
	if len(sys.argv)>2:
		rule=sys.argv[2]
  
	

#  print (parseFile(open(fn,"r")))


if(rule=='-s'):
	print('running with static scoping rules')
else:
	print("running with dynamic scoping rules")
	
	
# A simple program
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

neg="-3 2 add"
acc="/1 1 def"

ssps= '''
/x 4 def
/h { /x 5 x} def
/g { x } def
/f { /x 7 def g} def
f
'''

#interprete( parse (ssps))   

interprete(parseFile(open(fn,"r")))
print("opStack is:")
stack()

print("dictStack is:")
printDict() 


