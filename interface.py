import tkinter as tk
from tkinter import messagebox
from classes import *


class LibraryApp:

    def __init__(self, root):
        self.library = Library()
        self.root = root
        self.root.title("Library System")

        self.setup_ui()

    def setup_ui(self):
        self.tabs = tk.Frame(self.root)
        self.tabs.pack()

        self.catalog_tab_button = tk.Button(self.tabs, text="Catalog", command=self.open_catalog_tab)
        self.catalog_tab_button.pack(side=tk.LEFT)

        self.users_tab_button = tk.Button(self.tabs, text="Users", command=self.open_users_tab)
        self.users_tab_button.pack(side=tk.LEFT)

        self.search_tab_button = tk.Button(self.tabs, text="Search", command=self.open_search_tab)
        self.search_tab_button.pack(side=tk.LEFT)

        self.content_frame = tk.Frame(self.root)
        self.content_frame.pack()

        self.open_catalog_tab()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def open_catalog_tab(self):
        self.clear_content()

        tk.Label(self.content_frame, text="Catalog Management").pack()

        tk.Label(self.content_frame, text="Title:").pack()
        self.title_entry = tk.Entry(self.content_frame)
        self.title_entry.pack()

        tk.Label(self.content_frame, text="Author:").pack()
        self.author_entry = tk.Entry(self.content_frame)
        self.author_entry.pack()

        tk.Label(self.content_frame, text="Genre:").pack()
        self.genre_entry = tk.Entry(self.content_frame)
        self.genre_entry.pack()

        tk.Label(self.content_frame, text="Pages:").pack()
        self.pages_entry = tk.Entry(self.content_frame)
        self.pages_entry.pack()

        tk.Button(self.content_frame, text="Add Book", command=self.add_book).pack()

        tk.Button(self.content_frame, text="Show Catalog", command=self.show_catalog).pack()

    def open_users_tab(self):
        self.clear_content()

        tk.Label(self.content_frame, text="User Management").pack()

        tk.Label(self.content_frame, text="Name:").pack()
        self.user_name_entry = tk.Entry(self.content_frame)
        self.user_name_entry.pack()

        tk.Button(self.content_frame, text="Register User", command=self.register_user).pack()

        tk.Button(self.content_frame, text="Show Users", command=self.show_users).pack()

    def open_search_tab(self):
        self.clear_content()

        tk.Label(self.content_frame, text="Search Catalog").pack()

        tk.Label(self.content_frame, text="Query:").pack()
        self.search_query_entry = tk.Entry(self.content_frame)
        self.search_query_entry.pack()

        tk.Button(self.content_frame, text="Search", command=self.search_catalog).pack()

        self.search_results = tk.Text(self.content_frame, height=10, width=50)
        self.search_results.pack()

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        genre = self.genre_entry.get()
        pages = self.pages_entry.get()

        if title and author and genre and pages.isdigit():
            book = Book(len(self.library.catalog) + 1, title, author, genre, int(pages))
            self.library.add_item(book)
            messagebox.showinfo("Success", f"Added book: {title}")
        else:
            messagebox.showerror("Error", "Please fill all fields correctly.")

    def register_user(self):
        name = self.user_name_entry.get()
        if name:
            user = User(len(self.library.users) + 1, name)
            self.library.register_user(user)
            messagebox.showinfo("Success", f"Registered user: {name}")
        else:
            messagebox.showerror("Error", "Please enter a name.")

    def show_catalog(self):
        catalog_window = tk.Toplevel(self.root)
        catalog_window.title("Catalog")

        if self.library.catalog:
            tk.Label(catalog_window, text="Current Catalog:").pack()
            for item in self.library.catalog:
                tk.Label(catalog_window, text=str(item)).pack()
        else:
            tk.Label(catalog_window, text="Catalog is empty.").pack()

    def show_users(self):
        users_window = tk.Toplevel(self.root)
        users_window.title("Users")

        if self.library.users:
            tk.Label(users_window, text="Registered Users:").pack()
            for user in self.library.users:
                borrowed_items = ", ".join([item.title for item in user.borrowed_items]) or "No items"
                tk.Label(users_window, text=f"{user.name} (ID: {user.user_id}) - Borrowed: {borrowed_items}").pack()
        else:
            tk.Label(users_window, text="No registered users.").pack()

    def search_catalog(self):
        query = self.search_query_entry.get()
        results = [
            str(item) for item in self.library.catalog
            if query.lower() in item.title.lower() or query.lower() in item.author.lower()
        ]
        self.search_results.delete(1.0, tk.END)

        if results:
            self.search_results.insert(tk.END, "\n".join(results))
        else:
            self.search_results.insert(tk.END, "No items found.")
