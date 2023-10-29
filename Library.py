# Author: Zhiwei Cai
# GitHub username: zwcai0110
# Date: 10/16/2023
# Description: creates a "library" from the Library class, which allows "patrons" from the Patron class to check out,
# return, or request "library items" from the LibraryItem class, which has three subclasses called book,
# album, and movie. The library also keeps track of time and requires patrons to pay fines if item are due.
class LibraryItem:
    '''library items that are in the library; has three subclasses'''

    def __init__(self, library_item_id, title):
        self._library_item_id = library_item_id
        self._title = title
        self._location = 'ON_SHELF'
        self._checked_out_by = None
        self._requested_by = None
        self._date_checked_out = None

    def get_location(self):
        '''
        get method to get the location of the item
        :return: location of the item
        '''
        return self._location

    def set_location(self, location):
        '''
        set method to set the location of the item
        :param location: the location of the item to be set
        :return: nothing
        '''
        self._location = location

    def get_library_item_id(self):
        '''
        get method to retrieve the id of the item
        :return: library item id
        '''
        return self._library_item_id

    def get_checked_out_by(self):
        '''
        get method to get the person that checked out the item
        :return: who checked out the item
        '''
        return self._checked_out_by

    def set_checked_out_by(self, patron_id):
        '''
        set method to set the person that checked out the item
        :param patron_id: id for the patron
        :return: nothing
        '''
        self._checked_out_by = patron_id

    def get_requested_by(self):
        '''
        get method to get the person that requested the item
        :return: who requested the item
        '''
        return self._requested_by

    def set_requested_by(self, patron_id):
        '''
        set method to set the person that requested the item
        :param patron_id: id for the patron
        :return: nothing
        '''
        self._requested_by = patron_id

    def get_date_checked_out(self):
        '''
        get method to get the date the item was checked out
        :return: when the item was checked out
        '''
        return self._date_checked_out

    def set_date_checked_out(self, date):
        '''
        set method to set the date the item was checked out
        :param date: date the check out time will be set to
        :return: nothing
        '''
        self._date_checked_out = date


class Book(LibraryItem):
    '''subclass of the LibraryItem class'''

    def __init__(self, library_item_id, title, author):
        '''follows the superclass, adds one additional attribute'''
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        '''
        get method to get the author of the book
        :return: author for the book
        '''
        return self._author

    def get_check_out_length(self):
        '''
        get method that returns the check out length for books
        :return: the check out length for books
        '''
        return 21


class Album(LibraryItem):
    def __init__(self, library_item_id, title, artist):
        '''follows the superclass, adds one additional attribute'''
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        '''
        get method to get the artist of the album
        :return: artist for the album
        '''
        return self._artist

    def get_check_out_length(self):
        '''
        get method that returns the check out length for books
        :return: the check out length for albums
        '''
        return 14


class Movie(LibraryItem):
    def __init__(self, library_item_id, title, director):
        '''follows the superclass, adds one additional attribute'''
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        '''
        get method to get the director of the movie
        :return: director for the movie
        '''
        return self._director

    def get_check_out_length(self):
        '''
        get method that returns the check out length for movie
        :return: the check out length for movies
        '''
        return 7


class Patron:
    '''patrons that can check out, return, or request items from the library and pay fines'''

    def __init__(self, patron_id, name):
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        '''
        get method that returns the id for the patron
        :return: id for the patron
        '''
        return self._patron_id

    def get_fine_amount(self):
        '''
        get method that returns the fine amount for the patron
        :return: the total amount of fine
        '''
        return self._fine_amount

    def add_library_item(self, library_item):
        '''
        add an item to the list of items checked out by the patron
        :param library_item: the library item to be added
        :return: nothing
        '''
        self._checked_out_items.append(library_item)

    def remove_library_item(self, library_item):
        '''
        removes an item from the list of items checked out by the patron
        :param library_item: the library item to be removed
        :return: nothing
        '''
        self._checked_out_items.remove(library_item)

    def amend_fine(self, fine_amount):
        '''
        adjusts the amount of fine that a patron has accrued
        :param fine_amount: the amount to be adjusted by
        :return: nothing
        '''
        self._fine_amount += fine_amount


