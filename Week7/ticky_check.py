#! /usr/bin/python3


import re
import sys
import csv


def error_message():
    try:
    
        with open("syslog.log", "r+") as f:
            str_list = []
            number = []
            index = 0
            csv_column = ('Error', 'Count') 
            content = f.read()
            sep = content.strip().split("\n")
        
            for i in sep:
                if "ERROR" in i:
                    result = re.sub(r'(.*)(:\s)(ERROR\s)([^(]*)(.*)', "\\4", i)
                    str_list.append(str(result).strip())
        
            str_list = sorted(str_list)
            l2 = set(str_list)
            l2 = list(l2)
        
            for i in range(0, len(l2)):
                if l2[i] in str_list:
                    number.append(str_list.count(l2[i]))
        
            l2 = dict(zip(l2, number))
            number = sorted(number, reverse=True)
            l2 = sorted(l2, key=l2.get, reverse=True)
            l2 = dict(zip(l2, number))
        
            try:
                with open("error_message.csv", 'w') as csvfile:
                    #writer = csv.DictWriter(csvfile, fieldnames="Error Count")
                    #writer.writeheader()
                    writer = csv.writer(csvfile)
                    writer.writerow(csv_column)
                    for data in l2.items():
                        writer.writerow(data)
            except IOError:
                print("I/O error")
            print("Write Successfully !!!")
    except Exception as e:
        print(e)

def user_statistics():
    with open("syslog.log", "r+") as f:
        str_list = []
        name_list = []
        names = []
        str_set = []
        err_number = []
        info_number = []
        final_list = []
        csv_column = ('Username', 'INFO', 'ERROR') 
        content = f.read()
        sep = content.strip().split("\n")

        for i in sep:
            result = re.sub(r'(.*)(:\s)(\w*)\s([^\(]*)(\()([^\)]*)(\))', "\\6 \\3", i)
            str_list.append(str(result).strip())

            name = re.sub(r'(.*)(:\s)(\w*)\s([^\(]*)(\()([^\)]*)(\))', "\\6", i)
            name_list.append(str(name).strip())

        name_list = list(sorted(name_list))
        str_list = sorted(str_list)

        for line in str_list:
            if "jackowens" in line:
                break
            str_set.append(line)
            
        for name in name_list:
            if "jackowens" in name:
                break;
            names.append(name)

        str_set = list(sorted(str_set))
        names = list(sorted(set(names)))

        for i in range(0, len(names)):
            err_number.append(0)
        for i in range(0, len(names)):
            info_number.append(0)

        for index in range(0, len(names)):
            for j in range(0, len(str_set)):
                if names[index] + " ERROR" in str_set[j]:
                    err_number[index] += 1 
                elif names[index] + " INFO" in str_set[j]:
                    info_number[index] += 1
        for index in range(0, len(names)):
            final_list.append(names[index] + " " + str(info_number[index]) + " " + str(err_number[index]))

        try:
            with open("user_statistics.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(csv_column)
                for data in final_list:
                    writer.writerow(data.strip().split(" "))
        except Exception as e:
            print(e)



if __name__ == '__main__':
    error_message()
    user_statistics()
