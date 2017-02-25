import numpy as np
import tables as tb

f = tb.open_file("magresult.h5", "w")

f.flush()

f.close()
