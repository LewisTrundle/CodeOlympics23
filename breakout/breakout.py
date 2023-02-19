import numpy as np
import random

def make_teams():
    avg_len = round((len(kk_as_ids) / no_of_teams))
    teams = [ [] for i in range(no_of_teams) ]

    # Choosing user with friends as they are the most difficult to place
    for val in user_index_w_most_friends:
        user_code = kk_as_ids[val]
        for i, team in enumerate(teams):
            friend_exists = False
            for v in vv[val]:
                if v in team:
                    friend_exists = True

            if not friend_exists and (len(team) < avg_len):
                team.append(user_code)
                break

            # If user can not be placed, request smaller teams
            if i == (len(teams)-1):
                return teams, True

    return teams, False

friend_lists = {'Chris' : ['Paul','Dave'], 'Paul': ['Chris', 'Dave'], 'Dave':['Paul', 'Chris'],
    'Ryan': ['Harvey'], 'Harvey':['Ryan'], 
    'Lewis':['Connor'], 'Connor':['Lewis']}


kk = friend_lists.keys()
ids = {}
for i, name in enumerate(kk):
    ids[name] = i
kk_as_ids = [ids.get(name) for name in kk]

vv = [ np.array([ ids.get(f) for f in friends]) for friends in friend_lists.values()]
len_vv = [len(v) for v in vv]
user_index_w_most_friends = np.flip(np.argsort(len_vv))

# Find teams - smallest team will be of size 1 if everyone is friends with everyone
# This satisfies the condition for being people they do not know
no_of_teams = 2
flag = True
while flag:
    teams, flag = make_teams()
    no_of_teams += 1

# User codes to names
reversed_dict = {}
for key, value in ids.items():
    if value not in reversed_dict:
        reversed_dict[value] = key
    else:
        print("Error")

teams_and_names = [ [reversed_dict.get(name) for name in team] for team in teams]
print(teams_and_names)

