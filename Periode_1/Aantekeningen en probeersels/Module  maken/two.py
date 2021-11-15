import one

print ('Top level in two.py')

one.func()

if __name__ == '__main__':
    print ('One.py is being run directly')
else:
    print ('One.py has been imported')

