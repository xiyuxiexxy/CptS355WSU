#!/usr/bin/python3
import re
import sys

# Sept 21, 2011 -- fixed the handling of }{ -- each brace should be a separate token
# A regular expression that matches postscript each different kind of postscript token
pattern = '/?[a-zA-Z][a-zA-Z0-9_]*|[-]?[0-9]+|[}{]|%.*|[^\t\n ]'


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
'''

# Given a string, return the tokens it contains
def parse(s):
   tokens = re.findall(pattern, s)
   return tokens

# Given an open file, return the tokens it contains
def parseFile(f):
   tokens = parse(''.join(f.readlines()))
   return tokens

# Command line use: pass the filename as the first command-line argument
# if __name__ == "__main__":
#   fn = sys.argv[1]
#   print (parseFile(open(fn,"r")))


