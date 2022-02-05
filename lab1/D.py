data = int(input())
z = input()

if(z=='k'):
    c = int(input())
    converted_data = data/1024 #convert kilobyte to bye
    print(f'%.{c}f' % converted_data)


if(z=='b'):
    converted_data = data*1024  #convert byte to kilobyte
    print(converted_data)