"""This module contains classes for User, UserDecorator, AdminDecorator, and LoginSystem."""

from typing import List
import post as posting


class BaseUser:
    """Base class for User"""
    def create_post(self):
        raise NotImplementedError

    def update_post(self):
        raise NotImplementedError

    def create_reply(self):
        raise NotImplementedError

    def update_reply(self):
        raise NotImplementedError


class Login:
    """Interface for Login"""
    def login(self, email, password):
        raise NotImplementedError

    def signUp(self, name, email, password):
        raise NotImplementedError


class User(BaseUser):
    """Class representing a User"""
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        self.posts = []
        self.replies = []

    def get_password(self) -> str:
        return self.password

    def create_post(self):
        post = input(f"{self.name}, enter your post content: ")
        self.posts.append(post)
        print(f"Post created: {post}")

    def update_post(self):
        if not self.posts:
            print("No posts to update.")
            return
        post_id = int(
            input(
                f"{self.name}, enter the post ID to update (0 to {len(self.posts)-1}): "
            )
        )
        if 0 <= post_id < len(self.posts):
            new_content = input("Enter new content: ")
            self.posts[post_id] = new_content
            print(f"Post updated to: {new_content}")
        else:
            print("Invalid post ID.")

    def create_reply(self):
        reply = input(f"{self.name}, enter your reply content: ")
        self.replies.append(reply)
        print(f"Reply created: {reply}")

    def update_reply(self):
        if not self.replies:
            print("No replies to update.")
            return
        reply_id = int(
            input(
                f"{self.name}, enter the reply ID to update (0 to {len(self.replies)-1}): "
            )
        )
        if 0 <= reply_id < len(self.replies):
            new_content = input("Enter new content: ")
            self.replies[reply_id] = new_content
            print(f"Reply updated to: {new_content}")
        else:
            print("Invalid reply ID.")


class UserDecorator(BaseUser):
    """Decorator class for User"""
    def __init__(self, wrapped_user: BaseUser):
        self.wrapped_user = wrapped_user

    def create_post(self):
        self.wrapped_user.create_post()

    def update_post(self):
        self.wrapped_user.update_post()

    def create_reply(self):
        self.wrapped_user.create_reply()

    def update_reply(self):
        self.wrapped_user.update_reply()


class AdminDecorator(UserDecorator):
    """Decorator class for Admin User"""
    def delete_post(self):
        if not self.wrapped_user.posts:
            print("No posts to delete.")
            return
        post_id = int(
            input(
                f"{self.wrapped_user.name}, enter the post ID to delete (0 to {len(self.wrapped_user.posts)-1}): "
            )
        )
        if 0 <= post_id < len(self.wrapped_user.posts):
            deleted_post = self.wrapped_user.posts.pop(post_id)
            print(f"Post deleted: {deleted_post}")
        else:
            print("Invalid post ID.")

    def delete_reply(self):
        if not self.wrapped_user.replies:
            print("No replies to delete.")
            return
        reply_id = int(
            input(
                f"{self.wrapped_user.name}, enter the reply ID to delete (0 to {len(self.wrapped_user.replies)-1}): "
            )
        )
        if 0 <= reply_id < len(self.wrapped_user.replies):
            deleted_reply = self.wrapped_user.replies.pop(reply_id)
            print(f"Reply deleted: {deleted_reply}")
        else:
            print("Invalid reply ID.")

    def create_forum(self):
        print("Forum created.")

    def delete_forum(self):
        print("Forum deleted.")


class LoginSystem(Login):
    """Class representing a Login System"""
    def __init__(self):
        self.users_list = []
        admin = User("admin", "admin@gmail.com", "admin")
        self.users_list.append(admin)

    def login(self, email, password):
        for user in self.users_list:
            if user.email == email and user.get_password() == password:
                print(f"User {user.name} logged in successfully.")
                return user
        print("Login failed. Invalid email or password.")
        return None

    def signUp(self, name, email, password):
        if name.lower() == "admin":
            print("Cannot sign up as admin.")
            return None
        user = User(name, email, password)
        self.users_list.append(user)
        print(f"User {name} signed up successfully.")
        return user


