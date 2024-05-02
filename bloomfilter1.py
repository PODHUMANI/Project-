def hash1(num):
    return num % 1024

def hash2(num):
    return int(str(num)[::-1]) % 1024

def hash3(num):
    return sum(int(digit) for digit in str(num)) % 1024

def hash4(num):
    return 2*num % 1024

def add_card_number(bloom_bits, card_number):
    bloom_bits[hash1(card_number)] = 1
    bloom_bits[hash2(card_number)] = 1
    bloom_bits[hash3(card_number)] = 1
    bloom_bits[hash4(card_number)] = 1

    return bloom_bits

def is_valid(bits, card_number):   
    if bits[hash1(card_number)] == 0:
        return False
    if bits[hash2(card_number)] == 0:
        return False
    if bits[hash3(card_number)] == 0:
        return False
    if bits[hash4(card_number)] == 0:
        return False
    
    return True

# Example usage:
card_number1 = 1234567890123456
card_number2 = 1234567890123457

bloom_bits = [0]*1024

bloom_bits = add_card_number(bloom_bits, card_number1)
bloom_bits = add_card_number(bloom_bits, card_number2)

print(is_valid(bloom_bits, 1234567890123456)) # True
print(is_valid(bloom_bits, 1234567890123457)) # True

print(is_valid(bloom_bits, 1234567890123458)) # False
print(bloom_bits)
