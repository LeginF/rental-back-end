class Item:

    def __init__(self, id, name, description, image_url, count):
        self.id = id
        self.description = description
        self.image_url = image_url
        self.count = count
        self.booked = []

    def book(self, bookingDate):
        print(bookingDate)
        if self.isBooked(bookingDate):
            raise Exception("Already booked.")
        else:
            self.booked.append(bookingDate)

    def isBooked(self, bookingDate):
        print('book')
        print(len(self.booked))
        return bookingDate in self.booked
