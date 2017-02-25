import numpy as np
import tables as tb

f = tb.open_file("magresult.h5", "w", "Resulting data from Magboltz")

f.create_group(f.root, "xe", "Pure Xenon")
f.create_group(f.root, "ch4", "Mixture : Methane")
f.create_group(f.root, "co2", "Mixture : Carbon dioxide")
f.create_group(f.root, "cf4", "Mixture : Tetrafluoromethane")
f.create_group(f.root, "hexe", "Mixture : Helium")
f.create_group(f.root,"he3xe", "Mix : He3")

f.create_earray(f.root.xe, "xe20", tb.Float64Atom(), (0,9), "Pure Xenon, check attrs for infos")
f.create_earray(f.root.ch4, "ch420", tb.Float64Atom(), (0,12), "Xenon with Methane, check attrs for infos")
f.create_earray(f.root.co2, "co220", tb.Float64Atom(), (0,12), "Xenon with Carbon dioxide, check attrs for infos")
f.create_earray(f.root.cf4, "cf420", tb.Float64Atom(), (0,12), "Xenon with Tetrafluoromethane, check attrs for infos")
f.create_earray(f.root.hexe, "hexe20", tb.Float64Atom(), (0,12), "Xenon with Helium, check attrs for infos")

f.root.xe.xe20.attrs.nature = 'TransverseDiff mm/sqrt(m) // Err % // LongitudinalDiff mm/sqrt(m) // Err % // ZDriftVel mm/us // Err % // Efield V/cm // Pressure bar // Reduced Efield V/cm/bar'

f.root.ch4.ch420.attrs.nature = 'TransverseDiff mm/sqrt(m) // Err % // LongitudinalDiff mm/sqrt(m) // Err % // ZDriftVel mm/us // Err % // Efield V/cm // Pressure bar // Reduced Efield V/cm/bar // Attachment rate /cm // Err % // Percentage additive %'

f.root.co2.co220.attrs.nature = 'TransverseDiff mm/sqrt(m) // Err % // LongitudinalDiff mm/sqrt(m) // Err % // ZDriftVel mm/us // Err % // Efield V/cm // Pressure bar // Reduced Efield V/cm/bar // Attachment rate /cm // Err % // Percentage additive %'

f.root.cf4.cf420.attrs.nature = 'TransverseDiff mm/sqrt(m) // Err % // LongitudinalDiff mm/sqrt(m) // Err % // ZDriftVel mm/us // Err % // Efield V/cm // Pressure bar // Reduced Efield V/cm/bar // Attachment rate /cm // Err % // Percentage additive %'

f.root.hexe.hexe20.attrs.nature = 'TransverseDiff mm/sqrt(m) // Err % // LongitudinalDiff mm/sqrt(m) // Err % // ZDriftVel mm/us // Err % // Efield V/cm // Pressure bar // Reduced Efield V/cm/bar // Attachment rate /cm // Err % // Percentage additive %'

f.flush()

f.close()
