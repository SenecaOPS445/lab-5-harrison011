#!/usr/bin/env python3
# Author ID: hiruthayathas
# Author Name: Harrison Iruthayathas
# Date: July 12, 2024

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    f = open(file_name, 'r') # opens file to read from
    data = f.read() # reads contents and outputs as a string with newline characters
    f.close() # closes open file
    return data


def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    data = read_file_string(file_name) # uses previous function to get string output
    final_list = data.strip().split('\n') # strips any trailing spaces, and then splits string by using the new line character.
    return final_list

def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f1 = open(file_name, 'a')
    f1.write(string_of_lines)
    f1.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each item is one line
    f1 = open(file_name, 'w') # file to write to
    for line in list_of_lines: # go through list
        f1.write(line+'\n') # add newline character and eol and append
    f1.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new file, adds line number to new file
    fr = open(file_name_read, 'r') # file to read from
    data = fr.readlines()
    fr.close()
    
    fw = open(file_name_write, 'w') # file to write to
    count = 1
    for line in data:
        number_line = str(count) + ':' + line
        fw.write(number_line)
        count = count + 1
    fw.close()



if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))