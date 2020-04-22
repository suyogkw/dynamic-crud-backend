
import datetime

class ServerData(object):

    hostname = 'local'

    def __init__(self,reference, client, action):
        self.action = action
        if reference=='students':
            self.name = f'dear mr. {client.name}' if action=='INSERT' else client.name
       

    @property
    def timestamp(self):
        return datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]

    @property
    def context_user(self):
        return 'username'

    @property
    def create_name(self):
        return self.name