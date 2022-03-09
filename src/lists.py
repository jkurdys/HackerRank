'''
Lists

Consider a list (list = []).
You can perform the following commands:
insert i e: Insert integer at position.
print: Print the list.
remove e: Delete the first occurrence of integer.
append e: Insert integer at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n
followed by n lines of commands where each command
will be of the types listed above. Iterate through
each command in order and perform the corresponding
operation on your list. 
'''

import sys

if __name__ == '__main__':
    N = int(input())

    output = []

    for i in map(str.rstrip, sys.stdin):
        txt = i.split()

        func = txt[0]

        if func == 'print':
            print(output)
        else:
            if len(txt) == 3:
                eval('output.' + func + '(' + txt[1] + ',' + txt[2] + ')')
            elif len(txt) == 2:
                eval('output.' + func + '(' + txt[1] + ')')
            else:
                eval('output.' + func + '()')