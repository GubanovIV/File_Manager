from FileManager import *

command_dict = {'curdir':CurrentDirectory, 'newdir':CreatrDir, 'rmdir':RemoveDir, 'chdir':ChoseDirectory,
                'newfile':CreateFile, 'wrtfile':WriteFile, 'rdfile':ReadFile, 'rmfile':RemoveFile, 'cpfile':CopyFile,
                'mvfile':MoveFile, 'rnfile':RenameFile}
line = ''
while True:
    try:
        print(CurrentDirectory() + '$ ', end='')
        line = input()
        if line == '/exit':
            break
        command_list = line.split(' ')
        command_list = [i for i in command_list if i != '']
        lcm = len(command_list)
        if lcm == 1:
            command = command_list[0]
            command_dict[command]()
        elif lcm == 2:
            command = command_list[0]
            path1 = command_list[1]
            command_dict[command](path1)
        elif lcm == 3:
            command = command_list[0]
            path1 = command_list[1]
            path2 = command_list[2]
            command_dict[command](path1, path2)
        else:
            print('Command error')
    except KeyError:
        print('Command error')
    except TypeError:
        print('Parameter error')
    except FileNotFoundError:
        print('Path not exists')
