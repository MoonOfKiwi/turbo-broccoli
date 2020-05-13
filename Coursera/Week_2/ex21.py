previous_number = int(input())
current_length = 1
max_length = 1
while previous_number != 0:
    current_number = int(input())
    if previous_number == current_number:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
        previous_number = current_number
        current_length = 1
print(max_length)
