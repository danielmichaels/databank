from collections import namedtuple

"""This is a short script to demonstrate the namedtuple type."""

print()
print("""
Measurement = namedtuple('Measurement', 'length width height quantity')
measurements = Measurement(length='Length', width='Width', height='Height',
                          quantity='Quantity')
Above is how we setup namedtuple.
First we give the namedtuple variable a name (Measurement) and call namedtuple().
Inside it takes two arguments = typename and field names.
Type name is the subclasses name, and data types are the tuple like objects
that are accessible via attribute lookup as well as being indexed and iterated
over.
 """)


Measurement = namedtuple('Measurement', 'length width height quantity')

measurements = Measurement(length='Length', width='Width', height='Height',
                           quantity='Quantity')

print()
print("""This is an example of how to setup and use namedtuples.
Why use them? They offer a great way of making tuples readable during 
unpacking. The namedtuples can be passed around much easier as they are
an instanced type.""")

print('Here is the value of "Height" called by its keyword '
      '== measurements.height')
print('calling "measurements.height": {}'.format(measurements.height))
print()
print('"Height" could also be called by its index, but this is not obvious!')
print('calling "measurements[2]": {}'.format(measurements[2]))
print()

measurements2 = Measurement(2000, 200, 200, 1)
print('created new instance...\n ')
print('measurements2 = Measurement(2000, 200, 200, 1')
print()
print('lets print the new instance of namedtuple Measurement with variables'
      ' that are not keywords.')
print('print(measurements2) == {}'.format(measurements2))
print()
print('As we see its prints the variable with the keyword. Now lets call'
      ' one of the attributes [measurements2.length: {}] and one of the '
      'indexes [measurements2[1]: {}]'.
      format(measurements2.length, measurements2[1]))

