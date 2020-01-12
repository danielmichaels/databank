"""Calculate whether a LIC is trading at a Premium or Discount"""

lic = "Milton"
last_nta = 5.01
last_nta_date = f"{lic} NTA reported on 30 Dec 2019"
asx200_at_nta_date = 6846
current_asx200 = 6929
estimated_nta = ((current_asx200/asx200_at_nta_date)*last_nta)
current_lic_price = 4.97
result = (estimated_nta-current_lic_price)/estimated_nta
percentage = result * 100

if percentage > 0:
    print(f"{percentage:.2f}%")
elif percentage == 0:
    print("0% change")
else:
    print(f"-{percentage:.2f}%")
