"""
    Jarvis - A data-collecting chatbot for Slack
    Current Release: 1.0

    Jarvis is a chatbot designed for seamless integration with Slack 
    workspaces. It will collect data from users and train itself 
    to interact within the workspace.

    ------------------------------------------------------------------
    Release notes for v.1.0:
        - IN PROGRESS

    ------------------------------------------------------------------
    This project is released as open-source under the permissive MIT 
    license with the approval of its sponsor, Bagrow Industries.
"""
# Database management
import sqlite3

# Slack interaction
import websocket
try:
    import thread 
except ImportError:
    import _thread as thread

# Slack connection token
from botsettings import API_TOKEN


class Jarvis:
    def __init__(self):
        self.currentState = 'Idle'

    def start_training(self):
        self.currentState = 'Training'

    def stop_training(self):
        self.currentState = 'Idle'

    def create_database(self):
        pass

    def store_training_data(self, msg_txt, action):
        pass

    def get_stored_data(self):
        pass

# ==================================================================== #

# This is run when the script is run. So for example, calling: 
# python jarvis.py will execute this. This is where we will call all
# the main code. Functions will be defined above and called here.
if __name__ == '__main__':
    pass