from agent import Agent, Supervisor
from constants import AGENT_FILE_PATH
from store import load_data


def check_agent_username(username):
    agents_data = load_data(AGENT_FILE_PATH)
    _ = [Agent(**d) for d in agents_data]
    agent = Supervisor.search(username)
    return agent


def check_agent_password(agent, password):
    if agent.check_password(password):
        return True
    return False


def agent_auth():
    agent = None
    password_is_correct = False
    while agent is None:
        username = input('Please enter your username:')
        agent = check_agent_username(username)
        if agent is None:
            print('This username not found, try again...')
    while password_is_correct is False:
        password = input('Please enter your password:')
        password_is_correct = check_agent_password(agent, password)
        if password_is_correct:
            print('Welcome')
            password_is_correct = True
        else:
            print('Password is wrong, try again...')
