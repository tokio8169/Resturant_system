
from importlib.metadata import requires
from tkinter import*
from tkinter import filedialog,messagebox
import random
import time

import requests

#reset btn

def reset_btn():
      textreceipt.delete(1.0,END)
      #setvalue #food
      textroti.set('0')
      textdaal.set('0')
      textrice.set('0')
      texttanduri.set('0')
      textpanner.set('0')
      textchicken.set('0')
      textfish.set('0')
      textbiryani.set('0')
      textchinees.set('0')



      #drink setvalue
      textlassi.set('0')
      textcoffee.set('0')
      texttea.set('0')
      textfaluda.set('0')
      textshikanji.set('0')
      textjaljira.set('0')
      textmirinda.set('0')
      textmazza.set('0')
      textsprite.set('0')
      

      #cake setvalue 

      textoreo.set('0')
      textdark.set('0')
      textkitkat.set('0')
      textpineapple.set('0')
      textstawerry.set('0')
      textblackberry.set('0')
      textorange.set('0')
      textvanilla.set('0')
      textbanana.set('0')



      rotientry.config(state=DISABLED)
      daalentry.config(state=DISABLED)
      riceentry.config(state=DISABLED)
      tandurientry.config(state=DISABLED)
      pannerentry.config(state=DISABLED)
      chickenentry.config(state=DISABLED)
      fishentry.config(state=DISABLED)
      biryanientry.config(state=DISABLED)
      chineesentry.config(state=DISABLED)

      
      lassientry.config(state=DISABLED)
      coffeeentry.config(state=DISABLED)
      teaentry.config(state=DISABLED)
      faludaentry.config(state=DISABLED)
      shikanjientry.config(state=DISABLED)
      jaljiraentry.config(state=DISABLED)
      mirindaentry.config(state=DISABLED)
      mazzaentry.config(state=DISABLED)
      spriteentry.config(state=DISABLED)



      oreoentry.config(state=DISABLED)
      darkentry.config(state=DISABLED)
      kitkatentry.config(state=DISABLED)
      pineappleentry.config(state=DISABLED)
      stawerryentry.config(state=DISABLED)
      blackberryentry.config(state=DISABLED)
      orangeentry.config(state=DISABLED)
      vanillaentry.config(state=DISABLED)
      bananaentry.config(state=DISABLED)


       
      


      #food checkbutton
      var1.set('0')
      var2.set('0')
      var3.set('0')
      var4.set('0')
      var5.set('0')
      var6.set('0')
      var7.set('0')
      var8.set('0')
      var9.set('0')

      #drinkcheckbutton
      var10.set('0')
      var11.set('0')
      var12.set('0')
      var13.set('0')
      var14.set('0')
      var15.set('0')
      var16.set('0')
      var17.set('0')
      var18.set('0')

      #cakecheckbutton
      var19.set('0')
      var20.set('0')
      var21.set('0')
      var22.set('0')
      var23.set('0')
      var24.set('0')
      var25.set('0')
      var26.set('0')
      var27.set('0')


      textcostfood.set('')
      textcostdrink.set('')
      textcostcake.set('')
      textsubtotal.set('')
      textservice.set('')
      texttotal.set('')
      

#send
def send():
      if textreceipt.get(1.0,END)=='\n':
            pass
      else:    


        def send_msg():
              message=textarea.get(1.0,END)
              number=mobentry.get()

              auth='09B7RdI5EFlGgJ6C8jPhUzYQisXwxnSNfb4HOupV3okvqLMrWZmfePBRYGVhlD5aH73uXsjxb9K0yNAk'
              url='https://www.fast2sms.com/dev/bulk'


              params={
                'authorization':auth,
                'message':message,
                'sender-id':'FSTSMS',
                'route':'p',
                'language':'english'

            }
            
              response=requests.get(url,params=params)
              dic=response.json()
              result=dic.get('return')

              if result==True:
                    messagebox.showinfo('send successfully', 'Message Sent Successfully')

              else:
                    messagebox.showerror('Error','Something Went Wrong')
            
      root2=Toplevel()
      
      root2.title("Send Bill")
      root2.config(bg="Deepskyblue3")
      root2.geometry("555x660+50+50")

      logoimg=PhotoImage(file="13d@2x.png" ,width=110,height=110)
      label=Label(root2, text="Send",bg="Deepskyblue3", font="flat 26 bold", image=logoimg)
      label.pack(pady=10)


      moblabel=Label(root2, text="Mobile Number", font="flat 17 underline bold",bg="Deepskyblue3", fg="white")
      moblabel.pack(pady=5)
      
      mobentry=Entry(root2, font="flat 16 bold", width=22 ,bd=4, relief=RIDGE)
      mobentry.pack()

      
      billlabel=Label(root2, text="Bill Detail", font="flat 17 underline bold",bg="Deepskyblue3", fg="white")
      billlabel.pack(pady=15)

      textarea=Text(root2, font="flat 15 bold", width=35, height=13)
      textarea.pack(pady=4)

      textarea.insert(END, 'Receipt Ref: \t'+billnumber+'\t\t'+date +'\n\n')

      textarea.insert(END, 'Items:\t\t Cost of Item(Rs)\n') 
      textarea.insert(END, '---------------------------------------------------------\n')

      if textcostfood.get()!='0':
           textarea.insert(END, f'Cost Of Food\t\t{priceoffood} Rs\n')
      if textcostdrink.get()!='0':
          textarea.insert(END, f'Cost Of Drink\t\t{priceofdrink} Rs\n')
      if textcostcake.get()!='0':
          textarea.insert(END, f'Cost Of Cake\t\t{priceofcake} Rs\n')

          textarea.insert(END, f'Sub Total\t\t{subtotalitem} Rs\n')

          textarea.insert(END, f'Service Tax\t\t{50} Rs\n')

          textarea.insert(END, f'Total Cost\t\t{subtotalitem+50} Rs\n')


      sendbtn=Button(root2, text="Send",font="flat 13 bold", bg="lightgreen", bd=4, relief=RAISED, command=send_msg)
      sendbtn.pack()
 
          
      root2.mainloop()

