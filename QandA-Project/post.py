"""This module contains the classes for the Composite pattern. The classes are used to represent the forums, posts, and replies in the Q&A system."""
class Component:
    """Component class for the Composite pattern. This class is the base"""

    def add(self, component):
        raise NotImplementedError

    def remove(self, component):
        raise NotImplementedError

    def getChild(self, index):
        raise NotImplementedError

    def editContent(self):
        raise NotImplementedError

    def getID(self):
        raise NotImplementedError


class Forum(Component):
    """Concrete class implementing the Component interface for forums"""

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.posts = []

    def add(self, component):
        self.posts.append(component)

    def remove(self, component):
        self.posts.remove(component)

    def getChild(self, index):
        if 0 <= index < len(self.posts):
            return self.posts[index]
        return None

    def editContent(self):
        self.name = input(f"Forum {self.id}, enter new name: ")
        self.description = input(f"Forum {self.id}, enter new description: ")
        print(f"Forum updated: {self.name} - {self.description}")

    def getID(self):
        return self.id


class Post(Component):
    """Concrete class implementing the Component interface for posts"""

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.votes = {"upvotes": 0, "downvotes": 0}
        self.replies = []

    def add(self, component):
        self.replies.append(component)

    def remove(self, component):
        self.replies.remove(component)

    def getChild(self, index):
        if 0 <= index < len(self.replies):
            return self.replies[index]
        return None

    def editContent(self):
        self.title = input(f"Post {self.id}, enter new title: ")
        self.content = input(f"Post {self.id}, enter new content: ")
        print(f"Post updated: {self.title} - {self.content}")

    def getID(self):
        return self.id


class Reply(Component):
    """Concrete class implementing the Component interface for replies"""

    def __init__(self, id, content):
        self.id = id
        self.content = content

    def add(self, component):
        pass  

    def remove(self, component):
        pass  

    def getChild(self, index):
        return None  

    def editContent(self):
        self.content = input(f"Reply {self.id}, enter new content: ")
        print(f"Reply updated: {self.content}")

    def getID(self):
        return self.id
