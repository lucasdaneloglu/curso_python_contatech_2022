amount_apples = int(input("How many apples do you have? "))
APPLES_PER_BUCKET = 8
buckets_needed = amount_apples // APPLES_PER_BUCKET
if not amount_apples % APPLES_PER_BUCKET == 0:
    buckets_needed += 1
print(f'You need {buckets_needed} buckets to store all your apples.')
