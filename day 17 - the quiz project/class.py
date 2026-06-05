class User:
    def __init__(self,name):
        print("object is created")
        self.name=name
        self.follower=0
        self.following=0

    def follow(self,user):
        user.follower+=1
        self.following+=1


user1 = User("harshul")
user2=User("ayushi")
user2.follow(user1)
print(user1.follower)
print(user2.follower)
print(user1.following)
print(user2.following)