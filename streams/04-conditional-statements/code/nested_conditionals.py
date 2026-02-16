has_ticket = True
age = 15

if has_ticket:
    if age >= 18:
        print("Enjoy the R-rated movie")
    else:
        print("You need an adult with you")
else:
    print("Please buy a ticket first")

# day = "Saturday"

# if day == "Saturday" or day == "Sunday":
#     print("It's the weekend!")
# else:
#     print("Weekday")

# # Better way with 'in' (preview for later)
# if day in ["Saturday", "Sunday"]:
#     print("It's the weekend!")