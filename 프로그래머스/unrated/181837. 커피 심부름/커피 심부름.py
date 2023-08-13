def solution(order):
    price = 0
    for li in order:
        if "americano" in li or li == "anything":
            price += 4500          
        else:
            price += 5000
    return price