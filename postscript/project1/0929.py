Python 3.2.1 (default, Jul 10 2011, 21:51:15) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> pattern
'/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'
>>> prog=parse(demoProg)
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> opStack=[]
>>> opStack.append(prog[0][1:])
>>> opStack
['fact']
>>> type(parse)
<class 'function'>
>>> type(dict)
<class 'type'>
>>> def helperFun(prog)
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog
	
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		if (el='{')
		
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		if (el=='{')
		
SyntaxError: invalid syntax
>>>  def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		if (el=='{'):
			
SyntaxError: unexpected indent
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			inn=True
			count=count+1
		elif(el=='}')
		
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			inn=True
			count=count+1
		else(el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0)
		
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			inn=True
			count=count+1
		else (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0):
			
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			inn=True
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif(count==0):
			fun.append(el)
		else
		
SyntaxError: invalid syntax
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			inn=True
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif(count==0):
			fun.append(el)
		else:
			holer.append(el)

			
>>> def helperFun(prog):
	for el in prog:
		inn=Fasle
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			inn=True
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif(count==0):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperfun(prog)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    helperfun(prog)
NameError: name 'helperfun' is not defined
>>> helpFun(prog)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    helpFun(prog)
NameError: name 'helpFun' is not defined
>>> helperFun(prog)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    helperFun(prog)
  File "<pyshell#34>", line 3, in helperFun
    inn=Fasle
NameError: global name 'Fasle' is not defined
>>> def helperFun(prog):
	for el in prog:
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif(count==0):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> helperFun(prog)
['def']
>>>  def helperFun(prog):
	for el in prog:
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0):
			fun.append(el)
		else:
			holer.append(el)
	return fun

SyntaxError: unexpected indent
>>> def helperFun(prog):
	for el in prog:
		count=0
		holer=[]
		fun=[]
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> heplerFun(prog)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    heplerFun(prog)
NameError: name 'heplerFun' is not defined
>>> helperFun(prog)
['def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> def helperFun(prog):
	count=0
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], '}', 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0 and el not '}'):
			fun.append(el)
		elif (count not 1 and el not '{'):
			holer.append(el)
	return fun
SyntaxError: invalid syntax
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el not '}')):
			fun.append(el)
		elif ((count not 1 )and (el not '{')):
			holer.append(el)
	return fun
SyntaxError: invalid syntax
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif ((count != 1 )and (el != '{')):
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['1', 'x', '1', 'sub', 'fact', 'x', 'mul', '}'], 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif ((count != 1 )or (el != '{')):
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}'], 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif ((count = 1 )and (el != '{')):
		else
			holer.append(el)
	return fun
SyntaxError: invalid syntax
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif ((count ==1 )and (el == '{')):
		else
			holer.append(el)
	return fun
SyntaxError: expected an indented block
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif ((count ==1 )and (el == '{')):
		else:
			holer.append(el)
	return fun
SyntaxError: expected an indented block
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif (! ((count ==1 )and (el == '{'))):
			holer.append(el)
	return fun
SyntaxError: invalid syntax
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		elif ( not ((count ==1 )and (el == '{'))):
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}'], 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		if (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif((count==0 )and ( el != '}')):
			fun.append(el)
		elif ( not ((count ==1 )and (el == '{'))):
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', 'ifelse', 'end'], 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				holer=holer[1:]
				fun.append(holer)
		elif((count==0 )and ( el != '}')):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '1', 'x', '1', 'sub', 'fact', 'x', 'mul', 'ifelse', 'end'], 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> holer[1]
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    holer[1]
NameError: name 'holer' is not defined
>>> holer[0]
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    holer[0]
NameError: name 'holer' is not defined
>>>  def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif((count==0 )and ( el != '}')):
			fun.append(el)
		else:
			holer.append(el)
	return fun
