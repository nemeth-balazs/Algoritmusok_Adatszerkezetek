from pathlib import Path
from BuildingRoads import BuildingRoads

pathInputFolder ="..\Tests\input"
pathOutputFolder ="..\Tests\output"

try:
    input_file_folder = Path(pathInputFolder)
    if not input_file_folder.exists():
        exit()

    for item in input_file_folder.iterdir():
        if not item.is_file():
            continue

        with open(item, 'r') as InputFile:
            linesInFile = InputFile.readlines()
            arrNumberOfCitiesAndNumberOfRoads = linesInFile[0].removesuffix('\n').split(" ")
            arrRoads = [[int(value) for value in road.removesuffix('\n').split(" ")] for road in linesInFile[1:]]

            inputFileName = InputFile.name.split("\\")[-1]
            if len(arrNumberOfCitiesAndNumberOfRoads) != 2 or len(arrRoads) == 0:
                print("Invalid number of input parameters in file: " + inputFileName)
                continue

            road = BuildingRoads(int(arrNumberOfCitiesAndNumberOfRoads[0]), int(arrNumberOfCitiesAndNumberOfRoads[1]), arrRoads)
            result_by_calc = road.Calculate() if road.checkParameters() else None
            if result_by_calc is None:
                print(f"Invalid input parameters in file: {inputFileName}")

        with open(f"{pathOutputFolder}\\" + inputFileName.replace("in", "out"), 'r') as OutputFile:
            result_by_outPut = int(OutputFile.readline())

        print("Test file: "+ inputFileName+ ": " + f"Res by calc: {len(result_by_calc[1])}, res by output file: {result_by_outPut}. Equal? {len(result_by_calc[1])==result_by_outPut}")

except Exception as Ex:
    print(Ex)