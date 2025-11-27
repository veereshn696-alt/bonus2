import sys
if len(sys.argv)!=3 :
  print("usage : python script.py <salary> <bonus>")
  exit(1)
script=sys.argv[0]
salary=float(sys.argv[1])
bonus=float(sys.argv[2])
print("salary is ",salary)
print("bonus is ",bonus)
total=(salary * bonus/100)+salary
print("total salary is is ",total)
