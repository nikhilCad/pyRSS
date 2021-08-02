import tkinter as tk
import feedparser
from functools import partial#for commands in button click functions
from newspaper import Article

root = tk.Tk()
root.geometry("400x500")
root.title("pyRSSreader")

feedlist = [
##    "https://www.thenewsminute.com/kerala.xml",
##    "https://www.thenewsminute.com/tamil.xml",
##    "https://www.thehindu.com/news/national/kerala/feeder/default.rss",
##    "https://www.thehindu.com/news/national/tamil-nadu/feeder/default.rss"
    "http://rss.cnn.com/rss/edition.rss"
    ]

titles = []
links = []

labelList = []


startFrame = tk.Frame(root)
pageFrame = tk.Frame(root)

for frame in (startFrame, pageFrame):
    frame.grid(row=0, column=0, sticky = "news")#sticky makes it take full window size

startFrame.tkraise()

def raiseMain():
    startFrame.tkraise()
tk.Button(pageFrame, text = "Back to Main", command = raiseMain).pack()

pageLabel = tk.Message(pageFrame, text = " ", justify = "left", width =350)
pageLabel.pack()



def linkPress(link,title):#keep button functions above button call
    curArticle = Article (link, language="en")
    curArticle.download()
    curArticle.parse()
    pageLabel.config(text = title + "\n\n" +
                     curArticle.text
                     + curArticle.summary)#Change this later to parsed text
    pageFrame.tkraise()


for i in range(len(feedlist)):
    
    tempfeed = feedparser.parse(feedlist[i])

    for j in range(len(tempfeed.entries)):

        titles.append( tempfeed.entries[j].title )
        links.append( tempfeed.entries[j].link ) 




for i in range(len(titles)):
##    labelList.append( tk.Message(root, text = titles[i],
##                                 width = 200, anchor = "e",
##                                 ) )#e for East
    labelList.append( tk.Button(startFrame, text = titles[i],
                                wraplength = 400,
                                command = partial(linkPress, links[i],titles[i]) ))
                                  #use partial for adding argument
    labelList[i].pack()


root.mainloop()
