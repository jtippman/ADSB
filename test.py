import os

os.system("wget -O - -q http://10.0.0.109:30003 | egrep --line-buffered 'MSG,1,|MSG,3,|MSG,5,' >> log_python.txt")
