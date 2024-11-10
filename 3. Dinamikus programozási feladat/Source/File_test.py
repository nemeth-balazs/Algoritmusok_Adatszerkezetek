from pathlib import Path
from BookShop import BookShop

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
            arrBookNumberAndTotalMoney = InputFile.readline().removesuffix('\n').split(" ")
            arrPricesOfBooks = InputFile.readline().removesuffix('\n').split(" ")
            arrPagesOfBooks = InputFile.readline().removesuffix('\n').split(" ")

            inputFileName = InputFile.name.split("\\")[-1]
            if len(arrBookNumberAndTotalMoney) != 2 or len(arrPricesOfBooks) == 0 or len(arrPagesOfBooks) == 0:
                print("Invalid number of input parameters in file: " + inputFileName)
                continue

            shop = BookShop(int(arrBookNumberAndTotalMoney[0]), int(arrBookNumberAndTotalMoney[1]), [int(item) for item in arrPricesOfBooks ], [int(item) for item in arrPagesOfBooks ])
            result_by_calc = shop.Calculate() if shop.checkParameters() else None
            if result_by_calc is None:
                print(f"Invalid input parameters in file: {inputFileName}")

        with open(f"{pathOutputFolder}\\" + inputFileName.replace("in", "out"), 'r') as OutputFile:
            result_by_outPut = int(OutputFile.readline())

        print("Test file: "+ inputFileName+ ": " + f"Res by calc: {result_by_calc}, res by output file: {result_by_outPut}. Equal? {result_by_calc==result_by_outPut}")

except Exception as Ex:
    print(Ex)