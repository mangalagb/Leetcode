# Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path, return a list
# that only contains this file's name. If it is a directory path, return
# the list of file and directory names in this directory. Your output
# (file and directory names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist, you should make a
# new directory according to the path. If the middle directories in the
#  path don't exist either, you should create them as well. This function
# has void return type.
#
# addContentToFile: Given a file path and file content in string format.
# If the file doesn't exist, you need to create that file containing given
# content. If the file already exists, you need to append given content to
# original content. This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.


class Node:
    def __init__(self, name = None):
        self.name = name
        self.is_file = False
        self.children = {}
        self.content = None


class FileSystem:
    def __init__(self):
        self.root = Node("/")

    def ls(self, path):
        result_node = self.traverse(path)
        result = []

        if result_node.is_file:
            result.append(result_node.name)
        else:
            result = sorted(result_node.children.keys())
        return result


    def mkdir(self, path):
        self.traverse(path)


    def addContentToFile(self, filePath, content):
        node = self.traverse(filePath)
        node.is_file = True
        if not node.content:
            node.content = content
        else:
            node.content += content


    def readContentFromFile(self, filePath):
        node = self.traverse(filePath)
        if not node.is_file:
            return ""

        return node.content


    def traverse(self, path):
        dirs = path.split("/")

        current = self.root

        for dir in dirs:
            if dir is "":
                continue

            if dir not in current.children:
                child = Node(dir)
                current.children[dir] = child

            current = current.children[dir]
        return current


fs = FileSystem()
print(fs.ls("/"))
print(fs.mkdir("/a/b/c"))
print(fs.addContentToFile("/a/b/c/d", "hello"))
print(fs.ls("/"))
print(fs.readContentFromFile("/a/b/c/d"))
