import json

apartments = [
    [1, 'Eskilstuna', 'Skyttegatan', '7B', 3, 0, 77, 7938, 59.3668802, 16.4982711, ''],
    [2, 'Göteborg', 'Kobbarnas Väg', '15', 2, 5, 64, 9283, 57.7123000, 11.9973269, ''],
    [3, 'Eskilstuna', 'Skyttegatan', '1B', 3, 0, 77, 7938, 59.3681439, 16.4986661, ''],
    [4, 'Köping', 'Odensvivägen', '10D', 1, 0, 39, 2961, 59.5236983, 15.9890426, ''],
    [5, 'Höganäs', 'Storgatan', '44A', 3, 6, 77, 8883, 56.2003817, 12.5645483, ''],
    [6, 'Göteborg', 'Östra Keillersgatan', '8a', 1, 0, 43, 5550, 57.7161437, 11.9277611, ''],
    [7, 'Linköping', 'Barnhemsgatan', '4B', 1, 2, 35, 4277, 58.4080221, 15.6145183, ''],
    [8, 'Eskilstuna', 'Skyttegatan', '39B', 3, 0, 77, 7938, 59.3688665, 16.4961308, ''],
    [9, 'Göteborg', 'Sankt Pauligatan', '37c', 2, 3, 59, 8100, 57.7093656, 12.0036341, ''],
    [10, 'Nyköping', 'Bagaregatan', '17 B', 3, 3, 87, 7809, 58.7503910, 17.0045327, ''],
    [11, 'Karlbo', 'Björklidsvägen', '3B', 2, 1, 62, 5262, 60.1171152, 16.2516419, ''],
]
keys = ('id', 'city', 'street', 'street_number', 'rooms', 'floor', 'area', 'rent', 'latitude', 'longitude', 'description')

apartments = [dict(zip(keys, e)) for e in apartments]

print(json.dumps(apartments, indent=4))
