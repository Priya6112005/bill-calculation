
print("Bill Calculator")
bill=float(input("enter a bill amount"))
tip=int(input("enter tip percentage"))
person=int(input("enter no of people"))
tip=bill*(tip/100)
total_bill=bill+tip
print(f"Total_Bill:{total_bill}")
shares=total_bill/person
sh=round(shares, 2)
print(f"Share_Amount:{sh}")