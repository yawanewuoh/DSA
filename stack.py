#Is not advisable to use list with stack
# use deque instead.
# Inserting in stack,we use append.

from collections import deque
class Stack:
    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container)==0

    def size(self):
        return len(self.container)

    # exercise 1
    #write a function to reverse a string
    #         --ALGORITHM--
    # i) at every iteration, pop the stack to store the last letter
    # ii) return the reverse_word at the end of the iteration.

def reverse_string(string):

  stack=Stack()
  for ch in string:
      stack.push(ch)

  reverse_list = ''
  while stack.size()!=0:
      print(reverse_list)
      reverse_list+=stack.pop()

  return reverse_list

# exercise 2
# Write a function to check if a parenthesis is balanced
#         --ALGORITHM--
# i) store the first occurrence of any pair in a stack
# ii) compare the other pair if it matches the one's in the stack accordingly

def is_match(ch1, ch2):
    match_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    return match_dict[ch1] == ch2


def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch == '[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch == ']':
            # tackling the occurrence of only a pair.eg--> a+b)}
            if stack.size()==0:
                return False
            # tackles mismatching eg--> {[(a+b})]
            if not is_match(ch,stack.pop()):
                return False
# after looping,the size of the stack should be 0.
    return stack.size()==0


if __name__ == '__main__':
    print(is_balanced("({[a+b]})"))


