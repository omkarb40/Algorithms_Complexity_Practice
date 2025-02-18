# Coin Distribution Algorithm Implementation

### Overview
This program implements a greedy algorithm to distribute coins among multiple cashiers while minimizing the total number of coins used. The implementation ensures equal distribution of a total amount among cashiers using standard U.S. coin denominations (1, 5, 10, 25, 50 cents).

### Requirements
- Python 3.6 or higher

### File Structure
task3_coin_distribution/
│
├── task3_coin_distribution.py    # Main implementation file
└── README.md                     # This file

### How to Run the program
1. Navigate to the directory containing the script:
cd BFS_DFS_Greedy_Algorithms\task3_coin_distribution.py
2. Run the program
python task3_coin_distribution.py

### Testing the Implementation
total_amount = 1000 #cents
num_cashiers = 4
1. Test Case 1: Simple distribution

#Each cashier should receive $2.50 (250 cents)

result = distribute_coins(1000, 4)
print_distribution(result)

#Expected Output:
#Coin Distribution per cashier:
#5 coin(s) of 50 cents
#Total coins per cashier: 5

2. Test Case 2: Larger amount with mixed denominations

#Each cashier should receive $52.25 (5225 cents)

total_amount = 15675  # cents
num_cashiers = 3
result = distribute_coins(15675, 3)
print_distribution(result)

#Expected Output:
#Coin Distribution per cashier:
#104 coin(s) of 50 cents
#1 coin(s) of 25 cents
#Total coins per cashier: 105


3. Test Case 3: Small amount

#Each cashier should receive $0.25 (25 cents)

result = distribute_coins(125, 5)
print_distribution(result)

#Expected Output:
#Coin Distribution per cashier:
#1 coin(s) of 25 cents
#Total coins per cashier: 1

4. Test Case 4: Testing error handling - Indivisible amount

#This should raise a ValueError as 1000 cents cannot be evenly divided among 3 cashiers

try:
    result = distribute_coins(1000, 3)
    print_distribution(result)
except ValueError as e:
    print(f"Error: {e}")

#Expected Output:
#Error: Total amount must be evenly divisible by number of cashiers

5. Test Case 5: Testing error handling - Negative amount

#This should raise a ValueError as amount cannot be negative

try:
    result = distribute_coins(-5000, 2)
    print_distribution(result)
except ValueError as e:
    print(f"Error: {e}")

#Expected Output:
#Error: Total amount and number of cashiers must be positive

6. Test Case 6: Complex distribution using all denominations

#Each cashier should receive $5.97 (597 cents)

result = distribute_coins(1791, 3)
print_distribution(result)

#Expected Output:
#Coin Distribution per cashier:
#11 coin(s) of 50 cents
#1 coin(s) of 25 cents
#2 coin(s) of 10 cents
#0 coin(s) of 5 cents
#2 coin(s) of 1 cent
#Total coins per cashier: 16