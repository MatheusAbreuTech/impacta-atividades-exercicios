priceOfMerchandise = float(input())
quantityPurchased = int(input())

fixedDiscount = 0.1
discountPerUnit = 0.01
additionalDiscount = quantityPurchased * discountPerUnit
fullDiscount = fixedDiscount + additionalDiscount

priceWithoutDiscount = priceOfMerchandise * quantityPurchased
discountPrice = priceWithoutDiscount - (priceWithoutDiscount * fullDiscount)

print(f"{priceWithoutDiscount:.2f}")
print(f"{discountPrice:.2f}")