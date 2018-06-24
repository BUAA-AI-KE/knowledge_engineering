#! /usr/bin/env python
# -*- coding: utf-8 -*-
 
import tkinter as tk
import wikipedia as wiki

 
class TestUI(object):
    def __init__(self, master):
        self.root = master
        self.create_frame()

    def create_frame(self):
        '''
        create frame,left and right
        '''
        self.frm_left = tk.LabelFrame(self.root)
        self.frm_right = tk.LabelFrame(self.root)
 
        self.frm_left.grid(row=0, column=0, sticky="wesn")
        self.frm_right.grid(row=0, column=5, sticky="wesn")
 
        self.create_frm_left()
        #self.create_frm_right()
 
    def create_frm_left(self):
        self.search_btn = tk.Button(self.frm_left, text="搜索", command=self.showButton)
        self.search_Entry = tk.Entry(self.frm_left)

        self.brief_lable = tk.Label(self.frm_left, text="简介")
        self.brief_listbox = tk.Text(self.frm_left, height=30, width=30)

        self.search_words_lable = tk.Label(self.frm_left, text="相关搜索词")
        self.search_words_listbox = tk.Text(self.frm_left, height=30, width=30)

        self.link_lable = tk.Label(self.frm_left, text="介绍链接")
        self.link_listbox = tk.Text(self.frm_left, height=30, width=30)

        self.recommend_lable = tk.Label(self.frm_left, text="相关推荐")
        self.recommend_listbox = tk.Text(self.frm_left, height=30, width=30)


        self.search_btn.grid(row=0, column=2, padx=5, pady=5, sticky="wesn")
        self.search_Entry.grid(row=0, column=1, padx=5, pady=5, sticky="wesn")

        self.brief_lable.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.brief_listbox.grid(row=2, column=0, padx=5, pady=5, sticky="wesn")

        self.search_words_lable.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.search_words_listbox.grid(row=2, column=1, padx=5, pady=5, sticky="wesn")

        self.link_lable.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.link_listbox.grid(row=2, column=2, padx=5, pady=5, sticky="wesn")

        self.recommend_lable.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.recommend_listbox.grid(row=2, column=3, padx=5, pady=5, sticky="wesn")




    def showButton(self):
        self.brief_listbox.insert("end", wiki.summary(self.search_Entry.get()))
        self.search_words_listbox.insert("end", wiki.search(self.search_Entry.get()))
        self.link_listbox.insert("end", wiki.page(self.search_Entry.get()).url)
        self.recommend_listbox.insert("end", wiki.page(self.search_Entry.get()).links)

 
    def create_frm_right(self):
        self.frm_right_canvas = tk.Canvas(self.frm_right, bg="white")
 
        self.frm_right_canvas.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")



if __name__ == '__main__':
    '''
    main loop
    '''
    root = tk.Tk()
    root.title("知识图谱作业")

    TestUI(master=root)

    root.resizable(False, False)
    root.mainloop()


