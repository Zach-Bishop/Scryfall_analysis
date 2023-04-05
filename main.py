import requests
import pandas as pd
import json

keep_cols = ['name','type_line','mana_cost','oracle_text','set']
decks = set()
all_cards = pd.DataFrame()
set_portion = ''
for expansion in set_list:
    set_portion = set_portion + f'set:{expansion} or '
set_portion = '('+set_portion[:-3]+')'
for query in queries:
    request = requests.get(f'https://api.scryfall.com/cards/search?q={set_portion} {queries[query]}&unique')
    if 'data' in json.loads(request.content.decode()).keys():
        t = pd.DataFrame(json.loads(request.content.decode())['data'])
        query_parts = query.split('_')
        t[query_parts[0]] = query_parts[1]+' '
        all_cards = all_cards.append(t)
        decks.add(query_parts[0])
    else:
        print(f'{query} returned no results')
decks = list(decks)
all_cards.reset_index(inplace = True)
all_cards = all_cards.loc[all_cards['reprint']==False]
all_cards.fillna('', inplace=True)
all_cards_filtered_first = all_cards.groupby(keep_cols)[decks].first()
all_cards_filtered = all_cards.groupby(keep_cols).agg({deck: ''.join for deck in decks})
all_cards_filtered.to_csv('cards.csv')