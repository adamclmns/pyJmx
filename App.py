# Adam Clemons
# 03-18-2016
# App.py - Executes Tkinter UI for building and executing JMeter shell commands
# with user defined parameters.
import Tkinter
import subprocess, shlex, Tkconstants, tkFileDialog, tkMessageBox
import config, PyJmx


def updateSources():
	reload(config)
	reload(PyJmx)
	# reload(imageBytes)

def tick(pyJmx):
	updateSources()

if __name__=='__main__':
	root = Tkinter.Tk()
	root.resizable(width=False, height=False)
	pyJmxInstance = PyJmx.window(root)
	root.title("pyJMX")
	tick(pyJmxInstance)
	root.mainloop()
