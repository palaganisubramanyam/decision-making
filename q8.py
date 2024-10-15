'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''

def find_min_capacity_lab():
    a = int(input("Enter the seating capacity of L1: "))
    b = int(input("Enter the seating capacity of L2: "))
    c = int(input("Enter the seating capacity of L3: "))
    allocated_lab = input("Enter the lab allocated for ACE training (L1, L2, L3): ").strip()
    lab_capacities = {
        'L1': a,
        'L2': b,
        'L3': c
    }
    if allocated_lab in lab_capacities:
        del lab_capacities[allocated_lab]
    min_lab = min(lab_capacities, key=lab_capacities.get)
    print(min_lab)
find_min_capacity_lab()
