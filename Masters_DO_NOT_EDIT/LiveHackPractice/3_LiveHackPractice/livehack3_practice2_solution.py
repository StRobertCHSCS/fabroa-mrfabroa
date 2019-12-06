
#initialize counters
number_days = 0
total_spent = 0
daily_amount = 0

# loop to get user daily amounts and accumulate total
while daily_amount != -1:
    daily_amount = float(input("Enter a daily spent amount (-1 to stop): "))
    total_spent = total_spent + daily_amount
    number_days = number_days + 1

# compute allowable spent

# determine if a fee is owed.

