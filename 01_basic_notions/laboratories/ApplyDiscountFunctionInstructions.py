def apply_discount(price, discount):
    # valida tipo
    if not isinstance(price, (int, float)):
        return "The price should be a number."
    
    if not isinstance(discount, (int, float)):
        return "The discount should be a number."
    
    # valida valores
    if price <= 0:
        return "The price should be greater than 0."
    
    if discount < 0 or discount > 100:
        return "The discount should be between 0 and 100."
    
    # cálculo
    discount_amount = price * (discount / 100)
    final_price = price - discount_amount
    
    return final_price

print(apply_discount(50, 20))     # 40.0
print(apply_discount(100, 50))    # 50.0
print(apply_discount("50", 20))   # erro
print(apply_discount(50, 120))    # erro