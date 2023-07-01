import Pyro4

class StringInverter(object):
    def invert_string(self, text):
        return text[::-1]

daemon = Pyro4.Daemon()
uri = daemon.register(StringInverter)

print("Servidor aguardando conexões...")
daemon.requestLoop()
