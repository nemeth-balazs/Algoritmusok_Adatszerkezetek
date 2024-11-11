from pathlib import Path
from ConcertTickets import ConcertTickets

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
            arrTicketNumberCustomerNumber = InputFile.readline().removesuffix('\n').split(" ")
            arrTicketPrices = InputFile.readline().removesuffix('\n').split(" ")
            arrCustomerOffers = InputFile.readline().removesuffix('\n').split(" ")

            inputFileName = InputFile.name.split("\\")[-1]
            if len(arrTicketNumberCustomerNumber) != 2 or len(arrTicketPrices) == 0 or len(arrCustomerOffers) == 0:
                print("Invalid number of input parameters in file: " + inputFileName)
                continue

            ticket = ConcertTickets(int(arrTicketNumberCustomerNumber[0]), int(arrTicketNumberCustomerNumber[1]), [int(item) for item in arrTicketPrices ], [int(item) for item in arrCustomerOffers ])
            result_by_calc = ticket.Calculate() if ticket.checkParameters() else None
            if result_by_calc is None:
                print(f"Invalid input parameters in file: {inputFileName}")

        with open(f"{pathOutputFolder}\\" + inputFileName.replace("in", "out"), 'r') as OutputFile:
            result_by_outPut = [int(item.removesuffix('\n')) for item in OutputFile.readlines()]

        #print("Test file: "+ inputFileName+ ": " + f"Res by calc: {result_by_calc}, res by output file: {result_by_outPut}. Equal? {result_by_calc==result_by_outPut}")
        print("Test file: "+ inputFileName+ ": " + f"Equal? {result_by_calc==result_by_outPut}")

except Exception as Ex:
    print(Ex)






