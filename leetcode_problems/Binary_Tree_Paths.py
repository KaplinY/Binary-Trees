from dtos import Node

def print_paths(root):
    path = []
    print_path_rec(root,path,0)

def print_array(path, length):
    for i in range(length):
        if i != length - 1:
            print(path[i],"-> ",end="")
        else:
            print(path[i])

def print_path_rec(root,path,length):
    if root is None:
        return
    if(len(path) > length):
        path[length] = root.data
    else:
        path.append(root.data)
    length +=1

    if root.left is None and root.right is None:
        print_array(path, length)
    else:
        print_path_rec(root.left,path,length)
        print_path_rec(root.right,path,length)  
