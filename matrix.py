# Enter your code here. Read input from STDIN. Print output to STDOUT

class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

        
stdin=input()
lst=stdin.split(' ')
m,n=int(lst[0].strip()),int(lst[1].strip())
n,m=m,n
values=list()
for i in range(m*n):
    val=input()
    values.append(val.strip())
stk=Stack()
def postfixeval(rowvalues,counter):
    valuelist=rowvalues.split(' ')
    for char in valuelist:
              if char>='0' and char<='999':
                  stk.push(char)    
              elif ord(char[0])>=65 and ord(char[0])<=90:
                  j=(ord(char[0])-65)*n+(int(char[1])-1)
                  counter=counter+1
                  if counter>10:
                      print('Error:Cyclic Dependency!')
                      exit() 
                  stk.push(postfixeval(values[j],counter))    
              else:
                  if char=='+':
                      op2=stk.pop()
                      op1=stk.pop()
                      stk.push(str(round(float(op1)+float(op2),5)))
                  elif char=='-':
                      op2=stk.pop()
                      op1=stk.pop()
                      stk.push(str(round(float(op1)-float(op2),5)))
                  elif char=='*':
                      op2=stk.pop()
                      op1=stk.pop()
                      stk.push(str(round(float(op1)*float(op2),5)))
                  elif char=='/':
                      op2=stk.pop()
                      op1=stk.pop()
                      stk.push(str(round(float(op1)/float(op2),5)))
  
    result=stk.pop()
    return result
i=0
while i<len(values): 
    counter=0
    values[i]=postfixeval(values[i],counter)
    i=i+1
for value in values:
    print('{0:.5f}'.format(float(value)))


                               