if __name__ == "__main__":
    login_system = LoginSystem()
    forums = []

    while True:
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login_system.signUp(name, email, password)

        elif choice == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            logged_in_user = login_system.login(email, password)

            if logged_in_user:
                if (
                    logged_in_user.name == "admin"
                    and logged_in_user.email == "admin@gmail.com"
                ):
                    # Admin menu
                    admin_user = AdminDecorator(logged_in_user)
                    while True:
                        print("1. Create Post")
                        print("2. Update Post")
                        print("3. Create Reply")
                        print("4. Update Reply")
                        print(
                            "5. Admin Options (delete post/reply, create/delete forum)"
                        )
                        print("6. Manage Forums")
                        print("7. Logout")
                        user_choice = input("Choose an option: ")

                        if user_choice == "1":
                            logged_in_user.create_post()
                        elif user_choice == "2":
                            logged_in_user.update_post()
                        elif user_choice == "3":
                            logged_in_user.create_reply()
                        elif user_choice == "4":
                            logged_in_user.update_reply()
                        elif user_choice == "5":
                            print("1. Delete Post")
                            print("2. Delete Reply")
                            print("3. Create Forum")
                            print("4. Delete Forum")
                            admin_choice = input("Choose an admin option: ")
                            if admin_choice == "1":
                                admin_user.delete_post()
                            elif admin_choice == "2":
                                admin_user.delete_reply()
                            elif admin_choice == "3":
                                admin_user.create_forum()
                            elif admin_choice == "4":
                                admin_user.delete_forum()
                        elif user_choice == "6":
                            print("1. Create Forum")
                            print("2. Manage Forums")
                            forum_choice = input("Choose a forum option: ")
                            if forum_choice == "1":
                                id = len(forums) + 1
                                name = input("Enter forum name: ")
                                description = input("Enter forum description: ")
                                forum = posting.Forum(id, name, description)
                                forums.append(forum)
                                print(f"Forum created: {name} - {description}")
                            elif forum_choice == "2":
                                for i, forum in enumerate(forums):
                                    print(f"{i+1}. {forum.name} - {forum.description}")
                                forum_id = (
                                    int(input("Enter the forum ID to manage: ")) - 1
                                )
                                if 0 <= forum_id < len(forums):
                                    forum = forums[forum_id]
                                    while True:
                                        print("1. Add Post")
                                        print("2. Edit Forum")
                                        print("3. Remove Forum")
                                        print("4. Back")
                                        manage_choice = input("Choose an option: ")
                                        if manage_choice == "1":
                                            post_id = len(forum.posts) + 1
                                            title = input("Enter post title: ")
                                            content = input("Enter post content: ")
                                            post = post.Post(post_id, title, content)
                                            forum.add(post)
                                            print(f"Post added: {title}")
                                        elif manage_choice == "2":
                                            forum.editContent()
                                        elif manage_choice == "3":
                                            forums.remove(forum)
                                            print("Forum removed.")
                                            break
                                        elif manage_choice == "4":
                                            break
                                        else:
                                            print("Invalid choice.")
                        elif user_choice == "7":
                            break
                        else:
                            print("Invalid choice.")
                else:
                    # Normal user menu
                    while True:
                        print("1. Create Post")
                        print("2. Update Post")
                        print("3. Create Reply")
                        print("4. Update Reply")
                        print("5. Logout")
                        user_choice = input("Choose an option: ")

                        if user_choice == "1":
                            logged_in_user.create_post()
                        elif user_choice == "2":
                            logged_in_user.update_post()
                        elif user_choice == "3":
                            logged_in_user.create_reply()
                        elif user_choice == "4":
                            logged_in_user.update_reply()
                        elif user_choice == "5":
                            break
                        else:
                            print("Invalid choice.")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")
