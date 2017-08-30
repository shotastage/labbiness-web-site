#!/usr/bin/env python3

import os
import subprocess
import shutil


if __name__ == "__main__":
    try:
        print("Compiling pug...")
        output = subprocess.check_output(["./node_modules/.bin/pug", "index.pug"])
    except:
        print("Failed to exec builder!")
        exit(1)


    print("Making distribution...")

    try:
        shutil.move("./index.html", "./dist/")
    except:
        os.remove("./dist/index.html")
        shutil.move("./index.html", "./dist/")

    print("Completed!")
