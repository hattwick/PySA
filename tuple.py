from __future__ import division

__author__ = 'phil'

# exercises from Data Science from Scrath
# code may or may not mirror the text examples

# data set being analyzed is a list of users and connections

users = [
    {"id": 0, "name": "hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5,7), (6,8), (7,8), (8, 9)]


# now add list of friends/connections for each user

for user in users:
    user["friends"] = []

# for i,j in range(friendships):  this generated an error because range wanted integers, not a list
for i, j in friendships:
    users[i]["friends"].append(users[j])  # add i as a friend of j
    users[j]["friends"].append(users[i])

def number_of_friends(user):
    """How many friends does _user_ have?"""
    return len(user["friends"])      # Length of friends for  each user

print (number_of_friends(user))

total_connections = sum(number_of_friends(user)
                        for user in users)

print (total_connections)            # should be 24


# Compute averages

num_users = len(users)
avg_connections = total_connections / num_users
print ("There are ", num_users, "users.")
print (avg_connections, " Average connections")


# Sort from most to least friends

num_friends_by_id = [(user["id"], number_of_friends(user
)) for user in users]


print (num_friends_by_id)

# sorted(num_friends_by_id,
#       key=lambda user_id: number_of_friends)
