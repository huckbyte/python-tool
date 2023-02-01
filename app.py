import inspect
import sys
from tkinter import ttk,END,NORMAL,Tk,Text,Button,Frame,filedialog
import multiprocessing
from queue import Empty, Full
import time
from types import FunctionType
import os
from pathlib import Path
import shutil
from threading import Thread
import importlib


bg_gray  = '#ABB2B9'
bg_color  = '#17202A'
text_color = "black"
Font = 'Helvetica 11 bold'
Font_bold = 'Helvetica 14 bold'
switch = True

class Gui(object):
    def __init__(self,startvalue,endvalue=None,delay=1000):
        self.startvalue = startvalue
        self.startvalue = self.num  = self.startvalue
        self.endvalue = endvalue
        self.delay = delay
        self.running = False
        self.window = Tk()
        self.Setups()
        self.Gui_details()
        
        
    def run(self):
            self.window.mainloop()
        
    def Setups(self):
        self.window.title("PYTHON (PCSMT) METRICS TOOL")
        self.window.geometry("900x700")
        self.window.minsize(self.window.winfo_width(), self.window.winfo_height())
        self.x_cordinate = int((self.window.winfo_screenwidth() / 2) - (self.window.winfo_width() / 2))
        self.y_cordinate = int((self.window.winfo_screenheight() / 2) - (self.window.winfo_height() / 2))
        self.window.geometry("+{}+{}".format(self.x_cordinate, self.y_cordinate-20))
        
    def Text_clear(self):
        self.text_Area.configure(state=NORMAL)
        self.text_Area.delete(1.0,END)
        self.text_A.configure(state=NORMAL)
        self.text_A.delete(1.0,END)
        self.text_Ar.configure(state=NORMAL)
        self.text_Ar.delete(1.0,END)
        
    def openFile(self):
        global m 
        self.Text_clear()
        try:
            
            file_path = filedialog.askopenfilename(title="open file",
                                                filetypes=(("text files",".py"),("all file","*.*"))
                                                )
            file = open(file_path,mode="r")
            m = file.read()
            try:
                with open("Complex.py",mode="w") as f:
                    f.write(m)
                    f.read()
                    f.close()
                    print("reading file")
            except:
                with open("Complex.py",mode="x") as f:
                    f.write(m)
        except Exception as e:
            pass

    def CheckQueuePoll(self,c_queue,c1_queue,c2_queue):
        try:
            str = c_queue.get(0)
            str1 = c1_queue.get(0)
            str2 = c2_queue.get(0)
            self.text_Area.insert('end',str)
            self.text_A.insert('end',str1)
            self.text_Ar.insert('end',str2)
        except Empty:
            pass
        finally:
            self.window.after(1, self.CheckQueuePoll, c_queue,c1_queue,c2_queue)

    def start(self):
            self.Text_clear()
            print("starting")
            q = multiprocessing.Queue()
            q.cancel_join_thread()
            q1 = multiprocessing.Queue()
            q1.cancel_join_thread()
            q2 = multiprocessing.Queue()
            q2.cancel_join_thread()
            t1 = multiprocessing.Process(target=GenerateData,args=(q,q1,q2))
            t1.start()
            t1.join()
            self.window.after(1,self.CheckQueuePoll,q,q1,q2)
            if not self.running:
                self.running = True
                self._loop()
    
      
    def stop(self):
        print("stoping the function")
        if self.running:
            self.running = False
            
    def reset(self):
        self.Text_clear()
        print("reseting......")
        self.running = False
        self.num = 0
        
    def _loop(self):
        if self.running:
            if self.endvalue is not None and self.endvalue <= self.num:
                self.running = False
                print("end")
                self.num = self.startvalue
                return
            print(self.num)
            self.num += 1
            self.window.after(self.delay,self._loop)
            
    def toogle(self):
        global switch
        if switch == True:
            self.switchbtn.config(bg="#26242f",activebackground="#26242f")
            self.window.config(bg="#26242f")
            
            switch = False
        else:
            self.switchbtn.config(bg="white",activebackground="white")
            self.window.config(bg="#333333")
            
            switch = True

    def Gui_details(self):
        
        #menu buttons
        framemn = Frame(self.window)
        framemn.pack(fill="both",expand=True)
        op_btn = Button(framemn,text="open",width=7,height=1,bg="gray",font="Helvetica 13 bold",command=self.openFile)
        op_btn.grid(row=0,column=0)
        cl_btn3 = Button(framemn,text="close",width=7,height=1 ,bg="gray",font="Helvetica 13 bold",command=self.window.destroy)
        cl_btn3.grid(row=0,column=1)
        cl_btn1 = Button(framemn,text="run",width=7,height=1 ,bg="gray",font="Helvetica 13 bold",command=self.start)
        cl_btn1.grid(row=0,column=3,padx=0,pady=0)
        cl_btn2 = Button(framemn,text="reset",width=7,height=1 ,bg="gray",font="Helvetica 13 bold",command=self.reset)
        cl_btn2.grid(row=0,column=4,padx=0)
        cl_btn = Button(framemn,text="help",width=7,height=1 ,bg="gray",font="Helvetica 13 bold")
        cl_btn.grid(row=0,column=6,padx=self.x_cordinate + 400)
        
        self.switchbtn = Button(self.window,text="theme",bg="#26242f",command=self.toogle,activebackground="#26242f")
        #self.switchbtn.place(relx=0.87,rely=0)
        
        #notebook
        notebook = ttk.Notebook(self.window)
        notebook.place(rely=0.1,relx=0,relwidth=1,relheight=1)
        # notebook.pack(expand=True,fill="x")
        
        #tabs
        frame1 = Frame(notebook,width=500,height=500)
        frame2 = Frame(notebook,width=500,height=500)
        frame3 = Frame(notebook,width=500,height=500)
        
        notebook.add(frame1,text="Base Metrics")
        notebook.add(frame2,text="Derived Metrics")
        notebook.add(frame3,text="Reports")

        #frame1
        self.text_Area = Text(frame1,width=500,height=20,fg=text_color,padx=5,pady=5,font=Font)
        self.text_Area.place(relheight=0.8,relwidth=1,rely=0.1,relx=0.0)
        self.scrollbar = ttk.Scrollbar(self.text_Area)
        self.scrollbar.place(relheight=1,relx=0.974)
        self.scrollbar.configure(command=self.text_Area.yview)
        
        #frame2
        self.text_A = Text(frame2,width=30,height=20,fg=text_color,padx=5,pady=5,font=Font)
        self.text_A.place(relheight=0.8,relwidth=1,rely=0.1,relx=0)
        self.scrollbar = ttk.Scrollbar(self.text_A)
        self.scrollbar.place(relheight=1,relx=0.974)
        self.scrollbar.configure(command=self.text_A.yview)
        
        #frame3
        self.text_Ar = Text(frame3,width=20,height=20,fg=text_color,padx=5,pady=5,font=Font)
        self.text_Ar.place(relheight=0.8,relwidth=1,rely=0.1,relx=0)
        self.scrollbar = ttk.Scrollbar(self.text_Ar)
        self.scrollbar.place(relheight=1,relx=0.974)
        self.scrollbar.configure(command=self.text_Ar.yview)

