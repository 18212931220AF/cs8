from tasks import *

my_menu0 = {}
my_menu1 = {1: "One"}
my_menu2 = {'L': "List"}

result = check_option(1, my_menu0)
print(f"--> check_option(1, my_menu0) returned `{result}`\n")
assert result == "invalid"

result = check_option(1, my_menu1)
print(f"--> check_option(1, my_menu1) returned `{result}`\n")
assert result == "valid"

result = check_option('1', my_menu1)
print(f"--> check_option('1', my_menu1) returned `{result}`\n")
assert result == "invalid"

result = check_option('1', my_menu2)
print(f"--> check_option('1', my_menu2) returned `{result}`\n")
assert result == "invalid"

result = check_option('L', my_menu2)
print(f"--> check_option('L', my_menu2) returned `{result}`\n")
assert result == "valid"


assert is_valid_index(0, [["Quizzes", 25.5]]) == True
assert is_valid_index(1, [["Quizzes", 25.5]]) == False
assert is_valid_index(-1, [["Quizzes", 25.5]]) == False
assert is_valid_index(1, [["Quizzes", 25.5], ["Project", 20]]) == True


assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[0] == True
assert type(create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]) == dict
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['name'] == 'do dishes'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['description'] == 'wash the plates from dinner'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['deadline'] == '03/04/2022'
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['priority'] == 2
assert create_a_task('do dishes', 'wash the plates from dinner', '03/04/2022', '2', 'no')[1]['completed'] == False

assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[0] == True
assert type(create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]) == dict
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['name'] == 'see endgame'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['description'] == 'endgame with friends saturday'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['deadline'] == '01/18/2020'
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['priority'] == 3
assert create_a_task('see endgame', 'endgame with friends saturday', '01/18/2020', '3', 'yes')[1]['completed'] == True



assert slashes_to_written(["01", "02", "2022"]) == 'January 2, 2022'
assert slashes_to_written(["01", "12", "1970"]) == 'January 12, 1970'
assert slashes_to_written(["04", "14", "2020"]) == 'April 14, 2020'
assert slashes_to_written(["06", "19", "2000"]) == 'June 19, 2000'



tasks = [{
        'name': 'get groceries',
        'description': 'buy some jam and peanut butter',
        'deadline': '02/23/2022',
        'priority': 2,
        'completed': False
        },
        {
        'name': 'get some sleep',
        'description': '8 hours of sleep is necessary',
        'deadline': '02/03/2022',
        'priority': 3,
        'completed': True
        },
        {
        'name': 'compar. lit essay',
        'description': "finish comparative lit essay that's overdue",
        'deadline': '02/15/2022',
        'priority': 4,
        'completed': True
        }]

result = update_task(tasks, '5', 'name', 'go clubbing')
assert result[1] == "idx"
assert result[0] == False
print(f"--> update_task(my_list, '5', 'name', 'go clubbing') "+
          f"successfully returned error with `{result[1]}`\n")
    
result = update_task(tasks, '1', 'Get Gift', 'I\'m quite hungry though')
assert result[1] == "field"
assert result[0] == False
print(f"--> update_task(my_list, '1', 'Get Gift', 'I\'m quite hungry though') "+
          f"successfully returned error with `{result[1]}`\n")

result = update_task(tasks, '1', 'deadline', 'never')
assert result[1] == "deadline"
assert result[0] == False
print(f"--> update_task(my_list, '1', 'deadline', 'never') "+
          f"successfully returned error with `{result[1]}`\n")
    
result = update_task(tasks, '1', 'priority', 'pants on FIRE!!!!')
assert result[1] == "priority"
assert result[0] == False
print(f"--> update_task(my_list, '1', 'priority', 'pants on FIRE!!!!') "+
          f"successfully returned error with `{result[1]}`\n")
    
result = update_task(tasks, '1', 'completed', 'technically, yes')
assert result[1] == "completed"
assert result[0] == False
print(f"--> update_task(my_list, '1', 'completed', 'technically, yes') "+
          f"successfully returned error with `{result[1]}`\n")
    





