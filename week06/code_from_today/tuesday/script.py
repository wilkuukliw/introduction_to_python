import sys

def msg():
    if sys.argv[1] == 'Claus':
        print(sys.argv[0], ' You are in!')        
    elif sys.argv[1] == 'Anna':
        print(sys.argv[1], 'you are not in')
    else:
        print('NOP NO NO ')
        function_that_does_not_existst()

msg()
    



