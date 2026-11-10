#prices = [10,25,4,50]
#total = 0
#for price in prices:
#    total +=price
#print("Total price:", total)
#
#if total > 50:
#    print("Apply a discount")
#elif total == 50:
#    print("Total is exactly 50")
#else:
#    print("Total is less than 50")

#Count Down

#start = input("Enter a number to start: ")
#start = int(start)
#while start >= 0:
#    print(start)
#    start = start - 1
#
#print ("Blast off!")

#Shopping List

#shopping_list = []
##while True:
##    item = input("Enter an item (or'done'): ")
##    if item.lower() == "done":
##        break
##    shopping_list.append(item)
##
##print("You have", le#n(shopping_list), "items.")
#print(shopping_list)#

#Student name and major
#student = {}
#student["name"] = input("Student Name: ")
#student["id"] = input("Student ID: ")
#student["major"] = input("Student Major: ")

#print(student)
#print(f"{student['name']} (ID {student['id']}) studies {student['major']}.")

#order_total = float(input("Enter your order total: "))
#
#if order_total > 100:
#    order_total = order_total * 0.9
#
#print(f"Order total : {order_total}")

prices = [12.99, 55.0, 100.5, 49.99, 60]
print(prices)

size = len(prices)

for i in range(0, size):
    print("evaluating elemnt", i)
    if prices [i] > 50:
        discounted_price = prices[i] * 0.9
        prices[i] = prices[i] * 0.9

print(prices)