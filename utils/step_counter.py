#!/usr/bin/env python3

import os
import readline


file_list = []
count = 0


def get_files(dir):

    for f in os.listdir(dir):
        full_name = dir + f
        if os.path.isfile(full_name):
            if "node_module" in full_name:
                pass
            elif "dist" in full_name:
                pass
            elif "libs" in full_name:
                pass
            elif ".git" in full_name:
                pass
            elif ".vscode" in full_name:
                pass
            else:
                file_list.append(full_name)
        elif os.path.isdir(full_name):
            get_files(full_name + "/")




def count_line(file):

    counter = 0

    with open(file) as text:
        try:
            lines = text.readlines()
            for line in lines:
                counter += 1
        except:
            print("The file " + file + " is not source or text file.")

    return counter



if __name__ == "__main__":
    get_files(os.getcwd() + "/")

    for path in file_list:
        count += count_line(path)
    print("The number of steps is here =>=>=>=> " + str(count) + " <=<=<=<=")
