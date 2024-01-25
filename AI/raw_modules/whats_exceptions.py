# Updated 22/1/24

class CountryCodeException(Exception):
    """
    Country Code is not present in the Phone Number
    """
    pass

class CallTimeException(Exception):
    """
    Wait time is too short for WhatsApp Web to Open
    """
    pass

class InternetException(Exception):
    """
    Host machine is not connected to the Internet or the connection Speed is Slow
    """
    pass

class InvalidPhoneNumber(Exception):
    """
    Phone number given is invalid
    """
    pass

class UnsupportedEmailProvider(Exception):
    """
    Email provider used to send the Email is not supported
    """
    pass
