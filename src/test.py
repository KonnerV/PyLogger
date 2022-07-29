import PyLogger




def main(): 
    PyLogger.PyLog("This is a test log message.")
    PyLogger.PyLogErr("TEST ERROR")

    PyLogger.PyLogClear()



if __name__ == "__main__":
    main()