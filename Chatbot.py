# 1. Tanungin ang customer para sa kanyang Order 1, 2, at 3 at ang presyo nito sa Tagalog
unang_order = input("Ano ang iyong unang order? (Order 1): ")
presyo1 = float(input(f"Magkano ang {unang_order}? "))

pangalawang_order = input("Ano ang iyong pangalawang order? (Order 2): ")
presyo2 = float(input(f"Magkano ang {pangalawang_order}? "))

pangatlong_order = input("Ano ang iyong pangatlong order? (Order 3): ")
presyo3 = float(input(f"Magkano ang {pangatlong_order}? "))

# Kalkulahin ang kabuuang halaga
kabuuang_halaga = presyo1 + presyo2 + presyo3

# 2. Ulitin ang mga order ng customer sa Tagalog
print("\n--- Ang Iyong mga Inorder ---")
print("1.", unang_order)
print("2.", pangalawang_order)
print("3.", pangatlong_order)

# 3. Ipagbigay-alam ang kabuuang halaga ng mga order sa Tagalog
print("\n--- Kabuuang Halaga ---")
print("Ang kabuuang halaga ng iyong mga order ay: ₱", kabuuang_halaga)