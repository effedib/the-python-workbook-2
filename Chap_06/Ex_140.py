# Postal Codes

# Display where a Canadian postal code refers to and if the address is rural or urban.

postal_code = {
    'A': 'Newfoundland', 'B': 'Nova Scotia', 'C': 'Prince Edward Island', 'E': 'New Brunswick',
    'G': 'Quebec', 'H': 'Quebec', 'J': 'Quebec',
    'K': 'Ontario', 'L': 'Ontario', 'M': 'Ontario', 'N': 'Ontario', 'P': 'Ontario',
    'R': 'Manitoba', 'S': 'Saskatchewan', 'T': 'Alberta',
    'V': 'British Columbia', 'X': 'Nunavut or Northwest Territories', 'Y': 'Yukon'
}

address_pcode = input("Enter the postal code: ").upper()

if address_pcode[0] not in postal_code or address_pcode[1].isdigit() == False:
    print("Invalid postal code!")
else:
    if address_pcode[1] == '0':
        print('This postal code is for a rural address in {}'.format(postal_code[address_pcode[0]]))
    else:
        print('This postal code is for an urban address in {}'.format(postal_code[address_pcode[0]]))
