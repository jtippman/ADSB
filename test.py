import subprocess

logfile=open('log_python.txt','w')
ps = subprocess.Popen(('wget','-O','-','-q','http://10.0.0.109:30003'),stdout=subprocess.PIPE)
output=subprocess.Popen(('egrep','--line-buffered',"'|MSG,1,|MSG,3,|MSG,4,|'"),stdin=ps.stdout,stdout=subprocess.PIPE)

for line in output.stdout:
    logfile.write(line.decode('ascii'))

output.wait()

