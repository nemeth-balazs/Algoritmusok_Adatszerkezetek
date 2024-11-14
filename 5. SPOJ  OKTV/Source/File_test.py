from pathlib import Path
from DistanceQuery import DistanceQuery

pathInputFolder ="..\Tests\input"
pathOutputFolder ="..\Tests\output"

try:
    input_file_folder = Path(pathInputFolder)
    if not input_file_folder.exists():
        exit()

    for item in input_file_folder.iterdir():
        if not item.is_file():
            continue

        arrResult_by_cal = []
        with open(item, 'r') as InputFile:
            linesInFile = InputFile.readlines()
            nNumberOfCities = (int)(linesInFile[0].removesuffix('\n'))

            arrRoadsWithWeights = [[int(value) for value in road.removesuffix('\n').split(" ")] for road in linesInFile[1:nNumberOfCities]]
            arrCityToCity = [inner_list[:2] for inner_list in arrRoadsWithWeights]
            arrRoadLength = [inner_list[2] for inner_list in arrRoadsWithWeights]

            nNumberOfQueries = (int)(linesInFile[nNumberOfCities].removesuffix('\n'))
            arrQueries = [[int(value) for value in road.removesuffix('\n').split(" ")] for road in linesInFile[nNumberOfCities+1:nNumberOfCities+nNumberOfQueries+1]]

            inputFileName = InputFile.name.split("\\")[-1]
            if len(arrRoadLength) != len(arrCityToCity) or nNumberOfQueries != len(arrQueries):
                print("Invalid number of input parameters in file: " + inputFileName)
                continue

            for query in arrQueries:
                if len(query) != 2:
                    print("Invalid number of input parameters in file: " + inputFileName)
                    continue

                DistQuery = DistanceQuery(nNumberOfCities, arrCityToCity, arrRoadLength)
                result_by_calc = DistQuery.Calculate(query[0],query[1]) if DistQuery.checkParameters() else None
                if result_by_calc is None:
                    print(f"Invalid input parameters in file: {inputFileName}")
                    continue

                arrResult_by_cal.append(result_by_calc)


        with open(f"{pathOutputFolder}\\" + inputFileName.replace("in", "out"), 'r') as OutputFile:
            linesInFile = OutputFile.readlines()
            arrResult_by_file = [[int(value) for value in road.removesuffix('\n').split(" ")] for road in linesInFile]


        for (result_by_calc, result_by_file) in zip(arrResult_by_cal, arrResult_by_file):
            print("Test file: "+ inputFileName+ ": " + f"Res by calc: {result_by_calc}, res by output file: {result_by_file}. Equal? {result_by_calc==result_by_file}")

except Exception as Ex:
    print(Ex)