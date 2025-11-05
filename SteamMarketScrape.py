import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import requests
from urllib.parse import quote
import csv
from datetime import datetime
import webbrowser

APPID = 730  # CS2
CURRENCY = 1  # USD
HEADERS = {"User-Agent": "Mozilla/5.0"}

DEFAULT_ITEMS = [
    "MAC-10 | Neon Rider (Field-Tested)",
    "MP7 | Bloodsport (Field-Tested)",
    "MP7 | Bloodsport (Minimal Wear)",
    "Five-SeveN | Angry Mob (Field-Tested)",
    "Five-SeveN | Angry Mob (Minimal Wear)",
    "AUG | Chameleon (Field-Tested)",
    "M4A4 | Temukau (Minimal Wear)",
    "AK-47 | The Oligarch (Minimal Wear)",
    "★ Bowie Knife | Marble Fade (Factory New)",
    "★ Huntsman Knife | Slaughter (Minimal Wear)",
    "★ Moto Gloves | Blood Pressure (Field-Tested)",
    "★ Specialist Gloves | Marble Fade (Field-Tested)",
    "★ Moto Gloves | Polygon (Field-Tested)",
    "Sealed Genesis Terminal"

]

def make_price_url(market_hash_name: str) -> str:
    return f"https://steamcommunity.com/market/priceoverview/?currency={CURRENCY}&appid={APPID}&market_hash_name={quote(market_hash_name, safe='')}"

