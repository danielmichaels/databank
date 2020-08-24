# JSON tidbits

## datetime.datetime not JSON serializable error

```python
# wont work
nt_asdict = {'name': 'PyBites', 'founders': ('Julian', 'Bob'), 'started': datetime.datetime(2016, 12, 19, 0, 0), 'tags': ['Python', 'Code Challenges', 'Learn by Doing'], 'location': 'Spain/Australia', 'site': 'https://pybit.es'}

json.dumps(nt_asdict) # Error on Datetime

# Works

`json.dumps(my_dictionary, indent=4, sort_keys=True, default=str)` 

```

[ref](https://stackoverflow.com/a/36142844/9163110)
