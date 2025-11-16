from tkinter import *
import tkinter as tk
from tkinter import messagebox, PhotoImage
import random
from PIL import ImageTk, Image
import os
# window
window = tk.Tk()
window.title("Pizza App")
window.state("zoomed")
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img)
#images
ham_pizza_img = load_image("images/image(1).png", 100, 100)#adjust the height of the imgaes here
veg_pizza_img = load_image("images/image(2).png", 100, 100)
cheese_pizza_img = load_image("images/image(3).png", 100, 100)
meat_pizza_img = load_image("images/image(4).png", 100, 100)
huwain_pizza_img = load_image("images/image(5).png", 100, 100)
diavola_pizza_img = load_image("images/image(6).png", 100, 100)
supreme_pizza_img = load_image("images/image(7).png", 100, 100)
mushroom_pizza_img = load_image("images/image(8).png", 100, 100)
spicy_img = load_image("images/image(9).png", 100, 100)
four_cheese_pizza_img = load_image("images/image(11).png", 100, 100)
marg_pizza_img = load_image("images/image(10).png", 100, 100)
# pizza lists 
pizza_data = {
    "Margharita Pizza": {"desc": "A perfect harmony of fresh tomato sauce \ncreamy mozzarella, and fragrant basil, baked to perfection.", "image": ham_pizza_img, "price": 8},
    "Diavola": {"desc": "Topped with spicy Italian salami, mozzarella \nand a rich tomato sauce, this pizza packs a fiery punch in every bite.", "image": veg_pizza_img, "price": 10},
    "Vegetariana": {"desc": "Topped with fresh vegetables and mozzarella\nfor a healthy, flavorful option.", "image": cheese_pizza_img, "price": 12},
    "Quattro Formaggi": {"desc": "A decadent blend of four cheeses – mozzarella \ngorgonzola, parmesan, and fontina.", "image": cheese_pizza_img, "price": 14},
    "Pollo alla Griglia": {"desc": "Grilled chicken with cheese and tomato sauce.", "image": meat_pizza_img, "price": 9},
    "Carnivora": {"desc": "Loaded with pepperoni, ham, sausage\nand bacon over a luscious tomato base and mozzarella.", "image": huwain_pizza_img, "price": 11},
    "Capricciosa": {"desc": "Ham, mushrooms, artichokes, olives \nand mozzarella come together in a flavor-packed pizza.", "image": diavola_pizza_img, "price": 13},
    "Pollo Piccante": {"desc": "Spicy chicken, hot chili peppers, and mozzarella.", "image": supreme_pizza_img, "price": 15},
    "Prosciutto e Ananas": {"desc": "Thin slices of prosciutto paired with juicy pineapple,\nmozzarella, and tomato sauce.", "image": mushroom_pizza_img, "price": 12},
    "Spicy Jalapeno Pizza": {"desc": "Ricotta, mozzarella, and a drizzle of olive oil, baked to perfection.", "image": spicy_img, "price": 11},
    "Marinara": {"desc": "Savory tomato sauce, garlic, oregano \nand a hint of olive oil, baked with love.", "image": marg_pizza_img, "price": 16},
}
deal_pizza = random.choice(list(pizza_data.keys()))
deal_text = f"Deal of the Day: Buy 1 Get 1 Free on {deal_pizza}!"
cart = []#the cart
cart_total = tk.DoubleVar(value=0.0)
def add_to_cart(pizza_name, price, customizations=""):
    item_text = f"{pizza_name} {customizations} - ${price:.2f}"
    if pizza_name == deal_pizza:
        cart.append({"text": item_text, "price": price})
        cart.append({"text": item_text + " (fre)", "price": 0})
        cart_listbox.insert(END, item_text)
        cart_listbox.insert(END, item_text + " (free)")
        cart_total.set(cart_total.get() + price)
    else:
        cart.append({"text": item_text, "price": price})
        cart_listbox.insert(END, item_text)
        cart_total.set(cart_total.get() + price)
def remove_cart_item(event):
    try:
        selected_index = cart_listbox.curselection()[0]
    except IndexError:
        return
    item = cart.pop(selected_index)
    cart_listbox.delete(selected_index)
    cart_total.set(cart_total.get() - item["price"])
