# Sample python collection of unittest concepts

def get_formatted_name(first,last):
    """receive name and generate neatly-formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()

print('q to quit.')
while True:
    first = input('\nWhat is your first name? ')
    if first == 'q':
        break
    last = input('\nWhat is your last name? ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)

    print('\n Your full name is ' + formatted_name + '.')