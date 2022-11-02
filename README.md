# File_Manager
Принимают на вход только path:/n
  'curdir':CurrentDirectory - выбрать текущую директорию
  'newdir':CreatrDir - создать директорию
  'rmdir':RemoveDir - удалить директорию
  'chdir':ChoseDirectory - выбрать директорию, если вместо пути указать 'up', то вернётся в верхнюю директорию
  'newfile':CreateFile - создать файл
  'wrtfile':WriteFile - запись в файл(запись происходит, пока не введёшь строку /end)
  'rdfile':ReadFile - прочитать файл
  'rmfile':RemoveFile - удалить файл
Принимают на вход path и второй параметр:  
  'cpfile':CopyFile - скопировать файл в директорию(path, copy_path)
  'mvfile':MoveFile - переместить файл в директорию(path, move_path)
  'rnfile':RenameFile - переименовать файл(path, new_name)