# theme idk if we will keep it
def apply_theme(theme_name):
    pass
#no themes fo now
# Pizza customization
def customize_pizza(pizza_name, base_price):
    top = Toplevel(window)
    top.title(f"Customize {pizza_name}")
    top.geometry("400x600")
    Label(top, text=f"Customize {pizza_name}", font=("Arial", 16, "bold")).pack(pady=10)
    # size
    Label(top, text="Choose Size:", font=("Arial", 12)).pack(anchor="w", padx=10)
    size_var = StringVar(value="Medium")
    size_prices = {"Small": -2, "Medium": 0, "Large": 6} #change price addition
    for size in size_prices:
        Radiobutton(top, text=f"{size} (+${size_prices[size]})", variable=size_var, value=size).pack(anchor="w", padx=20)
    # Crust
    Label(top, text="Choose Crust:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10,0))
    crust_var = StringVar(value="Regular")
    for crust in ["Regular", "Thin", "Cheese stuffed"]:
        Radiobutton(top, text=crust, variable=crust_var, value=crust).pack(anchor="w", padx=20)
    # Toppings
    Label(top, text="Extra Toppings:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10,0))
    topping_vars = {}
    for topping in ["Mushrooms", "Olives", "Peppers", "Onions", "Bacon","Extra Sauce"]:
        var = BooleanVar()
        Checkbutton(top, text=topping, variable=var).pack(anchor="w", padx=20)
        topping_vars[topping] = var
    # Slices
    Label(top, text="Number of Slices:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=(10,0))
    slices_var = IntVar(value=8)
    Spinbox(top, from_=1, to=8, textvariable=slices_var).pack(anchor="w", padx=20)
    def confirm_customization():
        final_price = base_price
        size_choice = size_var.get()
        final_price += size_prices[size_choice]
        crust_choice = crust_var.get()
        if "Cheese Burst" in crust_choice:
            final_price += 2
        chosen_toppings = [t for t, v in topping_vars.items() if v.get()]
        if chosen_toppings:
            final_price += len(chosen_toppings)
        num_slices = slices_var.get()
        final_price = final_price * (num_slices / 8)
        custom_text = f"({size_choice}, {crust_choice}"
        if chosen_toppings:
            custom_text += ", Toppings: " + ", ".join(chosen_toppings)
        custom_text += f", {num_slices} slices)"
        add_to_cart(pizza_name, final_price, custom_text)
        top.destroy()
        messagebox.showinfo("Pizza Customized", f"{pizza_name} added to cart with customizations!")
    Button(top, text="Add to Cart", command=confirm_customization).pack(pady=20)
# the layout
main_frame = Frame(window)
main_frame.pack(fill="both", expand=True)
left_frame = Frame(main_frame)
left_frame.pack(side="left", fill="both", expand=True)
right_frame = Frame(main_frame, width=400, bd=2, relief="sunken")
right_frame.pack(side="right", fill="y")
# Search bar
search_var = StringVar()
search_entry = Entry(left_frame, textvariable=search_var, font=("Arial", 12))
search_entry.pack(pady=10)
canvas = Canvas(left_frame)
scrollbar = Scrollbar(left_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)
scroll_frame = Frame(canvas)
canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
# show the pizzas
def show_pizzas(pizzas):
    for widget in scroll_frame.winfo_children():
        widget.destroy()
    if not pizzas:
        Label(scroll_frame, text="No pizzas found!", font=("Arial", 16)).pack(pady=20)
        return
    for pizza_name in pizzas:
        pizza = pizza_data[pizza_name]
        frame = Frame(scroll_frame, pady=10, padx=10, relief="raised", bd=2)
        frame.pack(fill="x", pady=5, padx=10)
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=3)
        # Pizza name
        Label(frame, text=pizza_name, font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, sticky="w", pady=(0,5))
        # Pizza image
        Label(frame, image=pizza["image"]).grid(row=1, column=0, sticky="nsew")
        # Pizza description
        desc_label = Label(frame, text=pizza["desc"], font=("Arial", 10), justify="left")
        desc_label.grid(row=1, column=1, sticky="nsew", padx=10)
        frame.update_idletasks()
        col_width = frame.grid_bbox(column=1)[2]
        desc_label.config(wraplength=col_width)
        # buttons
        btn_frame = Frame(frame)
        btn_frame.grid(row=2, column=0, columnspan=2, pady=5, sticky="ew")
        Button(btn_frame, text=f"Add to Cart (${pizza['price']})",
               command=lambda n=pizza_name, p=pizza["price"]: add_to_cart(n, p)).pack(side="left", padx=5)
        Button(btn_frame, text="Customize",
               command=lambda n=pizza_name, p=pizza["price"]: customize_pizza(n, p)).pack(side="left", padx=5)
def update_display(*args):
    search_term = search_var.get().strip().lower()
    matching_pizzas = [name for name in pizza_data if search_term in name.lower()] if search_term else list(pizza_data.keys())
    show_pizzas(matching_pizzas)
search_var.trace("w", update_display)
# randomizes the deal of the day
deal_frame = Frame(right_frame, pady=10, padx=10, bd=2, relief="ridge")
deal_frame.pack(fill="x", pady=10, padx=10)
Label(deal_frame, text=deal_text, font=("Arial", 14, "bold"), fg="red").pack()
# cart panel
cart_frame = Frame(right_frame, bd=2, relief="sunken", pady=5)
cart_frame.pack(fill="both", expand=True, padx=10, pady=10)
Label(cart_frame, text="Shopping Cart", font=("Arial", 14, "bold")).pack(anchor="w")
cart_listbox = Listbox(cart_frame, height=15)
cart_listbox.pack(fill="both", expand=True, padx=10, pady=5)
cart_listbox.bind("<Button-3>", remove_cart_item)
Label(cart_frame, text="Total:", font=("Arial", 12, "bold")).pack(anchor="e", padx=10)
Label(cart_frame, textvariable=cart_total, font=("Arial", 16, "bold"), fg="green").pack(anchor="e", padx=10, pady=5)

def checkout():
    if not cart:
        messagebox.showwarning("Cart Empty", "Your cart is empty!")
        return
    top = Toplevel(window)
    top.title("Checkout")
    top.state("zoomed")
    Label(top, text="Order Summary", font=("Arial", 16, "bold")).pack(pady=10)
    order_frame = Frame(top)
    order_frame.pack(fill="both", expand=True, padx=10)
    canvas = Canvas(order_frame)
    scrollbar = Scrollbar(order_frame, orient="vertical", command=canvas.yview)
    scroll_frame = Frame(canvas)
    scroll_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scroll_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    # Display cart items
    for item in cart:
        Label(scroll_frame, text=item["text"], font=("Arial", 12)).pack(anchor="w", pady=2)
    # Total price
    Label(top, text=f"Total: ${cart_total.get():.2f}", font=("Arial", 14, "bold"), fg="green").pack(pady=10)
    order_id = f"ORD{random.randint(1000,9999)}"
    Label(top, text=f"Order ID: {order_id}", font=("Arial", 12, "bold")).pack(pady=5)
    def confirm_order():
        log_file = r".venv/logs/logs.txt"
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        with open(log_file, "a") as f:
            f.write(f"Order ID: {order_id}\n")
            for item in cart:
                f.write(f"{item['text']}\n")
            f.write(f"Total: ${cart_total.get():.2f}\n")
            f.write("-" * 40 + "\n")
        messagebox.showinfo("Order Placed", f"Your order {order_id} has been placed")
        top.destroy()
        cart.clear()
        cart_listbox.delete(0, END)
        cart_total.set(0.0)
    Button(top, text="Confirm Order", font=("Arial", 12, "bold"), command=confirm_order).pack(pady=20)
Button(cart_frame, text="Checkout", font=("Arial", 12, "bold"), command=checkout).pack(pady=10)
# show all pizzas initially
show_pizzas(list(pizza_data.keys()))
menubar = Menu(window)
window.config(menu=menubar)
window.mainloop()