class Library:
    '''represents the library, where all the items are stored and fines are assessed for patrons'''

    def __init__(self):
        self._holdings = {}
        self._members = {}
        self._current_date = 0

    def add_library_item(self, library_item):
        '''
        adds a library item to the library
        :param library_item: the library item to be added
        :return: nothing
        '''
        self._holdings[library_item.get_library_item_id()] = library_item
        # use a dict to store the items. Key is the item id, value is the item itself

    def add_patron(self, patron):
        '''
        add a patron to the list of patrons that the library has
        :param patron: the patron to be added
        :return: nothing
        '''
        self._members[patron.get_patron_id()] = patron
        # use a dict to store the patrons. Key is the patron id, value is the patron themselves

    def lookup_library_item_from_id(self, library_item_id):
        '''
        look up a library item using the item id
        :param library_item_id: id for the library item
        :return: None if the item cannot be found; the id for the library item otherwise
        '''
        if library_item_id not in self._holdings:
            # first check if the item id is stored in the dict
            return None
            # return None if can't be found
        return self._holdings[library_item_id]
        # otherwise, return the item corresponding to the item id

    def lookup_patron_from_id(self, patron_id):
        '''
        look up a patron using their id
        :param patron_id: id for the patron
        :return: None if the patron cannot be found; the id for the patron otherwise
        '''
        if patron_id not in self._members:
            # first check if the patron id is stored in the dict
            return None
            # return None if can't be found
        return self._members[patron_id]
        # otherwise, return the patron corresponding to the id

    def check_out_library_item(self, patron_id, library_item_id):
        '''
        represents that a patron checked out an item from the library
        :param patron_id: id for the patron checking out the item
        :param library_item_id: id for the library item to be checked out
        :return: text strings for different situations
        '''
        if patron_id not in self._members:
            # if patron doesn't exist
            return 'patron not found'
        if library_item_id not in self._holdings:
            # if the item doesn't exist
            return 'item not found'
        if self._holdings[library_item_id].get_checked_out_by() is not None:
            # if the item has already been checked out
            return 'item already checked out'
        if (self._holdings[library_item_id].get_requested_by() is not None and
                self._holdings[library_item_id].get_requested_by() != patron_id):
            # if the item has already been requested by another patron that's not the patron
            return 'item on hold by other patron'

        self._holdings[library_item_id].set_checked_out_by(patron_id)
        # first, change the attribute of the item itself to indicate who checked out the item
        self._holdings[library_item_id].set_date_checked_out(self._current_date)
        # next, change the attribute of the item to indicate when it was checked out
        self._holdings[library_item_id].set_location('CHECKED_OUT')
        # then, change the attribute of the item to set the location to CHECKED_OUT

        if self._holdings[library_item_id].get_requested_by() == patron_id:
            # check if the book is checked out by the patron it was on hold for
            self._holdings[library_item_id].set_requested_by(None)
            # if yes, set requested by to None

        self._members[patron_id].add_library_item(self._holdings[library_item_id])
        # finally, add the item to the patron's list of checked out items

        return 'check out successful'

    def return_library_item(self, library_item_id):
        '''
        represents that a patron returns the book to the library
        :param library_item_id: id for the library item to be returned
        :return: text strings for different situations
        '''
        if library_item_id not in self._holdings:
            # check if the library item actually exists
            return 'item not found'
        if self._holdings[library_item_id].get_checked_out_by() is None:
            # check if the library item has not been checked out yet
            return 'item already in library'

        patron = self._members[self._holdings[library_item_id].get_checked_out_by()]
        # select the patron by retrieving from the dict the person that checked out the item
        patron.remove_library_item(self._holdings[library_item_id])
        # remove the item for that patron's list of checked out items
        if self._holdings[library_item_id].get_location == 'CHECKED_OUT':
            # check if the item was checked out
            self._holdings[library_item_id].set_location('ON_SHELF')
            # if yes, put it back on the shelf
        if self._holdings[library_item_id].get_requested_by is not None:
            # check if the book was requested by someone
            self._holdings[library_item_id].set_location('ON_HOLD_SHELF')
            # if yes, put it on the hold shelf

        self._holdings[library_item_id].set_checked_out_by(None)
        # reset so no one checked out the item
        self._holdings[library_item_id].set_date_checked_out(None)
        # reset so the date the item was checked out is None

        return 'return successful'

    def request_library_item(self, patron_id, library_item_id):
        """
        represents when a patron requests a book that's been checked out by someone
        :param patron_id: id for the patron requesting the book
        :param library_item_id: id for the library item requested
        :return: text strings for different situations
        """
        if patron_id not in self._members:
            # check if the patron exists
            return 'patron not found'
        if library_item_id not in self._holdings:
            # check if the item exists
            return 'item not found'
        if self._holdings[library_item_id].get_requested_by() is not None:
            # check if someone already requested the item
            return 'item already on hold'

        self._holdings[library_item_id].set_requested_by(patron_id)
        # update the attribute of the item so show who requested the item

        if self._holdings[library_item_id].get_location() == 'ON_SHELF':
            # check if the item in on the shelf
            self._holdings[library_item_id].set_location('ON_HOLD_SHELF')
            # if yes, move it to the hold shelf

        return 'request successful'

    def pay_fine(self, patron_id, amount):
        '''
        represents when a patron pays the fine
        :param patron_id: id for the patron paying
        :param amount: the amount to be paid
        :return: text string if patron not found; otherwise nothing
        '''
        if patron_id not in self._members:
            # check if the patron exists
            return 'patron not found'
        self._members[patron_id].amend_fine(-amount)
        # append negative sign to the positive amount paid, so we subtract from the outstanding amount

        return 'payment successful'

    def increment_current_date(self):
        '''
        increments the date and update the fine if late
        :return: nothing
        '''
        self._current_date += 1
        # move the date forward by one
        for library_item in self._holdings:
            # iterate through all the library items in the library
            if (self._holdings[library_item].get_checked_out_by() is not None and
                    # check the first condition: when the item has been checked out
                    (self._current_date - self._holdings[library_item].get_date_checked_out() >
                     self._holdings[library_item].get_check_out_length())):
                # check the second condition: when the item has not been returned after permitted time
                self._members[self._holdings[library_item].get_checked_out_by()].amend_fine(0.1)
                # if checked out and late, then we increase each patron's  fines by 10 cents a day
