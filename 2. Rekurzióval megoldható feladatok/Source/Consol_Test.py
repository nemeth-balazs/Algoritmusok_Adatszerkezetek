from ConcertTickets import ConcertTickets

print("========================")
print("Specify the imput parameres: ")
print("first parameter: number of tickets (whole number), second parameter: number of offer (whole number), third parameter: price of tickets (whole numbers), forth parameter: offers of customers (whole numbers) ")
print("put the prices and offers of tickets in curly brackets '()' with space ' ' separator")
print("for example a possible parameter list: 5 3 (5 3 7 8 5) (4 8 3)")

try:
    arrParameters = input("Give me the parameters: ")

    parts = arrParameters.strip().split(")")
    if len(parts) < 2:
        print("Invalid parameter number or invalid format!")
        exit()

    part1 = parts[0].split("(")
    part2 = parts[1].split("(")

    strParams = part1[0].strip().split(" ")
    arrTicketPrices = part1[1].strip()
    arrCustomerOffers = part2[1].strip()

    if len(arrTicketPrices) <= 0 or len(arrCustomerOffers) <= 0 or len(strParams) < 2:
        print("Invalid parameter number or invalid format!")
        exit()

    ticket = ConcertTickets(int(strParams[0]), int(strParams[1]), [int(item) for item in arrTicketPrices.split(" ")], [int(item) for item in arrCustomerOffers.split(" ")] )
    result_by_calc = ticket.Calculate() if ticket.checkParameters() else None
    if result_by_calc is None:
        print(f"Invalid input parameters")
        exit()

    print(f"Result: {result_by_calc}")

except Exception as Ex:
    print(f"Invalid parameters! {Ex}")
print("========================")