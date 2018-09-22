import Tkinter as Tk
class App(object):
    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Compare string")
        self.label = Tk.Label(self.root, text="Please enter two strings and press OK.")
        self.label.grid(column=2, row=0,sticky='W')
        self.string1 = Tk.StringVar()
        self.string2 = Tk.StringVar()
        self.inputbox1= Tk.Label(self.root, text="Source: ",width="10").grid(column=1, row=1, sticky='E')
        Tk.Entry(self.root, textvariable=self.string1,width="50").grid(column=2, row=1, sticky='W'+'E')
        self.inputbox2= Tk.Label(self.root, text="Target: ",width="10").grid(column=1, row=2, sticky='E')
        Tk.Entry(self.root, textvariable=self.string2,width="50").grid(column=2, row=2, sticky='W'+'E')
        self.buttontext = Tk.StringVar()
        self.buttontext.set("OK")
        Tk.Button(self.root,
                  textvariable=self.buttontext,
                  command=self.clicked1).grid(column=2, row=3,sticky='W'+'E')

        self.label = Tk.Label(self.root, text="")
        self.label.grid(column=2, row=4)
        #self.label2 = Tk.Label(self.root, text="",width='100')
        #self.label2.grid(column=1, row=5, columnspan=3)
        #self.text = Tk.Text(self.root,height="10", width='100')
        #self.text.grid(column=0, row=6,columnspan=4,rowspan=1)
        self.text2 = Tk.Text(self.root,height='20',width='100')
        self.text2.grid(column=0, row=7,columnspan=4,rowspan=1)

        self.root.mainloop()

    def clicked1(self):
        source = self.string1.get().replace('\n', '').replace("  "," ")
        target = self.string2.get().replace('\n', '').replace("  "," ")
        a=[]
        b=[]
        a.append(0)
        b.append(0)

        s = source.split(" ")
        t = target.split(" ")
        if len(s)==1:
            s=[source]
        if len(t)==1:
            t=[target]
        mat = [[0 for x in range(len(t)+1)] for x in range(len(s)+1)]
        for i in range(len(s)+1):
            mat[i][0]=i
        for j in range(len(t)+1):
            mat[0][j]=j
        mat[0][0]=0
        for i in range(1,(len(s)+1)):
            for j in range(1,(len(t)+1)):
                fleft=(mat[i][j-1])+1
                ftop=(mat[i-1][j])+1
                if s[i-1]==t[j-1]  or (s[i-1].replace(",", "").replace('.', '').lower()==t[j-1].replace(",", "").replace('.', '').lower()):
                    fdia=(mat[i-1][j-1])
                else:
                    fdia=(mat[i-1][j-1])+1
                score=min(fleft,ftop,fdia)
                mat[i][j]=score
        Ldistance =mat[i][j]
        result=[]
        i=len(s)
        j=len(t)
        while True:
            if (s[i-1]==t[j-1]):
                if (mat[i][j]!=mat[i-1][j-1]):
                    if (mat[i][j]==(mat[i][j-1]+1)):
                        result.insert(0,["insert",i,(j-1)])
                        j-=1
                    elif (mat[i][j]==(mat[i-1][j]+1)):
                        result.insert(0,["delete",i,(j+1)])
                        i-=1
                elif  (mat[i][j]==mat[i-1][j-1]):
                    #result.insert(0,["nothing",(i-1),(j-1)])
                    i-=1
                    j-=1
            else:
                if (mat[i][j]==(mat[i-1][j-1]+1)):
                    result.insert(0,["replace",(i-1),(j-1)])
                    i-=1
                    j-=1
                elif (mat[i][j]==(mat[i][j-1]+1)):
                    result.insert(0,["insert",i,(j-1)])
                    j-=1
                elif (mat[i][j]==(mat[i-1][j]+1)):
                    result.insert(0,["delete",(i-1),j])
                    i-=1
                else:
                    result.append(["what",i,j])
                    i-=1
                    j-=1
            if mat[i][j]==0:
                break

        Leditops=result

        self.label.configure(text="Levenshtein Distance= "+str(Ldistance))#+'\n'+str(Leditops))
        #self.text.delete(0.0,'end')
        self.text2.delete(0.0,'end')
        #self.text.insert('end', ' '.join(map(str, s)))
        n=0
        for i in range(len(Leditops)):
            if Leditops[i][0]=='delete':
                t.insert((Leditops[i][2]+n),s[(Leditops[i][1])])
                n+=1
            if Leditops[i][0]=='replace':
                t.insert((Leditops[i][2]+n),s[Leditops[i][1]])
                n+=1

        self.text2.insert('end',' '.join(map(str, t)))
        target=' '.join(map(str, t))
        for si in range(len(source)):
            if source[si]==" ":
                a.append(si+1)
        for ti in range(len(target)):
            if target[ti]==" ":
                b.append(ti+1)
        a.append(len(source))
        b.append(len(target))

        n=0
        for i in range(len(Leditops)):
            if Leditops[i][0]=='insert':
                self.text2.tag_add("insert", ("1."+str(b[(Leditops[i][2])+n])),("1."+str(b[(Leditops[i][2])+1+n])))
            elif Leditops[i][0]=='delete':
                #self.text.tag_add("delete", ("1."+str(a[(Leditops[i][1])])), ("1."+str(a[(Leditops[i][1])+1])))
                self.text2.tag_add("delete", ("1."+str(b[(Leditops[i][2])+n])), ("1."+str(b[(Leditops[i][2])+1+n])))
                n+=1
            elif Leditops[i][0]=='replace':
                #self.text.tag_add("replace", ("1."+str(a[(Leditops[i][1])])),("1."+str(a[(Leditops[i][1])+1])))
                self.text2.tag_add("replace", ("1."+str(b[(Leditops[i][2])+n])),("1."+str(b[(Leditops[i][2])+1+n])))
                self.text2.tag_add("replace2", ("1."+str(b[(Leditops[i][2])+n+1])),("1."+str(b[(Leditops[i][2])+2+n])))
                n+=1

        self.text2.tag_config("insert", background="yellow", foreground="#33CCCC")
        self.text2.tag_config("delete", foreground="blue", overstrike=True)
        #self.text.tag_config("delete", foreground="blue", overstrike=True)
        #self.text.tag_config("replace", foreground="red")
        self.text2.tag_config("replace", foreground="red", overstrike=True)
        self.text2.tag_config("replace2", foreground="red")

        #self.label2.configure(text="hihi",background="blue", foreground="white")

    def button_click(self, e):
        pass
App()