#save 
def save():
      if textreceipt.get(1.0,END)=='\n':
         pass
      else:      
          url=filedialog.asksaveasfile(mode='w', defaultextension='.txt')
          if url==None:
                pass
          else:    
          
           bill_data=textreceipt.get(1.0,END)
           url.write(bill_data)
           url.close()
           messagebox.showinfo('Information', 'your Bill is Successfully Saved')

#Receiptbill function

def receiptitem():
     global billnumber,date 
    #  global priceoffood,priceofdrink,priceofcake,subtotalitem,servicetax,totalcostitem
   

     textreceipt.delete(1.0, END)
     x=random.randint(100, 10000) 
     billnumber='Bill '+str(x)
     date=time.strftime('%d/%m/%Y')
     textreceipt.insert(END , 'Receipt Ref:\t'+ billnumber +'\t\t' +date+'\n')
     textreceipt.insert(END, '-----------------------------------------------------------\n')
     textreceipt.insert(END, 'Items:\t\t Cost of Item(Rs)\n\n') 
     textreceipt.insert(END, '-----------------------------------------------------------\n')
        
        #food
     if textroti.get()!='0':
           textreceipt.insert(END,f'Roti\t\t\t{int(textroti.get())*10}\n\n' )

     if textdaal.get()!='0':
           textreceipt.insert(END,f'Daal\t\t\t{int(textdaal.get())*40}\n\n' )


     if textrice.get()!='0':
           textreceipt.insert(END,f'Rice\t\t\t{int(textrice.get())*60}\n\n' )


     if textpanner.get()!='0':
           textreceipt.insert(END,f'Panner\t\t\t{int(textpanner.get())*160}\n\n' )


     if texttanduri.get()!='0':
           textreceipt.insert(END,f'Tanduri\t\t\t{int(texttanduri.get())*20}\n\n' )

     if textchicken.get()!='0':
           textreceipt.insert(END,f'Chicken\t\t\t{int(textchicken.get())*260}\n\n' )
          

     if textfish.get()!='0':
           textreceipt.insert(END,f'Fish\t\t\t{int(textfish.get())*160}\n\n' )



     if textbiryani.get()!='0':
           textreceipt.insert(END,f'Biryani\t\t\t{int(textbiryani.get())*260}\n\n' )


     if textchinees.get()!='0':
           textreceipt.insert(END,f'Chinees\t\t\t{int(textchinees.get())*250}\n\n' )
          
          #drink
     if textlassi.get()!='0':
           textreceipt.insert(END,f'Lassi\t\t\t{int(textlassi.get())*30}\n\n' )


     if textcoffee.get()!='0':
           textreceipt.insert(END,f'Coffee\t\t\t{int(textcoffee.get())*20}\n\n' )


     if texttea.get()!='0':
         textreceipt.insert(END,f'Tea\t\t\t{int(texttea.get())*10}\n\n' )

    
     if textfaluda.get()!='0':
         textreceipt.insert(END,f'Faluda\t\t\t{int(textfaluda.get())*40}\n\n' )


     if textjaljira.get()!='0':
         textreceipt.insert(END,f'Jaljira\t\t\t{int(textjaljira.get())*30}\n\n' )


     if textshikanji.get()!='0':
         textreceipt.insert(END,f'Shikanji\t\t\t{int(textshikanji.get())*60}\n\n' )


     if textmirinda.get()!='0':
         textreceipt.insert(END,f'Mirinda\t\t\t{int(textmirinda.get())*60}\n\n' )


     if textmazza.get()!='0':
         textreceipt.insert(END,f'Mazza\t\t\t{int(textmazza.get())*60}\n\n' )


     if textsprite.get()!='0':
         textreceipt.insert(END,f'Sprite\t\t\t{int(textsprite.get())*50}\n\n' )

        #cake
     if textoreo.get()!='0':
         textreceipt.insert(END,f'Oreo\t\t\t{int(textoreo.get())*350}\n\n' )


     if textdark.get()!='0':
         textreceipt.insert(END,f'Dark\t\t\t{int(textdark.get())*400}\n\n' )


     if textkitkat.get()!='0':
         textreceipt.insert(END,f'Kitkat\t\t\t{int(textkitkat.get())*350}\n\n' )

     if textvanilla.get()!='0':
         textreceipt.insert(END,f'Vanilla\t\t\t{int(textvanilla.get())*340}\n\n' )

     if textpineapple.get()!='0':
         textreceipt.insert(END,f'Pineapple\t\t\t{int(textpineapple.get())*300}\n\n' )

     if textstawerry.get()!='0':
         textreceipt.insert(END,f'Stawerry\t\t\t{int(textstawerry.get())*600}\n\n' )
              
     if textblackberry.get()!='0':
         textreceipt.insert(END,f'Blackberry\t\t\t{int(textblackberry.get())*460}\n\n' )    

     if textorange.get()!='0':
             textreceipt.insert(END,f'Orange\t\t\t{int(textorange.get())*260}\n\n' )

     if textbanana.get()!='0':
           textreceipt.insert(END,f'Banana\t\t\t{int(textbanana.get())*350}\n\n' )

           textreceipt.insert(END, '-----------------------------------------------------------\n')   
     if textcostfood.get()!='0':
           textreceipt.insert(END, f'Cost Of Food\t\t{priceoffood} Rs\n\n')
     if textcostdrink.get()!='0':
           textreceipt.insert(END, f'Cost Of Drink\t\t{priceofdrink} Rs\n\n')
     if textcostcake.get()!='0':
           textreceipt.insert(END, f'Cost Of Cake\t\t{priceofcake} Rs\n\n')

           textreceipt.insert(END, f'Sub Total\t\t{subtotalitem} Rs\n\n')

           textreceipt.insert(END, f'Service Tax\t\t{50} Rs\n\n')

           textreceipt.insert(END, f'Total Cost\t\t{subtotalitem+50} Rs\n\n')
           textreceipt.insert(END, '-----------------------------------------------------------\n')




