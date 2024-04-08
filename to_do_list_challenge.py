""" Challenge to create a program that can modify a text file such that the user can 1) add a task, 2) delete a task, or 3) look at all tasks. Each task has a unique id generated. 
Note that for the program to execute, we need to import this code and then create the ToDoList class.

Sample:
x = ToDoList()
x.program_loop()

"""

import uuid
 
class ToDoList:
    def __init__(self):
        self.savefile = 'task_list.txt'
        # Initialize savefile
        sf = open(self.savefile, 'a+')
        sf.close()
        
    def print_main_menu(self):
        print('== TO DO LIST ==')
        print('[1] Show tasks')
        print('[2] Add task')
        print('[3] Complete task')
        print('[4] Exit')
        
    def read_from_savefile(self):
        with open(self.savefile, 'r+') as fs:     # Short for 'filestream'
            if fs.read(100) == '':                # Check first few characters                   
                print('Empty list\n')
                return
            fs.seek(0)                            # Reset reading
            lines = fs.readlines()
            for line in lines:
                task_array = line.split('|')
                id, task, deadline = task_array[0], task_array[1], task_array[2]
                print(f"{id} | {task} | {deadline}")
    
    def clear_file(self):
        with open(self.savefile, 'w') as fs:
            pass
        
    def create_unique_id(self):
        return str(uuid.uuid4())
    
    def get_user_task_details(self):
        try:
            task_input = input('What is the task? ')
            deadline_input = input('What is the deadline? ')
        except Exception as e:
            print('An exception occurred: ', e.errno)
        task_tuple = task_input, deadline_input
        return task_tuple
    
    def write_task_to_file(self, task_detail_tuple, task_id):
        ''' Check all task ids, one line at a time '''
        with open(self.savefile, 'r+') as fs:
            current_line = fs.readline()
            while current_line != '':
                stop_index = current_line.index('|')
                line_id = current_line[:stop_index]
                if task_id == line_id:
                    print(f'{task_id} - Task already in place')
                    return
                current_line = fs.readline()
        ''' If this is indeed a new task id, we add the entry '''
        task, deadline = task_detail_tuple
        with open(self.savefile, 'a+') as fs:
            fs.write(f"{task_id}|{task}|{deadline}\n")
            print(f"{task_id}|{task}|{deadline} - Successfully added\n")
    
    def remove_task(self, task_id):
        # Create a temporary savefile
        temp_file = 'temp_savefile.txt'
        
        # Read from savefile, write to temp_savefile, without the specific task
        with open(self.savefile, 'r+') as fs_one, open(temp_file, 'w') as fs_two:
            current_line = fs_one.readline()
            while current_line != '':
                line_id = current_line.split('|')[0]
                if line_id != task_id:
                    fs_two.write(current_line)
                current_line = fs_one.readline()
                    
        # Copy all items from temp_savefile back to savefile
        with open(self.savefile, 'w+') as fs_one, open(temp_file, 'r+') as fs_two:
            fs_one.write(fs_two.read())
            
        print(f"Done removing {task_id}!")
        
    def show_tasks_selected(self):
        try:
            print('\n[YOUR TASKS]')
            self.read_from_savefile()
        except Exception as e:
            print('An error occurred:', e)
            
    def add_task_selected(self):
        try:
            print('\n[ADD TASK]')
            task_details = self.get_user_task_details()
            new_id = self.create_unique_id()
            self.write_task_to_file(task_details, new_id)
        except Exception as e:
            print('An error occurred:', e)
            
    def complete_task_selected(self):
        try:
            self.show_tasks_selected()
            get_user_id = input('Enter id to complete: ')
            self.remove_task(get_user_id)
            self.show_tasks_selected()
        except Exception as e:
            print('An error occurred:', e)
    
    def program_loop(self):
        try:
            while True:
                self.print_main_menu()
                user_input = int(input('Your choice: '))
                if user_input == 4:
                    print('Bye!')
                    return
                function_dictionary = {
                        1: self.show_tasks_selected,
                        2: self.add_task_selected,
                        3: self.complete_task_selected,
                    }
                if user_input not in function_dictionary:
                    print('Invalid input, please try again')
                else:
                    function_dictionary[user_input]()
        except Exception as e:
            print('An error occurred:', e)
