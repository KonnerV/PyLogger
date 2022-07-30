
# imports used for testing
import time

# importing the module
import PyLogger

# some code to test the modules functions
def main(): 
    PyLogger.PyLogInit()
    time.sleep(10)
    print(PyLogger.PyLog("This is a test log message."))
    time.sleep(10)
    print(PyLogger.PyLogErr("TEST ERROR"))
    time.sleep(10)
    PyLogger.PyLogClear()
    time.sleep(10)
    PyLogger.PyLogDel()

if __name__ == "__main__":
    main()