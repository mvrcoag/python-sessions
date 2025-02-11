import os


class File:
    def __init__(self, filename, content):
        self.filename = filename
        self.content = content

    def append(self, content):
        self.content = self.content + content

    def write(self):
        file = open(self.filename, "a+")
        file.write(self.content)
        file.close()

    # Start static
    @staticmethod
    def cwd():
        return os.getcwd()

    # End static


# Start static
path = File.cwd()
# End static

if "dbaobfcpisdb" not in path:
    print("Not in valid dir")
    exit(1)

textfile = File("file.txt", "")
textfile.append("Prueba")
textfile.write()
