import sys
import getopt
import json
from datetime import datetime

argv = sys.argv[1:] 
    #print(argv)
file_path = "schema.json"


jsonFile = '{"name":"interpreter","size":4096,"time_modified":1699957865,"permissions":"-rw-r--r--","contents":[{"name":".gitignore","size":8911,"time_modified":1699941437,"permissions":"drwxr-xr-x"},{"name":"LICENSE","size":1071,"time_modified":1699941437,"permissions":"drwxr-xr-x"},{"name":"README.md","size":83,"time_modified":1699941437,"permissions":"drwxr-xr-x"},{"name":"ast","size":4096,"time_modified":1699957739,"permissions":"-rw-r--r--","contents":[{"name":"go.mod","size":225,"time_modified":1699957780,"permissions":"-rw-r--r--"},{"name":"ast.go","size":837,"time_modified":1699957719,"permissions":"drwxr-xr-x"}]},{"name":"go.mod","size":60,"time_modified":1699950073,"permissions":"drwxr-xr-x"},{"name":"lexer","size":4096,"time_modified":1699955487,"permissions":"drwxr-xr-x","contents":[{"name":"lexer_test.go","size":1729,"time_modified":1699955126,"permissions":"drwxr-xr-x"},{"name":"go.mod","size":227,"time_modified":1699944819,"permissions":"-rw-r--r--"},{"name":"lexer.go","size":2886,"time_modified":1699955487,"permissions":"drwxr-xr-x"}]},{"name":"main.go","size":74,"time_modified":1699950453,"permissions":"-rw-r--r--"},{"name":"parser","size":4096,"time_modified":1700205662,"permissions":"drwxr-xr-x","contents":[{"name":"parser_test.go","size":1342,"time_modified":1700205662,"permissions":"drwxr-xr-x"},{"name":"parser.go","size":1622,"time_modified":1700202950,"permissions":"-rw-r--r--"},{"name":"go.mod","size":533,"time_modified":1699958000,"permissions":"drwxr-xr-x"}]},{"name":"token","size":4096,"time_modified":1699954070,"permissions":"-rw-r--r--","contents":[{"name":"token.go","size":910,"time_modified":1699954070,"permissions":"-rw-r--r--"},{"name":"go.mod","size":66,"time_modified":1699944730,"permissions":"drwxr-xr-x"}]}]}'
data = json.loads(jsonFile)

def first_function(dd):
    print("call first")
    st = ""
    
    for content in data["contents"]:
        if ".gitignore" != content['name']:
            #print(content['name'])
            st += content['name'] + " "
    print(st)

def second_function():
    st = ""
    for content in data["contents"]:
        st += content['name'] + " "
        
    print(st)

def third_function():
    for content in data["contents"]:
        if ".gitignore" != content['name']:
            time_modified = datetime.fromtimestamp(int(content["time_modified"])).strftime('%d-%m-%Y %H.%M')
            print("{:<10} {:<10} {:<10} {:<10}".format(content['permissions'], content['size'], str(time_modified), content['name']))

    
def four_function():
    for content in data["contents"][::-1]:
        if ".gitignore" != content['name']:
            time_modified = datetime.fromtimestamp(int(content["time_modified"])).strftime('%d-%m-%Y %H.%M')
            print("{:<10} {:<10} {:<10} {:<10}".format(content['permissions'], content['size'], str(time_modified), content['name']))

def five_function():
    content_list = []
    
    for content in data["contents"]:
        contents_dict = dict()
        if ".gitignore" != content['name']:
            #content_list.append(content['permissions'])
            contents_dict["permissions"] = content['permissions']
            contents_dict["size"] = content['size']
            contents_dict["name"] = content['name']
            contents_dict["time_modified"] = content['time_modified']
            content_list.append(contents_dict)
    def humanize_unixtime(unix_time):
        time = datetime.fromtimestamp(int(unix_time)).strftime('%d-%m-%Y %H.%M')
        return time
    
    lsorted = sorted(content_list, key=lambda x: humanize_unixtime(x["time_modified"]),reverse=True)
    
    for content in lsorted:
        if ".gitignore" != content['name']:
            time_modified = datetime.fromtimestamp(int(content["time_modified"])).strftime('%d-%m-%Y %H.%M')
            print("{:<10} {:<10} {:<10} {:<10}".format(content['permissions'], content['size'], str(time_modified), content['name']))

def parser_list():
    for content in data["contents"]:
        if "parser" == content['name']:
            for parser_content in content["contents"]:
                time_modified = datetime.fromtimestamp(int(parser_content["time_modified"])).strftime('%d-%m-%Y %H.%M')
                print("{:<10} {:<10} {:<10} {:<10}".format(parser_content['permissions'], parser_content['size'], str(time_modified), parser_content['name']))

def sub_parser_list():
    for content in data["contents"]:
        if "parser" == content['name']:
            for parser_content in content["contents"]:
                if "parser.go" == parser_content['name']:
                    time_modified = datetime.fromtimestamp(int(parser_content["time_modified"])).strftime('%d-%m-%Y %H.%M')
                    print("{:<10} {:<10} {:<10} {:<10}".format(parser_content['permissions'], parser_content['size'], str(time_modified), parser_content['name']))

def parser_size():
    for content in data["contents"]:
        if "parser" == content['name']:
            for parser_content in content["contents"]:
                if int(parser_content["size"]) > 999:
                  parser_content['size'] = int(parser_content["size"]) / 1024
                time_modified = datetime.fromtimestamp(int(parser_content["time_modified"])).strftime('%d-%m-%Y %H.%M')
                print("{:<10} {:<10} {:<10} {:<10}".format(parser_content['permissions'], parser_content['size'], str(time_modified), parser_content['name']))