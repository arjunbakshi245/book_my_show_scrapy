import scrapy
from ..items import BookmyshowItem
from ..items import BookmyshowMovieItems
from tkinter import *
import tkinter.ttk as ttk
import csv

lis1 = []
start_urls = ""
data=""
str1=""
str2=""

def start_GUI():
    def information():
        window.destroy()
        window1 = Tk()
        window1.title('DS Project Crawler Information')
        frame = Frame(window1)
        frame.pack()
        tframe = Frame(window1)
        tframe.pack()
        sframe = Frame(window1)
        sframe.pack()
        bframe = Frame(window1)
        bframe.pack()
        window1.geometry('1920x1080')
        window1.minsize(800, 600)
        head1 = Label(frame, text='Welcome To Web Crawler', font=(
            'headache', 40, 'bold'), fg='white', bg='black')
        head1.pack(side=TOP)
        label1 = Label(frame, text=' ', font=('Calibri', 20), fg='white')
        label1.pack(side=BOTTOM)
        Label2=Label(tframe, text="This is a python code which specificaly scrapes a particular field of the BookMyShow website.",font=('Cornerstone','18'))
        Label3=Label(tframe, text="The crawler displays information of each recent Movie such as their name, available languages, critics,",font=('Cornerstone','18'),fg='black')
        Label4=Label(tframe, text="user and overall ratings, duration of the movie and the Genre of each movie as well.",font=('Cornerstone','18'),fg='black')
        Label5=Label(sframe, text="The Following Modules have been used for the creation of this crawler:",font=('Cornerstone','18'),fg='black')
        Label6=Label(sframe, text="1. Tkinter for maikg the GUI.",font=('Cornerstone','18'),fg='black')
        Label7=Label(sframe, text="2. Scrapy Module for scraping the website.",font=('Cornerstone','18'),fg='black')
        Label9=Label(sframe, text="3. CSV module for storing the data in a better format.",font=('Cornerstone','18'),fg='black')
        Label8=Label(sframe, text="Currently the spider can crawl Book My Show Site and store the scraped data in a text file and a CSV file.",font=('Cornerstone','18'),fg='black')
        Buttonback=Button(bframe,text='Back',font=('headache', 14),relief='raised', command=start_GUI)
        Label2.pack()
        Label3.pack()
        Label4.pack()
        Label5.pack()
        Label6.pack()
        Label7.pack()
        Label9.pack()
        Label8.pack()
        Buttonback.pack()
        window1.mainloop()
    def us():
        window.destroy()
        window1 = Tk()
        window1.title('DS Project Crawler Information')
        frame = Frame(window1)
        frame.pack()
        tframe = Frame(window1)
        tframe.pack()
        bframe = Frame(window1)
        bframe.pack()
        sframe = Frame(window1)
        sframe.pack()
        window1.geometry('1920x1080')
        window1.minsize(800, 600)
        head1 = Label(frame, text='Welcome To Web Crawler', font=(
            'headache', 40, 'bold'), fg='white', bg='black')
        head1.pack(side=TOP)
        label1 = Label(frame, text=' ', font=('Calibri', 20), fg='white')
        label1.pack(side=BOTTOM)
        Label2=Label(tframe, text="This Python code is developed by the students of Group 10.",font=('Cornerstone','18'))
        Label7=Label(tframe, text="Following is the list of students:",font=('Cornerstone','18'),fg='black')
        Label3=Label(bframe, text="1. Arjun Bakshi  A6",font=('Cornerstone','18'),fg='black')
        Label4=Label(sframe, text="2. Aman Kumar Singh  A5",font=('Cornerstone','18'),fg='black')
        Label5=Label(sframe, text="3. Kawal Nain Singh Batra A6 ",font=('Cornerstone','18'),fg='black')
        Label6=Label(sframe, text="4. Kashish Chhotaria  A6",font=('Cornerstone','18'),fg='black')
        Buttonback=Button(sframe,text='Back',font=('headache', 14),relief='raised', command=start_GUI)
        Label2.pack()
        Label7.pack()
        Label3.pack()
        Label4.pack()
        Label5.pack()
        Label6.pack()
        Buttonback.pack()
        window1.mainloop()
    
    def create_new_project():
        def display():
            global lis1
            global str2
            name = e1.get()
            lis1.append(name)
            start_urls = e2.get()
            start_urls = [start_urls]
            lis1.append(start_urls)
            str1=str(lis1[0])+".txt"
            f=open(str1,'w')
            f.close()
            str2=str(lis1[0])+".csv"
            csvtry= open(str2, 'w')
            csvwriter= csv.writer(csvtry)
            csvwriter.writerow(["movie_name"," movie_genre", "movie_lang"," movie_percent", "movie_userrating", "movie_criticsrating", "movie_link"])
            csvtry.close()
            window1.destroy()
        window.destroy()
        window1 = Tk()
        window1.title('Create a New Project')
        tframe = Frame(window1)
        tframe.pack()
        frame = Frame(window1)
        frame.pack()
        bframe = Frame(window1)
        bframe.pack()
        sframe = Frame(window1)
        sframe.pack()
        window1.geometry('1920x1080')
        window1.minsize(800, 600)
        head1 = Label(tframe, text='Welcome To Web Scraper', font=(
            'headache', 40, 'bold'), fg='white', bg='black')
        head1.pack(side=TOP)
        label1 = Label(frame, text='Project Name ', font=('Calibri', 20))
        label2 = Label(bframe, text='  Homepage   ', font=('Calibri', 20))
        e1 = Entry(frame, bd=5)
        e2 = Entry(bframe, bd=5)
        label1.pack(side=LEFT)
        e1.pack(side=RIGHT)
        label2.pack(side=LEFT)
        e2.pack(side=RIGHT)
        submit = Button(sframe, text='Submit', relief='raised', command=display)
        Buttonback=Button(sframe,text='Back',relief='raised', command=start_GUI)
        submit.pack(side = LEFT)
        Buttonback.pack(side = RIGHT)
        window1.mainloop()
    window = Tk()
    window.title('Spyder')
    frame = Frame(window)
    frame.pack()
    bframe = Frame(window)
    bframe.pack()
    btframe=Frame(window)
    btframe.pack()
    window.title("Web Scraper")
    head1 = Label(frame, text='Welcome To Web Scraper', font=('headache', 40, 'bold'), fg='white', bg='black')
    head1.pack(side=LEFT)
    window.geometry('1920x1080')
    window.minsize(800, 600)
    Button1 = Button(bframe, text='Create a New Project', font=('headache', 20), relief='solid', command=create_new_project)
    Button1.pack(side=TOP)
    label = Label(frame, text='                  ')
    label.pack(side=TOP)
    Button2 = Button(bframe, text='Information About The Crawler',
                    font=('headache', 20), relief='solid', command=information)
    Button3 = Button(btframe, text='About Us',
                    font=('headache', 20), relief='solid', command=us)
    Button2.pack(side=BOTTOM)
    Button3.pack(side=BOTTOM)
    window.mainloop()
