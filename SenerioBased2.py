class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = float(price)
        self.category = self._categorize()

    def _categorize(self):
        """Categorize the vehicle based on its price."""
        # Assuming vehicles 20 Lakhs (2,000,000) and above are Luxury
        if self.price >= 2000000:
            return "Luxury"
        else:
            return "Economy"

    def __str__(self):
        return f"Vehicle No: {self.vehicle_number} | Brand: {self.brand} | Price: ₹{self.price:,.2f} | Category: {self.category}"


class Showroom:
    def __init__(self):
        self.inventory = []

    def add_vehicle(self, vehicle):
        """Add a new vehicle to the showroom's inventory."""
        self.inventory.append(vehicle)
        print(f"\nSuccess: Vehicle '{self.brand}' ({self.vehicle_number}) has been added to the showroom.")

    def display_vehicles(self):
        """Display all vehicles currently in the showroom."""
        if not self.inventory:
            print("\nThe showroom is currently empty.")
            return
        
        print("\n" + "="*70)
        print("CURRENT SHOWROOM INVENTORY")
        print("="*70)
        for index, vehicle in enumerate(self.inventory, start=1):
            print(f"{index}. {vehicle}")
        print("="*70)


# ==========================================
# Driver Code / Interactive Menu
# ==========================================
if __name__ == "__main__":
    my_showroom = Showroom()
    
    while True:
        print("\n--- Vehicle Showroom Management System ---")
        print("1. Add a new vehicle")
        print("2. Display all vehicles")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            try:
                vehicle_no = input("Enter Vehicle Number (e.g., MH-12-AB-1234): ")
                brand = input("Enter Brand (e.g., Honda, Mercedes): ")
                price = float(input("Enter Price: "))
                
                new_vehicle = Vehicle(vehicle_no, brand, price)
                my_showroom.add_vehicle(new_vehicle)
            except ValueError:
                print("\nError: Please enter a valid number for the price.")
                
        elif choice == '2':
            my_showroom.display_vehicles()
            
        elif choice == '3':
            print("Exiting the Showroom Management System. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please select 1, 2, or 3.")