import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def search_and_replace():
    search_phrase = search_text.get("1.0", tk.END).strip()
    replace_phrase = replace_text.get("1.0", tk.END).strip()

    file_path = file_entry.get().strip()

    if not search_phrase or not replace_phrase or not file_path:
        result_label.config(text='Please provide all required information.')
        return

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        replaced_content = file_content.replace(search_phrase, replace_phrase)

        with open(file_path, 'w') as file:
            file.write(replaced_content)

        result_label.config(text='Replacement completed.')

    except FileNotFoundError:
        result_label.config(text='File not found.')

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)

# Create the main window
window = tk.Tk()
window.title('Search and Replace')
window.geometry('400x400')

# Create a style for ttk widgets
style = ttk.Style()
style.theme_use('default')
style.configure('TLabel', font=('Arial', 11))
style.configure('TButton', font=('Arial', 11))

# Create a frame for search phrase
search_frame = ttk.Frame(window)
search_frame.pack(pady=20)

search_label = ttk.Label(search_frame, text='Search phrase:')
search_label.pack(side=tk.LEFT, padx=5)

search_text = tk.Text(search_frame, height=5, width=30, font=('Arial', 11))
search_text.pack(side=tk.LEFT, padx=5)

# Create a frame for replace phrase
replace_frame = ttk.Frame(window)
replace_frame.pack(pady=10)

replace_label = ttk.Label(replace_frame, text='Replace phrase:')
replace_label.pack(side=tk.LEFT, padx=5)

replace_text = tk.Text(replace_frame, height=5, width=30, font=('Arial', 11))
replace_text.pack(side=tk.LEFT, padx=5)

# Create the file selection section
file_frame = ttk.Frame(window)
file_frame.pack(pady=10)

file_label = ttk.Label(file_frame, text='File:')
file_label.pack(side=tk.LEFT, padx=5)

file_entry = ttk.Entry(file_frame, width=30, font=('Arial', 11))
file_entry.pack(side=tk.LEFT, padx=5)

file_button = ttk.Button(file_frame, text='Select', command=open_file_dialog)
file_button.pack(side=tk.LEFT, padx=5)

# Create the replace button
replace_button = ttk.Button(window, text='Replace', command=search_and_replace)
replace_button.pack(pady=20)

# Create the result label
result_label = ttk.Label(window, text='', font=('Arial', 11), foreground='green')
result_label.pack()

# Configure window padding
window.configure(padx=20, pady=20)

# Start the main event loop
window.mainloop()
