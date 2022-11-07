from csv import reader

with open('./data/currency_rates.csv', 'r') as file:
    data = reader(file)
    for datum in data:
        if 'Bangladesh' in datum[0]:
            # print(type(datum[3]))
            print(f'BDT 5000 = USD {5000*float(datum[2])}')
            print(f'USD 50 = BDT {50*float(datum[3])}')

    file.close()
