import re

my_string = "Place of delivery of goods: 82172, Ukraine, Lviv Region, Stryi, str. Doroshenko, 1. Deadline for delivery of goods: 31.12.2024"


if __name__ == '__main__':
    data = {
        'country': re.search(r'(?<=,\s)[A-Z][a-z]+', my_string).group(),
        'region': re.search(r'[A-Z][a-z]+ Region', my_string).group(),
        'city': re.search(r'S+[a-z]+', my_string).group(),
        'postal': re.search(r'[0-9]{5}', my_string).group(),
        'address': re.search(r'str\. [A-Z][a-z]+, [0-9]+', my_string).group(),
        'deadline': re.search(r'\d{2}\.\d{2}\.\d{4}', my_string).group(),
    }
    print(data)
