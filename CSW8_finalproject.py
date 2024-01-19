from tasks import *

if __name__ == "__main__":
    the_menu = {
                'P' : 'Print tasks',
                'A' : 'Add a task',
                'U' : 'Update a task',
                'D' : 'Delete a task',
                'SI' : 'Show incomplete tasks',
                'SC' : 'Show completed tasks', 
                'SP' : 'Show tasks sorted by priority, highest first',
                'SD' : 'Show tasks sorted by due date, earliest first',
                'S' : 'Save tasks',
                'L' : 'Load tasks from file',
                'Q' : 'Quit this program'
                } #TODO: add the menu options from the instructions

    tasks = []
    opt = None

    while True:
        print_main_menu(the_menu) #TODO
        print("::: Enter an option")
        opt = input("Enter an option")
        opt = opt.upper()

        if opt == 'Q' or opt == 'q': #TODO: make Q or q quit the program
            print("See you next time!")
            break # exit the main `while` loop
        else:
            if check_option(opt, the_menu) == "invalid": #TODO
                print(f"WARNING: `{opt}` is an invalid option.\n")
                continue
        print("You selected option {} to {}.".format(opt, the_menu[opt]))

        if opt == 'P' or opt == 'p': #TODO
            print_formatted_tasks(tasks)
            
        elif opt == 'A' or opt == 'a': #TODO
            print("Enter the task information: ")
            name = input('name: ')
            description = input('description: ')
            date = input('date: ')
            priority = input('priority: ')
            completed = input('completed: ')
            a = create_a_task(name, description, date, priority, completed)
            tasks.append(a)
            print("Enter another task? Enter 'y' to continue.")
            user_option = input()
            if user_option != 'y':
                break                
            
        elif opt == 'U' or opt == 'u':
            print("Which task would you like to update?")
            print("Enter the number corresponding to the task.")
            task_id = int(input())
            if not task_id.isdigit():
                print(f"WARNING: `{task_id}` is an invalid task number!")
            else:
                print("Enter the task informations: ")
                task_field = input('task field: ')
                task_update = input('task update: ')
                update_task(tasks, task_id, task_field, task_update)
            
        elif opt == 'D' or opt == 'd':
            print("Which task would you like to delete?")
            print("Enter the number corresponding to the task.")
            task_id = int(input())
            if not task_id.isdigit():
                print(f"WARNING: `{task_id}` is an invalid task number!")
            else:
                delete_task(task_id, tasks)
            
        elif opt == 'SI' or opt == 'si':
            print_tasks_by_status(tasks, False)
            
        elif opt == 'SC' or opt == 'sc':
            print_tasks_by_status(tasks, True)
            
        elif opt == 'S' or opt == 's':
            save_to_csv(tasks, input())
            
        elif opt == 'L' or opt == 'l':
            b = input()
            if not b in filename:
                print(f'WARNING: Cannot find a CSV file named {b}')
            else:
                load_from_csv(b)
            
        else:
            print("This option is not yet implemented.") #TODO

        opt = input("::: Press Enter to continue...")

    print("Have a productive day!")
