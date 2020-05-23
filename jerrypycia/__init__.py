#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 16:55:46 2020

@author: andrewblance
"""
__version__ = '0.1.3'

from . import datasets 
import pkg_resources
import pandas as pd
import matplotlib.pyplot as plt

class Show():
    def __init__(self, row):
        self.showNum = row.name
        self.Venue = row['Venue']
        self.City = row['City']
        self.State = row['State']
        self.Country = row['Country']
        self.Date = row['Date']
        self.Year = row['Year']
        self.Setlist = row['Setlist']
    
    def __repr__(self):
        return 'show( Pandas Series Object )' 

    def __str__(self):
        return 'Show Number: ' + str(self.showNum) + '\n' \
                'Date: ' + str(self.Date) + '\n' +\
                'Address: ' + str(self.Venue) + ', ' +  str(self.City) + ', ' + str(self.State) + ', ' + str(self.Country) + '\n' + \
                'Setlist: ' + str(self.Setlist) 
                
def helper(x, name):
    """
    going to use this to find if a song is in a setlist
    """
    return name in x

class Dataset:
    def __init__(self, dataset):
        self.data = dataset
        self.iter = dataset.iterrows()
    
    def __repr__(self):
        return 'Dataset( Pandas DataFrame Object)'
        
    def randomShow(self):
        """
        given the set of gigs, 
        return a random one, as the declared Show() class
        """
        ran = self.data.sample(n=1)
        series = ran.iloc[0]
        return Show(series)
    
    def nextShow(self):
        """
        iterate through the gigs
        return as the declared Show() class
        """
        it = iter(self.iter)
        try:
            elem = next(it)
            return Show(elem[1])
        except StopIteration:
            print("End of list of gigs!")
            return
    
    def _first_last(self, ent):
        """
        find index of first and last True in ent (which is list of if a song was played in each gig)
        Then, find info on these gigs
        """
        first = list(ent).index(True) - 1
        firstShow = Show(self.data.iloc[first])

        print("First at " + str(firstShow.Venue) + ', ' +  str(firstShow.City) + ' in ' + str(firstShow.Country) + " on " + str(firstShow.Date)) 

        last = len(list(ent)) - list(ent)[::-1].index(True) - 1
        lastShow = Show(self.data.iloc[last])
        print("and for the last time at " + str(lastShow.Venue) + ', ' +  str(lastShow.City) + ' in ' + str(lastShow.Country) + " on " + str(lastShow.Date))
    
    def _plotter(self, entries, songName):
        """
        plot how many times each year a song was played
        """
        year = range(1972,1996)
        count = self.data['Year'][entries].value_counts(sort=False)
        
        # if they didnt play the song in a year, it wont be in count
        # I think these years should be in the plot though, so we can put em back in 
        for x in year:
            if x not in count:
                count[x] = 0

        fig, ax = plt.subplots(figsize=(8, 8))
        count.sort_index().plot.bar(color='#f79447')
        
        m = max(count)
        plt.text(-2, m + 5, "How often did Grateful Dead play", fontsize=20, ha="left")
        plt.text(-2, m + 3, str(songName)+"?", fontsize=20, ha="left")
        
        plt.yticks(fontsize=13)    
        plt.xticks(fontsize=13) 
        
        ax.spines["top"].set_visible(False)    
        ax.spines["bottom"].set_visible(False)    
        ax.spines["right"].set_visible(False)    
        ax.spines["left"].set_visible(False)  

        ax.get_xaxis().tick_bottom()    
        ax.get_yaxis().tick_left()

        plt.show()       
        
    def song_search(self, songName, plot=False):
        """
        given a song name, check through every setlist and check if song was played
        then, print out info on first and last gigs
        make a plot (maybe!)
        """
        songNameLow = str.lower(songName)
        entries = self.data["Setlist"].apply(helper, name = songNameLow)

        if sum(entries) > 0:
            print("They played " + songName + " " + str(sum(entries)) + " times")

            self._first_last(entries)
            if plot==True:
                self._plotter(entries, songName)

        else:
            print("It doesn't look like they ever played that song?...")    
    
def grateful_loader():
    resource_path = '/'.join(('datasets', 'GratefulDead.csv'))
    my_data = pkg_resources.resource_filename(__name__, resource_path)
    
    rawdata = pd.read_csv(my_data, index_col=0, converters={'Setlist': eval})
    data = Dataset(rawdata)
    return data, rawdata







