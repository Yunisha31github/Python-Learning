def announce(f):
    def wrapper():
        print("about to run a function..")
        f()
        print("Done with the function.")
    return wrapper
@announce
def hello():
    print("Hello, World")

hello()