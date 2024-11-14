from DistanceQuery import DistanceQuery

print("========================")
print("Specify the imput parameres: ")
print("first parameter: number of cities (whole number), second parameter: roads between two cities and distances (whole numbers)")
print("put the cities and road length in curly brackets '()' with space ' ' separator")
print("the number of provided roads with distances must be: number of cities minus 1")
print("for example a possible parameter list: 5 (2 3 100) (4 3 200) (1 5 150) (1 3 50)")

try:
    arrParameters = input("Give me the parameters: ")
    arrQueryParameters = input("Give me two city indexes to find the min. and max. distances, for example: 2 4: ")
    parts = arrParameters.strip().split(")")
    if len(parts) < 1:
        print("Invalid parameter number or invalid format!")
        exit()

    part1 = parts[0].split("(")
    nNumberOfCities = int(part1[0].strip().split(" ")[0])

    firstRoad = [part1[1].strip()]
    firstRoad = [list(map(int, item.split())) for item in firstRoad]
    roads = [road.replace("(", "").strip() for road in parts[1:-1]]
    roads = [list(map(int, item.split())) for item in roads]
    roads.append(firstRoad[0])

    arrQueryParameters = [int(value) for value in arrQueryParameters.split(" ")]
    if nNumberOfCities == 0 or len(roads) != nNumberOfCities-1 or len(arrQueryParameters) != 2:
        print("Invalid parameter number or invalid format!")
        exit()

    arrCityToCity = [inner_list[:2] for inner_list in roads]
    arrRoadLength = [inner_list[2] for inner_list in roads]

    DistQuery = DistanceQuery(nNumberOfCities, arrCityToCity, arrRoadLength)
    result_by_calc = DistQuery.Calculate(arrQueryParameters[0], arrQueryParameters[1]) if DistQuery.checkParameters() else None
    if result_by_calc is None:
        print(f"Invalid input parameters")
        exit()

    print(f"Result: {result_by_calc}")

except Exception as Ex:
    print(f"Invalid parameters! {Ex}")
print("========================")