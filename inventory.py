import math

class inventory:
    def __init__(self, annual_demand, order_cost, holding_rate, unit_cost, lead_time, working_days):
        self.annual_demand = annual_demand
        self.order_cost = order_cost
        self.holding_rate = holding_rate
        self.unit_cost = unit_cost
        self.lead_time = lead_time
        self.working_days = working_days
    def eoq(self):
        return math.sqrt(2 * self.order_cost * self.annual_demand / (self.holding_rate * self.unit_cost))
    def total_cost_of_purchased_inventory(self):
        return self.unit_cost * self.annual_demand
    def annual_inventory_holding_cost(self):
        return self.order_cost * self.unit_cost * self.eoq() / 2
    def annual_order_cost(self):
        return (self.annual_demand / self.eoq()) * self.order_cost
    def annual_total_cost(self):
        return self.total_cost_of_purchased_inventory() + self.annual_inventory_holding_cost() + self.annual_order_cost()
    def reorder_point(self):
        return (self.annual_demand / self.working_days) * self.lead_time
    def number_of_orders(self):
        return self.annual_demand / self.eoq()
    def time_between_orders(self):
        return self.working_days / (self.annual_demand / self.eoq())
    def display(self):
        print(f'EOQ = {self.eoq()}')
        print(f'Total cost of purchased inventory = {self.total_cost_of_purchased_inventory()}')
        print(f'Annual inventory holding cost = {self.annual_inventory_holding_cost()}')
        print(f'Annual order cost = {self.annual_order_cost()}')
        print(f'Annual total cost = {self.annual_total_cost()}')
        print(f'Reorder points = {self.reorder_point()}')
        print(f'Number of orders: {self.number_of_orders()}')
        print(f'Time between orders: {self.time_between_orders()}')

def show_info(p):
    p.display()

database = []
if __name__ == '__main__':
    while True:
        checker = int(input('Insert 1 to input data or any other number to cancel: '))
        if checker == 1:
            annual_demand = int(input('Annual demand (D): '))
            order_cost = int(input('Order cost (Co): '))
            holding_rate = float(input('Holding rate (Ci): '))
            unit_cost = int(input('Unit cost (Pu): '))
            lead_time = int(input('Lead time (LT): '))
            working_days_per_year = int(input('Working days per year: '))
            data = inventory(annual_demand, order_cost, holding_rate, unit_cost, lead_time, working_days_per_year)
            database.append(data)
        else:
            break
    for i in database:
        print(f'---------------------------DATA {database.index(i)}-------------------------')
        show_info(i)