import time
from datetime import datetime

timestamp = time.time()
print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation")
now = datetime.now()
print(now.strftime("%b %d %Y"))
