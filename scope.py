def changeValue():
    try:
        aValue += 1
        print('What is the value of aValue inside the changeValue funtion?', aValue)
    except:
        print('aValue is not definded in this scope')


def changeValuePlus(aValue):
    try:
        aValue += 10
        print('What is the value of aValue inside the changeValue funtion?', aValue)
    except:
        print('aValue is not definded in this scope')

def changeValuePlus(aValue):
    try:
        aValue += 100
        print('What is the value of aValue inside the changeValue funtion?', aValue)
    except:
        print('aValue is not definded in this scope')
    
    return aValue

def changeValueArray(anArray):
    try:
        for i in range(len(anArray)):
        
            anArray[i] += 100
        print('What is the value of aValue inside the changeValueArray funtion?', anArray)
    except:
        print('Fubar')

##############TEXTBLOOKS#######################
###############################################        
def textBlockA(aValue):
    print('Lets talk about scope.\n \nTo start aValue = 1')
    print('What is the value of aValue?', aValue)
    input('Press enter to continue \n')
    print('#' * 30)
    print('def changeValue()\n   aValue += 1\n   print(aValue)\n\n')
    print('def main():\n   aValue = 1\n   changeValue()\n   print(aValue)\n\n')
    print('if __name__=="__main__":\n   main()\n')
    print('#' * 30)
    print('\nThe __name__=="__main__" thing. You could run the code with out it by just calling main() in the global.\nHowever its handy when making modules.')
    input('Press enter to continue\n')
    print('\nAnd with that the program falls over.\nSomthing about aValue not being defined\n')
    print('Adding a try catch block')
    input('Press enter to continue\n')
    print('#' * 30)
    print('\ndef changeValue():')
    print('   try:\n      aValue += 1\n      print(aValue)\n   excpet:\n      print("There is no aValue")\n')
    print('def main():\n   aValue = 1\n   changeValue()\n   print(aValue)\n\n')
    print('if __name__=="__main__":\n   main()\n')
    print('#' * 30)
def textBlockB(aValue):
    print('What is the value of aValue?', aValue)
    print('\nValues can be passed into a function in the form of arguments.\ndef function(argument).\n\nYeah.  Values are called arguments.\n Wait until methods come up.\nA function need defined with what arguments it takes.\nSo changrValue() change to changeValue(aValue)')
    print('There is something called overloading, but python does not support it.\nNew function name is needed. changeValuePlus(aValue)')
    print('next\n')
    input('Press enter to continue\n')
    print('#' * 30)
    print('\ndef changeValuePlus(aValue)')
    print('   try:\n      aValue += 10\n      print(aValue)\n   excpet:\n      print("There is no aValue")\n')
    print('def main():\n   aValue = 1\n   changeValuePlus()\n   print(aValue)\n\n')
    print('if __name__=="__main__":\n   main()\n')
    print('#' * 30)
    input('Press enter to continue\n')
def textBlockC(aValue):
    print('However the value in the main aValue is ', aValue)
    input('Press enter to continue\n')
    print('Now for a return. This give a funtion a value\n')
    input('Press enter to continue\n')
    print('#' * 30)
    print('\ndef changeValuePlusPlus(aValue)')
    print('   try:\n      aValue += 100\n      print(aValue)\n   excpet:\n      print("There is no aValue")\n   retuen aValue')
    print('def main():\n   aValue = 1\n   aValue = changeValuePlus(aValue)\n   print(aValue)\n\n')
    print('if __name__=="__main__":\n   main()\n')
    print('#' * 30)
    input('Press enter to continue\n')
def textBlockD(aValue):
    print('The value in the main is ', aValue)
    print('This may seen to be a little over the top.  There is a reason.\n\n')
    input('Press enter to continue\n')
    print('Function are a way of braking down a program in to smaller problems.\nDef somefunctions (args kwargs)\n   Do something\n   return oneThing\nSo while the above programs are pointless.\nUsing DnD.  Handing in dice roll, modifiers, and AC, in order to return a true or false, has a use\n')
    print('While a function can take multiple arguments.\nIt will only ever return one\nIf there a need for more there are pointers and references')
    print('Python dose not have pointer, but there are reference.\n')
    print('anArry = [0,1,2,3,4]')
    input('Press enter to continue\n')
    print('#' * 30)
    print('\ndef changeValueArray(anArray)')
    print('   try:\n      for i in anArray:\n         anArray[i] += 10     print(anArray)\n   excpet:\n      print("There is no aValue")\n   retuen aValue')
    print('def main():\n   anArray = [0,1,2,3,4]\n   bnArray = anArray\n   anArray = changeValueArray(anArray)\n   print(anArray)\n\n')
    print('if __name__=="__main__":\n   main()\n')
    print('#' * 30)
    input('Press enter to continue\n')
    print('please note bnArray = anArray')
    input('Press enter to continue\n')
########################################    
########################################
    
def main():
    aValue = 1
    anArray = [0,1,2,3,4]
    
    textBlockA(aValue)
    changeValue()
    textBlockB(aValue)
    changeValuePlus(aValue)
    textBlockC(aValue)
    aValue = changeValuePlus(aValue)
    textBlockD(aValue)
    bnArray = anArray
    changeValueArray(anArray)

    print('Nothing retuened but ', anArray)
    
    print('The value of anArray is a reference.\n  This is a space in memory where the array is stored.\n  Here be dragons')
    input('Press enter to continue\n')
    print('call changeValueArray(anArray) again')
    changeValueArray(anArray)
    
    print('And printing bnArray ', bnArray)
    print('Because bnArray is pointing at the reference made with anArray')
    
    
if __name__=='__main__':
    main()
