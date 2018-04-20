# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:28:23 2015

@author: Jibo

Crawl number of review pages


http://www.amazon.com/gp/cdp/member-reviews/A2D1LPEUCTNT8X?ie=UTF8&display=public&page=1&sort_by=MostRecentReview


sample reviewer #:
    A2D1LPEUCTNT8X
    A1E1LEVQ9VQNK

    http://www.amazon.com/gp/cdp/member-reviews/A1E1LEVQ9VQNK?ie=UTF8&display=public&page=1&sort_by=MostRecentReview

"""


import multiprocessing as mp
import random
import string
import threading
from time import ctime,sleep

import urllib
from BeautifulSoup import BeautifulSoup
import urllib2
import cPickle as p


def LoadCachedPage(reviewerID,PageIndex):

    reviewfile = r"/Users/hejibo/Downloads/Step 4. crawl  all review pages/All review page cache/%s/reviewer-%s-%s-page.data"%(reviewerID,reviewerID,PageIndex)
    # the name of the file where we will store the object
    # Write to the file

    f = file(reviewfile)
    soup = p.load(f)
    f.close()
    return soup

def LoadCachedPageFromFile(reviewfile):

    #reviewfile = r"/Users/hejibo/Downloads/Step 4. crawl  all review pages/All review page cache/%s/reviewer-%s-%s-page.data"%(reviewerID,reviewerID,PageIndex)
    # the name of the file where we will store the object
    # Write to the file

    f = file(reviewfile)
    soup = p.load(f)
    f.close()
    return soup

def getInfo(rankIndexValue, 	name ,	reviewerID ,	TotalReviews ,	HelpfulVotes ,	crNumPercentHelpful ,	crNumFanVoters,PageIndex):
    '''
    get text between links
    http://stackoverflow.com/questions/6251319/extract-text-between-link-tags-in-python-using-beautifulsoup
    '''

    #sample
    # the following will get "<span class="h3color tiny">This review is from: </span>,
    #print soup
    #soupParsed = BeautifulSoup(soup)
    #print soupParsed
    soup =  LoadCachedPage(reviewerID,PageIndex)
    productInfo = parseSourceCode(soup,rankIndexValue, 	name ,	reviewerID ,	TotalReviews ,	HelpfulVotes ,	crNumPercentHelpful ,	crNumFanVoters)
    return productInfo

def parseSourceCode(soup,rankIndexValue, 	name ,	reviewerID ,	TotalReviews ,	HelpfulVotes ,	crNumPercentHelpful ,	crNumFanVoters):
    soupParsed = BeautifulSoup(soup)

    # the second table is for the review content
    datapart= soupParsed.findAll("table",{"class":"small"})
    # review part is marked by "<div style="margin-left:0.5em;">"
    reviewParts= soupParsed.findAll("div",{"style":"margin-left:0.5em;"})

    # for the review section of each product, there are two table with class value of small
    # so table 1, 4, 7, 10 is for the product link
    # in the product section, if the product is a vine free product, there is no price tag.
    productInfo=[]
    for productIndex in range(0,10):
        try:
            #productIndex=1
            productPart = datapart[productIndex*3+1]
            productName= productPart.text
            price = productName[productName.find("Price:")+6:]
            price.replace("$","")
            productName = productName[:productName.find("Price:")]

            #print len(datapart)
            #print "----------------------------------------------"
            #print productPart
            productLink = productPart.find("a")['href']
            #print productLink
            #productInfo.append([productName,productLink])

            #reviewPartsIndex=0
            reviewPart= reviewParts[productIndex]
            starReview=reviewPart.find("img")["title"]

            #print starReview
            reviewTime = reviewPart.find("nobr").text

            isVerifiedPurchase="Not Verified"

            CountVerifiedPurchase = reviewPart.findAll("span",{"class":"crVerifiedStripe"})
            if CountVerifiedPurchase:
                #isVerifiedPurchase = reviewPart.find("span",{"class":"crVerifiedStripe"}).text
                isVerifiedPurchase ="Verified Purchase"

            print 'isVerifiedPurchase:',isVerifiedPurchase,'\n'

            #print reviewTime
            AllReviewText =  reviewParts[productIndex].text
            if "Vine Customer Review of Free Product" in AllReviewText:
                IsVineReviewFreeProduct="YesVineReviewFreeProduct"
            else:
                IsVineReviewFreeProduct="NoVineReviewFreeProduct"
            #print IsVineReviewFreeProduct
            reviewText=reviewPart.find("div",{"class":"reviewText"}).text
            print "productName,",productName,"\n"
            print "productLink:\n", productLink,"\n"
            print "starReview:\n",starReview,"\n"
            print "reviewTime:\n",reviewTime,"\n"
            print "IsVineReviewFreeProduct:\n",IsVineReviewFreeProduct,"\n"
            print reviewText
            print "------------------------------------------------------------"
            productInfo.append([rankIndexValue, 	name ,	reviewerID ,	TotalReviews ,	HelpfulVotes ,	crNumPercentHelpful ,	crNumFanVoters,productName,price,productLink,starReview,reviewTime,isVerifiedPurchase,IsVineReviewFreeProduct,reviewText])
        except:
            print 'failed this product section'
        #productReviewInfo=zip(productInfo,reviewInfo)
        #break
    return productInfo


