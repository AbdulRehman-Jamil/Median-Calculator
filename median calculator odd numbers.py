print('''              Median calculator 
     (Only works on an odd amount of 1 digit numbers )              
     ''')

numbers=input('Enlist all numbers with commas between every number: ')
count=int(len(numbers))
commas=int((count-1)/2)
inputtednumbers=count-commas
medianindex=int(((inputtednumbers-1)/2)+1)
medianindexcommas=medianindex-1
medianindexreal=int((medianindex+medianindexcommas)-1)
print('The median of the set of numbers is '+numbers[medianindexreal])


