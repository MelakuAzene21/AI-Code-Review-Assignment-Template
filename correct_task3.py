def average_valid_measurements(values):
    if not isinstance(values, list):
        return 0.0
        
    total = 0.0
    valid_count = 0
    
    for v in values:
        if v is None:
            continue
            
        try:
            # Try to convert to float, skip if conversion fails
            num = float(v)
            total += num
            valid_count += 1
        except (ValueError, TypeError):
            # Skip invalid numeric values
            continue
    
    # Return 0.0 if no valid measurements
    return total / valid_count if valid_count > 0 else 0.0
