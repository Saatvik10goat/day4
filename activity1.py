feild1=100
feild2=120
feild3=115
feild4=105
feild5=145

total=feild1 + feild2 + feild3 + feild4 + feild5
average=total/5

print("Total harvert in kg: ",total,"kg")
print("Average harvest in kg: ",average,"kg")

price_per_kg=15
earnings=total*price_per_kg

print(" total earning in Rs is:  ₹",earnings)

#pack the harvest into bags of 25kg each
bags=total//25
leftover=total%25

print("No. of bags packed: ",bags)
print("Left over grain in kg: ",leftover,"kg")

#compare this years harvest with last year
last_year=500
print("better than last year?", total>last_year)
print("same as last year?", total==last_year)
print("atleast as good as last year?", total>=last_year)

#bonus feild adds 30kg to the total grain
total+=30 #we can also write total=total+30
print("after bonus: ",total)

#subract 15kg saved as seeeds for next season
total-=15
print("after seed reserved total is: ",total)

#final bag count after all adjustments
bags=total//25
print("FINAL BAGS COUNT: ",bags)