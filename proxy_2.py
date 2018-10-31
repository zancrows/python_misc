# coding: utf-8
# python 3.7.0 x86_64

class Image:
    def __init__(self, name:str):
        self.name = name
        self.load()
    
    def display(self) -> None:
        print(f"display image {self.name}")
    
    def load(self):
        print(f"load image {self.name}")
    
class ProxyImage():
    
    def __init__(self, name:str):
        self.name = name
        self.image = None
    
    def display(self) -> None:
        if self.image is None:
            self.image = Image(self.name)
        self.image.display()

def main():
    image_1 = ProxyImage("meme.gif")
    image_2 = ProxyImage("paysage.png")
    image_3 = ProxyImage("wallpaper.jpg")
    
    image_1.display()
    image_2.display()
    image_1.display()

    
if __name__ == "__main__":
    main()