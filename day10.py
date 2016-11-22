#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/10

import sys

def look_say(line):
  combo = 1
  lns = ""
  prev_char=line[0]
  for x in line[1:]:
    #increment combo until you find a different char
    if x == prev_char:
      combo += 1
      continue
    #once the combo ends, add the char + value to a string, then reset to 0
    lns += str(combo)+prev_char
    combo = 1
    prev_char = x
  return lns+str(combo)+prev_char

def lns_40(filename):
  len_after_40 = 0
  loops = 0
  lns = ""
  #since the input has to be one line, read() must be used
  input = open(filename, 'rU').read()
  lns = look_say(input)
  while loops <= 48:
    lns = look_say(lns)
    loops += 1
  len_after_40 = len(str(lns))
  return len_after_40

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = lns_40(sys.argv[1])
  print "After 40 loops of Look And Say, the input is length: " + str(a)

if __name__ == '__main__':
  main()