def citi_country(city, country, cont=''):
    if cont:
        get_formatted_city_country = f"{city} {country} {cont}"
    else:
        get_formatted_city_country = f"{city} {country}"
    
    return get_formatted_city_country.title()
