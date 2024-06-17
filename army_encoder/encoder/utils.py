def encode_message(message, day_type='odd'):
    odd_day_map = {chr(i + 65): f"{i + 1:02d}" for i in range(26)}
    even_day_map = {chr(i + 65): f"{i + 501}" for i in range(26)}

    if day_type == 'odd':
        code_map = odd_day_map
    else:
        code_map = even_day_map

    encoded_message = ''.join(code_map[char] for char in message.upper() if char.isalpha())
    return encoded_message
