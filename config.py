# Adam Clemons
# 03-18-2016
# config.py - constants meant to be used by the other scripts.
# 03-20-2016
# updated with os-specific settings, based on relative directories. 

import os

if (os.name == 'nt'): # Returns "nt" on windows 10
    thisDir = os.getcwd()
    jMeterPath="jmeter\\bin\\"
    jmxFolderPath="jmeter\\bin\\tests\\"
    #Update path, for convinience
    setPathCommand = "SET PATH=%PATH%;"+jMeterPath
else: #Assuming linux, need to test
    thisDir = os.getcwd()
    jMeterPath="jmeter\\bin\\"
    jmxFolderPath="jmeter\\bin\\tests\\"
    #Update path, for convinience
