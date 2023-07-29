import tkinter as tk
from linkedin_automation import LinkedInAutomation

def send_connections():
    # Get LinkedIn credentials from the user
    username = username_entry.get()
    password = password_entry.get()

    # Initialize the automation class
    linkedin_bot = LinkedInAutomation()

    # Log in to LinkedIn
    linkedin_bot.login(username, password)

    # Send connection requests to potential connections
    linkedin_bot.send_connection_requests()

    # Clear input fields
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Create the main application window
app = tk.Tk()
app.title("LinkMate - LinkedIn Connection Automator")

# Create labels and entry fields for LinkedIn credentials
username_label = tk.Label(app, text="LinkedIn Username/Email:")
username_label.pack()
username_entry = tk.Entry(app)
username_entry.pack()

password_label = tk.Label(app, text="LinkedIn Password:")
password_label.pack()
password_entry = tk.Entry(app, show="*")
password_entry.pack()

# Create a button to send connections
send_button = tk.Button(app, text="Send Connections", command=send_connections)
send_button.pack()

# Start the main application event loop
app.mainloop()
