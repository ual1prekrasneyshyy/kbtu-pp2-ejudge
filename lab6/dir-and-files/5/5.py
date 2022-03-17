li = list(
    ('18',
     '2003',
     'Uali',
     'Amangaliyev',
     'KBTU',
     'Spring Semester',
     'Faculty of information technologies'
     )
)

f = open('output.txt', 'w')

for s in li:
    f.write(s+'\n')
