import numpy as np
import tables as tb

f = tb.open_file("magresult.h5", "w", "Resulting data")

f.flush()

f.close()
