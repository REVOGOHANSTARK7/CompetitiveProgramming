'''
friendsOfFriends(d) [15 pts]
Background: we can create a dictionary mapping people to sets of their friends. For example, we might say:
d = { }
d["jon"] = set(["arya", "tyrion"])
d["tyrion"] = set(["jon", "jaime", "pod"])
d["arya"] = set(["jon"])
d["jaime"] = set(["tyrion", "brienne"])
d["brienne"] = set(["jaime", "pod"])
d["pod"] = set(["tyrion", "brienne", "jaime"])
d["ramsay"] = set()

With this in mind, write the function friendsOfFriends(d) that takes such a dictionary mapping people to sets of friends and returns a new dictionary mapping all the same people to sets of their friends of friends. For example, since Tyrion is a friend of Pod, and Jon is a friend of Tyrion, Jon is a friend-of-friend of Pod. This set should exclude any direct friends, so Jaime does not count as a friend-of-friend of Pod (since he is simply a friend of Pod) despite also being a friend of Tyrion's.

Thus, in this example, friendsOfFriends should return:
{
 'tyrion': {'arya', 'brienne'}, 
 'pod': {'jon'}, 
 'brienne': {'tyrion'}, 
 'arya': {'tyrion'}, 
 'jon': {'pod', 'jaime'}, 
 'jaime': {'pod', 'jon'}, 
 'ramsay': set()
}
'''
def readDict():
    a = {}
    n = int(input())
    for i in range(n):
        s = input().split()
        a[s[0]] = set(s[1:])
    return a

def friendsOfFriends(d):
    new=dict()
    for i in d:
        new[i]=set()
        for j in d[i]:
            if j in d:
                new[i].update(d[j]-d[i])
        new[i]=new[i]-set([i])
    d=new
    return(d)
d = friendsOfFriends(readDict())

for i in sorted(d.keys()):
    print(i, sorted(d[i]))