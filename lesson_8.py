#1
import re
def determine_license_type(license_plate):
    license_plate = license_plate.upper()
    private_car_pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    taxi_pattern = r'[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'
    if re.fullmatch(private_car_pattern, license_plate):
        return 'Частный автомобиль'
    if re.fullmatch(taxi_pattern, license_plate):
        return 'Такси'
    return 'Некорректный номер'
print(determine_license_type('a123bc34'))
print(determine_license_type('ab12345'))
print(determine_license_type('abc1234567'))

#2
with open("input.txt") as file:
    words_count = len(re.split(r'\s+', file.read().strip()))

#3
import re
def replace_times(text):
    pattern = r'\b([0-1]?[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?\b'
    result = re.sub(pattern, '(TBD)', text)
    return result
input_text = "Уважаемые! Если вы к 09:00 не вернёте чемодан, то уже в 09:00:01 я за себя не отвечаю."
output_text = replace_times(input_text)
print(output_text)

#4
import re
def find_abbreviations(text):
    pattern = r'\b[A-Z]{2,}(\s+[A-Z]{2,})*\b'
    abbreviations = re.findall(pattern, text)
    return abbreviations
document = """
ФГУП НИЦ ГИДГЕО занимается исследованием геологических данных. 
ФГОУ ЧШУ АПК предлагает образовательные услуги.
"""
result = find_abbreviations(document)
for abbreviation in result:
    print(abbreviation)