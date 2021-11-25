import math

class Pagination():

    """

    |----------------------------------------------------------------------------
    |                                                                           |
    |     Pagination Class                                                      |
    |                                                                           |
    |----------------------------------------------------------------------------
    |                                                                           |
    |   1 - initial Class                                                       |
    |                                                                           |
    |   2 - Items property                                                      |
    |                                                                           |
    |   3 - Items setter                                                        |
    |                                                                           |
    |   4 - PageSize property                                                   |
    |                                                                           |
    |   5 - PageSize setter                                                     |
    |                                                                           |
    |   6 - return content of current page                                      |
    |                                                                           |
    |   7 - goto previous page                                                  |
    |                                                                           |
    |   8 - goto next page                                                      |
    |                                                                           |
    |   9 - goto first page                                                     |
    |                                                                           |
    |   10 - goto last page                                                     |
    |                                                                           |
    |   11 - change page                                                        |
    |                                                                           |
    |   12 - __str__ magic method return total page and current page content    |
    |                                                                           |
    |   13 - __repr__ magic method return object information                    |
    |                                                                           |
    -----------------------------------------------------------------------------

    """

    # -> 1
    def __init__(self, items , page_size):
        self.Items = items
        self.PageSize = int(page_size)
        self.current_page = 1
        self.total_pages = math.ceil(len(items)/int(page_size))

    # -> 2
    @property
    def Items(self):
        return self._items

    # -> 3
    @Items.setter
    def Items(self, Items):
        self._items = Items

    # -> 4
    @property
    def PageSize(self):
        return self._page_size

    # -> 5
    @PageSize.setter
    def PageSize(self, PageSize):
        self._page_size = PageSize

    # -> 6
    def getVisibleItems(self):
        currentPageContent = ''
        for i in range(self.PageSize):
            if len(self.Items) >  ((self.current_page-1)*self.PageSize + i):
                currentPageContent += self.Items[(self.current_page-1)*self.PageSize + i] + ' '
        return currentPageContent

    # -> 7
    def prevPage(self):
        if self.current_page>1:
            self.current_page -= 1

    # -> 8
    def nextPage(self):
        if self.current_page < self.total_pages:
            self.current_page += 1

    # -> 9
    def firstPage(self):
        self.current_page = 1

    # -> 10
    def lastPage(self):
        self.current_page = self.total_pages

    # -> 11
    def goToPage(self, page):
        page = int(page)
        if page > self.total_pages:
            self.current_page = self.total_pages
        elif page < 1:
            self.current_page = 1
        else:
            self.current_page = page


    # -> 12
    def __str__(self):
        currentPageContent = ''
        for i in range(self.PageSize):
            currentPageContent += self.Items[(self.current_page-1)*self.PageSize + i] + ' '
        return 'we are on page ' + str(self.current_page) + ' the total pages is ' +  str(self.total_pages) + '.\n' + 'content of current page: ' + currentPageContent

    # -> 13
    def __repr__(self):
        return type(self).__name__ + ' object with ' + str(self.total_pages) + ' and now on page ' + str(self.current_page)


# get items and page size from user
items = input().split(' ')
pageSize = input()
orderCount = int(input())

pagination = Pagination(items, pageSize)

orderList = []

# get orders from user
for order in range(orderCount):
    orderList.append(input())

# do orders
for order in orderList:
    eval(order)