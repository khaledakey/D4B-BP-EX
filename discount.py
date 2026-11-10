#discount.py

def calculate_discount(price, discount_rate):
   """
   Returns the final price after applying a discount.
   price: float
   discount_rate: float (0.1 = 10% discount)
   """
   # INTENDED BEHAVIOR: final price = price * (1 - discount_rate)
   # Let's insert a small logic error or potential pitfall.
   final_price = price * (1 - discount_rate)  # CORRECT: applying the discount rate properly

   return final_price