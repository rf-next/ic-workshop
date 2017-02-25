import numpy as np
import tables as tb

f = tb.open_file("magresult.h5", "w") again

f.flush()

f.close()
