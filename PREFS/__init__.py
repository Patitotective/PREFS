import ast

class PREFS(object):
    """docstring for PREFS"""
    def __init__(self, prefs, filename = "prefs", separator = "=", interprete = False):
        super(PREFS, self).__init__()
        self.prefs = prefs
        self.filename = filename
        self.separator = separator
        self.interprete = interprete

        self.ReadPrefs()
        
    def ReadPrefs(self):
        try:
            prefsTXT = open(f"{self.filename}.txt", "r")
            
            #Do something with the file
            content = {}
            lines = prefsTXT.readlines()
            e = 0
            for line in lines:
                lines[e] = line.replace("\n", "")
                e += 1

            for line in lines:
                #print(line)
                if not self.interprete:
                    content[line.split(self.separator)[0]] = line.split(self.separator)[1]
                elif self.interprete:
                    content[line.split(self.separator)[0]] = ast.literal_eval(line.split(self.separator)[1])

            #print(content)
            prefsTXT.close()
            return content

        except FileNotFoundError:
            try:
                self.CreatePrefs(self.prefs())
            except TypeError:
                self.CreatePrefs(self.prefs)

    def CreatePrefs(self, prefsDictionarie):
        prefsTXT = open(f"{self.filename}.txt","w+")
        for i in prefsDictionarie.items():
            prefsTXT.write(f"{i[0]}={i[1]}\n")

        prefsTXT.close()

        self.ReadPrefs()

    def WritePrefs(self, pref, value):
        content = self.ReadPrefs()
        content[pref] = value

        text = ""
        for item in content.items():
            text += f"{item[0]}{self.separator}{item[1]}\n"

        prefsTXT = open(f"{self.filename}.txt","w+")
        prefsTXT.write(text)
        prefsTXT.close()