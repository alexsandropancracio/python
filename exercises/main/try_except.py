#try, except

try:
    a = 10
    b = 0
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError as error:
    print(error.__class__.__name__)
    print(error)
except NameError:
    print('NameError')
except (TypeError, IndexError) as error:#Isso não é muito aconselhado fazer, pois caso você queira identificar qual foi a exceção, é melhor elas estarem em exceções separadas.
    print('TypeError ou IndexError')
    print('NotificationError:', error)
    print('NomeError:', error.__class__.__name__)
except Exception:
    print('Exception')

print('Continuar')
