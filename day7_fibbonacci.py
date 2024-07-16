def fibonacci_series(n):
    """
    Generate a Fibonacci series up to the n-th term.

    Parameters:
    n (int): The number of terms in the Fibonacci series to generate.

    Returns:
    list: A list containing the Fibonacci series.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    series = [0, 1]
    while len(series) < n:
        series.append(series[-1] + series[-2])
    
    return series

# Example usage
n = 10
print(f"Fibonacci series up to {n} terms:")
print(fibonacci_series(n))
