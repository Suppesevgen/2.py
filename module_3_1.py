calls = 0
def count_calls():
    global calls
    calls += 1
    return calls
def string_info(string):
    count_calls()
    return (len(string), string.lower(), string.upper())
def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in [a.lower() for a in list_to_search]

print(string_info('University'))
print(string_info('Pyton'))
print(string_info('Evgenicus'))
print(is_contains('Evgeniy', ['EvGeniy', 'gen', 'niy']))
print(is_contains('Tyumen',['Tmen', 'TyMEN']))
print(calls)

