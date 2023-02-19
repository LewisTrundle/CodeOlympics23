import numpy as np

friend_lists = {'Chris' : ['Paul','Dave'], 'Paul': ['Chris', 'Dave'], 'Dave':['Paul', 'Chris'],
    'Ryan': ['Harvey'], 'Harvey':['Ryan'], 
    'Lewis':['Connor'], 'Connor':['Lewis']}





kk = friend_lists.keys()
print(kk)
ids = {}
for i, name in enumerate(kk):
    ids[name] = i

kk_as_ids = [ids.get(name) for name in kk]
print(kk_as_ids)

vv = [ np.array([ ids.get(f) for f in friends]) for friends in friend_lists.values()]
print(vv)

len_vv = [len(v) for v in vv]

print(len_vv)

user_index_w_most_friends = np.flip(np.argsort(len_vv))

no_of_teams = 3
teams = [ [] for i in range(no_of_teams) ]
print(teams)
for val in user_index_w_most_friends:
    user_code = kk_as_ids[val]
    print(user_code)

    for team in teams:
        friend_exists = False
        for v in vv[val]:
            if v in team:
                friend_exists = True

        if not friend_exists:
            team.append(user_code)
            print(team)



