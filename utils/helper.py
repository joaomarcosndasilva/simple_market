
def formata_float_str_moeda(valor: float) -> str:
    from babel.numbers import format_currency
    #valor = 1234.56
    valor_formatado = format_currency(valor, 'BRL', locale='pt_BR')
    print(valor_formatado)


formata_float_str_moeda('1234.56')