import sys
car_stats = sys.argv[1]
input_file = open(car_stats, 'r')
whole_fuel_sum = 0
fuel_quantity_multiplied_by_a_hundred = 0
month = set()
for line in input_file:
    data = line.split(',')
    whole_fuel_sum = whole_fuel_sum + int(data[3])
    single_date = data[0].split('/')
    month_info = single_date[2] +single_date[0]
    month.add(month_info)
    number_of_months = len(month)
    whole_run = data[1]
    fuel_quantity_multiplied_by_a_hundred = fuel_quantity_multiplied_by_a_hundred + 100*(int(data[3])/int(data[4]))
    fuel_left = data[2]
average_sum_in_month = whole_fuel_sum/number_of_months
average_consumption_in_hundred_km = float(fuel_quantity_multiplied_by_a_hundred - 100*(float(fuel_left)))/float(whole_run)
print ("{} BYR is whole sum spended during {} months".format(whole_fuel_sum, number_of_months))
print("{} BYR in average per month".format(average_sum_in_month))
print ("{} litres is an average comsumption per 100 km".format(round(average_consumption_in_hundred_km, 2)))
