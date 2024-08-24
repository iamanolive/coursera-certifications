def is_lunchtime(hour, is_am):
    if hour == 11 and is_am:
        return True
    elif hour == 12 and (not is_am):
        return True
    else:
        return False