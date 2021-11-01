import tkinter as tk
import tkinter.filedialog as fd
import sys, logging, zlib
from rainbow_logging_handler import RainbowLoggingHandler

CURSOR_UP_ONE = '\x1b[1A' 
ERASE_LINE = '\x1b[2K'
ERASE_PREV =  CURSOR_UP_ONE + ERASE_LINE
FILES = 1
FOLDERS = 2
pathList = []
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s]  %(message)s")
logo = """
	─────────────────────────────────────────────────────────────────────
	─████████──████████─██████████████─██████████████─████████████████───
	─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
	─████░░██──██░░████─██░░██████░░██─██░░██████████─██░░████████░░██───
	───██░░░░██░░░░██───██░░██──██░░██─██░░██─────────██░░██────██░░██───
	───████░░░░░░████───██░░██████░░██─██░░██████████─██░░████████░░██───
	─────████░░████─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───
	───────██░░██───────██░░██████████─██░░██████████─██░░██████░░████───
	───────██░░██───────██░░██─────────██░░██─────────██░░██──██░░██─────
	───────██░░██───────██░░██─────────██░░██████████─██░░██──██░░██████─
	───────██░░██───────██░░██─────────██░░░░░░░░░░██─██░░██──██░░░░░░██─
	───────██████───────██████─────────██████████████─██████──██████████─
	───────────────────────────────────────────────────────────── v 1.0 ─ 


			 __      __   _                  
			 \ \    / /__| |__ ___ _ __  ___ 
			  \ \/\/ / -_) / _/ _ \ '  \/ -_)
			   \_/\_/\___|_\__\___/_|_|_\___|
                                 

                                         

"""


def showBrowsDialog(selectType):
	root = tk.Tk()
	root.withdraw()
	if selectType == FOLDERS:
		dirselect = fd.askdirectory(parent=root, title='Choose folder')
	elif selectType == FILES:
		filez = fd.askopenfilenames(parent=root, title='Choose files')
	else:
		log.error("[-] selectType value must be 1 or 2")
		exit()
	
def createFilesList(self,selectType):
	filesList = showBrowsDialog(selectType)
	if(len(filesList[0]) > 0):
		for path in filesList[0]:
			if(path not in pathList):
				pathList.append(path)
	if(len(pathList) > 0 ):
		log.info("[+] Path list\n----------------------------------------\n")
		for path in self.pathList:
			log.info(path)

def secure_delete(path):
	with open(path, "ba+", buffering=0) as delfile:
	    length = delfile.tell()
	delfile.close()
	print("Length of file:%s" % length)
	
	with open(path, "br+", buffering=0) as delfile:
	    for i in range(passes):
	        delfile.seek(0,0)
	        delfile.write(os.urandom(length))
	    
	    delfile.seek(0)
	    for x in range(length):
	        delfile.write(b'\x00')
	os.remove(path)

def Exit():

	exit()

def main():


	print(logo.replace('─',' '))
	mainMenu = """

	└─► Main Menu

		│ 1. Add File(s)
		│ 2. Add a Folder [Default]
		│ 3. Exit
		└─────────────────────────────────
		"""
	actionMenu = """

	└─► Action Menu

		│ 1. Remove/Unlink (Fast)
		│ 2. Secure Remove (Slow)
		│ 3. Main Menu
		└─────────────────────────────────
		"""

	
	print(mainMenu)

	x = ""
	# x = input("\tPlease select one of the above options : ")
	if (x == "" or x == 2):showBrowsDialog(FOLDERS)
	elif(x == 1): showBrowsDialog(FILES)
	else: 
		print("\t¿? Wrong Choice !")
		Exit()
	print(actionMenu)
	

	log.debug("debug msg")

if __name__ == '__main__':
	handler = RainbowLoggingHandler(sys.stderr, color_funcName=('black', 'yellow', True))
	handler.setFormatter(formatter)
	log.addHandler(handler)
	main()
