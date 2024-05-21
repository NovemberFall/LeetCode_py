class testZip:
    def testZipFunction(self, s: str, t: str):
        zipped = zip(s, t)

        # Iterate through the zipped elements
        for element in zipped:
            print(element)

if __name__ == "__main__":
    testZip = testZip()
    testZip.testZipFunction("AB", "CD")

'''
('A', 'C')
('B', 'D')


`zip`: This is the function name that performs the zipping operation.
`s`: This is the first iterable you want to zip.
`t`: This is the second iterable you want to zip.

How it works:

1. `zip` iterates through both `s` and `t` simultaneously, 
    pairing elements from corresponding positions in each iterable.
    
2. It creates a new iterator that holds tuples containing these paired elements.

3. The iterator stops when the shorter of the two input iterables is exhausted.


Key points:

- If s and t have different lengths, zip will only iterate up to the length of the shorter one.
- zip can be used with more than two iterables as well. For example, zip(s, t, u) 
  will create an iterator of triples.
- The result of zip is an iterator, not a list. 
  You can convert it to a list using the list function if needed.
'''


