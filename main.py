units = [
    "",
    "jeden",
    "dwa",
    "trzy",
    "cztery",
    "pięć",
    "sześć",
    "siedem",
    "osiem",
    "dziewięć",
]
teens = [
    "dziesięć",
    "jedenaście",
    "dwanaście",
    "trzynaście",
    "czternaście",
    "piętnaście",
    "szesnaście",
    "siedemnaście",
    "osiemnaście",
    "dziewiętnaście",
]
tens = [
    "",
    "dziesięć",
    "dwadzieścia",
    "trzydzieści",
    "czterdzieści",
    "pięćdziesiąt",
    "sześćdziesiąt",
    "siedemdziesiąt",
    "osiemdziesiąt",
    "dziewięćdziesiąt",
]
hundreds = [
    "",
    "sto",
    "dwieście",
    "trzysta",
    "czterysta",
    "pięćset",
    "sześćset",
    "siedemset",
    "osiemset",
    "dziewięćset",
]
thousands = ["tysiąc", "tysiące", "tysięcy"]
millions = ["milion", "miliony", "milionów"]
billions = ["miliard", "miliardy", "miliardów"]


def number_to_text(number):
    if number == 0:
        return "zero"

    def part_of_number(n, units):
        if n == 0:
            return ""
        return (
            number_to_text(n)
            + " "
            + (
                units[0]
                if n == 1
                else units[1]
                if 2 <= n % 10 <= 4 and (n % 100 < 10 or n % 100 >= 20)
                else units[2]
            )
        )

    parts = []

    # Billions
    bln = number // 1000000000
    if bln:
        parts.append(part_of_number(bln, billions))
        number %= 1000000000

    # Millions
    mln = number // 1000000
    if mln:
        parts.append(part_of_number(mln, millions))
        number %= 1000000

    # Thousands
    ths = number // 1000
    if ths:
        parts.append(part_of_number(ths, thousands))
        number %= 1000

    # Hundreds
    if number >= 100:
        parts.append(hundreds[number // 100])
        number %= 100

    # Tens
    if 10 <= number < 20:
        parts.append(teens[number - 10])
    else:
        if number >= 20:
            parts.append(tens[number // 10])
            number %= 10
        # Units
        if number > 0:
            parts.append(units[number])

    return " ".join(parts)


def price_to_text(price):
    zloty = int(price)
    # If last digit is "2", "3", or "4" - word is "złote", else: "złotych"
    if str(zloty)[-1] in ["2", "3", "4"]:
        zloty_word = "złote"
    else:
        zloty_word = "złotych"

    grosze = round((price - zloty) * 100)
    if str(grosze)[-1] in ["2", "3", "4"]:
        grosz_word = "grosze"
    else:
        grosz_word = "groszy"

    result_zloty = f"{number_to_text(zloty)} {zloty_word}"
    result_grosz = f" {number_to_text(grosze)} {grosz_word}"
    return result_zloty + result_grosz if grosze else result_zloty


if __name__ == "__main__":
    print(price_to_text(897234.56))
    print(price_to_text(2354789.00))
