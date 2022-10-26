from prettytable import PrettyTable

tb=PrettyTable()

tb.field_names=['key', 'value']
tb.add_rows([
    ['1','4k'],
    ['2','角色扮演'],
    ['3','八重'],
    ['4','排行榜']
])
print(tb)