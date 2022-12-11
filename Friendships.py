users = [

    {"id": 2, "name" : "George"},
    {"id": 3, "name" : "Elijah"},
    {"id": 4, "name" : "Grace"},
    {"id": 1, "name" : "Mohjen"}
    
    ]
friendships = {user["id"]: [] for user in users}
for i,j in friendships:
    friendships[i].append(j)
    friendships[j].append(i)
    
print(friendships)
