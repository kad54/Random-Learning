import tkinter as tk
from tkinter import filedialog

def search_and_replace():
    search_phrase = search_entry.get()
    replace_phrase = replace_entry.get()
    
    file_path = file_entry.get()
    
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
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

# Create the main window
window = tk.Tk()
window.title('Search and Replace')
window.geometry('400x200')

# Create the search phrase label and entry
search_label = tk.Label(window, text='Search phrase:')
search_label.pack()
search_entry = tk.Entry(window)
search_entry.pack()

# Create the replace phrase label and entry
replace_label = tk.Label(window, text='Replace phrase:')
replace_label.pack()
replace_entry = tk.Entry(window)
replace_entry.pack()

# Create the file selection button
file_button = tk.Button(window, text='Select File', command=open_file_dialog)
file_button.pack()

# Create the file entry field
file_entry = tk.Entry(window)
file_entry.pack()

# Create the replace button
replace_button = tk.Button(window, text='Replace', command=search_and_replace)
replace_button.pack()

# Create the result label
result_label = tk.Label(window, text='')
result_label.pack()

# Start the main event loop
window.mainloop()