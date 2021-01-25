# Cell Phone Bill

# Read the number of minutes and text message used in a month and display the total bill amount

# Constants amounts
BASE_CHARGE     = 15.00
MINUTE_ADD      = 0.25
MESSAGE_ADD     = 0.15
SUPPORT_CALLS   = 0.44
TAX             = 0.05

# Read minutes and messages from user
minutes, messages = input("Enter the number of minutes and text messages used in a month, separated by a space: ").split()
minutes, messages = (float(minutes), float(messages))

# Calculate extras and the total bill
extra_minutes, extra_messages = (0,0)
if minutes > 50:
    extra_minutes = (minutes - 50) * MINUTE_ADD
if messages > 50:
    extra_messages = (messages - 50) * MESSAGE_ADD

charges_bill    = sum([BASE_CHARGE, extra_minutes, extra_messages, SUPPORT_CALLS])
tax_bill        = charges_bill * TAX
total_bill      = charges_bill + tax_bill

# Display the results
print("{:30}{:>5.2f}".format("Base Charge: ", BASE_CHARGE))
if extra_minutes > 0:
    print("{:30}{:>5.2f}".format("Additional Minutes: ", extra_minutes))
if extra_messages > 0:
    print("{:30}{:>5.2f}".format("Additional Text Messages: ",extra_messages))
print("{:30}{:>5.2f}".format("911 Fee: ", SUPPORT_CALLS))
print("{:30}{:>5.2f}".format("Tax: ", tax_bill))
print("{:30}{:>5.2f}".format("Total Bill Amount: ", total_bill))