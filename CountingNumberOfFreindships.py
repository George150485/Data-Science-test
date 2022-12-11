users = [

    {"id": 2, "name" : "George"},
    {"id": 3, "name" : "Elijah"},
    {"id": 4, "name" : "Grace"},
    {"id": 1, "name" : "Mohjen"}
    
    ]
friendships = {user["id"]: [] for user in users}
print(friendships)

def number_of_users(user):
    user_id  = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)

toatl_freinds = sum(number_of_users(user) for user in users)

print(toatl_freinds)
#Average connection per person = total number of connections / No. of Users