#totalbuuton function

def totalcost():
      global priceoffood,priceofdrink,priceofcake,subtotalitem,servicetax,totalcostitem
     
#food checkbutton

      if   var1.get()!=0 or var2.get()!=0 or  var3.get()!=0 or var4.get()!=0 or var4.get()!=0 or \
        var6.get()!=0 or var7.get()!=0 or var8.get()!=0 or var10.get()!=0 or var11.get()!=0 or\
        var12.get()!=0 or   var13.get()!=0 or var14.get()!=0 or var15.get()!=0 or var16.get()!=0 or \
        var17.get()!=0 or var18.get()!=0 or var19.get()!=0 or var20.get()!=0 or var21.get()!=0 or \
        var21.get()!=0 or var22.get()!=0 or var23.get()!=0 or var24.get()!=0 or var25.get()!=0 or \
        var26.get()!=0 or var27.get()!=0 :
        

    # else:
    #     messagebox.showerror('Error','No item is selected')



      #food
       item1=int(textroti.get())
       item2=int(textdaal.get())
       item3=int(textrice.get())
       item4=int(textpanner.get())
       item5=int(texttanduri.get())
       item6=int(textchicken.get())
       item7=int(textfish.get())
       item8=int(textbiryani.get())
       item9=int(textchinees.get())

     #drink

       item10=int(textlassi.get())
       item11=int(textcoffee.get())
       item12=int(texttea.get())
       item13=int(textfaluda.get())
       item14=int(textjaljira.get())
       item15=int(textshikanji.get())
       item16=int(textmirinda.get())
       item17=int(textmazza.get())
       item18=int(textsprite.get())

      #cake
       item19=int(textoreo.get())
       item20=int(textdark.get())
       item21=int(textkitkat.get())
       item22=int(textvanilla.get())
       item23=int(textpineapple.get())
       item24=int(textstawerry.get())
       item25=int(textblackberry.get())
       item26=int(textorange.get())
       item27=int(textbanana.get())

       priceoffood=(item1*10)+(item2*40)+(item3*60)+(item4*160)+(item5*20)+(item6*260)+(item7*160)\
             +(item8*260)+(item9*250)

       priceofdrink=(item10*30)+(item11*20)+ (item12*10)+ (item13*40)+ (item14*30)+ (item15*60)\
        +  (item16*60)+ (item17*60)+(item18*50)

       priceofcake=(item19*350)+(item20*400)+ (item21*350)+ (item22*340)+ (item23*300)+ (item24*600)\
        +  (item25*460)+ (item26*260)+(item27*350)

       textcostfood.set(str(priceoffood)+' Rs')

       textcostdrink.set(str(priceofdrink)+' Rs')

       textcostcake.set(str(priceofcake)+' Rs')
       


    #subtotalitem
       subtotalitem=priceoffood+priceofdrink+priceofcake
       textsubtotal.set(str(subtotalitem )+' Rs')


       textservice.set('50 Rs')


       totalcostitem=subtotalitem+50
       texttotal.set(str(totalcostitem)+' Rs')

      else:
            messagebox.showerror('Error','No item is selected')
             
         


#Function

def roti():
    if var1.get()==1:
     rotientry.config(state=NORMAL)
     rotientry.delete(0,END)
     rotientry.focus()
    else:
        rotientry.config(state=DISABLED)
        textroti.set('0')
                
