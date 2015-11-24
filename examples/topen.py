from tabulator import topen, loaders, parsers, processors


path = 'https://raw.githubusercontent.com/okfn/tabulator-py/master/examples/data/valid.csv'
with topen(path, encoding='utf-8', format='csv') as table:
    table.add_processor(processors.Headers(index=1))
    for row in table.readrow(with_headers=True):
        print(row)
