#!/usr/bin/env python3

#this snags the play data from bgg by date range
import urllib.request
import re
import copy
import calendar
import numpy as np
import bgg_most_played as bgg

def flatten(mat):
    groups = mat.shape[0]
    rows = mat.shape[1]
    out = mat[0] #start with the first submatrix
    for g in range(1,groups):
        for r in range(rows):
            game = mat[g,r,1]
            i = np.where( out[:,1] == game )[0]
            if(i.size):
                #game is already in the matrix
                i = i[0]
                for c in (0, 2, 3):
                    out[i,c] += mat[g,r,c]
            else:
                #append row to matrix
                out = np.vstack([out,mat[g,r]])
    #average the rankings
    out[:,0] /= groups
    return out


try:
   t12m = np.load( "t12m.npy" )
except IOError:
    print("could't find 12m data")
    a = bgg.getTopPlayedGames( startmonth = 1, timerangemonths = 12 , pages = 5 )
    t12m = np.array([a])
    np.save( "t12m", t12m )

try:
   t6m = np.load( "t6m.npy" )
except IOError:
    print("could't find 6m data")
    a = bgg.getTopPlayedGames( startmonth = 1, timerangemonths = 6 , pages = 5 )
    b = bgg.getTopPlayedGames( startmonth = 7, timerangemonths = 6 , pages = 5 )
    t6m = np.array([a,b])
    np.save( "t6m", t6m )

try:
   t3m = np.load( "t3m.npy" )
except IOError:
    print("could't find 3m data")
    a = bgg.getTopPlayedGames( startmonth = 1, timerangemonths = 3 , pages = 5 )
    b = bgg.getTopPlayedGames( startmonth = 4, timerangemonths = 3 , pages = 5 )
    c = bgg.getTopPlayedGames( startmonth = 7, timerangemonths = 3 , pages = 5 )
    d = bgg.getTopPlayedGames( startmonth = 10, timerangemonths = 3 , pages = 5 )
    t3m = np.array([a,b,c,d])
    np.save( "t3m", t3m )

try:
   t1m = np.load( "t1m.npy" )
except IOError:
    print("could't find 1m data")
    a = bgg.getTopPlayedGames( startmonth = 1, timerangemonths = 1 , pages = 5 )
    b = bgg.getTopPlayedGames( startmonth = 2, timerangemonths = 1 , pages = 5 )
    c = bgg.getTopPlayedGames( startmonth = 3, timerangemonths = 1 , pages = 5 )
    d = bgg.getTopPlayedGames( startmonth = 4, timerangemonths = 1 , pages = 5 )
    e = bgg.getTopPlayedGames( startmonth = 5, timerangemonths = 1 , pages = 5 )
    f = bgg.getTopPlayedGames( startmonth = 6, timerangemonths = 1 , pages = 5 )
    g = bgg.getTopPlayedGames( startmonth = 7, timerangemonths = 1 , pages = 5 )
    h = bgg.getTopPlayedGames( startmonth = 8, timerangemonths = 1 , pages = 5 )
    i = bgg.getTopPlayedGames( startmonth = 9, timerangemonths = 1 , pages = 5 )
    j = bgg.getTopPlayedGames( startmonth = 10, timerangemonths = 1 , pages = 5 )
    k = bgg.getTopPlayedGames( startmonth = 11, timerangemonths = 1 , pages = 5 )
    l = bgg.getTopPlayedGames( startmonth = 12, timerangemonths = 1 , pages = 5 )
    t1m = np.array([a,b,c,d,e,f,g,h,i,j,k,l])
    np.save( "t1m", t1m )

t1mflattened = flatten(t1m)
t1mflattened.view('f8,f8,f8,f8')[::-1].sort( order=['f3'], axis=0)
print(t1mflattened.shape)
print(t12m[:,:10,:], "\n\n" , t1mflattened[:10,:])