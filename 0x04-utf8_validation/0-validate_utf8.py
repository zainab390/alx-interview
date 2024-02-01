#!/usr/bin/python3
"""UTF-8 validation module.
"""
def validUTF8(data):
    # Helper function to check if a byte is a valid continuation byte
    def is_continuation_byte(byte):
        return (byte & 0b11000000) == 0b10000000
    
    # Iterate through the data
    i = 0
    while i < len(data):
        # Count the number of bytes for the current character
        num_bytes = 0
        leading_bits = data[i] & 0b11111111
        
        # Determine the number of bytes in the current character
        while leading_bits & (0b10000000 >> num_bytes):
            num_bytes += 1
        
        # Check if the number of bytes is valid
        if num_bytes == 1 or num_bytes > 4:
            return False
        
        # Check if the subsequent bytes are valid continuation bytes
        for j in range(1, num_bytes):
            if i + j >= len(data) or not is_continuation_byte(data[i + j]):
                return False
        
        # Move to the next character
        i += num_bytes
    
    return True

