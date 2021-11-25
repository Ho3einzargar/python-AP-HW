"""Account class definition."""
from decimal import Decimal

class Account:
    """Account class for maintaining a bank account balance."""
    
    def __init__(self, name, balance, username, password): # Dunder methods | magic methods
        """Initialize an Account object."""
        
        # account2 = Account('Julia Green', Decimal('50.00')) # account holder’s name (a string) and balance (a Decimal)
        # Account.__init__(account1, 'John Green', Decimal('50.00'))
        # Account.__init__(account1, 'John Green', Decimal('50.00'))

        # if balance is less than 0.00, raise an exception
        if balance < Decimal('0.00'):
            raise ValueError('Initial balance must be >= to 0.00.')

        self.name = name # account2.name = 'Julia Green'
        self.balance = balance # account2.balance = Decimal('50.00')
        self.username = username # account2.username = username
        self.password = password # account2.password = password

    @property # ! read property
    def username(self):
        """Return the username."""
        return self.username

    @property # ! read property
    def password(self):
        """Return the password."""
        return self.password
    

    def deposit(self, amount):
        """Deposit money to the account."""

        # if amount is less than 0.00, raise an exception
        if amount < Decimal('0.00'):
            raise ValueError('amount must be positive.')

        self.balance += amount
# timewithproperties.py
"""Class Time with read-write properties."""

class Time:
    """Class Time with read-write properties."""

    def __init__(self, hour=0, minute=0, second=0): # attributes: _hour , _minute , _second
        """Initialize each attribute."""
        self._hour = hour # hour(hour)
        self.minute = minute
        self.second = second
    

    @property # read property
    def hour(self): # get_hour | getter | read attribute
        """Return the hour."""
        return self._hour
    
    @hour.setter # write property
    def hour(self, hour): # wirte to attribute | set_hour | setter
        """Set the hour."""
        if not (0 <= hour < 24):
            raise ValueError(f'Hour ({hour}) must be 0-23')
        self._hour = hour
        
    @property
    def minute(self):
        """Return the minute."""
        return self._minute
    
    @minute.setter
    def minute(self, minute):
        """Set the minute."""
        if not (0 <= minute < 60):
            raise ValueError(f'Minute ({minute}) must be 0-59')
        self._minute = minute
        
    @property
    def second(self):
        """Return the second."""
        return self._second
    
    @second.setter
    def second(self, second):
        """Set the second."""
        if not (0 <= second < 60):
            raise ValueError(f'Second ({second}) must be 0-59')
        self._second = second

    @property
    def universal_str(self):
        """Return the second."""
        return str(self._hour) + ':' + str(self._minute) + ':' + str(self._second)
    
    def __repr__(self):
        """Return Time string for repr()."""
        return (f'Time(hour={self.hour}, minute={self.minute}, ' + 
                f'second={self.second})')

    def __str__(self):
        """Return Time string in 12-hour clock format.""" 
        return f'{str(12) if self.hour in (0,12) else str(self.hour % 12)}:{self.minute:02}:{self.second:02} ' +\
            ('AM' if self.hour < 12 else 'PM')


acount1 = Account('ali barkook', 0, 'AliBarkook', '12345678')
print(acount1._username)

acount1._balance = 20
print(acount1._balance)

# time1 = Time(22, 30, 0)

# print(time1.universal_str) # read attribute hour
