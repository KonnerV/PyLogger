
# imports
import os

# module code
def PyLogInit():
    try:
        logFile = open("LOGFILE.log", "w")
    except:
        print("Couldn't create log file.")
    finally:
        logFile.close()

def PyLog(LogMessage) -> str:
    try:
        logFile = open("LOGFILE.log", "at")
        try:
            logFile.write(f'#~/: {LogMessage}\n')
        except:
            print("Something went wrong when writing to the file")
        finally:
            logFile.close()
    except:
        print("Something went wrong when opening the file")
    return f'#~/ PYLOGGER: LOGGED {LogMessage}'

def PyLogErr(ErrorMessage) -> str:
    try:
        logFile = open("LOGFILE.log", "at")
        try:
            logFile.write(f'#~/: {ErrorMessage}\n')
        except:
            print("Something went wrong when writing to the file")
        finally:
            logFile.close()
    except:
        print("Something went wrong when opening the file")
    return f'#~/ PYLOGGER ERROR: ERROR {ErrorMessage}'

def PyLogClear():
    try:
        logFile = open("LOGFILE.log", "w")
        try:
            logFile.write("")
        except:
            print("Something went wrong when writing to the file")
        finally:
            logFile.close()
    except:
        print("Something went wrong when opening the file")

def PyLogDel():
    if os.path.exists("LOGFILE.log"):
        os.remove("LOGFILE.log")
    else:
        print("File doesn't exist.")
