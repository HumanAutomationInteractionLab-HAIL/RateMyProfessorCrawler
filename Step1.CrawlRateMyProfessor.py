
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
import urllib
import cPickle

sampleURL= "http://www.ratemyprofessors.com/ShowRatings.jsp?tid=1901092"

def DownloadSignlePage(url):

    pageFile = urllib.urlopen(url)
    pageHtml = pageFile.read()
    pageFile.close()
    soup1 = BeautifulSoup("".join(pageHtml))
    reviewfile = 'DownloadedRateMyProfessorData/prof-sample-page.data'
        # the name of the file where we will store the object
        # Write to the file

    f = file(reviewfile, 'w')
    cPickle.dump(soup1, f)  # dump the object to a file
    f.close()


def DownloadSignlePage1(url):      
    try:
        #url ='http://www.amazon.com/gp/cdp/member-reviews/%s?ie=UTF8&display=public&page=%d&sort_by=MostRecentReview'%(memberID,PageIndex)
        pageFile = urllib.urlopen(url)
        pageHtml = pageFile.read()
        pageFile.close()
        soup1 = BeautifulSoup("".join(pageHtml))
        reviewfile = 'DownloadedRateMyProfessorData/prof-sample-page.data'
        # the name of the file where we will store the object
        # Write to the file
    
        f = file(reviewfile, 'w')
        p1.dump(soup1, f) # dump the object to a file
        f.close()
    except:
        print 'failed for  page'

DownloadSignlePage(sampleURL)
