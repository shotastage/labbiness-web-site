#!/usr/bin/env python3

import os
import subprocess
import shutil


## Function for debug console.
def Log(string):
    print("Site Deployer: " + string)



## Preparation function
def preparation():

    # Check deploy gate dir.
    if not os.path.isdir("./dist"):
        Log("Dist directory does not exists.")
        os.mkdir("./dist")
        Log("Created distribution directory.")

    if not os.path.isdir("./node_modules"):
        Log("Node requirements are not installed.")
        try:
            subprocess.call(["yarn", "install"])
        except:
            Log("Failed to run yarn install.")
            Log("Node.js and Yarn haven't installed?")
            exit(1)



# Cleaner
def clean():
    Log("Cleaning source tree.")
    if os.path.isdir("./dist"):
        shutil.rmtree("./dist/")


class Compiler():

    def compile_pug(self):
        target_pages = [
            "index.pug",
            "debug.pug",
        ]

        Log("Compiling pug...")
        for page in target_pages:
            try:
                output = subprocess.check_output(["./node_modules/.bin/pug", page, "--out", "./dist/"])
            except:
                Log("Failed to exec builder!")
                Log("You may not install pug and pug-cli.")
                exit(1)


    def compile_sass(self):
        Log("Compiling sass...")
        try:
            output = subprocess.check_output(["./node_modules/.bin/node-sass", "./styles/site.scss", "./dist/styles/site.css"])
        except:
            Log("Failed to exec builder!")
            Log("You may not install node-sass.")
            exit(1)





if __name__ == "__main__":

    # Clean
    clean()

    # Preparing to build.
    preparation()


    # Compile
    compiler = Compiler()

    compiler.compile_pug()
    compiler.compile_sass()


    Log("Completed!")
