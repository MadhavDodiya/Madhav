# error => compiletime
# exception => runtime

try:
    print(4//0)
except:
    print("Please check your numbers")
else:
    print("Done")
finally:
    print("No Idea !!")

