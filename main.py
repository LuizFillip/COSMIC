import datetime


class split_filename:
    """
    Split filename into informations from radio occultations
    of COSMIC 2 
    """
    
    def __init__(self, filename):
        
        self.filename = filename
        
        if self.filename[:3] == 'GIS':
            args = self.filename.split('_')
            self._name = args[0]
            self._year = int(args[5])
            self._doy = int(args[6])
            self._hour = int(args[7].replace('.nc', ''))
            
        else:
            args = self.filename.split('.')
            self._leo = args[0]
            self._year = int(args[1])
            self._doy = int(args[2])
            self._hour = int(args[3])
            self._minute = int(args[4])
            self._time = datetime.time(self._hour, self._minute)


            
        self._date = datetime.date(self._year, 1, 1) + datetime.timedelta(self._doy - 1)
        
    
    @property
    def year(self):
        return self._year
    @property
    def doy(self):
        return self._doy
    @property
    def hour(self):
        return self._hour
    @property
    def minute(self):
        return self._minute
    @property
    def date(self):
        return self._date
    @property
    def time(self):
        return self._time
    