def daal():
    if var2.get()==1:
     daalentry.config(state=NORMAL)
     daalentry.delete(0,END)
     daalentry.focus()
    else:
        daalentry.config(state=DISABLED)
        textdaal.set('0')

def rice():
    if var3.get()==1:
     riceentry.config(state=NORMAL)
     riceentry.delete(0, END)
     riceentry.focus()

    else:
        riceentry.config(state=DISABLED)
        textrice.set('0')


def panner():
    if var4.get()==1:
     pannerentry.config(state=NORMAL)
     pannerentry.delete(0,END)
     pannerentry.focus()
    else:
        pannerentry.config(state=DISABLED)
        textpanner.set('0')        



def tanduri():
    if  var5.get()==1:
      tandurientry.config(state=NORMAL)
      tandurientry.delete(0,END)
      tandurientry.focus()
    else:
        tandurientry.config(state=DISABLED)
        texttanduri.set('0')   

def chicken():
    if var6.get()==1:
        chickenentry.config(state=NORMAL)
        chickenentry.delete(0,END)
        chickenentry.focus()
    else:
        chickenentry.config(state=DISABLED)
        textchicken.set('0')   

def fish():
    if var7.get()==1:
        fishentry.config(state=NORMAL)
        fishentry.delete(0,END)
        fishentry.focus()
    else:
        fishentry.config(state=DISABLED)
        textfish.set('0')  


def biryani():
      if var8.get()==1:
        biryanientry.config(state=NORMAL)
        biryanientry.delete(0,END)
        biryanientry.focus()
      else:
        biryanientry.config(state=DISABLED)
        textbiryani.set('0')  


def chinees():    
       if var9.get()==1:
         chineesentry.config(state=NORMAL)
         chineesentry.delete(0,END)
         chineesentry.focus()
       else:
         chineesentry.config(state=DISABLED)
         textchinees.set('0')  


def lassi():
       if var10.get()==1:
         lassientry.config(state=NORMAL)
         lassientry.delete(0,END)
         lassientry.focus()
       else:
         lassientry.config(state=DISABLED)
         textlassi.set('0')  



def coffee():
       if var11.get()==1:
         coffeeentry.config(state=NORMAL)
         coffeeentry.delete(0,END)
         coffeeentry.focus()
       else:
         coffeeentry.config(state=DISABLED)
         textcoffee.set('0')  


def tea():
       if var12.get()==1:
         teaentry.config(state=NORMAL)
         teaentry.delete(0,END)
         teaentry.focus()
       else:
         teaentry.config(state=DISABLED)
         texttea.set('0')  


def faluda():
       if var13.get()==1:
         faludaentry.config(state=NORMAL)
         faludaentry.delete(0,END)
         faludaentry.focus()
       else:
         faludaentry.config(state=DISABLED)
         textfaluda.set('0')  


def jaljira():
       if var14.get()==1:
         jaljiraentry.config(state=NORMAL)
         jaljiraentry.delete(0,END)
         jaljiraentry.focus()
       else:
         jaljiraentry.config(state=DISABLED)
         textjaljira.set('0')  


def shikanji():
       if var15.get()==1:
         shikanjientry.config(state=NORMAL)
         shikanjientry.delete(0,END)
         shikanjientry.focus()
       else:
         shikanjientry.config(state=DISABLED)
         textshikanji.set('0')  



def mirinda():
       if var16.get()==1:
         mirindaentry.config(state=NORMAL)
         mirindaentry.delete(0,END)
         mirindaentry.focus()
       else:
         mirindaentry.config(state=DISABLED)
         textmirinda.set('0')  


def mazza():
       if var17.get()==1:
         mazzaentry.config(state=NORMAL)
         mazzaentry.delete(0,END)
         mazzaentry.focus()
       else:
         mazzaentry.config(state=DISABLED)
         textmazza.set('0')  


def sprite():
       if var18.get()==1:
         spriteentry.config(state=NORMAL)
         spriteentry.delete(0,END)
         spriteentry.focus()
       else:
         spriteentry.config(state=DISABLED)
         textsprite.set('0')  

def oreo():
       if var19.get()==1:
         oreoentry.config(state=NORMAL)
         oreoentry.delete(0,END)
         oreoentry.focus()
       else:
         oreoentry.config(state=DISABLED)
         textoreo.set('0')  

def dark():
       if var20.get()==1:
         darkentry.config(state=NORMAL)
         darkentry.delete(0,END)
         darkentry.focus()
       else:
         darkentry.config(state=DISABLED)
         textdark.set('0')  

def kitkat():
       if var21.get()==1:
         kitkatentry.config(state=NORMAL)
         kitkatentry.delete(0,END)
         kitkatentry.focus()
       else:
         kitkatentry.config(state=DISABLED)
         textkitkat.set('0')  

def vanilla():
       if var22.get()==1:
         vanillaentry.config(state=NORMAL)
         vanillaentry.delete(0,END)
         vanillaentry.focus()
       else:
         vanillaentry.config(state=DISABLED)
         textvanilla.set('0')  

