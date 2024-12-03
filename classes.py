class Item:

    def __init__(self, item_id, title, author):
        self.id = item_id
        self.title = title
        self.author = author
        self.is_available = True
    def __str__(self):
        return f"{self.title} by {self.author} (ID: {self.id})"

class Book(Item):

    def __init__(self, item_id, title, author, genre, pages):
        super().__init__(item_id, title, author)
        self.genre = genre
        self.pages = pages

class User:

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.borrowed_items = []

    def borrow_item(self, item):
        if item.is_available:
            item.is_available = False
            self.borrowed_items.append(item)
            print(f"{self.name} borrowed {item.title}.")
        else:
            print(f"{item.title} is not available.")

    def return_item(self, item):
        if item in self.borrowed_items:
            item.is_available = True
            self.borrowed_items.remove(item)
            print(f"{self.name} returned {item.title}")
        else:
            print(f"{self.name} doesn't have {item.title}")

    def get_info(self):
        borrowed_titles = ", ".join([item.title for item in self.borrowed_items])
        print(f"User {self.name} has borrowed: {borrowed_titles or 'No items'} (ID: {self.user_id})")

class Library:

    def __init__(self):
        self.catalog = []
        self.users = []

    def add_item(self, item):
        self.catalog.append(item)
        print(f"Added {item.title} to the catalog.")

    def register_user(self,user):
        self.users.append(user)
        print(f"User {user.name} is registered.")

    def lend_item(self, item, user):
        user.borrow_item(item)

    def return_item(self, item, user):
        user.return_item(item)

    def search_catalog(self, query):
        results = [
            item for item in self.catalog
            if query.lower() in item.title.lower() or query.lower() in item.author.lower()
        ]
        if results:
            print(f"Found {len(results)} item(s):")
            for item in results:
                print(f"- {item}")
        else:
            print("No items found matching your query.")
