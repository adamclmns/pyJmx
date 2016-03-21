# pyJmx
Python UI to execute JMeter load test scripts without using the Jmeter UI, with as little prerequisite knowledge as possible.

INSTALLATION:
You need to have Python 2.7 installed and on your path. You will need to have Jmeter extracted in the pyJmx directory. There are no other pre-requisites. 
 -You can check this by running "python --version" in your command prompt or terminal
You will need to place the extracted jmeter, and this script as shown below

+-[ pyJmx Directory ]
  -- App.py
  -- config.py
  +- jmeter [extracted jmeter binary zip]
    +- bin
      -- [ jmeter executable ]
      +- tests [ default jmx directory ]


To change the directory names, just edit config.py. 
If you have jmeter on your system path, you can set the jmeterPath to ''

This was written on Ubuntu, and then ported to windows for a proof of concept. 
This is not a finished product. 

Known issues: 
 * No spaces allowed in paths or file names on Windows (test in Windows 10)
   Code changes required between Linux and Windows. Need to make these dynamic.
 * Console is not thread safe on UI. You can wait a long time for your output. 
  
  
  
Intended features:
  Run configurations - A small set of parameters (thread count, csv source, master-hostname, etc) 
      could be injected into the jmx file according to a saved pyJmx confiruation file, allowing 
      more user-frienly execution of Jmeter tests. 
