import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# Connect to Django database
DB_PATH = "db.sqlite3"  # Ensure this matches your Django project's database

# Function to add a movie
def add_movie():
    title = title_entry.get()
    genre = genre_entry.get()
    year = year_entry.get()
    status = status_var.get()

    if title and genre and year.isdigit():
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO movies_movie (title, genre, release_year, status) VALUES (?, ?, ?, ?)",
                       (title, genre, int(year), status))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Movie added successfully!")
        refresh_movies()
    else:
        messagebox.showerror("Error", "Please enter valid movie details.")

# Function to load movies
def refresh_movies():
    tree.delete(*tree.get_children())
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, genre, release_year, status FROM movies_movie")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# GUI setup
root = tk.Tk()
root.title("Movie Watchlist")

# Input fields
tk.Label(root, text="Title:").grid(row=0, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Genre:").grid(row=1, column=0)
genre_entry = tk.Entry(root)
genre_entry.grid(row=1, column=1)

tk.Label(root, text="Release Year:").grid(row=2, column=0)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1)

tk.Label(root, text="Status:").grid(row=3, column=0)
status_var = tk.StringVar(value="to_watch")
ttk.Combobox(root, textvariable=status_var, values=["watched", "to_watch"]).grid(row=3, column=1)

# Buttons
tk.Button(root, text="Add Movie", command=add_movie).grid(row=4, column=0, columnspan=2)

# Movie List
tree = ttk.Treeview(root, columns=("Title", "Genre", "Year", "Status"), show="headings")
tree.heading("Title", text="Title")
tree.heading("Genre", text="Genre")
tree.heading("Year", text="Year")
tree.heading("Status", text="Status")
tree.grid(row=5, column=0, columnspan=2)

refresh_movies()

# Run the application
root.mainloop()
