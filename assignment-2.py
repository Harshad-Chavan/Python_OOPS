# assignment-2
import datetime,abc
dt_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

class WriteFile(abc.ABC):
    __metaclass__ = abc.ABC

    def __init__(self,filename,delim=""):
        self.filename = filename
        self.delim = delim
        self.fileobj = open(filename,'w')
    
    @abc.abstractmethod
    def write(self):
        return
    
class LogFile(WriteFile):
    def write(self,text):
        self.fileobj.write(dt_str + " " + text + "\n")
        
class DelimFile(WriteFile):
    def write(self,lst):
        text = self.delim.join(lst)
        self.fileobj.write(text + "\n")
        
    

log = LogFile('log.txt')                  # passes the filename to write to
mydelim = DelimFile('data.csv', ',')      # passes the filename to write to
                                          # and a delimeter

log.write('this is a log message')        # writes a message to the file
log.write('this is another log message')  # same

mydelim.write(['a', 'b', 'c', 'd'])       # writes a list of values separated
                                          # by comma to the file
mydelim.write(['1', '2', '3', '4'])       # same

