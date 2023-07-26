# Let's illustrate the use of the Singleton pattern with an example scenario. 
# Suppose we want to create a logger class that logs messages to a file, 
# and we want to ensure that there is only one instance of the logger throughout 
# the application.


class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.log_file = "app_log.txt"

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(message + "\n")

# Usage
logger1 = Logger()
logger2 = Logger()

logger1.log("Log message 1")
logger2.log("Log message 2")

# Both logger instances will log to the same file.
