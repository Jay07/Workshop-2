ShippingCost = 0
number = int(input("Enter Number of Items: "))

while number < 1:
    print("Invalid number of items")
    number = int(input("Enter Number of Items: "))


cost = float(input("Enter Shipping Cost per Item: $"))
ShippingCost = number*cost

if ShippingCost > 100:
    ShippingCost = ShippingCost * 0.9
    print("Shipping cost is $", '{:.2f}'.format(ShippingCost))

else:
    print("Shipping cost is $", '{:.2f}'.format(ShippingCost))

