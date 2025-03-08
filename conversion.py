# Define the unit names
unit_names = {
    "meter": "Meter",
    "kilometer": "Kilometer",
    "centimeter": "Centimeter",
    "millimeter": "Millimeter",
    "micrometer": "Micrometer",
    "nanometer": "Nanometer",
    "gram": "Gram", 
    "kilogram": "Kilogram",
    "milligram": "Milligram",   
    "microgram": "Microgram",
    "nanogram": "Nanogram",
    "pound": "Pound",
    "square_meter": "Square Meter",
    "square_kilometer": "Square Kilometer",
    "square_centimeter": "Square Centimeter",
    "square_millimeter": "Square Millimeter",
    "hectare": "Hectare",
    "acre": "Acre",
    "meter_per_second": "Meter per Second",
    "kilometer_per_hour": "Kilometer per Hour",
    "mile_per_hour": "Mile per Hour",
    "foot_per_second": "Foot per Second",
    "liter": "Liter",
    "milliliter": "Milliliter",
    "cubic_meter": "Cubic Meter",
    "cubic_centimeter": "Cubic Centimeter",
    "celsius": "Celsius",
    "fahrenheit": "Fahrenheit",
    "kelvin": "Kelvin",
    "second": "Second",
    "minute": "Minute",
    "hour": "Hour",
    "day": "Day",
    "week": "Week",
    "year": "Year",
    "joule": "Joule",
    "kilojoule": "Kilojoule",
    "calorie": "Calorie",
    "kilocalorie": "Kilocalorie",
    "watt_hour": "Watt Hour",
    "electron_volt": "Electron Volt",
    "pascal": "Pascal",
    "bar": "Bar",
    "psi": "Pound per Square Inch",
    "atmosphere": "Atmosphere",
    "torr": "Torr",
    "bit": "Bit",
    "byte": "Byte",
    "kilobyte": "Kilobyte",
    "megabyte": "Megabyte",
    "gigabyte": "Gigabyte",
    "terabyte": "Terabyte",
}

