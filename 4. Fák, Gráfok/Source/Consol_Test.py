from BuildingRoads import BuildingRoads

print("========================")
print("Specify the imput parameres: ")
print("first parameter: number of cities (whole number), second parameter: number of roads (whole number), third parameter: roads between two cities (whole numbers)")
print("put the roads between two cities in curly brackets '()' with space ' ' separator")
print("for example a possible parameter list: 10 10 (2 5) (5 6) (1 4) (6 8) (2 6) (3 6) (1 10) (8 9) (2 3) (5 8)")

try:
    arrParameters = input("Give me the parameters: ")
    parts = arrParameters.strip().split(")")
    if len(parts) < 1:
        print("Invalid parameter number or invalid format!")
        exit()

    part1 = parts[0].split("(")
    arrNumberOfCitiesAndNumberOfRoads = part1[0].strip().split(" ")
    firstRoad = [part1[1].strip()]
    firstRoad = [list(map(int, item.split())) for item in firstRoad]
    roads = [road.replace("(", "").strip() for road in parts[1:-1]]
    roads = [list(map(int, item.split())) for item in roads]
    roads.append(firstRoad[0])

    if len(roads) <= 0  or len(arrNumberOfCitiesAndNumberOfRoads) < 2:
        print("Invalid parameter number or invalid format!")
        exit()

    road = BuildingRoads(int(arrNumberOfCitiesAndNumberOfRoads[0]), int(arrNumberOfCitiesAndNumberOfRoads[1]), roads )
    result_by_calc = road.Calculate() if road.checkParameters() else None
    if result_by_calc is None:
        print(f"Invalid input parameters")
        exit()

    print(f"Result: {result_by_calc}")

except Exception as Ex:
    print(f"Invalid parameters! {Ex}")
print("========================")