

if __name__ == '__main__':
    N = int(input())

    list_numbers = []
    for x in range(N):
        commands, *line = input().split()
        values = list(map(int, line))

        if commands == 'append':
            list_numbers.append(values[0])
            values = []

        elif commands == 'print':
            print(list_numbers)

        elif commands == 'insert':
            list_numbers.insert(values[0], values[-1])
            values = []

        elif commands == 'remove':
            list_numbers.remove(values[0])

        elif commands == 'sort':
            list_numbers.sort()
            values = []

        elif commands == 'pop':
            list_numbers.pop()
            values = []

        elif commands == 'reverse':
            list_numbers.reverse()   
            values = []     


'''
Consider a list (list = []). You can perform the following commands:

1. insert I E: Insert integer E at position I .
2. print: Print the list.
3. remove e: Delete the first occurrence of integer E .
4. append e: Insert integer E at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.

Initialize your list and read in the value of  followed by  lines of commands where each command 
will be of the  types listed above. Iterate through each command in order and perform the 
corresponding operation on your list.


---Sample Input 0---
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

---Sample Output 0---
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''
      

