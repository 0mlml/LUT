with open("titanic.csv", 'r') as file:
    lines = file.readlines()

data = lines[1:]

male_count = 0
female_count = 0
total_age = 0
age_count = 0
oldest_age = 0

for line in data:
    parts = line.strip().split(',')

    sex = parts[5]

    if sex == "male":
        male_count += 1
    elif sex == "female":
        female_count += 1

    age_str = parts[6]
    if age_str:
        age = float(age_str)
        total_age += age
        age_count += 1
        oldest_age = max(oldest_age, age)

average_age = round(total_age / age_count) if age_count > 0 else 0

print(f"The number of male passengers: {male_count}")
print(f"The number of female passengers: {female_count}")
print(f"The average age of passengers: {average_age}")
print(f"The age of the oldest passenger: {int(oldest_age)}")
