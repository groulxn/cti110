# Calculates male and female percentages in a class
# 10 / 1
# CTI-110 P2HW2 - Male Female Percentage
# Noah Groulx
#

male = int(input("Enter the number of male students:"))

female = int(input("Enter the number of female students:"))
total = male + female

malePer = int(male / total * 100)

femalePer = int(female / total * 100)
r
print("The class is",malePer,"percent male and",femalePer,"percent female")