def pineapple():
      if  var23.get()==1:
         pineappleentry.config(state=NORMAL)
         pineappleentry.delete(0,END)
         pineappleentry.focus()
      else:
         pineappleentry.config(state=DISABLED)
         textpineapple.set('0') 

def stawerry():
      if  var24.get()==1:
         stawerryentry.config(state=NORMAL)
         stawerryentry.delete(0,END)
         stawerryentry.focus()
      else:
         stawerryentry.config(state=DISABLED)
         textstawerry.set('0') 

def blackberry():
      if var25.get()==1:
         blackberryentry.config(state=NORMAL)
         blackberryentry.delete(0,END)
         blackberryentry.focus()
      else:
         blackberryentry.config(state=DISABLED)
         textblackberry.set('0') 


def orange():
      if var26.get()==1:
         orangeentry.config(state=NORMAL)
         orangeentry.delete(0,END)
         orangeentry.focus()
      else:
         orangeentry.config(state=DISABLED)
         textorange.set('0') 

def Banana():
      if var27.get()==1:
         bananaentry.config(state=NORMAL)
         bananaentry.delete(0,END)
         bananaentry.focus()
      else:
         bananaentry.config(state=DISABLED)
         textbanana.set('0') 




root=Tk()

root.geometry("1270x690+0+0")

root.title("Resturant Management System")

root.config(bg="Deepskyblue3")

top_frame=Frame(root, border=8, bg="Deepskyblue3", borderwidth=8, relief=RIDGE)
top_frame.pack(side=TOP)

top_label=Label(top_frame, text="RESTURANT MANAGEMENT SYSTEM", width=40, font=" flat 34 bold", bg="Deepskyblue2", fg="yellow")
top_label.grid(row=0, column=0)


#menuFrame

menuframe=Frame(root, bd=10, relief=RIDGE, bg="Deepskyblue3")
menuframe.pack(side=LEFT)

#costframe
costframe=Frame(menuframe, bd=8, relief=RIDGE,borderwidth=8, bg="Deepskyblue3")
costframe.pack(side=BOTTOM,pady=5)

#Right frame
rightframe=Frame(root, bd=4, bg="Deepskyblue3", borderwidth=6, relief=RIDGE)
rightframe.pack(side=RIGHT)


#buttonframe
buttonframe=Frame(rightframe, bd=3, bg="Deepskyblue3", borderwidth=4, relief=RIDGE)
buttonframe.pack(side=BOTTOM)

#calculator frame
calframe=Frame(rightframe, bd=3, bg="Deepskyblue3", borderwidth=2)
calframe.pack()


#recipt frame
reciptframe=Frame(rightframe, bd=4, borderwidth=3, relief=RIDGE)
reciptframe.pack(side=TOP)




#food checkbutton
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()

#drinkcheckbutton
var10=IntVar()
var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()

#cakecheckbutton
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()


#foodEntry var #entryvar

textroti=StringVar()
textdaal=StringVar()
textrice=StringVar()
texttanduri=StringVar()
textpanner=StringVar()
textchicken=StringVar()
textfish=StringVar()
textbiryani=StringVar()
textchinees=StringVar()

#setvalue #food
textroti.set('0')
textdaal.set('0')
textrice.set('0')
texttanduri.set('0')
textpanner.set('0')
textchicken.set('0')
textfish.set('0')
textbiryani.set('0')
textchinees.set('0')


#drinkEntry var 
textlassi=StringVar()
textcoffee=StringVar()
texttea=StringVar()
textfaluda=StringVar()
textshikanji=StringVar()
textjaljira=StringVar()
textmirinda=StringVar()
textmazza=StringVar()
textsprite=StringVar()


#drink setvalue
textlassi.set('0')
textcoffee.set('0')
texttea.set('0')
textfaluda.set('0')
textshikanji.set('0')
textjaljira.set('0')
textmirinda.set('0')
textmazza.set('0')
textsprite.set('0')


#cakeEntry var
textoreo=StringVar()
textdark=StringVar()
textkitkat=StringVar()
textpineapple=StringVar()
textstawerry=StringVar()
textblackberry=StringVar()
textorange=StringVar()
textvanilla=StringVar()
textbanana=StringVar()


#cake setvalue 

textoreo.set('0')
textdark.set('0')
textkitkat.set('0')
textpineapple.set('0')
textstawerry.set('0')
textblackberry.set('0')
textorange.set('0')
textvanilla.set('0')
textbanana.set('0')

#costvar
textcostfood=StringVar()
textcostdrink=StringVar()
textcostcake=StringVar()
textsubtotal=StringVar()
textservice=StringVar()
texttotal=StringVar()



#foodframe
foodFrame=LabelFrame(menuframe,  text="Food", font="flat 19 bold" ,bd=10, borderwidth=8, relief=RIDGE)
foodFrame.pack(side=LEFT)

#foodcheckbutton
roti=Checkbutton(foodFrame, text="Roti", font="flat 18 bold",  onvalue=1, offvalue=0, variable=var1,command=roti)
roti.grid(row=0, column=0, sticky=W , pady=5)

