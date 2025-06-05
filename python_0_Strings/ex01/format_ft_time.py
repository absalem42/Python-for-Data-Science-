import time
from datetime import date


# Get seconds since January 1, 1970
# integer part represents whole seconds, and the fractional part represents fractions of a second
seconds_since_epoch = time.time()
print(
    f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} in scientific notation"
)

# Get the current date
today = date.today()
formatted_date = today.strftime("%b %d %Y")
print(formatted_date)
