# Adam Clemons
# 03-18-2016
# App.py - Executes Tkinter UI for building and executing JMeter shell commands
# with user defined parameters.
import Tkinter
import subprocess, shlex, Tkconstants, tkFileDialog
import config 

class PyJmx(Tkinter.Frame):

	def __init__(self, root):

		Tkinter.Frame.__init__(self, root)
		# options for buttons
		button_style = {'fill': Tkconstants.BOTH, 'padx': 5, 'pady': 5}

		# define buttons and labels
		self.currentFile = Tkinter.StringVar()
		self.currentFile.set('[No file Chosen]')
		Tkinter.Label(self, textvariable=self.currentFile).pack()

		Tkinter.Button(self, text='Select File', command=self.getFilename).pack(**button_style)
		Tkinter.Button(self, text="Run With JMeter", command=self.runJmeter).pack(**button_style)
		# define options for opening or saving a file
		self.file_opt = options = {}
		options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
		options['initialdir'] = config.jmxFolderPath
		options['parent'] = root
		options['title'] = 'select a jmx file: '

	def getFilename(self):
		# get filename
		filename = tkFileDialog.askopenfilename(**self.file_opt)
		self.currentFile.set(filename)

	def runJmeter(self):
		reload(config)
		subprocess.call(config.setPathCommand, shell=True)
		jmxName = self.currentFile.get()
		jmxName=jmxName.replace('/','\\')
		# Comment out for Windows:
		#jmxName=jmxName.replace(' ','\ ')
		print(jmxName)
		cmdStr = config.jMeterPath+'jmeter.bat -n -t ' + jmxName + ' -l  testResults.jtl'
		print(cmdStr)
                #This method doesn't lock the UI, but only works on Linux
		#cmdStr = shlex.split(cmdStr)
		#subprocess.Popen(cmdStr)
		subprocess.call(cmdStr, shell=True)
	

if __name__=='__main__':
	root = Tkinter.Tk()
	PyJmx(root).pack()
	root.mainloop()