daal=Checkbutton(foodFrame, text="Daal", font="flat 18 bold", onvalue=1, offvalue=0, variable=var2 , command=daal)
daal.grid(row=1,column=0, sticky=W ,pady=5)

rice=Checkbutton(foodFrame, text="Rice", font="flat 18 bold", onvalue=1, offvalue=0, variable=var3 ,command=rice)
rice.grid(row=2, column=0, sticky=W,pady=5)

panner=Checkbutton(foodFrame, text="Panner", font="flat 18 bold", onvalue=1, offvalue=0, variable=var4 ,command=panner)
panner.grid(row=3, column=0 ,sticky=W,pady=5)

tanduri=Checkbutton(foodFrame, text="Tanduri", font="flat 18 bold", onvalue=1, offvalue=0, variable=var5 , command=tanduri)
tanduri.grid(row=4, column=0 ,sticky=W,pady=5)

chicken=Checkbutton(foodFrame, text="Chicken", font="flat 18 bold", onvalue=1, offvalue=0, variable=var6 , command=chicken)
chicken.grid(row=5, column=0, sticky=W,pady=5)

fish=Checkbutton(foodFrame, text="Fish", font="flat 18 bold", onvalue=1, offvalue=0, variable=var7 ,command=fish)
fish.grid(row=6, column=0,sticky=W,pady=5)

biryani=Checkbutton(foodFrame, text="Biryani", font="flat 18 bold", onvalue=1, offvalue=0, variable=var8 , command=biryani)
biryani.grid(row=7, column=0,sticky=W,pady=5)

chinees=Checkbutton(foodFrame, text="Chinees", font="flat 18 bold", onvalue=1, offvalue=0, variable=var9 , command=chinees)
chinees.grid(row=8, column=0 ,sticky=W,pady=5)


#foodEntry 

rotientry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textroti )
rotientry.grid(row=0, column=1)


daalentry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textdaal)
daalentry.grid(row=1, column=1)

riceentry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textrice)
riceentry.grid(row=2, column=1)


pannerentry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textpanner)
pannerentry.grid(row=3, column=1)

tandurientry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=texttanduri)
tandurientry.grid(row=4, column=1)

chickenentry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textchicken)
chickenentry.grid(row=5, column=1)

fishentry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textfish)
fishentry.grid(row=6, column=1)

biryanientry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textbiryani)
biryanientry.grid(row=7, column=1)

chineesentry=Entry(foodFrame,font="flat 18 bold", bd=7, width=6, state=DISABLED, textvariable=textchinees)
chineesentry.grid(row=8, column=1)



#drinkframe
drinkFrame=LabelFrame(menuframe, text="Drinks", font="flat 19 bold" ,bd=10, borderwidth=8, relief=RIDGE)
drinkFrame.pack(side=LEFT)

#drinkcheckbutton

lassi=Checkbutton(drinkFrame, text="Lassi", font="flat 18 bold", onvalue=1,offvalue=0,variable=var10 ,command=lassi)
lassi.grid(row=0, column=0, sticky=W,pady=5)

coffee=Checkbutton(drinkFrame, text="Coffee", font="flat 18 bold", onvalue=1,offvalue=0,variable=var11 ,command=coffee)
coffee.grid(row=1, column=0,sticky=W ,pady=5)

tea=Checkbutton(drinkFrame, text="Tea", font="flat 18 bold", onvalue=1,offvalue=0,variable=var12 ,command=tea)
tea.grid(row=2, column=0,sticky=W, pady=5)

faluda=Checkbutton(drinkFrame, text="Faluda", font="flat 18 bold", onvalue=1,offvalue=0,variable=var13 ,command=faluda)
faluda.grid(row=3, column=0,sticky=W, pady=5)

jaljira=Checkbutton(drinkFrame, text="jai-jeera", font="flat 18 bold", onvalue=1,offvalue=0,variable=var14 ,command=jaljira)
jaljira.grid(row=4, column=0,sticky=W ,pady=5)

shikanji=Checkbutton(drinkFrame, text="Shikanji", font="flat 18 bold", onvalue=1,offvalue=0,variable=var15 ,command=shikanji)
shikanji.grid(row=5, column=0,sticky=W ,pady=5)

mirinda=Checkbutton(drinkFrame, text="Mirinda", font="flat 18 bold", onvalue=1,offvalue=0,variable=var16, command=mirinda)
mirinda.grid(row=6, column=0,sticky=W ,pady=5)

mazza=Checkbutton(drinkFrame, text="Mazza", font="flat 18 bold", onvalue=1,offvalue=0,variable=var17, command=mazza)
mazza.grid(row=7, column=0, sticky=W ,pady=5)

sprite=Checkbutton(drinkFrame, text="Sprite", font="flat 18 bold", onvalue=1,offvalue=0,variable=var18, command=sprite)
sprite.grid(row=8, column=0, sticky=W, pady=5)

#drinkEntry

lassientry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7, state=DISABLED, textvariable=textlassi)
lassientry.grid(row=0, column=1)

coffeeentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7, state=DISABLED, textvariable=textcoffee)
coffeeentry.grid(row=1, column=1)

teaentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7, state=DISABLED, textvariable=texttea)
teaentry.grid(row=2, column=1)

faludaentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7, state=DISABLED, textvariable=textfaluda)
faludaentry.grid(row=3, column=1)

jaljiraentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7,  state=DISABLED, textvariable=textjaljira)
jaljiraentry.grid(row=4, column=1)

shikanjientry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7,  state=DISABLED, textvariable=textshikanji)
shikanjientry.grid(row=5, column=1)

mirindaentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7,  state=DISABLED, textvariable=textmirinda)
mirindaentry.grid(row=6, column=1)

mazzaentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7,  state=DISABLED, textvariable=textmazza)
mazzaentry.grid(row=7, column=1)

spriteentry=Entry(drinkFrame, font=" flat 18 bold", width=6,bd=7, state=DISABLED, textvariable=textsprite)
spriteentry.grid(row=8, column=1)



#cakeframe
cakeFrame=LabelFrame(menuframe, text="Cakes", font="flat 19 bold" ,bd=10, borderwidth=8, relief=RIDGE)
cakeFrame.pack(side=LEFT)

#cakebutton

oreo=Checkbutton(cakeFrame,text="Oreo" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var19 ,command=oreo)
oreo.grid(row=0, column=0,sticky=W ,pady=5)

dark=Checkbutton(cakeFrame,text="Dark" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var20, command=dark)
dark.grid(row=1, column=0,sticky=W ,pady=5)

kitkat=Checkbutton(cakeFrame,text="Kitkat" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var21, command=kitkat)
kitkat.grid(row=2, column=0,sticky=W ,pady=5)

vanilla=Checkbutton(cakeFrame,text="Vanilla" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var22, command=vanilla)
vanilla.grid(row=3, column=0,sticky=W ,pady=5)

pineapple=Checkbutton(cakeFrame,text="Apple" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var23, command=pineapple)
pineapple.grid(row=4, column=0,sticky=W ,pady=5)

stawerry=Checkbutton(cakeFrame,text="Jelly" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var24, command=stawerry)
stawerry.grid(row=5, column=0,sticky=W ,pady=5)


orange=Checkbutton(cakeFrame,text="Orange" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var25, command=orange)
orange.grid(row=6, column=0,sticky=W ,pady=5)

blackberry=Checkbutton(cakeFrame,text="Berry" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var26, command=blackberry)
blackberry.grid(row=7, column=0,sticky=W ,pady=5)

Banana=Checkbutton(cakeFrame,text="Banana" ,font="flat 18 bold", onvalue=1,offvalue=0,variable=var27, command=Banana)
Banana.grid(row=8, column=0,sticky=W ,pady=5)


#cakeEntry

oreoentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7, state=DISABLED, textvariable=textoreo)
oreoentry.grid(row=0 , column=1)

darkentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7,state=DISABLED, textvariable=textdark)
darkentry.grid(row=1 , column=1)

kitkatentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7, state=DISABLED, textvariable=textkitkat)
kitkatentry.grid(row=2 , column=1)


vanillaentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7, state=DISABLED, textvariable=textvanilla)
vanillaentry.grid(row=3, column=1)

pineappleentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7,state=DISABLED, textvariable=textpineapple)
pineappleentry.grid(row=4, column=1)


stawerryentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7,state=DISABLED, textvariable=textstawerry)
stawerryentry.grid(row=5, column=1)

orangeentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7,state=DISABLED, textvariable=textorange)
orangeentry.grid(row=6, column=1)

blackberryentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7,state=DISABLED, textvariable=textblackberry)
blackberryentry.grid(row=7 , column=1)

bananaentry=Entry(cakeFrame, font=" flat 18 bold", width=6, bd=7,state=DISABLED, textvariable=textbanana)
bananaentry.grid(row=8 , column=1)



#costlabel and entry 

costoflabelfood=Label(costframe, text="Cost Of Food", font="flat 16 bold", bg="Deepskyblue3", fg="yellow")
costoflabelfood.grid(row=0 , column=0)

entrycostfood=Entry(costframe, width=13, state='readonly', textvariable=textcostfood,  font="flat 16 bold", bd=6)
entrycostfood.grid(row=0,column=1,padx=30)


costoflabeldrink=Label(costframe, text="Cost Of Drink", font="flat 16 bold", bg="Deepskyblue3", fg="yellow")
costoflabeldrink.grid(row=1 , column=0)

entrycostdrink=Entry(costframe, width=13, state='readonly', textvariable=textcostdrink, font="flat 16 bold", bd=6)
entrycostdrink.grid(row=1,column=1,padx=30)


costoflabelcake=Label(costframe, text="Cost Of Cake", font="flat 16 bold", bg="Deepskyblue3", fg="yellow")
costoflabelcake.grid(row=2 , column=0)

entrycostcake=Entry(costframe, width=13, state='readonly',textvariable=textcostcake, font="flat 16 bold", bd=6)
entrycostcake.grid(row=2,column=1,padx=30)


costoflabelsubtotal=Label(costframe, text="Sub Total", font="flat 16 bold", bg="Deepskyblue3", fg="yellow")
costoflabelsubtotal.grid(row=0 , column=2)