SyntaxError: unexpected indent
>>> 
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		elif((count==0 )and ( el != '}')):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '1', 'x', '1', 'sub', 'fact', 'x', 'mul', 'ifelse', 'end'], 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				holder=holer[1:]
				fun.append(holer)
		if((count==0 )and ( el != '}')):
			fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}'], 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0 ):
			if( el!='}')
				fun.append(el)
		else:
			holer.append(el)
	return fun

SyntaxError: invalid syntax
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				fun.append(holer)
		if(count==0 ):
			if( el!='}'):
				fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if (el=='{'):
			count=count+1
		elif (el=='}'):
			count=count-1
			if (count==0):
				holer=holer[1:]
				fun.append(holer)
		if(count==0 ):
			if( el!='}'):
				fun.append(el)
		else:
			holer.append(el)
	return fun

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 'def']
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
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

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 'def']
>>> opStack=[]
>>> dictStack=[]
>>> def def:
	
SyntaxError: invalid syntax
>>> def Def:
	
SyntaxError: invalid syntax
>>> def define:
	
SyntaxError: invalid syntax
>>> def fact:
	
SyntaxError: invalid syntax
>>> def 'def'():
	
SyntaxError: invalid syntax
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
		if(el=='def'):
			el='deF'
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

>>> helperFun(prog)
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'deF', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 'deF']
>>> def deF():
	op1=opStack.pop()
        op2=opStack.pop()
        newDict={op2:op1}
        dictStack.append(newDict)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def deF():
	op1=opStack.pop()
	op2=opStack.pop()
	newDict={op2:op1}
	dictStack.append(newDict)

	
>>> operations={'def':deF,}
>>> operations={'def':deF,}
>>> def helperFun(prog):
	count=0
	left=False
	right=False
	holer=[]
	fun=[]
	for el in prog:
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

>>> pro=helperFun(prog)
>>> pro
['/fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 'def']
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(operation[el])==function):
			operation[el]()
		else
		
SyntaxError: invalid syntax
>>> type(deF)
<class 'function'>
>>> type(deF)==function
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    type(deF)==function
NameError: name 'function' is not defined
>>> type(7)==int
True
>>> type(1)
<class 'int'>
>>> type(deF)==fun
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    type(deF)==fun
NameError: name 'fun' is not defined
>>> class
SyntaxError: invalid syntax
>>> <class int>
SyntaxError: invalid syntax
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type():
			operation[el]()
		else
		      
SyntaxError: invalid syntax
>>> type(deF)==<class 'function'>
SyntaxError: invalid syntax
>>> type(deF)==class function
SyntaxError: invalid syntax
>>>  def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list)
			opStack.append(el)
		else
		
SyntaxError: unexpected indent
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list)
			opStack.append(el)
		else
		
SyntaxError: invalid syntax
>>> type([])==list
True
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		else:
			operation[el]()

			
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    running(prog)
  File "<pyshell#149>", line 9, in running
    operation[el]()
NameError: global name 'operation' is not defined
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		else:
			operations[el]()

			
