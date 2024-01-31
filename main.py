def do_stuff(num=0): # the function can be separately called and the argument can be given
    try:
        if num:
            return int(num) + 5
        elif num == 0:
            return "no zeroes allowed"
        else:
            return "please enter number"
    except ValueError as err:
        return err
