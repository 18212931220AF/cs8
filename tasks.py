from validate import *

def print_main_menu(menu):
    """
    print the main menu
    """
    print("**************************")
    print("What would you like to do?")
    for k,v in menu.items():
        print(f'{k} - {v}')
    print("**************************")


def check_option(option, menu):
    """
    check the option whether in menu or not
    """

    if option in menu:
        return 'valid'
    else:
        return 'invalid'


def create_a_task(name, description, date, priority, completed):
    '''
    validate each parameter starting from "name" and until "completed"
    If one of them fails, return (False, <name of parameter>)
    ex. (False, "name") if "name" is not 3-15 characters long
    or (False, "completed") if completed is not a "yes" or "no"
    If all validations pass, return (True, <dictionary with fields name, description...>)
    '''
    d = {'name': name, 'description': description, 'deadline': date, 'priority': int(priority), 'completed': completed}

    if validate_name(name) == False:   
        return False, 'name'
    elif validate_description(description) == False: 
        return False, 'description'
    elif validate_date(date) == False:
        return False, 'deadline'
    elif validate_priority(priority) == False:
        return False, 'priority'
    elif validate_completed(completed) == False:
        return False, 'completed'
    else:
        if (completed == 'No') or (completed == 'no'):
            d['completed'] = False
        else:
            #d['completed'] == 'Yes' or d['completed'] == 'yes':
            d['completed'] = True
        
        return True, d


def slashes_to_written(date_list):
    """
    change the date into US format
    """
    
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = int(date_list[0])
    date = int(date_list[1])
    year = int(date_list[2])
    result = month_names[month] + ' ' + str(date) + ", " + str(year) 
    return result



def print_formatted_tasks(tasks_list):
    """
    takes in a list of dictionaries, each dictionary representing a task
    """

    # Finish the function definition
    months = {
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December'
        }
    priority = {1:"Lowest",
                2:"Low",
                3:"Medium",
                4:"High",
                5:"Highest"}
    complete = {True:'Yes', 'False':'No'}
   
    for i in range(len(tasks_list)):
        print(f"{i}:  {tasks_list[i]['name'].upper()}")
        print(f"    Description: {tasks_list[i]['description']}")
        print(f"    Priority: {priority[tasks_list[i]['priority']]}")
        d = tasks_list[i]['deadline'].split('/')
        print(f"    Deadline: {months[int(d[0])]} {int(d[1])}, {d[2]}")
        if tasks_list[i]['completed'] == True:
            print(f'    Completed: Yes')
        else:
            print(f'    Completed: No')
        print()



def print_tasks_by_status(all_tasks, completed=False):
    """
    Prints tasks from 'all_tasks',
    based on the value of 'completed' of each task.
    If there are no tasks that are incomplete,
    prints 'You do not have incomplete tasks.'
    If there are no tasks that are completed,
    prints 'You do not have completed tasks.'
    Otherwise, prints the requested tasks.
    """

    result2 = []
    for j in range(len(all_tasks)):
        result2.append(all_tasks[j]['completed'])
    if False not in result2 and completed == False:
        print('You do not have incomplete tasks.')
    elif True not in result2 and completed == True:
        print('You do not have completed tasks.')





def update_task(task_list, task_id, task_field, task_update):
    """ Given
    * the task list (`task_list`)
    * the task index that has been selected (`task_id`)
    * the field of the selected task (`task_field`)
    * the updated information (`task_update`)
    Validate the parameters to check for syntax and structure. 
    If all validations passed, return a tuple with a boolean True and 
    the updated task (a dictionary from the `task_list` at the provided `task_id`).
    Ff validations fail, return a tuple with a boolean False and 
    a string with the task_field that caused the error during validation.
    """

    fields = [
    'name',
    'description',
    'deadline',
    'priority',
    'completed'
            ] #you may use this to validate field_name
    
    if is_valid_index(int(task_id), task_list) == False:
        return False, 'idx'
        
    if not task_field in fields:
        return False, 'field'
        
    if task_field == 'name': # use the correct function call(s)
        if validate_name(task_update) == True :#validate update using the correct function call(s)
            task_list[int(task_id)][task_field] = task_update
            return True, task_list[int(task_id)]#TODO: return the necessary tuple
        else:
            return False, 'name'#TODO: update the task list accordingly
    elif task_field == 'description': 
        if validate_description(task_update) == True :
            task_list[int(task_id)][task_field] = task_update
            return True, task_list[int(task_id)]
        else:
            return False, 'description'
    elif task_field == 'deadline': 
        if validate_date(task_update) == True :
            task_list[int(task_id)][task_field] = task_update
            return True, task_list[int(task_id)]
        else:
            return False, 'deadline'
    elif task_field == 'priority': 
        if validate_priority(task_update) == True :
            task_list[int(task_id)][task_field] = task_update
            return True, task_list[int(task_id)]
        else:
            return False, 'priority'
    elif task_field == 'completed': 
        if validate_completed(task_update) == True:
            if (task_update == 'Yes') or (task_update == 'yes'):
                task_update = True
                
            elif task_update == 'No' or task_update == 'no':
                task_update = False
        else:
            return False, 'completed'
    task_list[int(task_id)][task_field] = task_update
    return (True, task_list[int(task_id)])



def delete_task(idx, tasks):
    """
    Checks if idx, which is an integer, is a valid index inside Tasks
    If not, returns False
    If a valid index, removes the element at index 'idx'
      from tasks, and returns True
    """
    
    if is_valid_index(idx,tasks) == True:
        tasks.remove(tasks[idx])
        return True
    else:
        return False



import csv

def save_to_csv(my_list, filename):
    """
    save the dictionary into CSV type
    """


    with open(filename, 'w', newline='') as csvfile:
        task_writer = csv.writer(csvfile)
        for current_dict in my_list:
             task_data=[current_dict['name'], 
                        current_dict['description'], 
                        current_dict['deadline'], 
                        current_dict['priority'], 
                        current_dict['completed']]
             task_writer.writerow(task_data)



def load_from_csv(filename):
    """
    reads data from a csv file and put that data into our list of tasks
    """
    
    new_list = [] # empty list to store the data from the csv file
    
    with open(filename, 'r') as f:
        reader_object = csv.reader(f) #TODO: initiate csv.reader object

        for values in reader_object:
            if len(values) == 5:#check if there are 5 items in the list 'values'
                if values[4] == 'False':
                    values[4] = 'no'
                elif values[4] == 'True':
                    values[4] = 'yes'
                result = create_a_task(values[0],values[1],values[2],values[3],values[4])
                if result[0] == True:
                    if values[4] == 'Yes' or values[4] == 'yes':
                        values[4] = True
                    else:
                        values[4] = False
                    result[1]['completed'] = values[4]
                    new_list += [result[1]]

                else:
                    print("WARNING: invalid data -", values)
                    return "invalid data"

            else: #if data formatting is inconsistent
                print("WARNING: invalid data -", values)
                print("WARNING: Data formatting is inconsistent with the task manager!")
                return "inconsistent format"

    return new_list

         
