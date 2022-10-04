from product_function import save

def register(data,cid):
    items = save(data.decode('utf-8'),cid)
    item = items[0]

    if not item['enriched']:
        print(f'item {item} are not enriched! ')
    else:
        print(f'item {item} already enriched!!')