entrycostsubtotal=Entry(costframe, width=13, state='readonly', textvariable=textsubtotal, font="flat 16 bold", bd=6)
entrycostsubtotal.grid(row=0,column=3,padx=30)


servicetax=Label(costframe, text="Service Tax", font="flat 16 bold", bg="Deepskyblue3", fg="yellow")
servicetax.grid(row=1 , column=2)

entryservicetax=Entry(costframe, width=13, state='readonly', textvariable=textservice, font="flat 16 bold", bd=6)
entryservicetax.grid(row=1,column=3,padx=30)
 
costoflabeltotal=Label(costframe, text="Total", font="flat 16 bold", bg="Deepskyblue3", fg="yellow")
costoflabeltotal.grid(row=2 , column=2)

entrycosttotal=Entry(costframe, width=13, state='readonly', textvariable=texttotal, font="flat 16 bold", bd=6)
entrycosttotal.grid(row=2,column=3,padx=30)


#buuton

buttontotal=Button(buttonframe, text="Total", font="flat 12 bold",  relief=RAISED, bd=3, borderwidth=2,  bg="Deepskyblue3",fg="yellow", command=totalcost)
buttontotal.grid(row=0, column=0)

buttonreceipt=Button(buttonframe, text="Receipt",font="flat 12 bold",  relief=RAISED, bd=3,borderwidth=2, bg="Deepskyblue3",fg="yellow",command=receiptitem)
buttonreceipt.grid(row=0, column=1)


buttonsave=Button(buttonframe, text="Save", font="flat 12 bold",relief=RAISED, bd=3, borderwidth=2, bg="Deepskyblue3",fg="yellow", command=save)
buttonsave.grid(row=0, column=2)


buttonsend=Button(buttonframe, text="Send", font="flat 12 bold", relief=RAISED, bd=3, borderwidth=2,  bg="Deepskyblue3",fg="yellow", command=send)
buttonsend.grid(row=0, column=3)

buttonreset=Button(buttonframe, text="Reset", font="flat 12 bold", relief=RAISED, bd=3, borderwidth=2,  bg="Deepskyblue3",fg="yellow",command=reset_btn)
buttonreset.grid(row=0, column=4)


#text receipt

textreceipt=Text(reciptframe ,font="flat 12 bold", bd=3 ,width=44,height=19)
textreceipt.grid(row=0, column=0)


#calculator
operator=''
def buttonClick(numbers):
  
    global operator;
    operator=operator+numbers 
    calfield.delete(0, END)
    calfield.insert(END, operator)


def buttonClear():
    global operator
    operator=''
    calfield.delete(0,END)


def answer():
    global operator
    result=str(eval(operator))
    calfield.delete(0,END)
    calfield.insert(0,result)
    operator=''




calfield=Entry(calframe, font="flat 16 bold", width=26, bd=3)
calfield.grid(row=0, column=0, columnspan=4)

#calbutton
#1row
button7=Button(calframe, text='7' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('7'))
button7.grid(row=1, column=0)

button8=Button(calframe, text='8' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('8') )
button8.grid(row=1, column=1)

button9=Button(calframe, text='9' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('9') )
button9.grid(row=1, column=2)

buttonplus=Button(calframe, text='+' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5 , command=lambda:buttonClick('+') )
buttonplus.grid(row=1, column=3)

#2row
button4=Button(calframe, text='4' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('4') )
button4.grid(row=2, column=0)

button5=Button(calframe, text='5' ,font="flat 15 bold", fg="red", bg="white", bd=3, width=5 , command=lambda:buttonClick('5'))
button5.grid(row=2, column=1)

button6=Button(calframe, text='6' ,font="flat 15 bold", fg="red", bg="white", bd=3, width=5 ,command=lambda:buttonClick('6') )
button6.grid(row=2, column=2)

buttonminus=Button(calframe, text='-' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('-') )
buttonminus.grid(row=2, column=3)

#3row
button1=Button(calframe, text='1' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('1') )
button1.grid(row=3, column=0)

button2=Button(calframe, text='2' ,font="flat 15 bold", fg="red", bg="white", bd=3, width=5, command=lambda:buttonClick('2') )
button2.grid(row=3, column=1)

button3=Button(calframe, text='9' ,font="flat 15 bold", fg="red", bg="white", bd=3, width=5, command=lambda:buttonClick('3') )
button3.grid(row=3, column=2)

buttonmulti=Button(calframe, text='*' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('*') )
buttonmulti.grid(row=3, column=3)

#4row
buttonans=Button(calframe, text='Ans' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5 ,command=answer)
buttonans.grid(row=4, column=0)

buttonclear=Button(calframe, text='Clear' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5 ,command=buttonClear)
buttonclear.grid(row=4, column=1)

button0=Button(calframe, text='0' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('0') )
button0.grid(row=4, column=2)

buttondivide=Button(calframe, text='/' ,font="flat 15 bold", fg="yellow", bg="Deepskyblue3", bd=3, width=5, command=lambda:buttonClick('/') )
buttondivide.grid(row=4, column=3)



root.mainloop()