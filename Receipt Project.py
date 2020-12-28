lovely_loveseat_description = "Description here, "
lovely_loveseat_price = 0

stylish_settee_description = "Description here"
stylish_settee_price = 0

luxurious_lamp_description = "Description here"
luxurious_lamp_price = 0

sales_tax = 0

customer_one_total = 0

customer_one_itemization = (""+ lovely_loveseat_description + luxurious_lamp_description)

customer_one_total += lovely_loveseat_price
customer_one_total += luxurious_lamp_price
customer_one_tax = customer_one_total * sales_tax
print("Customer One Items: " + customer_one_itemization)
print("Customer One Total: " +str(customer_one_total))