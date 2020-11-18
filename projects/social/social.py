import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        # Add users
        # call add_user() until our number of users is num_users
        for i in range(num_users):
            self.add_user(f"User {i+1}")
        # Create friendships
        # totalFriendships = avg_friendships * num_users
        # Generate a list of all possible friendships
        possibleFriendships = []
        # Avoid dups by ensuring the first ID is smaller than the second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possibleFriendships.append((user_id, friend_id))
        # Shuffle the list
        random.shuffle(possibleFriendships)
        # print("random friendships:")
        # print(possibleFriendships)

        # Slice off totalFriendships from the front, create friendships
        totalFriendships = avg_friendships * num_users // 2
        print(f"Friendships to create: {totalFriendships}\n")
        for i in range(totalFriendships):
            friendship = possibleFriendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = []
        q.append(user_id)
        # initialize first path
        visited[user_id] = [user_id]
        # while queue is not empty
        while len(q) > 0:
            # grab first element from queue
            cur = q.pop(0)
            # for each friendship of cur
            for friend in self.friendships[cur]:
                # if friend has not been visited/is not key in visited dictionary
                if friend not in visited:
                    # add key to visited dictionary with existing path from userID plus the friend ID
                    visited[friend] = visited[cur] + [friend]
                    # add friend to queue
                    q.append(friend)
        percentage = len(visited.keys())/len(self.users.keys()) * 100
        length = [len(x) for x in visited.values()]
        # average subtracts 1 since first connection is from self
        average = round(sum(length) / len(visited.keys()), 2) - 1
        return f"{visited} \npercentage of all users in network: {percentage}% \naverage degree of separation: {average}"


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
