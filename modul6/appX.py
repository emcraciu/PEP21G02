from random import randint

class Device():
    local_key = None
    remote_key = None

    def generate_key(self):
        self.local_key = randint(129, 255)

    def get_remote_key(self, remote_key):
        self.remote_key = remote_key

    def sent_local_key(self):
        return self.local_key

class Client(Device):
    pass

class Server(Device):
    pass


client = Client()
server = Server()

client.generate_key()
server.generate_key()

print('', client.local_key)
print('', server.local_key)