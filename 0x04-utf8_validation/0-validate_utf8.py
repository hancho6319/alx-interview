def validUTF8(data):
    # Count of remaining bytes expected for the current UTF-8 character
    remaining = 0
    
    for num in data:
        # Check if the byte is the start of a new UTF-8 character
        if remaining == 0:
            # Determine the number of leading 1s in the byte
            mask = 1 << 7
            while mask & num:
                remaining += 1
                mask >>= 1
            
            # 1-byte characters
            if remaining == 0:
                continue
            
            # Invalid starting byte for multi-byte sequence
            if remaining == 1 or remaining > 4:
                return False
            
        else:
            # Check if the byte is a continuation byte
            if not (num >> 6 == 0b10):
                return False
            
        remaining -= 1
    
    # If we finish with no remaining bytes expected, it's valid
    return remaining == 0

