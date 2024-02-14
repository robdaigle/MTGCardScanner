import cardSearch

result = cardSearch.searchbyname()

for i in result:
        print(i.name, i.set_name, i.multiverse_id, i.image_url)