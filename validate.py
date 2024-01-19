def print_main_menu(menu):
    print('**************************')
    print('What would you like to do?')
    for k,v in menu.items():
        print(f'{k} - {v}')
    print('**************************')
    

def check_option(option, menu):
    """
    check whether the option is in the menu or not
    """
    
    if option in menu:
        return 'valid'
    else:
        return 'invalid'


def is_valid_index(idx, in_list):
    """
    Checks whether the provided index `idx`
    is a valid positive index that can retrieve
    an element from `in_list`.
    Returns False if `idx` is negative or exceeds
    the size of `in_list` - 1.
    """
    if idx < 0 or idx > (len(in_list)-1):
        return False
    else:
        return True


def validate_name(name):
    '''
    validates the "name" parameter
    Returns True if the name is between 3 and 15 characters long, inclusive
    Returns False otherwise
    '''
    if 3 <= len(name) <= 15:
        return True
    else:
        return False


def validate_description(desc):
    '''
    validates the "desc" parameter
    Returns True if desc is a non-empty string
    Returns False otherwise
    '''
    if len(desc) != 0:
        return True
    else:
        return False


def validate_date(date_string):
    '''
    validate the "date_string"
    Returns True if date_string is a valid date string
    in slashes format (lab 8.16)
    Returns False otherwise
    '''
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    
    date = date_string.split('/')
    if len(date) != 3:
        return False
    if not date[0].isdigit() or not date[1].isdigit() or not date[2].isdigit():
        return False
    
    month = int(date_string[0:2])
    day = int(date_string[3:5])
    
    if month not in num_days:
        return False
    if day < 1 or day > num_days[month]:
        return False
    
    return True


def validate_priority(priority):
    '''
    validate the "priority" parameter
    Returns True if "priority" is a string containing a number 1-5
    Returns False otherwise
    '''
    if priority.isdigit():
        if 1 <= int(priority) <= 5:
            return True
     
    return False



def validate_completed(comp):
    '''
    validate the "comp" parameter.
    Returns True if s is one of: "yes", "no", "Yes", "No"
    Returns False otherwise
    '''
    a = ['yes', 'no', 'Yes', 'No']
    if comp in a:
        return True
    else:
        return False



def is_numeric(val):
    """
    Returns True if the string `val`
    contains a valid integer or a float.
    Returns False otherwise.
    """
    try:
      val = float(val)
      return True
    except ValueError:
      return False
    


