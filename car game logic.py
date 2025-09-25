print('1.start')
print('2.stop')
print('3.exit')
state='stop'
while True:
    ch=int(input('choose one option:'))
    if ch==1:
        if state=='started':
            print('the car is already started')
        else:
            print('the car is stared succesfully')
            state='started'
    elif ch==2:
        if state=='stopped':
            print('the car is already stopped')
        else:
            print('the car is stopped succesfully')
            state='stopped'
    elif ch==3:
        print('exit')
        break
    else:
        print('choose corect option:')
    
