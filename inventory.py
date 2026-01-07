
# Assumptions for Inventory Class:
# - Product has: product_id, name, price, quantity, expiry_date.
# - Sale will call Inventory to reduce stock using product_id and quantity_sold.
# - Inventory will store products in a dictionary keyed by product_id.
# - Low stock threshold = 5 units.
# - No negative quantities or zero prices allowed.
# - Expired products are flagged when checked.