#Define unit categories
unit_categories = {
    "Length": ["meter", "kilometer", "centimeter", "millimeter", "micrometer", "nanometer"],
    "Weight": ["gram", "kilogram", "milligram", "microgram", "nanogram", "pound"],
    "Area": ["square_meter", "square_kilometer", "square_centimeter", "square_millimeter", "hectare", "acre"],
    "Speed": ["meter_per_second", "kilometer_per_hour", "mile_per_hour", "foot_per_second"],
    "Volume": ["liter", "milliliter", "cubic_meter", "cubic_centimeter"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["second", "minute", "hour", "day", "week", "year"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "electron_volt"],
    "Pressure": ["pascal", "bar", "psi", "atmosphere", "torr"],
    "Data": ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte"]
}

# Define the conversions
conversions = {
        "meter_kilometer": 0.001, # 1 meter = 0.001 kilometer
        "kilometer_meter": 1000, # 1 kilometer = 1000 meter

        "meter_centimeter": 100, # 1 meter = 100 centimeter
        "centimeter_meter": 0.01, # 1 centimeter = 0.01 meter

        "meter_millimeter": 1000, # 1 meter = 1000 millimeter
        "millimeter_meter": 0.001, # 1 millimeter = 0.001 meter
        
        "meter_micrometer": 1000000, # 1 meter = 1000000 micrometer
        "micrometer_meter": 0.000001, # 1 micrometer = 0.000001 meter

        "meter_nanometer": 1000000000, # 1 meter = 1000000000 nanometer
        "nanometer_meter": 0.000000001, # 1 nanometer = 0.000000001 meter
        
        "kilometer_centimeter": 100000, # 1 kilometer = 100000 centimeter
        "centimeter_kilometer": 0.00001, # 1 centimeter = 0.00001 kilometer

        "kilometer_millimeter": 1000000, # 1 kilometer = 1000000 millimeter
        "millimeter_kilometer": 0.000001, # 1 millimeter = 0.000001 kilometer
        
        "kilometer_micrometer": 1000000000000, # 1 kilometer = 1000000000000 micrometer
        "micrometer_kilometer": 0.000000000001, # 1 micrometer = 0.000000000001 kilometer
        
        "kilometer_nanometer": 1000000000000000, # 1 kilometer = 1000000000000000 nanometer
        "nanometer_kilometer": 0.0000000000000001, # 1 nanometer = 0.0000000000000001 kilometer
            
        "centimeter_millimeter": 10, # 1 centimeter = 10 millimeter
        "millimeter_centimeter": 0.1, # 1 millimeter = 0.1 centimeter

        "centimeter_micrometer": 10000, # 1 centimeter = 10000 micrometer
        "micrometer_centimeter": 0.0001, # 1 micrometer = 0.0001 centimeter

        "centimeter_nanometer": 100000000, # 1 centimeter = 100000000 nanometer
        "nanometer_centimeter": 0.00000001, # 1 nanometer = 0.00000001 centimeter

        "millimeter_micrometer": 1000, # 1 millimeter = 1000 micrometer
        "micrometer_millimeter": 0.001, # 1 micrometer = 0.001 millimeter

        "millimeter_nanometer": 1000000, # 1 millimeter = 1000000 nanometer
        "nanometer_millimeter": 0.0000001, # 1 nanometer = 0.0000001 millimeter
        
        "micrometer_nanometer": 1000, # 1 micrometer = 1000 nanometer
        "nanometer_micrometer": 0.000001, # 1 nanometer = 0.000001 micrometer
      
        "gram_kilogram": 0.001, # 1 gram = 0.001 kilogram
        "kilogram_gram": 1000, # 1 kilogram = 1000 gram
        
        "milligram_gram": 0.001, # 1 milligram = 0.001 gram
        "gram_milligram": 1000, # 1 gram = 1000 milligram

        "microgram_gram": 0.000001, # 1 microgram = 0.000001 gram
        "gram_microgram": 1000000, # 1 gram = 1000000 microgram

        "nanogram_gram": 0.000000001, # 1 nanogram = 0.000000001 gram
        "gram_nanogram": 1000000000, # 1 gram = 1000000000 nanogram

        "pound_gram": 453.592, # 1 pound = 453.592 gram
        "gram_pound": 0.00220462, # 1 gram = 0.00220462 pound

        "kilogram_milligram": 1000000, # 1 kilogram = 1000000 milligram
        "milligram_kilogram": 0.000001, # 1 milligram = 0.000001 kilogram

        "kilogram_microgram": 1000000000, # 1 kilogram = 1000000000 microgram
        "microgram_kilogram": 0.000000001, # 1 microgram = 0.000000001 kilogram

        "kilogram_nanogram": 1000000000000, # 1 kilogram = 1000000000000 nanogram
        "nanogram_kilogram": 0.000000000001, # 1 nanogram = 0.000000000001 kilogram
        
        "kilogram_pound": 2.20462, # 1 kilogram = 2.20462 pound
        "pound_kilogram": 0.453592, # 1 pound = 0.453592 kilogram
        
        "milligram_microgram": 0.001, # 1 milligram = 0.001 microgram
        "microgram_milligram": 1000, # 1 microgram = 1000 milligram

        "milligram_nanogram": 1000000, # 1 milligram = 1000000 nanogram
        "nanogram_milligram": 0.000001, # 1 nanogram = 0.000001 milligram
        
        "milligram_pound": 0.00000220462, # 1 milligram = 0.00000220462 pound
        "pound_milligram": 453592, # 1 pound = 453592 milligram

        "microgram_nanogram": 1000, # 1 microgram = 1000 nanogram
        "nanogram_microgram": 0.001, # 1 nanogram = 0.001 microgram

        "microgram_pound": 0.00000000220462, # 1 microgram = 0.00000000220462 pound
        "pound_microgram": 453592000, # 1 pound = 453592000 microgram
        
        "nanogram_pound": 0.000000000000000220462, # 1 nanogram = 0.000000000000000220462 pound
        "pound_nanogram": 453592000000, # 1 pound = 453592000000 nanogram
        
        "square_meter_square_kilometer": 0.000001, # 1 square meter = 0.000001 square kilometer
        "square_kilometer_square_meter": 1000000, # 1 square kilometer = 1000000 square meter
        
        "square_meter_square_centimeter": 10000, # 1 square meter = 10000 square centimeter
        "square_centimeter_square_meter": 0.0001, # 1 square centimeter = 0.0001 square meter
        
        "square_meter_square_millimeter": 1000000, # 1 square meter = 1000000 square millimeter
        "square_millimeter_square_meter": 0.000001, # 1 square millimeter = 0.000001 square meter
        
        "square_meter_hectare": 0.0001, # 1 square meter = 0.0001 hectare
        "hectare_square_meter": 10000, # 1 hectare = 10000 square meter 
        
        "square_meter_acre": 0.000247105, # 1 square meter = 0.000247105 acre
        "acre_square_meter": 4046.86, # 1 acre = 4046.86 square meter

        "square_kilometer_square_centimeter": 10000000000, # 1 square kilometer = 10000000000 square centimeter
        "square_centimeter_square_kilometer": 0.0000000001, # 1 square centimeter = 0.0000000001 square kilometer

        "square_kilometer_square_millimeter": 1000000000000, # 1 square kilometer = 1000000000000 square millimeter
        "square_millimeter_square_kilometer": 0.000000000001, # 1 square millimeter = 0.000000000001 square kilometer

        "square_kilometer_hectare": 100, # 1 square kilometer = 100 hectare
        "hectare_square_kilometer": 0.01, # 1 hectare = 0.01 square kilometer

        "square_kilometer_acre": 247.105, # 1 square kilometer = 247.105 acre
        "acre_square_kilometer": 0.00404686, # 1 acre = 0.00404686 square kilometer

        "square_centimeter_square_millimeter": 0.01, # 1 square centimeter = 0.01 square millimeter
        "square_millimeter_square_centimeter": 100, # 1 square millimeter = 100 square centimeter

        "square_centimeter_hectare": 0.000001, # 1 square centimeter = 0.000001 hectare
        "hectare_square_centimeter": 100000000, # 1 hectare = 100000000 square centimeter

        "square_centimeter_acre": 0.0000000247105, # 1 square centimeter = 0.0000000247105 acre
        "acre_square_centimeter": 40468600, # 1 acre = 40468600 square centimeter

        "square_millimeter_hectare": 0.0000000001, # 1 square millimeter = 0.0000000001 hectare
        "hectare_square_millimeter": 10000000000, # 1 hectare = 10000000000 square millimeter

        "square_millimeter_acre": 0.000000000247105, # 1 square millimeter = 0.000000000247105 acre
        "acre_square_millimeter": 4046860000, # 1 acre = 4046860000 square millimeter
        
        "hectare_acre": 2.47105, # 1 hectare = 2.47105 acre
        "acre_hectare": 0.404686, # 1 acre = 0.404686 hectare
        
        "meter_per_second_kilometer_per_hour": 3.6, # 1 meter per second = 3.6 kilometer per hour
        "kilometer_per_hour_meter_per_second": 0.277778, # 1 kilometer per hour = 0.277778 meter per second
        
        "meter_per_second_mile_per_hour": 2.23694, # 1 meter per second = 2.23694 mile per hour
        "mile_per_hour_meter_per_second": 0.44704, # 1 mile per hour = 0.44704 meter per second
        
        "meter_per_second_foot_per_second": 3.28084, # 1 meter per second = 3.28084 foot per second
        "foot_per_second_meter_per_second": 0.3048, # 1 foot per second = 0.3048 meter per second   
        
        "liter_milliliter": 1000, # 1 liter = 1000 milliliter
        "milliliter_liter": 0.001, # 1 milliliter = 0.001 liter
        
        "liter_cubic_meter": 0.001, # 1 liter = 0.001 cubic meter
        "cubic_meter_liter": 1000, # 1 cubic meter = 1000 liter
        
        "liter_cubic_centimeter": 1000, # 1 liter = 1000 cubic centimeter
        "cubic_centimeter_liter": 0.001, # 1 cubic centimeter = 0.001 liter

        "milliliter_cubic_meter": 0.000001, # 1 milliliter = 0.000001 cubic meter
        "cubic_meter_milliliter": 1000000, # 1 cubic meter = 1000000 milliliter

        "milliliter_cubic_centimeter": 1, # 1 milliliter = 1 cubic centimeter
        "cubic_centimeter_milliliter": 1, # 1 cubic centimeter = 1 milliliter
        
        "cubic_centimeter_cubic_meter": 0.000001, # 1 cubic centimeter = 0.000001 cubic meter
        "cubic_meter_cubic_centimeter": 1000000, # 1 cubic meter = 1000000 cubic centimeter
        
        "celsius_fahrenheit": 1.8, # 1 celsius = 1.8 fahrenheit
        "fahrenheit_celsius": 0.555556, # 1 fahrenheit = 0.555556 celsius   
        
        "celsius_kelvin": 273.15, # 1 celsius = 273.15 kelvin
        "kelvin_celsius": -273.15, # 1 kelvin = -273.15 celsius
        
        "fahrenheit_kelvin": 255.372, # 1 fahrenheit = 255.372 kelvin
        "kelvin_fahrenheit": 459.67, # 1 kelvin = 459.67 fahrenheit
        
        "second_minute": 60, # 1 second = 60 minutes
        "minute_second": 0.016667, # 1 minute = 0.016667 seconds
        
        "second_hour": 3600, # 1 second = 3600 hours
        "hour_second": 0.000278, # 1 hour = 0.000278 seconds    
        
        "second_day": 86400, # 1 second = 86400 days
        "day_second": 0.000011574, # 1 day = 0.000011574 seconds
        
        "second_week": 604800, # 1 second = 604800 weeks
        "week_second": 0.000001653, # 1 week = 0.000001653 seconds
        
        "second_year": 31536000, # 1 second = 31536000 years
        "year_second": 0.000000032, # 1 year = 0.000000032 seconds
        
        "minute_hour": 0.016667, # 1 minute = 0.016667 hours
        "hour_minute": 60, # 1 hour = 60 minutes    
        
        "minute_day": 0.000694444, # 1 minute = 0.000694444 days
        "day_minute": 1440, # 1 day = 1440 minutes
        
        "minute_week": 0.000019013, # 1 minute = 0.000019013 weeks
        "week_minute": 525600, # 1 week = 525600 minutes
        
        "minute_year": 0.0000000063115, # 1 minute = 0.0000000063115 years
        "year_minute": 1440, # 1 year = 1440 minutes
        
        "hour_day": 0.041667, # 1 hour = 0.041667 days
        "day_hour": 24, # 1 day = 24 hours      
        
        "hour_week": 0.00595238, # 1 hour = 0.00595238 weeks
        "week_hour": 168, # 1 week = 168 hours
        
        "hour_year": 0.0000000000317098, # 1 hour = 0.0000000000317098 years
        "year_hour": 8760, # 1 year = 8760 hours

        "day_week": 0.142857, # 1 day = 0.142857 weeks
        "week_day": 7, # 1 week = 7 days
        
        "day_year": 0.00273973, # 1 day = 0.00273973 years
        "year_day": 365.242, # 1 year = 365.242 days
        
        "week_year": 0.0191657, # 1 week = 0.0191657 years
        "year_week": 52.1429, # 1 year = 52.1429 weeks  
        
        "joule_kilojoule": 0.001, # 1 joule = 0.001 kilojoule
        "kilojoule_joule": 1000, # 1 kilojoule = 1000 joule
        
        "joule_calorie": 0.239006, # 1 joule = 0.239006 calorie
        "calorie_joule": 4.184, # 1 calorie = 4.184 joule
        
        "joule_kilocalorie": 0.000238846, # 1 joule = 0.000238846 kilocalorie
        "kilocalorie_joule": 4184, # 1 kilocalorie = 4184 joule
        
        "joule_watt_hour": 0.000277778, # 1 joule = 0.000277778 watt hour
        "watt_hour_joule": 3600, # 1 watt hour = 3600 joule 
        
        "joule_electron_volt": 6.241509e18, # 1 joule = 6.241509e18 electron volts
        "electron_volt_joule": 1.602177e-19, # 1 electron volt = 1.602177e-19 joules

        "kilojoule_calorie": 0.239006, # 1 kilojoule = 0.239006 calorie
        "calorie_kilojoule": 4.184, # 1 calorie = 4.184 kilojoule

        "kilojoule_kilocalorie": 0.239006, # 1 kilojoule = 0.239006 kilocalorie
        "kilocalorie_kilojoule": 4.184, # 1 kilocalorie = 4.184 kilojoule

        "kilojoule_watt_hour": 0.000277778, # 1 kilojoule = 0.000277778 watt hour
        "watt_hour_kilojoule": 3600, # 1 watt hour = 3600 kilojoule

        "kilojoule_electron_volt": 6.241509e18, # 1 kilojoule = 6.241509e18 electron volts
        "electron_volt_kilojoule": 1.602177e-19, # 1 electron volt = 1.602177e-19 kilojoules

        "calorie_kilocalorie": 0.001, # 1 calorie = 0.001 kilocalorie
        "kilocalorie_calorie": 1000, # 1 kilocalorie = 1000 calorie

        "kilocalorie_watt_hour": 1.163, # 1 kilocalorie = 1.163 watt hour
        "watt_hour_kilocalorie": 0.860421, # 1 watt hour = 0.860421 kilocalorie

        "kilocalorie_electron_volt": 2.611446e19, # 1 kilocalorie = 2.611446e19 electron volts
        "electron_volt_kilocalorie": 3.829298e-20, # 1 electron volt = 3.829298e-20 kilocalories

        "watt_hour_electron_volt": 2.246943e17, # 1 watt hour = 2.246943e17 electron volts
        "electron_volt_watt_hour": 4.450492e-17, # 1 electron volt = 4.450492e-17 watt hours
        
        "pascal_bar": 0.00001, # 1 pascal = 0.00001 bar
        "bar_pascal": 100000, # 1 bar = 100000 pascals

        "pascal_psi": 0.000145038, # 1 pascal = 0.000145038 psi
        "psi_pascal": 6894.76, # 1 psi = 6894.76 pascals
        
        "pascal_atmosphere": 0.00000986923, # 1 pascal = 0.00000986923 atmosphere
        "atmosphere_pascal": 101325, # 1 atmosphere = 101325 pascals
        
        "pascal_torr": 0.00750062, # 1 pascal = 0.00750062 torr
        "torr_pascal": 133.322, # 1 torr = 133.322 pascals  

        "bar_atmosphere": 0.986923, # 1 bar = 0.986923 atmosphere
        "atmosphere_bar": 1.01325, # 1 atmosphere = 1.01325 bar

        "bar_torr": 750.062, # 1 bar = 750.062 torr
        "torr_bar": 0.00133322, # 1 torr = 0.00133322 bar

        "bar_psi": 14.5038, # 1 bar = 14.5038 psi
        "psi_bar": 0.0689476, # 1 psi = 0.0689476 bar

        "psi_atmosphere": 0.068046, # 1 psi = 0.068046 atmosphere
        "atmosphere_psi": 14.6959, # 1 atmosphere = 14.6959 psi

        "psi_torr": 51.7149, # 1 psi = 51.7149 torr
        "torr_psi": 0.0192901, # 1 torr = 0.0192901 psi

        "torr_atmosphere": 0.00131579, # 1 torr = 0.00131579 atmosphere
        "atmosphere_torr": 760, # 1 atmosphere = 760 torr
        
        "bit_byte": 0.125, # 1 bit = 0.125 bytes
        "byte_bit": 8, # 1 byte = 8 bits

        "gigabyte_byte": 1073741824, # 1 gigabyte = 1073741824 bytes
        "byte_gigabyte": 0.000000000931323, # 1 byte = 0.000000000931323 gigabytes
        
        "gigabyte_bit": 8796093022208, # 1 gigabyte = 8796093022208 bits
        "bit_gigabyte": 0.000000000113687, # 1 bit = 0.000000000113687 gigabytes

        "byte_kilobyte": 0.000976562, # 1 byte = 0.000976562 kilobytes
        "kilobyte_byte": 1024, # 1 kilobyte = 1024 bytes

        "kilobyte_bit": 8192, # 1 kilobyte = 8192 bits
        "bit_kilobyte": 0.00012207, # 1 bit = 0.00012207 kilobytes
        
        "kilobyte_megabyte": 0.000976562, # 1 kilobyte = 0.000976562 megabytes
        "megabyte_kilobyte": 1024, # 1 megabyte = 1024 kilobytes
        
        "kilobyte_gigabyte": 0.000000953674, # 1 kilobyte = 0.000000953674 gigabytes
        "gigabyte_kilobyte": 1048576, # 1 gigabyte = 1048576 kilobytes      
        
        "megabyte_gigabyte": 0.000976562, # 1 megabyte = 0.000976562 gigabytes
        "gigabyte_megabyte": 1024, # 1 gigabyte = 1024 megabytes

        "megabyte_byte": 1048576, # 1 megabyte = 1048576 bytes
        "byte_megabyte": 0.000000953674, # 1 byte = 0.000000953674 megabytes

        "megabyte_bit": 8388608, # 1 megabyte = 8388608 bits
        "bit_megabyte": 0.000000119209, # 1 bit = 0.000000119209 megabytes
        
        "terabyte_byte": 8796093022208, # 1 terabyte = 8796093022208 bytes
        "byte_terabyte": 0.000000000113687, # 1 byte = 0.000000000113687 terabytes

        "terabyte_bit": 8796093022208, # 1 terabyte = 8796093022208 bits
        "bit_terabyte": 0.000000000113687, # 1 bit = 0.000000000113687 terabytes
        
        "gigabyte_terabyte": 0.000976562, # 1 gigabyte = 0.000976562 terabytes
        "terabyte_gigabyte": 1024, # 1 terabyte = 1024 gigabytes 
        
        "terabyte_megabyte": 1024, # 1 terabyte = 1024 megabytes
        "megabyte_terabyte": 0.000976562, # 1 megabyte = 0.000976562 terabytes
        
        "terabyte_kilobyte": 1073741824, # 1 terabyte = 1073741824 kilobytes
        "kilobyte_terabyte": 0.000000000931323, # 1 kilobyte = 0.000000000931323 terabytes
        
         }