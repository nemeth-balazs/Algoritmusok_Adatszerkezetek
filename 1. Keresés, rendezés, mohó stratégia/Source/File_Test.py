from pathlib import Path
from FerrisWheel import FerrisWheel

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
            arrChildrenNumberAndTotalWeight = InputFile.readline().removesuffix('\n').split(" ")
            arrWeightOfChildren = InputFile.readline().removesuffix('\n').split(" ")

            inputFileName = InputFile.name.split("\\")[-1]
            if len(arrChildrenNumberAndTotalWeight) != 2 or len(arrWeightOfChildren) == 0:
                print("Invalid number of input parameters in file: " + inputFileName)
                continue

            wheel = FerrisWheel(int(arrChildrenNumberAndTotalWeight[0]), int(arrChildrenNumberAndTotalWeight[1]), [int(item) for item in arrWeightOfChildren ])
            result_by_calc = wheel.Calculate() if wheel.checkParameters() else None
            if result_by_calc is None:
                print(f"Invalid input parameters in file: {inputFileName}")

        with open(f"{pathOutputFolder}\\" + inputFileName.replace("in", "out"), 'r') as OutputFile:
            result_by_outPut = int(OutputFile.readline())

        print("Test file: "+ inputFileName+ ": " + f"Res by calc: {result_by_calc}, res by output file: {result_by_outPut}. Equal? {result_by_calc==result_by_outPut}")

except Exception as Ex:
    print(Ex)






