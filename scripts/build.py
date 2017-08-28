#!/usr/bin/env python3

import os
import subprocess


def Log(string):
    print("Site Deployer: " + string)

def preparation():

    # Check deploy gate dir.
    if not os.path.isdir("./dist"):
        Log("Dist directory does not exists.")
        os.mkdir("./dist")
        Log("Created distribution directory.")

    if not os.path.isdir("./node_modules")
        Log("Node requirements are not installed.")
        subprocess.run("yarn install")



if __name__ == "__main__":
    preparation()
