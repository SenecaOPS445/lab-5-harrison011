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

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))