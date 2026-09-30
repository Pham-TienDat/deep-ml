def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    Max = max(x)
    Min = min(x)
    if(Max==Min):
        for i in range(len(x)):
            x[i] = 0
    else:
        for i in range(len(x)):
            x[i] = (x[i]-Min)/(Max-Min)
    return x