calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    string_upper = string.upper()
    string_lower = string.lower()
    result_string = (len(string), string_upper, string_lower)
    return result_string

def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    is_cont = False
    for i in range(len(list_to_search)):
        if string == list_to_search[i].lower():
            is_cont = True
    return is_cont

print(string_info('Backtester'))
print(string_info('Wonderful'))
print(string_info('Look is this it'))
print(is_contains('GlobaL', ['raiN', 'gloBal', 'board', 'test']))
print(is_contains('car', ['Car1', 'traIn', 'sPacE']))
print(calls)