'''
def search():
    def sumbit():
        def result():
            window1.destroy()
            window2 = Tk()
            window2.title('Spyder')
            tframe = Frame(window2)
            window2.geometry('1920x1080')
            window2.minsize(800, 600)
            head1 = Label(tframe, text='Welcome To Web Crawler', font=('Comic Sans MS', 40, 'bold'), fg='white',
                          bg='black')
            head1.pack(side=TOP)
            number = e1.get()
            csv_file = csv.reader(open('test.csv', "r"), delimiter=",")
            for row in csv_file:
                # if current rows 2nd value is equal to input, print that row
                if number in row[0]:
                    print(row)
            row=str(row)
            result=Label(tframe,text=row)
            result.pack(side=BOTTOM)
            window1.mainloop()
        root.destroy()
        window1 = Tk()
        window1.title('Spyder')
        tframe = Frame(window1)
        tframe.pack()
        frame = Frame(window1)
        frame.pack()
        sframe = Frame(window1)
        sframe.pack()
        window1.geometry('1920x1080')
        window1.minsize(800, 600)
        head1 = Label(tframe, text='Welcome To Web Crawler', font=('Comic Sans MS', 40, 'bold'), fg='white',bg='black')
        head1.pack(side=TOP)
        label1 = Label(frame, text='Movie Name: ', font=('Calibri', 20),fg='black')
        e1 = Entry(frame, bd=5)
        label1.pack(side=LEFT)
        e1.pack(side=RIGHT)
        submit = Button(sframe, text='Submit', relief='raised', command=result)
        submit.pack(side=BOTTOM)
        window1.mainloop()
    root = Tk()
    root.title('Spyder')
    frame = Frame(root)
    frame.pack()
    bframe = Frame(root)
    bframe.pack()
    root.title("Web Crawler")
    head1 = Label(frame, text='Welcome To Web Crawler', font=('Comic Sans MS', 40, 'bold'), fg='white', bg='black')
    head1.pack(side=LEFT)
    root.geometry('1920x1080')
    root.minsize(800, 600)
    Button1 = Button(bframe, text='Search', font=('Comic Sans MS', 20), relief='solid',
                     command=sumbit)
    Button1.pack(side=TOP)
    label = Label(frame, text='                  ')
    label.pack(side=TOP)
    Button2 = Button(bframe, text='Display Result', font=('Comic Sans MS', 20), relief='solid')
    Button2.pack(side=BOTTOM)
    root.mainloop()
 '''   
   

start_GUI()
class Bookmyshow(scrapy.Spider):
    name = "bookmyshowspider"
    start_urls = lis1[1]
    def parse(self, response):
        items= BookmyshowItem()
        show_links= response.css('div.mv-row a').xpath("@href").extract()
        for link in show_links:
            next_url= "https://in.bookmyshow.com"+str(link)
            yield response.follow(next_url, callback=self.parse1)

        yield items
        
    def parse1(self, response):
            items1= BookmyshowMovieItems()
            movie_genre= response.css(".__genre-tag::text").extract()
            movie_userrating= response.css("div.user-rating span.__rating ul").xpath("@data-value").extract()
            movie_criticsrating= response.css("div.critic-rating span.__rating ul").xpath("@data-value").extract()
            movie_lang= response.css('.__language::text').extract()
            movie_name= response.css('#eventTitle').xpath("@title").extract()
            movie_time = response.css('.__time::text').extract()
            movie_percent= response.css("span.__percentage::text").extract()
            movie_link=str("https://in.bookmyshow.com")+ response.css("div.format-dimensions a").xpath("@href")[0].extract()
            items1['movie_name']= movie_name
            items1['movie_genre']= movie_genre
            items1['movie_lang']= movie_lang
            items1['movie_percent']= movie_percent
            
            items1['movie_userrating']= movie_userrating
            items1['movie_criticsrating']= movie_criticsrating           
            
            items1['movie_time']= movie_time
            items1['movie_link']= movie_link
            global data 
            data=items1
            print(data)
            str1=str(lis1[0])+".txt"
            data=str(data)
            with open(str1, 'a' ) as f:
                f.write(data)
            str2=str(lis1[0])+".csv"
            
            csvtry= open(str2, 'a')
            csvwriter= csv.writer(csvtry)
            csvwriter.writerow([movie_name, movie_genre, movie_lang, movie_percent, movie_userrating, movie_criticsrating, movie_link])
            csvtry.close()
    

    
    
            
