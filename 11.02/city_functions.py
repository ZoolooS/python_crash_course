'''

'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
def city_name_format(country, city, population=''):
    if population:
        return f'"{city.title()}, {country.title()} - population {population}"'
    else:
        return f'"{city.title()}, {country.title()}"'

# ====== main code ====================================== #


# ====== end of code ==================================== #