class SteamPriceChecker:
    def __init__(self, root):
        self.root = root
        root.title("Steam Market Price Checker")
        root.geometry("1200x600")

        self.last_prices = {}
        self.counts = {}

        # --- Top Frame ---
        top = tk.Frame(root)
        top.pack(fill="x", padx=8, pady=6)
        tk.Label(top, text="Item name (paste full market name):").pack(anchor="w")
        self.item_entry = tk.Entry(top)
        self.item_entry.pack(fill="x", pady=4)
        btn_frame = tk.Frame(top)
        btn_frame.pack(fill="x", pady=2)
        tk.Button(btn_frame, text="Add Item", command=self.add_item).pack(side="left")
        tk.Button(btn_frame, text="Remove Selected", command=self.remove_selected).pack(side="left", padx=6)

        # --- Treeview ---
        columns = ("Item", "Lowest Price", "Median Price", "Volume", "Checked At", "% Change", "Count")
        self.tree = ttk.Treeview(root, columns=columns, show="headings", selectmode="browse")
        for col in columns:
            self.tree.heading(col, text=col)
            if col == "Item":
                self.tree.column(col, width=360, anchor="w")
            elif col == "Count":
                self.tree.column(col, width=80, anchor="center")
            else:
                self.tree.column(col, width=110, anchor="center")
        self.tree.pack(fill="both", expand=True, padx=8, pady=6)

        # --- Bottom Buttons ---
        bottom = tk.Frame(root)
        bottom.pack(fill="x", padx=8, pady=6)
        tk.Button(bottom, text="Check Prices", command=self.fetch_prices).pack(side="left")
        tk.Button(bottom, text="Open Market Page", command=self.open_selected_in_browser).pack(side="left", padx=8)
        tk.Button(bottom, text="Save CSV", command=self.save_csv).pack(side="left")
        tk.Button(bottom, text="Load Defaults", command=self.load_defaults).pack(side="right")

        # --- Counter Controls ---
        counter_frame = tk.Frame(root)
        counter_frame.pack(fill="x", pady=4)
        tk.Button(counter_frame, text="+", width=4, command=self.increment_count).pack(side="left", padx=4)
        tk.Button(counter_frame, text="-", width=4, command=self.decrement_count).pack(side="left", padx=4)
        self.total_label = tk.Label(counter_frame, text="Total Value: $0.00", font=("Segoe UI", 10, "bold"))
        self.total_label.pack(side="right", padx=8)

        self.items = []
        self.load_defaults()

    def load_defaults(self):
        self.items = DEFAULT_ITEMS.copy()
        self.refresh_tree_empty()

    def refresh_tree_empty(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for item in self.items:
            self.tree.insert("", "end", values=(item, "-", "-", "-", "-", "-", 0))
            self.counts[item] = 0

    def add_item(self):
        val = self.item_entry.get().strip()
        if not val:
            messagebox.showinfo("Add Item", "Please paste full market name.")
            return
        self.items.append(val)
        self.counts[val] = 0
        self.item_entry.delete(0, tk.END)
        self.refresh_tree_empty()

    def remove_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Remove Item", "Select a row to remove.")
            return
        idx = self.tree.index(sel[0])
        del self.counts[self.items[idx]]
        del self.items[idx]
        self.refresh_tree_empty()

    def fetch_prices(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        for item in self.items:
            lowest = median = volume = "-"
            percent_change = "-"
            checked_at = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

            try:
                url = make_price_url(item)
                resp = requests.get(url, headers=HEADERS, timeout=10)
                data = resp.json() if resp.status_code == 200 and resp.text else {}
                if data.get("success"):
                    lowest = data.get("lowest_price", "-")
                    median = data.get("median_price", "-")
                    volume = data.get("volume", "-")

                    # --- Calculate % Change ---
                    try:
                        current_price = float(lowest.replace("$", "").replace(",", ""))
                        if item in self.last_prices:
                            old_price = self.last_prices[item]
                            if old_price != 0:
                                change = (current_price - old_price) / old_price * 100
                                percent_change = f"{change:+.2f}%"
                        self.last_prices[item] = current_price
                    except Exception:
                        percent_change = "-"
            except Exception:
                lowest = median = volume = percent_change = "Error"

            count = self.counts.get(item, 0)
            self.tree.insert("", "end", values=(item, lowest, median, volume, checked_at, percent_change, count))

        self.update_total_value()

    def increment_count(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Count", "Select an item row first.")
            return
        idx = self.tree.index(sel[0])
        item = self.items[idx]
        self.counts[item] = self.counts.get(item, 0) + 1
        self.update_row_count(item)

    def decrement_count(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Count", "Select an item row first.")
            return
        idx = self.tree.index(sel[0])
        item = self.items[idx]
        if self.counts.get(item, 0) > 0:
            self.counts[item] -= 1
        self.update_row_count(item)

    def update_row_count(self, item):
        for iid in self.tree.get_children():
            values = list(self.tree.item(iid)["values"])
            if values[0] == item:
                values[-1] = self.counts[item]
                self.tree.item(iid, values=values)
                break
        self.update_total_value()

    def update_total_value(self):
        total = 0.0
        for iid in self.tree.get_children():
            values = self.tree.item(iid)["values"]
            item = values[0]
            price_str = values[1]
            count = self.counts.get(item, 0)
            try:
                if isinstance(price_str, str) and price_str.startswith("$"):
                    price = float(price_str.replace("$", "").replace(",", ""))
                    total += price * count
            except Exception:
                continue
        self.total_label.config(text=f"Total Value: ${total:,.2f}")

    def open_selected_in_browser(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showinfo("Open Market Page", "Select an item row first.")
            return
        idx = self.tree.index(sel[0])
        market_name = self.items[idx]
        url = f"https://steamcommunity.com/market/listings/{APPID}/{quote(market_name, safe='')}"
        webbrowser.open(url)

    def save_csv(self):
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if not path:
            return
        rows = [self.tree.item(row)["values"] for row in self.tree.get_children()]
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Item", "Lowest Price", "Median Price", "Volume", "Checked At", "% Change", "Count"])
            writer.writerows(rows)
        messagebox.showinfo("Saved", f"Saved {len(rows)} rows to {path}")

def main():
    root = tk.Tk()
    app = SteamPriceChecker(root)
    root.mainloop()

if __name__ == "__main__":
    main()
