from grades_system import check_option
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


from grades_system import is_numeric
result = is_numeric('123')
print(f"--> is_numeric('123') returned `{result}`")
assert result == True

result = is_numeric('abc')
print(f"--> is_numeric('abc') returned `{result}`")
assert result == False

result = is_numeric('5.5')
print(f"--> is_numeric('5.5') returned `{result}`")
assert result == True

result = is_numeric('5.5.')
print(f"--> is_numeric('5.5.') returned `{result}`")
assert result == False


from grades_system import create_category
assert create_category("Quizzes") == -2 
assert create_category("Quizzes 25.5 ignorethis") == -2
assert create_category("Quizzes A") == -1
assert create_category("Quizzes 25.5") == ["Quizzes", 25.5]


from grades_system import print_categories
assert print_categories([]) == 0
print()
assert print_categories([["Quizzes", 25.5]]) == 1
print()
assert print_categories([['Exam1', 20.0], ['Exam2', 25.0]]) == 2


from grades_system import is_valid_index
assert is_valid_index(0, [["Quizzes", 25.5]]) == True
assert is_valid_index(1, [["Quizzes", 25.5]]) == False
assert is_valid_index(-1, [["Quizzes", 25.5]]) == False
assert is_valid_index(1, [["Quizzes", 25.5], ["Project", 20]]) == True


from grades_system import update_category
assert update_category("invalid category", -1, []) == -3
assert update_category("invalid category", 1, []) == -3
result = update_category("Reflection 5", 0, [["RA", 2.0]])
expected = ["Reflection", 5.0]
print(f'update_category("Reflection 5", 0, [["RA", 2.0]]) \n returned {result} \n expected result is {expected}')
assert result == expected


from grades_system import create_grade_list
result = create_grade_list("90 99 98")
print(f"--> create_grade_list('90 99 98') returned `{result}`\n")
assert result == [90.0, 99.0, 98.0]

result = create_grade_list("100 A A- B")
print(f"--> create_grade_list('100 A A- B') returned `{result}`\n")
assert result == -1

result = create_grade_list("")
print(f"--> create_grade_list(\"\") returned `{result}`\n")
assert result == []

result = create_grade_list("95.0 90 60")
print(f"--> create_grade_list('95.0 90 60') returned `{result}`\n")
assert result == [95.0, 90.0, 60.0]


from grades_system import sum_grades
all_categories = [
    ["PA", 5, [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]],
    ["CA", 15, [100.0, 100.0, 98.0, 95.0, 0.0, 100.0]],
    ["LA", 25, [100.0, 100.0, 100.0, 5.0, 0.0, 70.0]],
    ["Quiz", 25, []],
    ["Project", 25, []]
]
assert sum_grades(all_categories) == 32.20

all_categories = []
assert sum_grades(all_categories) == 0.00

all_categories = [["PA", 5, [100.0, 100.0, 100.0, 100.0, 100.0, 0.0, 95.0]]]
assert sum_grades(all_categories) == 4.25
