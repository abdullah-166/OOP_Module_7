class Engine:
    def __init__(self) -> None:
        pass
        
    def start(self):
        return "Engine started"

class Driver:
    def __init__(self) -> None:
        pass

#car has an engine    
class Car:
    def __init__(self) -> None:
        self.engine = Engine()
        self.driver = Driver()

    def start(self):
        self.engine.start()