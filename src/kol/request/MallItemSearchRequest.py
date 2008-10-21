from GenericRequest import GenericRequest
from kol.database import ItemDatabase
from kol.manager import PatternManager

class MallItemSearchRequest(GenericRequest):
	"""
	Searches for an item at the mall. Note that stores from which you have already purchased
	the max that day will not appear.
	"""
	
	def __init__(self, session, itemName, limit=-1):
		super(MallItemSearchRequest, self).__init__(session)
		self.url = session.serverURL + 'searchmall.php'
		self.requestData['whichitem'] = itemName
		if limit > 0:
			self.requestData['cheaponly'] = 'on'
			self.requestData['shownum'] = limit
		
	def parseResponse(self):
		items = []
		
		itemNoLimitPattern = PatternManager.getOrCompilePattern('mallItemSearchNoLimit')
		for match in itemNoLimitPattern.finditer(self.responseText):
			itemId = int(match.group(3))
			item = ItemDatabase.getItemFromId(itemId, self.session)
			item["quantity"] = int(match.group(1))
			item["storeId"] = int(match.group(2))
			item["price"] = int(match.group(4))
			item["storeName"] = match.group(5).replace('<br>', ' ')
			items.append(item)
		
		itemLimitPattern = PatternManager.getOrCompilePattern('mallItemSearchLimit')
		for match in itemLimitPattern.finditer(self.responseText):
			itemId = int(match.group(4))
			item = ItemDatabase.getItemFromId(itemId, self.session)
			item["quantity"] = int(match.group(1))
			item["limit"] = int(match.group(2))
			item["storeId"] = int(match.group(3))
			item["price"] = int(match.group(5))
			item["storeName"] = match.group(6).replace('<br>', ' ')
			items.append(item)
		
		items.sort(lambda x, y: cmp(x["price"], y["price"]))
		self.responseData["results"] = items
