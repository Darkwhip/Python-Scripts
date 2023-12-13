import math as m

target=int(input("Enter amount of resource to mine: "))
eff=float(input("Refine Efficiency(0.6): "))
unit=int(input("Amount of resource per reprocess ore: "))
unitV=float(input("Volume of one unit of ore: "))
cargo=int(input("Ore hold volume(m³): "))
ans=m.ceil(((((target/eff)/unit)*100)*unitV)/cargo)
print("It'll take ",ans," full loads to meet the demand.")

