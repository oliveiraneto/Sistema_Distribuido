import Pyro4

class NumberAdder(object):
    def add_numbers(self, num1, num2):
        return num1 + num2

daemon = Pyro4.Daemon()
uri = daemon.register(NumberAdder)

print("Servidor aguardando conexões...")
daemon.requestLoop()
