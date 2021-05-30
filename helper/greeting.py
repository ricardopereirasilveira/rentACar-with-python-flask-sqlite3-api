from datetime import datetime

hour = int(datetime.now().strftime("%H:%M:%S")[:2])


def returningGreeting() -> str:
    """
    that method receive a paramet to return the greeting to user ( if not logged ).
    :return: It return a string with greeting to user in index page
    """
    if hour >= 00:
        return 'Good Morning'
    elif hour >= 12:
        return 'Good Afternoon'
    else:
        return 'Good Evening'