>>> running(prog)
>>> dictStack
[{'fact': ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end']}]
>>> opStack.append(5)
>>> opStack
['fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 5]
>>> opStack.pop()
5
>>> opStack()
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    opStack()
TypeError: 'list' object is not callable
>>> opStack
['fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end']]
>>> opStack.append(5)
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> prog=['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', 5, fact]
Traceback (most recent call last):
  File "<pyshell#162>", line 1, in <module>
    prog=['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', 5, fact]
NameError: name 'fact' is not defined
>>> prog=['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', '5', 'fact']
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		else:
			lookDict()

			
>>> def lookDict()def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		else:
			lookDict(el)
			
SyntaxError: invalid syntax
>>> def lookDict():
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		else:
			lookDict(el)

			
>>> len([1, 2, 3])
3
>>> def lookDict(name):
	i=len(dictStack)-1
	while(i>=0):
		if( dictStack[i].has_key(el))
		
SyntaxError: invalid syntax
>>> def lookDict(name):
	i=len(dictStack)-1
	while(i>=0):
		if( dictStack[i].has_key(el)):
			running(dictStack[i][el])
			break

	
>>> pro=['/y','{','1','}' 'def']
>>> running(pro)
>>> dictStack
[{'fact': ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end']}]
>>> helperFun(pro)
['/y']
>>> pro=['/y','{','1','}', 'def']
>>> helperFun(pro)
['/y', ['1'], 'def']
>>> running(pro)
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    running(pro)
  File "<pyshell#165>", line 11, in running
    lookDict()
TypeError: lookDict() takes exactly 1 argument (0 given)
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		else:
			lookDict(el)

			
>>> running(pro)
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    running(pro)
  File "<pyshell#187>", line 11, in running
    lookDict(el)
  File "<pyshell#178>", line 4, in lookDict
    if( dictStack[i].has_key(el)):
AttributeError: 'dict' object has no attribute 'has_key'
>>>  def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		elif (operations.has_key(el):
			operations[el]()
		      
SyntaxError: unexpected indent
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		elif (operations.has_key(el):
			operations[el]()
		      
SyntaxError: invalid syntax
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		elif (operations.has_key(el)):
			operations[el]()
		else
		
SyntaxError: invalid syntax
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		elif (operations.has_key(el)):
			operations[el]()
		else:
			lookDict(el)

			
>>> running(pro)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    running(pro)
  File "<pyshell#195>", line 10, in running
    elif (operations.has_key(el)):
AttributeError: 'dict' object has no attribute 'has_key'
>>> d={1:2,3:4}
>>> d.has_key(1)
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    d.has_key(1)
AttributeError: 'dict' object has no attribute 'has_key'
>>> 1 in d
True
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			oopStack.append(int(el))
		elif (el in operations):
			operations[el]()
		else:
			lookDict(el)

			
>>> running(pro)
>>> dictStack
[{'fact': ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end']}, {'y': ['1']}]
>>> pro
['/y', '{', '1', '}', 'def']
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', '5', 'fact']
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    running(prog)
  File "<pyshell#201>", line 9, in running
    oopStack.append(int(el))
NameError: global name 'oopStack' is not defined
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			opStack.append(int(el))
		elif (el in operations):
			operations[el]()
		else:
			lookDict(el)

			
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    running(prog)
  File "<pyshell#208>", line 13, in running
    lookDict(el)
  File "<pyshell#178>", line 4, in lookDict
    if( dictStack[i].has_key(el)):
AttributeError: 'dict' object has no attribute 'has_key'
>>> def lookDict(name):
	i=len(dictStack)-1
	while(i>=0):
		if( el in dictStack[i]):
			running(dictStack[i][el])
			break

		
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#212>", line 1, in <module>
    running(prog)
  File "<pyshell#208>", line 13, in running
    lookDict(el)
  File "<pyshell#211>", line 4, in lookDict
    if( el in dictStack[i]):
NameError: global name 'el' is not defined
>>> def lookDict(name):
	i=len(dictStack)-1
	while(i>=0):
		if( name in dictStack[i]):
			running(dictStack[i][el])
			break

		
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#215>", line 1, in <module>
    running(prog)
  File "<pyshell#208>", line 13, in running
    lookDict(el)
  File "<pyshell#214>", line 5, in lookDict
    running(dictStack[i][el])
NameError: global name 'el' is not defined
>>> def lookDict(name):
	i=len(dictStack)-1
	while(i>=0):
		if( name in dictStack[i]):
			running(dictStack[i][name])
			break

		
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    running(prog)
  File "<pyshell#208>", line 13, in running
    lookDict(el)
  File "<pyshell#217>", line 5, in lookDict
    running(dictStack[i][name])
  File "<pyshell#208>", line 13, in running
    lookDict(el)
  File "<pyshell#217>", line 4, in lookDict
    if( name in dictStack[i]):
KeyboardInterrupt


>>> opStack
['fact', ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end'], 5, 'y', 'y', ['1'], 'y', ['1'], 'y', ['1'], 5, 5, 5, 5, 1]
>>> opStack.clear()
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    opStack.clear()
AttributeError: 'list' object has no attribute 'clear'
>>> opStack=[]
>>> dictStack=[]
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', '5', 'fact']
>>> prog=prog[:-2]
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def']
>>> running(prog)
>>> dictStack
[{'fact': ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end']}]
>>> opStack
[]
>>> prog=prog+['5','fact']
>>> running()
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    running()
TypeError: running() takes exactly 1 argument (0 given)
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', '5', 'fact']
>>> operations
{'def': <function deF at 0x02C21468>}
>>> def lookDict(name):
	i=len(dictStack)-1
	while(i>=0):
		if( name in dictStack[i]):
			running(dictStack[i][name])
			break
		i=i-1

		
>>> dictStack=[]
>>> running(prog)
>>> dictStack
[{'fact': ['1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end']}, {1: 'x'}]
>>> opStack
[5, 0, ['1'], ['x', '1', 'sub', 'fact', 'x', 'mul']]
>>> def running(l):
	l=helperFun(l)
	for el in l:
		if (el[0]=='/'):
			opStack.append(el[1:])
		elif (type(el)==list):
			opStack.append(el)
		elif (el.isdigit()==True):
			opStack.append(int(el))
		elif (el in operations):
			operations[el]()
		else:
			lookDict(el)

			
>>> 
def dict():
        arg=opStack.pop()
        newDict={}
        opStack.append(newDict)

        
>>> operations
{'def': <function deF at 0x02C21468>}
>>> operations.updata('dict':dict)
SyntaxError: invalid syntax
>>> operations.update({'dict':dict})
>>> operations
{'dict': <function dict at 0x02C16C90>, 'def': <function deF at 0x02C21468>}
>>> def deF():
        op1=opStack.pop()
        op2=opStack.pop()
        newDict={op2:op1}
        dictStack.append(newDict)
def exch():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1)
        opStack.append(op2)
def dup():
        op1=opStack.pop()
        opStack.append(op1)
        opStack.append(op1)
def pop():
        op1=opStack.pop()
        
SyntaxError: invalid syntax
>>> def deF():
        op1=opStack.pop()
        op2=opStack.pop()
        newDict={op2:op1}
        dictStack.append(newDict)
def exch():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1)
        opStack.append(op2)
def dup():
        op1=opStack.pop()
        opStack.append(op1)
        opStack.append(op1)
def pop():
        op1=opStack.pop()
        
SyntaxError: invalid syntax
>>> def dup():
        op1=opStack.pop()
        opStack.append(op1)
        opStack.append(op1)

        
>>> def exch():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1)
        opStack.append(op2)

        
>>> operations
{'dict': <function dict at 0x02C16C90>, 'def': <function deF at 0x02C21468>}
>>> def begin():
        arg=opStack.pop()
        dictStack.append(arg)


>>> def begin():
        arg=opStack.pop()
        dictStack.append(arg)

def end():
        dictStack.pop()
        
SyntaxError: invalid syntax
>>> def begin():
        arg=opStack.pop()
        dictStack.append(arg)

        
>>> def end():
        dictStack.pop()

        
>>> operations.update({'begin':begin)
		  
SyntaxError: invalid syntax
>>> operations.update({'begin':begin})
>>> prog
['/fact', '{', '1', 'dict', 'begin', '/x', 'exch', 'def', 'x', '0', 'eq', '{', '1', '}', '{', 'x', '1', 'sub', 'fact', 'x', 'mul', '}', 'ifelse', 'end', '}', 'def', '5', 'fact']
>>> operations.update({'exch':exch})
>>> def eq():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1==op2)

        
>>> operations.update({'eq':eq})
>>> def sub():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op2-op1)

        
>>> operations.update({'sub':sub})
>>> def mul():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1*op2)

        
>>> operations.update({'mul':mul})
>>> def ifelse():
	op1=opStack.pop()
        op2=opStack.pop()
        op3=opStack.pop()
        if (op1==True)
        
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def ifelse():
	op1=opStack.pop()
        op2=opStack.pop()
        op3=opStack.pop()
        if (op1==True):
		
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> def ifelse():
	op1=opStack.pop()
	op2=opStack.pop()
	op3=opStack.pop()
	if (op3==True):
		opStack.append(op2)
	else
	
SyntaxError: invalid syntax
>>> def ifelse():
	op1=opStack.pop()
	op2=opStack.pop()
	op3=opStack.pop()
	if (op3==True):
		opStack.append(op2)
	else:
		opStack.append(op1)

		
>>> operations.update({'ifelse':ifelse})
>>> running(prog)
Traceback (most recent call last):
  File "<pyshell#284>", line 1, in <module>
    running(prog)
  File "<pyshell#241>", line 13, in running
    lookDict(el)
  File "<pyshell#235>", line 5, in lookDict
    running(dictStack[i][name])
  File "<pyshell#241>", line 13, in running
    lookDict(el)
  File "<pyshell#235>", line 5, in lookDict
    running(dictStack[i][name])
  File "<pyshell#241>", line 2, in running
    l=helperFun(l)
  File "<pyshell#123>", line 7, in helperFun
    for el in prog:
TypeError: 'int' object is not iterable
>>> operations
{'begin': <function begin at 0x02C21738>, 'ifelse': <function ifelse at 0x02C21858>, 'dict': <function dict at 0x02C16C90>, 'def': <function deF at 0x02C21468>, 'mul': <function mul at 0x02C21810>, 'eq': <function eq at 0x02C21780>, 'exch': <function exch at 0x02C216A8>, 'sub': <function sub at 0x02C217C8>}
>>> 
>>> 
>>> 
>>> prog='''
3 4 add
'''
>>> opStack=[]
>>> dictStack=[]
>>> running(parse(prog))
>>> opStack
[3, 4]
>>> operations
{'begin': <function begin at 0x02C21738>, 'ifelse': <function ifelse at 0x02C21858>, 'dict': <function dict at 0x02C16C90>, 'def': <function deF at 0x02C21468>, 'mul': <function mul at 0x02C21810>, 'eq': <function eq at 0x02C21780>, 'exch': <function exch at 0x02C216A8>, 'sub': <function sub at 0x02C217C8>}
>>> 'add' in operations
False
>>> type(add)
Traceback (most recent call last):
  File "<pyshell#298>", line 1, in <module>
    type(add)
NameError: name 'add' is not defined
>>> def add():
        op1=opStack.pop()
        op2=opStack.pop()
        opStack.append(op1+op2)

        
>>> operations.update({'add':add})
>>> opStack=[]
>>> dictStack=[]
>>> runnning(parse(prog))
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    runnning(parse(prog))
NameError: name 'runnning' is not defined
>>> running(parse(prog))
>>> opStack
[7]
>>> dictStack
[]
>>> def stack():
        for element in opStack:
            print (element)

            
>>> stack()
7
>>> operations.update({'stack':stack})
>>> def clear():
	opStack=[]

	
>>> clear()
>>> running(parse('''
3 4 add 2 mul
'''))
>>> stack
<function stack at 0x02C218E8>
>>> stack()
7
14
>>> def stack()
SyntaxError: invalid syntax
>>> def stack():
	i=len(opStack)-1
	while (i>=0):
		print (opStack[i])

		
>>> stack()
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14

14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
14
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    stack()
  File "<pyshell#326>", line 4, in stack
    print (opStack[i])
KeyboardInterrupt
>>> def stack()
SyntaxError: invalid syntax
>>> def stack():
	i=len(opStack)-1
	while(i>=0)
	
SyntaxError: invalid syntax
>>> def stack():
	i=len(opStack)-1
	while(i>=0):
		print(opStack[i])
		i=i-1

		
>>> stack()
14
7
>>> 
