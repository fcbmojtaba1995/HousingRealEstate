from auth import agent_auth
from constants import PROFILES_FILE_PATH
from agent import Agent
from store import save_to_file

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
            data.append({'{}'.format(input_tuples[i][0] + '_' + input_tuples[i][1]): '{}'.format(profiles[i])})
        final_data = [{'{}'.format(agent_obj.username): data}]
        save_to_file(PROFILES_FILE_PATH, final_data)
        agent()


def agent():
    agent_options_input = input('Please choose add profile(p) or add deal(d) or search(s) or exit(e):')
    if agent_options_input == 'p':
        agent_obj = agent_auth()
        add_profile(agent_obj)
    elif agent_options_input == 'd':
        pass
    elif agent_options_input == 's':
        pass
    elif agent_options_input == 'e':
        print('#' * 40, 'BY', '#' * 40)


if __name__ == '__main__':
    print('#' * 40, 'WELCOME', '#' * 40)
    agent()
