# import sys
# print(sys.argv)#by this we can give arguments in terminal and those arguments will be printed in a form of list 
# python main2.py kanika bhupesh 3167  ->this is how we will pass agument using this sys library argv function
# as an o/p ['min.py','kanika','bhupesh','3167'] this list will be printed
# name=sys.argv[1] #we have passed index here ao the argument will be at index 1
# print('hello '+name)
# tyhere is another library which also gives user feedback if not using program correctly this is better than sys lib 
import argparse
parser=argparse.ArgumentParser(description='this prgrm prints the name of my dogs')#Creates a parser object which will read and understand the command-line inputs. description → just a text that explains what your program does (helpful when someone runs python file.py --help).
parser.add_argument('-c','--color',metavar='color',required=True,choices={'red','yellow','black','blue','pink'},help='the color to search for') #This defines a new argument the program expects.
#'-c' → short option (you can write -c red).'--color' → long option (you can write --color red).metavar='color' → just how the argument name will appear in the help message.required=True → means this argument must be provided, otherwise the program will show an error. help='the color to search for' → message shown in the help menu.
# This means the program expects you to give a color as input when running it.
args=parser.parse_args()#This line reads the actual arguments from the command line and stores them in a variable args. args behaves like an object, so you can access values like args.color.
print(args.color)#Finally, it prints the value of the color you entered in the terminal.
# now we can't run this prgrm without the argument
# we can also limit this argument option by using choices. we can add color names in this choices so that user can't write anything other than these options