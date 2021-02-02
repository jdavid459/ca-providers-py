import pandas as pd

csv_provided = pd.read_csv('x_ca_omcc_providers.csv', names=["provider_name", "type_of_care", "address", "city", "state", "zip", "phone"])
api_data = pd.read_csv('outputs/api_data.csv')
scraped_data = pd.read_csv('outputs/scraped_data.csv')

# Would prefer to do this in SQL (matching phone format to other sources)

clean_nums = []
for phone_no in csv_provided['phone']:
    contactphone = "(%c%c%c) %c%c%c-%c%c%c%c" % tuple(map(ord,list(str(phone_no)[:10])))    
    clean_nums.append(contactphone)

csv_provided['phone'] = clean_nums


#  With more time, I'd wrap this in a function and print out differences

csv_provided = csv_provided.drop_duplicates()   # 51 dupes removed
scraped_data = scraped_data.drop_duplicates()  # No dupes removed
api_data = api_data.drop_duplicates() # No dupes removed


csv_provided.to_csv('outputs/csv_provided.csv', index=None)
api_data.to_csv('outputs/api_data.csv', index=None)
scraped_data.to_csv('outputs/scraped_data.csv', index=None)