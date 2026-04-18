EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
    
def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return( EXPECTED_BAKE_TIME - elapsed_bake_time)

def preparation_time_in_minutes(number_of_layers):
    """Calculate prep time by multiplying layers by PREPARATION_TIME constant."""
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate total elapsed time from prep and baking so far."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time