from auth import agent_auth
from constants import PROFILES_FILE_PATH, DEALS_FILE_PATH
from agent import Agent
from store import save_to_file, load_data
import uuid

profiles = list()
input_tuples = list()


def add_profile(agent_obj):
    input_tuple, profile = Agent.add_profile(agent_obj)
    input_tuples.append(input_tuple)
    profiles.append(profile)
    print('Added profile successfully')
    add_again = input('Are you want add more profile(y or n)?')
    if add_again == 'y':
        add_profile(agent_obj)
    elif add_again == 'n':
        data = list()
        for i in range(len(input_tuples)):
            data.append({'id': str(uuid.uuid1()),
                         '{}'.format(input_tuples[i][0] + '_' + input_tuples[i][1]): '{}'.format(profiles[i])})
        final_data = [{'{}'.format(agent_obj.username): data}]
        save_to_file(PROFILES_FILE_PATH, final_data)
        agent()


def add_deal(agent_obj):
    username = agent_obj.username
    profiles_data = load_data(PROFILES_FILE_PATH)
    profiles_founded = None
    for profile in profiles_data:
        profiles_founded = profile[username]
    print(profiles_founded)
    id_selected = str(input('Please your profile for deal(enter id):'))
    for profile_founded in profiles_founded:
        if profile_founded['id'] == id_selected:
            deal = Agent.add_deal(agent_obj)
            data = [
                {'agent_name': '{}'.format(agent_obj.username), 'profile_id': '{}'.format(id_selected), 'deal': deal}
            ]
            save_to_file(DEALS_FILE_PATH, data)
            print('Added deal successfully')
            agent()


def agent():
    agent_options_input = input('Please choose add profile(p) or add deal(d) or search(s) or exit(e):')
    if agent_options_input == 'p':
        agent_obj = agent_auth()
        add_profile(agent_obj)
    elif agent_options_input == 'd':
        agent_obj = agent_auth()
        add_deal(agent_obj)
    elif agent_options_input == 's':
        pass
    elif agent_options_input == 'e':
        print('#' * 40, 'BY', '#' * 40)


if __name__ == '__main__':
    print('#' * 40, 'WELCOME', '#' * 40)
    agent()
