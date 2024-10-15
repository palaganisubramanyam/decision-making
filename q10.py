'''
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''

def allocate_lab():
    x = int(input("Enter the seating capacity of L1: "))
    y = int(input("Enter the seating capacity of L2: "))
    z = int(input("Enter the seating capacity of L3: "))
    n = int(input("Enter the number of students: "))
    suitable_lab = None
    max_capacity_used = -1
    if x >= n:
        capacity_used = x - n
        if capacity_used > max_capacity_used:
            max_capacity_used = capacity_used
            suitable_lab = "L1"
    
    if y >= n:
        capacity_used = y - n
        if capacity_used > max_capacity_used:
            max_capacity_used = capacity_used
            suitable_lab = "L2"
    
    if z >= n:
        capacity_used = z - n
        if capacity_used > max_capacity_used:
            max_capacity_used = capacity_used
            suitable_lab = "L3"
    if suitable_lab:
        print(suitable_lab)
    else:
        print("No suitable lab available")
allocate_lab()
