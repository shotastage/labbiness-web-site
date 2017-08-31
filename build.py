#!/usr/bin/env python3

import os
import subprocess
import shutil
import sys


## Function for debug console.
def Log(string, withError = False):
    if withError:
        print('\033[31mSite Deployer: ' + string + '\033[0m')
    else:
        print('\033[32mSite Deployer: \033[0m' + string)


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
            Log("Failed to run yarn install.", withError = True)
            Log("Node.js and Yarn haven't installed?", withError = True)
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
                Log("Failed to exec builder!", withError = True)
                Log("You may not install pug and pug-cli.", withError = True)
                exit(1)


    def compile_sass(self):
        Log("Compiling sass...")
        try:
            output = subprocess.check_output(["./node_modules/.bin/node-sass", "./styles/site.scss", "./dist/styles/site.css"])
        except:
            Log("Failed to exec builder!", withError = True)
            Log("You may not install node-sass.", withError = True)
            exit(1)

    def create_assets(self):
        Log("Creating assets pack....")
        try:
            shutil.copytree("./assets/", "./dist/assets/")
        except:
            Log("Failed to copy assets directory. ", withError = True)



class DebugUtils():
    def open_in_chrome(self):
        Log("Opening in Chrome...")
        subprocess.call(["open", "-a", "Google Chrome", os.curdir + "/dist/index.html"])


    def open_in_safari(self):
        Log("Opening in Chrome...")
        subprocess.call(["open", "-a", "Google Chrome", os.curdir + "/dist/index.html"])



class Deploy():

    def check(self):
        pass


if __name__ == "__main__":

    # Script running mode.
    try:
        SCRIPT_MODE = sys.argv[1]
    except:
        SCRIPT_MODE = "Always"

    # Clean
    clean()

    # Preparing to build.
    preparation()


    # Compile
    compiler = Compiler()

    compiler.compile_pug()
    compiler.compile_sass()
    compiler.create_assets()


    if SCRIPT_MODE == "--production":
        deployer = Deploy()
    elif SCRIPT_MODE == "--debug-upload":
        # Upload
        pass
    else:
        debugger = DebugUtils()

        if not SCRIPT_MODE == "--no-open":
            debugger.open_in_chrome()

    Log("Completed!")
