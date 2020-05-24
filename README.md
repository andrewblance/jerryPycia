# jerryPycia

## what a long strange pip its been

```pip install jerryPycia```

Tutorial:

```
import jerrypycia as jPy
data, raw = jPy.grateful_loader()
```

Data has some methods you can use! ```print(data.randomShow())``` will give you a random show while ```print(data.nextShow())``` will iterate through the data and always give you the next one.

If you wanted to investigate a particular song you can do:
```
data.song_search('sugar magnolia', plot=True)
```

This will return a bunch of info on sugar magnolia, even a plot if you request it!

Finally, ```raw``` is a pandas dataframe of (almost) all of the Grateful Deads gigs. It is based on https://www.cs.cmu.edu/~mleone/gdead/setlists.html. 




