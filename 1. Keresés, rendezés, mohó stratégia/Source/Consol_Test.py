from FerrisWheel import FerrisWheel

print("========================")
print("Specify the imput parameres: ")
print("first parameter: number of children (whole number), second parameter: total weight of gondola (whole number), third parameter: weight of children (whole numbers)  ")
print("put the weight of children in curly brackets '()' with space ' ' separator")
print("for example a possible parameter list: 3 9 (2 3 5)")

arrParameters = input("Give me the parameters: ")
strParams = arrParameters.strip().replace('(', "").replace(')', "").split(" ")

if len(strParams) < 3:
    print("Invalid parameter number or invalid format!")
    exit()

try:
    wheel = FerrisWheel(int(strParams[0]), int(strParams[1]),[int(item) for item in strParams[2:] ] )
    result_by_calc = wheel.Calculate() if wheel.checkParameters() else None
    if result_by_calc is None:
        print(f"Invalid input parameters")
        exit()

    print(f"Result: {result_by_calc}")

except Exception as Ex:
    print(f"Invalid parameters! {Ex}")
print("========================")