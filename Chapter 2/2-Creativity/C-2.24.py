# Suppose you are on the design team for a new e-book reader. What are the
#  primary classes and methods that the Python software for your reader will
#  need? You should include an inheritance diagram for this code, but you
#  do not need to write any actual code. Your software architecture should
#  at least include ways for customers to buy new books, view their list of
#  purchased books, and read their purchased books.


class Library:

    def book_list(self):
        """Return available book list"""

    def purchase_book(self, bookname):
        """Buy new book"""


class User:

    def purchased_book(self):
        """Return purchased book list"""


class Reader:

    def render(self, book):
        """Render the cover of the book onto the screen"""

    def next_page(self):
        """Render the next page"""

    def previous_page(self):
        """Render the previous page"""
