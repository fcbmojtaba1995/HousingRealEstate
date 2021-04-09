import sys
from utils import check_credentials
from agent import Supervisor
from store import save_to_file
from constants import AGENT_FILE_PATH

if __name__ == '__main__':
    if check_credentials(sys.argv):
        print('Welcome!!!')
        agent = Supervisor.create_agent()
        save_to_file(AGENT_FILE_PATH, Supervisor.agent_data())

    else:
        print('Wrong credentials, try again...')