def indent_check(object):
    import Complex
    import re
    indent_list = []
    x = (inspect.getsourcelines(object)[0])
    for mark , linex in enumerate(x):
        x = len(re.findall("^ *",linex)[0])
        z = linex.lstrip().splitlines()
        indent_list.append(x)
    from collections import Counter
    x = Counter(indent_list)
    z = [[k,]*v for k ,v in x.items()]
    m = format(len(z))
    return m
def GenerateData(q,q1,q2):
    import Complex
    WPC = 0
    CS = 0
    class_num1 = []
    for name ,obj in  inspect.getmembers(sys.modules["Complex"]):
        class_num = []
        if inspect.isclass(obj):
            class_num1.append(name)
            classes = (f"\nclass: {name}\n")
            ind = 0
            try:
                ind = indent_check(obj)
            except:
                print("")
            r = int(ind)
            q1.put(classes)
            q2.put(classes)
            q.put(classes)
            static_wt = 2
            insta_wt = 1
            insta_len = 0
            static_len = 0
            try:
                
                static_vb = ([ x for x in dir(obj) if  isinstance(getattr(obj,x),(str,int))
                            if not x.startswith("__")])
                static_len = len([ x for x in dir(obj) if  isinstance(getattr(obj,x),(str,int))
                            if not x.startswith("__")])
                
                insta_vb = [obj.__init__.__code__.co_names]
                insta_len = len(obj.__init__.__code__.co_names)
            except Exception as e:
                print("no..............")
                
            st = (f"\nNo of Instance variable(s): {insta_len}\n")
            q.put(st)
            cl = (f"No of Class variable(s) : {static_len}\n")
            q.put(cl)
            WVC = ((static_len * static_wt) + (insta_len * insta_wt))
            
            wvc = (f"WVCpy : {WVC}\n")
            wvc1 = (f"Weighted Variable Complexity : {WVC}\n")
            
            q1.put(wvc)
            q2.put(wvc1)
            func_name =[]
            class_name = []
            static_name = []
            
            y =[v for k,v in obj.__dict__.items() if not k.startswith("__")]
            
            for v in y:
                if "staticmethod" in str(v):
                    if isinstance(v,staticmethod):
                        k = (v.__name__)
                        static_name.append(k)
                elif "classmethod" in str(v):
                    if isinstance(v,classmethod):
                        k = (v.__name__)
                        class_name.append(k)
    
                elif  "function" in str(v):
                    if isinstance(v,FunctionType):
                        k = (v.__name__)
                        func_name.append(k)
            
            ista_m = (len(func_name))
            ista_wt = 1
            insm = (f"No of Instance method(s) :{ista_m}\n")
            q.put(insm)
            stat_m = (len(static_name))
            stat_wt = 2
            stm = (f"No of Staticmethod(s) :{stat_m}\n")
            q.put(stm)
            class_m = (len(class_name))
            class_wt = 3
            clm = (f"No of Classmethod :{class_m}\n")
            q.put(clm)
            blk = (f"No of code blocks : :{ind}\n")
            q.put(blk)
            
            WMC = ((ista_m * ista_wt) + (stat_m * stat_wt) + (class_m * class_wt))
            wmc = (f"WMCpy : {WMC}\n")
            wmc1 = (f"Weighted Method Complexity : {WMC}\n")
            q1.put(wmc)
            q2.put(wmc1)
            
            WCC = (WVC + WMC)
            wcc = (f"WCCpy : {WCC}\n")
            wcc1 = (f"Weighted Class Complexity : {WCC}\n")
            sc = (f"CSpy : {ind}\n")
            cs = (f"Class Size : {ind}\n")
            q1.put(wcc)
            q2.put(wcc1)
            q1.put(sc)
            q2.put(cs)
            
            
            WPC +=WCC
            CS += r
            class_num1.append(name)
    wsc =(f"\nWSCpy: {WPC}")
    wsc1 = (f"\nWeighted System Complexity : {WPC}\n")
    ss = (f"\nSSpy : {CS}\n")
    cs = (f"System Size: {CS}\n")
    q1.put(wsc)
    q2.put(wsc1)
    q1.put(ss)
    q2.put(cs)
    for x in range(len(class_num1)):
        q1.put("")
        q2.put("")
    
    
if __name__ == '__main__':
    app = Gui(startvalue=0,endvalue=5)
    app.run()
