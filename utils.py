from constants import SUPERVISOR_CREDENTIALS


def check_credentials(user_credentials):
    if len(user_credentials) > 2:
        for i in range(len(SUPERVISOR_CREDENTIALS)):
            if user_credentials[1] in SUPERVISOR_CREDENTIALS[i]['username'] and\
                    user_credentials[2] in SUPERVISOR_CREDENTIALS[i]['password']:
                return True
    return False
