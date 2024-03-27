import json
import os
from py_ds_hw_3.items import AuthorItem, QuoteItem

__current_directory = os.getcwd()
def get_file_path(file_name: str)->str:
    return os.path.join(__current_directory, file_name)



class QuoteJsonWriterPipeline:
    __file_path_qoutes = "quotes.json"
    def open_spider(self, spider):
        self.quote = []
    def close_spider(self, spider):
        with open(get_file_path(self.__file_path_qoutes), 'w') as f:
            json.dump(self.quote, f, indent=4)
    def process_item(self, item, spider):
        if isinstance(item, QuoteItem):
            item = item.to_dict()
            self.quote.append(item)
        return item
    
class AuthorJsonWriterPipeline:
    __file_path_authors = "authors.json"

    def open_spider(self, spider):
        self.authors = []
    def close_spider(self, spider):
        with open(get_file_path(self.__file_path_authors), 'w') as f:
            json.dump(self.authors, f, indent=4)

    def process_item(self, item, spider):
        if isinstance(item, AuthorItem):
            item = item.to_dict()
            self.authors.append(item)
        return item    