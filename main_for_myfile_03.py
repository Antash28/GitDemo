f = open('myfile03.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3']
f.writelines(lines)
f.close()