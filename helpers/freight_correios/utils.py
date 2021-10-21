def comma_separated_to_float(value):
    return float(value.replace(',', '.'))


def s_n_to_bool(value):
    return {'S': True, 'N': False, None: None}[value]
