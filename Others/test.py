import json

with open('response.json') as f:
  data = json.load(f)

for hotel in data["hotels"]:
    key = "minimumCash"
    if key in hotel:
        minimum_cash = hotel[key]
        minimum_cash.pop("identifier", None)

        key2 = "undiscountedRate"
        if key2 in minimum_cash:
            undiscounted_rate = minimum_cash[key2]
            undiscounted_rate.pop("identifier", None)
#
# for rate in data["rates"]:
#     rate.pop("identifier", None)
#
#     key = "undiscountedRate"
#     if key in rate:
#         undiscounted_rates = rate[key]
#         undiscounted_rates.pop("identifier", None)



with open('result.json', 'w') as fp:
    json.dump(data, fp)
