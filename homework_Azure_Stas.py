import requests
import csv

locations = ('eastasia', 'southeastasia', 'centralus', 'eastus', 'eastus2', 'westus', 'northcentralus',
             'southcentralus', 'northeurope', 'westeurope', 'japanwest', 'japaneast', 'brazilsouth', 'australiaeast',
             'australiasoutheast',  'southindia', 'centralindia', 'westindia', 'canadacentral', 'canadaeast',
             'uksouth', 'ukwest', 'westcentralus',  'westus2', 'koreacentral', 'koreasouth', 'francecentral',
             'francesouth', 'australiacentral', 'australiacentral2', 'uaecentral', 'uaenorth', 'southafricanorth',
             'southafricawest', 'switzerlandnorth', 'switzerlandwest', 'germanynorth', 'germanywestcentral',
             'norwaywest', 'norwayeast', 'brazilsoutheast', 'westus3')

option = "productName eq 'Virtual Machines FS Series Windows' and meterName eq 'F16s'"

results = {}

for location in locations:
    r = requests.get(f"https://prices.azure.com/api/retail/prices?$filter=armRegionName eq '{location}' and {option}")
    data = r.json()
    offers_list = data['Items']
    for offer in offers_list:
        if offer['type'] == 'Consumption':
            results[location] = offer['retailPrice']

values_list = list()
for value in results.values():
    values_list.append(value)

with open('C:\\Users\\halaimov.stanislav\\Documents\\Prices_Azure.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Region', 'Price'])
    for key, value in results.items():
        writer.writerow([key, value])
    writer.writerow(["Max: {}".format(max(values_list))])
    writer.writerow(["Min: {}".format(min(values_list))])
    writer.writerow(["AVG: {}".format(sum(values_list)/len(values_list))])




