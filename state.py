# coding: utf-8
# python 3.7.0 x86_64

class State:
    name = "state"
    allowed = []
    
    def switch(self, state) -> None:
        if state.name in self.allowed:
            self.__class__ = state
        else:
            print(f"impossible to switch {self.name} to {state.name}")
    
    def action(self, song) -> None:
        raise NotImplementedError()

class Play(State):
    name = "Play"
    allowed = ["Pause", "Stop"]
    
    def action(self, song) -> None:
        print(f"{song} in play state")
    
class Pause(State):
    name = "Pause"
    allowed = ["Play"]
    
    def action(self, song) -> None:
        print(f"{song} in pause state")
    
class Stop(State):
    name = "Stop"
    allowed = ["Play"]
    
    def action(self, song) -> None:
        print(f"{song} in stop state")

class Player:
    
    def __init__(self, song:str):
        self.state = Stop()
        self.song = song
    
    def switch(self, state):
        self.state.switch(state)
        return self

    def action(self) -> None:
        self.state.action(self.song)

def main():
    player = Player("Duality")
    
    states = [Play, Pause, Play, Stop, Stop, Pause]
    for s in states:
        player.switch(s).action()
    
    

if __name__ == "__main__":
    main()