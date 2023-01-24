# Kosningar
Reiknar út sætafjölda miðað við kosningarniðurstöður

## Notkun:
```
python3 kosningar.py -f [path/to/file] -s [num seats] -t [threshold] -o -m [method]
```

## Flögg
```
-f: Path to csv file containing election/polling results (No default, required)
-s: Number of seats to allocate (Default: 63)
-l: Threshold in percentage for getting alloted seats (No default, optional)
-o: Print order in which seats are allocated (Optional)
-m: Method to calculate allocation (Default: dhont, optional, options=[dhont, saintlague])
```
