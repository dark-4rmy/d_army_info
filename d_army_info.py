import whois
import socket
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

# Function to get WHOIS data using 'whois' Python library
def get_whois_data(domain):
    try:
        domain_info = whois.whois(domain)
        return domain_info
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while fetching WHOIS data: {e}")
        return None

# Function to resolve domain to IP address using 'socket'
def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while resolving IP address: {e}")
        return None

# Function to draw relationships graph
def draw_graph(domain, ip_address, whois_data):
    G = nx.Graph()

    # Add the domain and IP address nodes
    G.add_node(domain)
    if ip_address:
        G.add_edge(domain, ip_address)

    # Add WHOIS related nodes (e.g., registrar, nameservers)
    if whois_data:
        if whois_data.registrar:
            G.add_edge(domain, whois_data.registrar)

        if whois_data.name_servers:
            for ns in whois_data.name_servers:
                G.add_edge(domain, ns)

    # Plot the graph with colors
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', font_weight='bold', font_size=10, edge_color='orange')
    plt.title("d-army Information Graph", fontsize=15, fontweight='bold', color='navy')
    plt.show()

# Function for the GUI and data input
def start_tool():
    root = tk.Tk()
    root.title("d-army informations getting IP or URL")  # Set the window title
    root.geometry("400x200")  # Set the window size
    root.config(bg='lightgray')  # Background color

    # Add a label
    label = ttk.Label(root, text="Enter a domain or URL:", background='lightgray', font=("Arial", 14))
    label.pack(pady=20)

    # Add an entry box
    domain_entry = ttk.Entry(root, width=30)
    domain_entry.pack(pady=10)

    # Add a button to submit
    def on_submit():
        domain = domain_entry.get()
        if domain:
            whois_data = get_whois_data(domain)
            ip_address = get_ip_address(domain)

            if whois_data or ip_address:
                messagebox.showinfo("Domain Info", f"Domain: {domain}\nIP Address: {ip_address}\nRegistrar: {whois_data.registrar if whois_data else 'N/A'}")
                # Draw the graph
                draw_graph(domain, ip_address, whois_data)
            else:
                messagebox.showerror("Error", "Failed to retrieve data.")
        else:
            messagebox.showerror("Error", "Please enter a valid domain.")

    submit_button = ttk.Button(root, text="Get Info", command=on_submit)
    submit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    start_tool()
