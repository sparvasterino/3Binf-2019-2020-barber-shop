class Shop:
    def __init__(self,address,open_hour,close_hour,min_price,max_price,walk_in_start_hour,walk_in_stop_hour):
        self.address = address
        self.open_hour = open_hour
        self.close_hour = close_hour
        self.min_price = min_price
        self.max_price = max_price
        self.avg_price = (max_price + min_price) /2
        self.walk_in_start_hour = walk_in_start_hour
        self.walk_in_stop_hour = walk_in_stop_hour