import os


dark_list = ['.git', '__pycache__', '.vscode', 'list_dir', '.mypy_cache']
def dark_list_modules(List:list):
    for i in List:
        if i in dark_list:
            List.remove(i)
    return List





def list_modules(dir_base, List: list = [], direc: str = None):
    temp_directory = dir_base
    print(List)
    temp: list = dark_list_modules(os.listdir(temp_directory))
    temp2: list = List
    for i in temp:
        print(i)
        if os.path.isdir(os.path.join(dir_base, i)):
            # temp.remove(i)
            list_modules(os.path.join(temp_directory,i), temp2, i)
        else:

            temp2.append(i)
        # print(os.path.join(temp_directory,i))
    return temp2
