
def print_main_menu(menu):
    print("**************************")
    print("What would you like to do?")
    for k,v in menu.items():
        print(f'{k} - {v}')
    print("**************************")
    
    
def check_option(option, menu):
    if option in menu:
        return 'valid'
    else:
        return 'invalid'

def is_numeric(val):
    try:
      val = float(val)
      return True
    except ValueError:
      return False
    

def create_category(info):
    
    info = info.split()
    if len(info) != 2:
        return -2
    elif is_numeric(info[1]) == False:
        return -1
    info[1] = float(info[1]) 
    return info

def print_categories(main_list):
    if len(main_list) == 0:
        print('There are no categories')
    else:
        for i in range(len(main_list)):
            print(f'{i+1}. {main_list[i][0]} - {main_list[i][1]}%')
    return len(main_list)
    

def is_valid_index(idx, in_list):
    if idx < 0 or idx > (len(in_list)-1):
        return False
    else:
        return True
    

def update_category(info_str, idx, main_list):
    if is_valid_index(idx, main_list) == False:
        return -3
    return create_category(info_str)


def create_grade_list(grade_info):
    if len(grade_info) == 0:
        return []
    grade = grade_info.split(" ")
    for i in range(len(grade)):
        if is_numeric(grade[i]) == False:
            return -1
        else:
            grade[i] = float(grade[i])
    if len(grade) == 0:
        grade = []
    return grade


def sum_grades(all_categories):
    avg_sum = 0
    for category in all_categories:  
        category_grade = 0
        if len(category) == 2 or category[2] == []:
            avg_sum += category_grade
        else:
            category_grade = (sum(category[2]) / len(category[2])) * category[1] / 100  
            avg_sum += category_grade
    return avg_sum
    
    
    


if __name__ == "__main__":
    the_menu = {'P' : 'Print categories',
                'A' : 'Add a category',
                'U' : 'Update a category',
                'G' : 'Add grades',
                'C' : 'Compute the grade',
                'Q' : 'Quit this program',
                } 
    all_categories = [] # store the records for each individual category (the list of lists)

    opt = None

    while True:
        print_main_menu(the_menu)
        opt = input("Enter an option")

        if opt == 'Q' or opt == 'q': 
            print("Goodbye!")
            break 
        elif check_option(opt, the_menu) == "invalid": 
            print(f"WARNING: `{opt}` is an invalid option.\n")
            continue
        print(f"You selected option `{opt}` to {the_menu[opt]}.")

        if opt == 'P': 
            print_categories(all_categories)
        elif opt == 'A': 
            while True:
                print("Enter the category name and percentage: ")
                cat_info = input()
                cat_list = create_category(cat_info)
                if type(cat_list) == list:
                    all_categories.append(cat_list)
                else: 
                    print("WARNING: invalid category information!")
                    print(f"Category information `{cat_info}` was not added.")
                print("Enter another category? Enter 'y' to continue.")
                user_option = input()
                if user_option != 'y':
                    break
        elif opt == 'U':
            print_categories(all_categories)
            print("Which category would you like to update?")
            print("Enter the number corresponding to the category.")
            user_option = input()
            if not user_option.isdigit():
                print(f"WARNING: `{user_option}` is an invalid category number!")
            else:
                idx = int(user_option) - 1
                if not is_valid_index(idx, all_categories):
                    print(f"WARNING: `{user_option}` is an invalid category number!")
                else:
                    print(f"Updating category {all_categories[idx][0]}")
                    print("Enter the category name and percentage: ")
                    cat_info = input()
                    cat_list = update_category(cat_info, idx, all_categories)
                    if type(cat_list) == list:
                        all_categories[idx] = cat_list
                    else:
                        print("WARNING: invalid category information!")
                        print(f"Category information `{cat_info}` was not added.")
        elif opt == 'G': 
            print_categories(all_categories)
            print("To which category would you like to add grades?")
            print("Enter the number corresponding to the category.")
            user_option = input()
            if not user_option.isdigit():
                print(f"WARNING: `{user_option}` is an invalid category number!")
            else:
                idx = int(user_option) - 1
                if not is_valid_index(idx, all_categories):
                    print(f"WARNING: `{user_option}` is an invalid category number!")
                else:
                    print(f"Adding grades to category {all_categories[idx][0]}")
                    print("Enter the numeric grades separated by spaces: ")
                    grade_info = input()
                    grade_list = create_grade_list(grade_info)
                    if type(grade_list) == list:
                        if len(all_categories[idx]) == 2:
                            print("Adding new grades")
                            all_categories[idx].append(grade_list)
                        else:
                            print("Updating the grades")
                            all_categories[idx][2] += grade_list
                        print("-" * 45)
                        print("Category:", all_categories[idx][0])
                        print("Grades:", grade_list) 
                        print("-" * 45)
                    else:
                        print("WARNING: invalid grade information!")
                        print(f"The grade data `{grade_info}` was not added.")
        elif opt == 'C': 
            avg_grade = sum_grades(all_categories)  
            print(f"Average Grade is: {avg_grade}")


        else:
            print("This option is not yet implemented.") # TODO: implement the rest of the options

    print("See you next time!")
