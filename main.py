from dtos import Node
import random
from leetcode_problems.Invert_binary_tree import invert
from leetcode_problems.Binary_Tree_Paths import print_paths

root = Node(1)
for i in range(1,20):
    f = random.randrange(1,100)
    root.insert(f)
root.display()
invert(root)
root.display()
print_paths(root)