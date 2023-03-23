class cars(object):
    def __init__(self,name,colour,model):
        self.name=name
        self.colour=colour
        self.model=model

    def start(self):
        print("started")
    def run(self):
        print("moving")
    def stop(self):
        print("stopped")

porsche=cars("porsche","red","2022")             
audi=cars("audi","white","2020")
#audi.start()
#print(audi.model)
print(porsche.name)
porsche.run()