# coding: utf-8
# python 3.7.0 x86_64

class File:
    
    def __init__(self, name: str, data:str, lvl_read:int=0, lvl_write:int=0):
        self.name = name
        self.data = data
        self.lvl_read = lvl_read
        self.lvl_write = lvl_write
     
    def read(self, lvl) -> None:
        raise NotImplementedError("impossible to read directly this file without check its habilitations")
    
    def write(self, lvl, data:str) -> None:
        raise NotImplementedError("impossible to write directly this file without check its habilitations")


class ProxyFile:
    
    def __init__(self, file: File):
        self.file = file
    
    def read(self, lvl) -> None:
        if self.file.lvl_read <= lvl:
            print(self.file.data)
        else:
            raise Exception(f"you have no permission to read '{self.file.name}'")
            
    def write(self, lvl, data) -> None:
        if self.file.lvl_read <= lvl:
           self.file.data = data
        else:
            raise Exception(f"you have no permission to write in '{self.file.name}'")


class User:
    
    def __init__(self, name:str, lvl_read:int=0, lvl_write:int=0):
        self.name = name
        self.lvl_read = lvl_read
        self.lvl_write = lvl_write
    
    def read_file(self, file:File) -> None:
        file.read(self.lvl_read)
    
    def write_file(self, file:File, data:str) -> None:
        file.write(self.lvl_write, data)
        
def main():
    file_1 = ProxyFile(File("fichier_texte", "hello world", 7, 3))
    quidam = User("quidam", 7, 1)
    
    
    quidam.read_file(file_1)
    # quidam.write_file(file_1, "goodbye world")

    
if __name__ == "__main__":
    main()