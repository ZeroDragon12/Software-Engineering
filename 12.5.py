class MailServer:
    def __init__(self):
        self.inbox = []

    def receive_mail(self):
        if len(self.inbox) == 0:
            return None
        else:
            mail = self.inbox.pop(0)
            return mail

    def send_mail(self, recipient, message):
        recipient.inbox.append(message)


class MailClient:
    def __init__(self, server, user):
        self.server = server
        self.user = user

    def receive_mail(self):
        return self.server.receive_mail()

    def send_mail(self, server, message):
        server.send_mail(server, message)


server1 = MailServer()
server2 = MailServer()

servers = {"server1": server1, "server2": server2}

client1 = MailClient(server1, "user1")
client2 = MailClient(server2, "user2")

client1.send_mail(server1, "Hello, user1! This is a message from server1.")
print(client1.receive_mail())  # Output: Hello, user1! This is a message from server1.
client2.send_mail(server2, "Hello, user2! This is a message from server2.")
print(client2.receive_mail())  # Output: Hello, user2! This is a message from server2.
client1.send_mail(server1, "How Are You?")
print(client1.receive_mail())
