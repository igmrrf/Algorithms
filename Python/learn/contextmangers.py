# Context managers allow for the setup and cleanup of resources. They are often used with statements (e.g. file handling)
class MyContextManager:
    def __enter__(self):
        print("Entering the context.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting the context.")


with MyContextManager():
    print("inside the context")
    print("you can do anything within the context and have it clean up")


with open("course/text.txt", "a") as f:
    print("writing")
    f.write("how are you")
    f.write("how are you")
    f.close()
