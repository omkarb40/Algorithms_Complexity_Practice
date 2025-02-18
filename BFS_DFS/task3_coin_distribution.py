def distribute_coins(total_amount: int, num_cashiers: int) -> dict:
    """
    Distributes coins among cashiers using a greedy approach to minimize total coins used.
    
    Args:
        total_amount: Total amount to distribute in cents
        num_cashiers: Number of cashiers to distribute among
    
    Returns:
        dict: Distribution of coins per cashier with coin counts
        
    Raises:
        ValueError: If inputs are invalid or amount can't be distributed equally
    """
    # Input validation
    if total_amount <= 0 or num_cashiers <= 0:
        raise ValueError("Total amount and number of cashiers must be positive")
    
    if total_amount % num_cashiers != 0:
        raise ValueError("Total amount must be evenly divisible by number of cashiers")
    
    # Available coin denominations in cents (largest to smallest)
    denominations = [50, 25, 10, 5, 1]
    
    # Calculate amount per cashier
    amount_per_cashier = total_amount // num_cashiers
    
    # Initialize result dictionary
    distribution = {d: 0 for d in denominations}
    remaining = amount_per_cashier
    
    # Greedy coin selection
    for denomination in denominations:
        if remaining >= denomination:
            num_coins = remaining // denomination
            distribution[denomination] = num_coins
            remaining = remaining % denomination
    
    return distribution

def print_distribution(distribution: dict) -> None:
    """
    Prints the coin distribution in a formatted manner.
    
    Args:
        distribution: Dictionary containing coin counts per denomination
    """
    total_coins = sum(distribution.values())
    print("\nCoin Distribution per Cashier:")
    print("-" * 40)
    for denomination, count in distribution.items():
        if count > 0:
            print(f"{count} coin(s) of {denomination} cents")
    print("-" * 40)
    print(f"Total coins per cashier: {total_coins}")

def main():
    """
    Main function to demonstrate the coin distribution algorithm.
    """
    try:
        
        total_amount = 1000  # $10.00 in cents
        num_cashiers = 4
        
        print(f"\nDistributing ${total_amount/100:.2f} among {num_cashiers} cashiers")
        
        distribution = distribute_coins(total_amount, num_cashiers)
        print_distribution(distribution)
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()