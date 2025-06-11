# flag = False
# while flag:
#     length = float(input("What is the length of the parcel?"))
#     width = float(input("What is the width of the parcel?"))
#     depth = float(input("What is the depth of the parcel?"))
#     if length > 50 and length > 50 and depth > 50:
#         parcel_size = "large"
#     elif length > 50 and width > 50 or depth > 50:
#         parcel_size = "medium"
#     elif:
#         parcel_size = "small"
#     more_parcels = input("Do you want to enter another parcel? Y or N ")
#     if more_parcels = N:
#         flag = True
# print("The size of your parcel is", more_parcels)




flag = True # changed flase to True
while flag:
    length = int(input("What is the length of the parcel: ? "))
    width = float(input("What is the width of the parcel: ?"))
    depth = float(input("What is the depth of the parcel: ?"))
    if length > 50 and width > 50 and depth > 50: # changed duped length to width
        parcel_size = "large"
    elif length > 50 and width > 50 and depth <= 50: # change > to < # chnage or to and
        parcel_size = "medium"
    elif length <= 50 or width <= 50: #added the statment to determine if parcel is small
        parcel_size = "small"
    more_parcels = input("Do you want to enter another parcel? Y or N ")
    print("The size of your parcel is", parcel_size) # changed more_parcels to parcel_size #moved to state parcel size before asking if user wants to check another parcel
    if more_parcels == "N": # fxed one = to two == # changed N from variable to string
        flag = False # changed true to false
    






