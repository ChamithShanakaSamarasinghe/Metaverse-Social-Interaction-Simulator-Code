class User:
    def __init__(self, username):
        self.username = username
        self.friends = []
        self.messages = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)
            print(f"{friend.username} has been added to your friends list.")
        else:
            print(f"{friend.username} is already your friend.")

    def send_message(self, friend, message):
        if friend in self.friends:
            friend.messages.append((self.username, message))
            print(f"Message sent to {friend.username}: '{message}'")
        else:
            print(f"{friend.username} is not in your friends list.")

    def view_messages(self):
        if self.messages:
            print(f"\nMessages for {self.username}:")
            for sender, message in self.messages:
                print(f"{sender}: {message}")
        else:
            print("No messages.")

    def view_friends(self):
        if self.friends:
            print(f"\nFriends of {self.username}:")
            for friend in self.friends:
                print(friend.username)
        else:
            print("No friends added.")

def main():
    users = {}
    
    # Create users
    while True:
        username = input("\nEnter a username (or type 'exit' to finish): ")
        if username.lower() == 'exit':
            break
        if username in users:
            print("Username already taken. Please choose another one.")
        else:
            users[username] = User(username)
            print(f"User {username} created.")

    # User interactions
    while True:
        print("\n--- Menu ---")
        print("1. Add Friend")
        print("2. Send Message")
        print("3. View Messages")
        print("4. View Friends")
        print("5. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            username = input("Enter your username: ")
            friend_username = input("Enter your friend's username: ")
            if username in users and friend_username in users:
                users[username].add_friend(users[friend_username])
            else:
                print("Invalid usernames.")
        elif choice == '2':
            username = input("Enter your username: ")
            friend_username = input("Enter your friend's username: ")
            message = input("Enter your message: ")
            if username in users and friend_username in users:
                users[username].send_message(users[friend_username], message)
            else:
                print("Invalid usernames.")
        elif choice == '3':
            username = input("Enter your username: ")
            if username in users:
                users[username].view_messages()
            else:
                print("Invalid username.")
        elif choice == '4':
            username = input("Enter your username: ")
            if username in users:
                users[username].view_friends()
            else:
                print("Invalid username.")
        elif choice == '5':
            print("Exiting the simulator.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
