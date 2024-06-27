import sys
import getopt
import json
import datetime
from pys import main

def create():
    #print("Hi")
    argv = sys.argv[1:] 

    #python main.py -m pyls
    if "-m" in argv and "-A" not in argv and  "-l" not in argv:
        main.first_function("st")

    #python main.py -m -A
    elif "-m" in argv and "-A" in argv:
        main.second_function()
    
    #python main.py -m -l
    elif "-m" in argv and "-l" in argv and "-r" not in argv and "-t" not in argv and "parser" not in argv and "parser/parser.go" not in argv:
        main.third_function()
    
    #python main.py -m -l -r
    elif "-m" in argv and "-l" in argv and "-r" in argv and "-t" not in argv and "parser" not in argv and "parser/parser.go" not in argv:
        main.four_function()

    #python main.py -m -l -r -t
    elif "-m" in argv and "-l" in argv and "-r" in argv and "-t" in argv and "parser" not in argv and "parser/parser.go" not in argv:
        main.five_function()
    
    #python main.py -m -l parser
    elif "-m" in argv and "-l" in argv and "parser" in argv and "-h" not in argv:
        main.parser_list() 
    
    #python main.py -m -l parser/parser.go
    elif "-m" in argv and "-l" in argv and "parser/parser.go" in argv:
        main.sub_parser_list() 
    
    #python main.py -m -l parser -h size in KB
    elif "-m" in argv and "-l" in argv and "parser" in argv and "-h" in argv:
        main.parser_size() 

if __name__ == '__main__':
    create()