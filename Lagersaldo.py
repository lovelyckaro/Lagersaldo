from datetime import date

def handle_sale(sale, result_array):
    amount = sale[0]
    # if result_array[1] is negative we want to treat it as if we have
    # no pending stock
    pending = max(0, result_array[1])
    actual = result_array[0]
    # Allocate from pending first
    result_array[1] -= min(pending, amount)
    amount -= min(pending, amount)
    # Then allocate from actual (if there is any left)
    result_array[0] -= min(actual, amount)
    amount -= min(actual, amount)
    # if we cannot allocate enough from pending and
    # actual to cover the sale, we've sold to much.
    # pending becomes negative to cover the sale with future
    # deliveries (sale might have to be delayed :( )
    if amount > 0:
        result_array[1] -= amount
    # if we use up the pending stock, remove the pending date
    if result_array[1] <= 0:
        result_array[2] = None

def handle_purchase(purchase, result_array):
    result_array[1] += purchase[0]
    result_array[2] = purchase[1]

def calculateShopInventory(actual_inventory, sales_lines, purchase_lines):
    result_array = [actual_inventory, 0, None]
    s = 0
    p = 0
    # For every sale and purchase in chronological order
    while s < len(sales_lines) or p < len(purchase_lines):
        # If we've run out of purchases
        if p >= len(purchase_lines):
            handle_sale(sales_lines[s], result_array)
            s+= 1
        # if we've run out of sales
        elif s >= len(purchase_lines):
            handle_purchase(purchase_lines[p], result_array)
            p += 1
        # if the closest purchase is before the closest sale
        elif purchase_lines[p][1] <= sales_lines[s][1]:
            handle_purchase(purchase_lines[p], result_array)
            p += 1
        else:
            handle_sale(sales_lines[s], result_array)
            s += 1
    return result_array

def main():
    inventory = 34
    sales_lines = [[19, date(2021, 1, 3)]
                  ,[3, date(2021, 1, 15)]
                  ,[20, date(2021, 1, 17)]]
    purchase_lines = [[15, date(2021, 1, 6)]
                     ,[50, date(2021, 2, 1)]]
    print(calculateShopInventory(inventory, sales_lines, purchase_lines))

if __name__ == "__main__":
    main()
