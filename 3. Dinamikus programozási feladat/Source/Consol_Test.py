from BookShop import BookShop

print("========================")
print("Specify the imput parameres: ")
print("first parameter: number of books (whole number), second parameter: total budget (whole number), third parameter: price of books (whole numbers), forth parameter: pages of books (whole numbers) ")
print("put the prices and pages of books in curly brackets '()' with space ' ' separator")
print("for example a possible parameter list: 4 10 (4 8 5 3) (5 12 8 1)")

try:
    arrParameters = input("Give me the parameters: ")

    parts = arrParameters.strip().split(")")
    if len(parts) < 2:
        print("Invalid parameter number or invalid format!")
        exit()

    part1 = parts[0].split("(")
    part2 = parts[1].split("(")

    strParams = part1[0].strip().split(" ")
    arrPriceOfBooks = part1[1].strip()
    arrPagesOfBooks = part2[1].strip()

    if len(arrPriceOfBooks) <= 0 or len(arrPagesOfBooks) <= 0 or len(strParams) < 2:
        print("Invalid parameter number or invalid format!")
        exit()

    book = BookShop(int(strParams[0]), int(strParams[1]), [int(item) for item in arrPriceOfBooks.split(" ")], [int(item) for item in arrPagesOfBooks.split(" ")] )
    result_by_calc = book.Calculate() if book.checkParameters() else None
    if result_by_calc is None:
        print(f"Invalid input parameters")
        exit()

    print(f"Result: {result_by_calc}")

except Exception as Ex:
    print(f"Invalid parameters! {Ex}")
print("========================")