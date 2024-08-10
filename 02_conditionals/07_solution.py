# Coffee Customization

order_size = input("Enter a order size:").lower()
extra_shot = True

if extra_shot:
    coffee = order_size + " coffee with an exta shot"
else:
    coffee = order_size + " coffee"

print('Order: ',coffee)