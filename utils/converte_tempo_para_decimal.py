def converte_tempo_para_decimal(horas: int, minutos: int) -> float:
    '''
    Converte o tempo dado em horas e minutos para um valor decimal.

    Args:
    - horas (int): O número de horas.
    - minutos (int): O número de minutos.

    Returns:
    - float: O tempo total em formato decimal.

    A função calcula o valor decimal equivalente ao tempo fornecido em horas e minutos.
    Os minutos são convertidos para frações decimais das horas, e o valor total é retornado.
    '''

    # Convertendo minutos para fração decimal de uma hora
    minutos_decimal = minutos / 60
    minutos_decimal_float = float('{:.2f}'.format(minutos_decimal))  # Arredondando para 2 casas decimais

    # Somando as horas e minutos convertidos para obter o tempo total em formato decimal
    hora_decimal = horas + minutos_decimal_float
    return hora_decimal