from tkinter import *
from tkinter import ttk
import random
import tkinter.messagebox
from tkinter import messagebox
import datetime
class ReasonForMedication:
    def __init__(self,root):
        self.root=root
        self.root.title("Welcome To Reason For Medication")
        self.root.geometry("1350x800+0+0")
        self.root.configure(background='Blue')

        #===============================================================Frame=Widget=====================================================================#
        MainFrame=Frame(self.root)
        MainFrame.grid()

        TitleFrame=Frame(MainFrame, bd=10,width=1350,padx=35,bg='Blue',relief=RIDGE)
        TitleFrame.pack(side=TOP)
        
        self.root=Label(TitleFrame,width=45,font=('arial',35,  'bold'),text="Welcome To Reason For Medication",padx=11,fg='white',bg='Blue')
        self.root.grid()
        
        BottomFrame=LabelFrame(MainFrame, bd=10,pady=5,width=45,padx=35,height=70,relief=RIDGE,font=('arial',20,'bold'), text=" Reason For Medication", fg='black',bg='Blue',)
        BottomFrame.pack(side=BOTTOM)
        
        MiddleFrame=Frame(MainFrame,bd=10,width=1200,height=100,padx=32,relief=RIDGE,bg='Blue')
        MiddleFrame.pack(side=BOTTOM)
        
        DataFrame=LabelFrame(MainFrame,bd=10,width=1200,height=400,padx=34,relief=RIDGE,bg='Blue')
        DataFrame.pack(side=BOTTOM)
        
        UpperFrameLeft=Frame(DataFrame,bd=10,width=700,height=220,padx=20,relief=RIDGE)
        UpperFrameLeft.pack(side=LEFT)
        UpperFrameRight=Frame(DataFrame,bd=10,width=570,height=220,padx=20,pady=4,relief=RIDGE,bg='Blue')
        UpperFrameRight.pack(side=RIGHT)
        
        LowerFrameLeft=LabelFrame(MiddleFrame,bd=10,width=570,height=220,padx=20, pady=4,relief=RIDGE,font=('arial',25,'bold'),bg='Blue',fg='white')
        LowerFrameLeft.pack(side=LEFT)
        LowerFrameRight=LabelFrame(MiddleFrame,bd=10,width=570,height=220,padx=20,relief=RIDGE,font=('arial',25,'bold'),bg='Blue',fg='white')
        LowerFrameRight.pack(side=RIGHT)
        
        #================================================================Variable==========================================================================#
        MeditationPeriod=StringVar() 
        MeditationCode_no=StringVar()
        Payment=StringVar()
        PayDate=StringVar()
        DactorRef=StringVar()  
        NonDiscountFees =StringVar()
        PayingFees=StringVar()
        PayAfterDiscount=StringVar()
        PayBeforeDiscount=StringVar()
        NetPay=StringVar()
        CompleteFees=StringVar()
        Deduction=StringVar()
        RegNumber=StringVar()  
        RefCode=StringVar()
        Dactor=StringVar()
        Patient=StringVar()  
        DiseaseName=StringVar()
        PayBeforeDiscount.set(250)
    
         #===============================================================Function=========================================================================#
        def Exit():
            Exit=tkinter.messagebox.askyesno("Reason For Medication ","Conform if you want to LogOut")
            if Exit>0:
                root.destroy()
                return
        def Reset():
            MeditationPeriod.set("Select Period")
            MeditationCode_no.set(" Select Code")
            Payment.set("Select Payment")
            PayDate.set("")
            DactorRef.set("")
            NonDiscountFees.set("")
            PayingFees.set("")
            PayAfterDiscount.set("")
            PayBeforeDiscount.set("")
            NetPay.set("")
            CompleteFees.set("")
            Deduction.set("")
            RegNumber.set("")
            RefCode.set("")
            Dactor.set("")
            Patient.set("")
            DiseaseName.set("")
        def PayDay():
            d1=datetime.date.today()
            PayDate.set(d1)
            NonDiscountFees.set(PayBeforeDiscount.get())
            q=float(Payment.get())
            p=float(NonDiscountFees.get())
            PayingFees.set( q - p)

            x=random.randint(200,7999)
            randomRef=str(x)
            DactorRef.set(randomRef)

        def DactorCode(evt):
    
            values=str(self.cboMeditationCode_no.get())
            TCode=values
            if(TCode=="TC1"):
                Payment.set(PayBeforeDiscount.get())
                PayDay()
                TPaid=float(PayingFees.get())
                if(TPaid <=250):
                    PayAfterDiscount.set(TPaid)

            elif(TCode =="TC2"):
               Payment.set("500")
               PayDay()
               TPaid=float( PayingFees.get())
               if(TPaid <=500):
                  PayAfterDiscount.set((TPaid*5)/100)
            elif(TCode =="TC3"):
                Payment.set("750")
                PayDay()
                TPaid=float( PayingFees.get())
                if(TPaid <=7500):
                    PayAfterDiscount.set((TPaid*20)/100)
            elif(TCode =="TC4"):
               Payment.set("1000")
               PayDay()
               TPaid=float(PayingFees.get())
               if(TPaid <=1000):
                 PayAfterDiscount.set((TPaid*30)/100)

                 
        def TotalFees():
             n=float(Payment.get())
             s=float(PayAfterDiscount.get())
             AfterDiscount=(n-s)
             G="$",str('%.2f' %(n))
             CompleteFees.set(G)
             D="$",str('%.2f' %(s))
             Deduction.set(D)
             pay=AfterDiscount
             iFees="$",str('%.2f' %((pay)))
             NetPay.set(iFees)
             PayDay()
            
       

        
            
        
        #================================================================Widget==========================================================================#
        self.rootMeditationPeriod =Label(UpperFrameRight,font=('arial',18,'bold'), text=" MedicationPeriod",padx=1,pady=2,bg='Blue',fg='white')
        self.rootMeditationPeriod.grid(row=0,column=0,sticky=W)
        self.cboMeditationPeriod=ttk.Combobox(UpperFrameRight,textvariable=MeditationPeriod,state='readonly', font=('arial',22,'bold'),width=27)
        self.cboMeditationPeriod['value']=('Select Treatment period','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
        self.cboMeditationPeriod.current(0)
        self.cboMeditationPeriod.grid(row=0,column=1,pady=2)
        
        self.rootMeditationCode_no=Label(UpperFrameRight,font=('arial',18,'bold'), text="MeditationCode",padx=1,pady=2,bg='Blue',fg='white')
        self.rootMeditationCode_no.grid(row=1,column=0,sticky=W)
        self.cboMeditationCode_no=ttk.Combobox(UpperFrameRight,textvariable=MeditationCode_no,state='readonly', font=('arial',22,'bold'),width=26)
        self.cboMeditationCode_no.bind("<<ComboboxSelected>>",DactorCode)
        self.cboMeditationCode_no['value']=('SelectMeditationCode_no','TC1','TC2','TC3','TC4')
        self.cboMeditationCode_no.current(0)
        self.cboMeditationCode_no.grid(row=1,column=1,pady=2)
        
        self.rootRegNumber=Label(UpperFrameRight,font=('arial',18,'bold'), text="RegNumber",padx=1,pady=2,bg='Blue',fg='white')
        self.rootRegNumber.grid(row=2,column=0,sticky=W)
        self.txtRegNumber=Entry(UpperFrameRight,width=21,font=('arial',26,'bold'), textvariable=RegNumber)
        self.txtRegNumber.grid(row=2,column=1,sticky=W)
          
        self.rootPayDueDay=Label(UpperFrameRight,font=('arial',18,'bold'), text="Ref Code",padx=1,pady=2,bg='Blue',fg='white')
        self.rootPayDueDay.grid(row=3,column=0,sticky=W)
        self.txtRefCode=Entry(UpperFrameRight,width=21,font=('arial',26,'bold'), textvariable=RefCode)
        self.txtRefCode.grid(row=3,column=1,sticky=W)

        #==============================================================UpperLeftFrame======================================================================#
        self.rootReference=Label(UpperFrameLeft,font=('arial',18,'bold'), text="Reference No",padx=1,pady=2,bg='Blue',fg='white')
        self.rootReference.grid(row=0,column=0,sticky=W)
        self.txtReference=Entry(UpperFrameLeft,width=21,font=('arial',26,'bold'), textvariable=DactorRef)
        self.txtReference.grid(row=0,column=1,sticky=W)
        
        self.rootDactor=Label(UpperFrameLeft,font=('arial',18,'bold'), text="Dactor",padx=1,pady=2,bg='Blue',fg='white')
        self.rootDactor.grid(row=1,column=0,sticky=W)
        self.txtDactor=Entry(UpperFrameLeft,width=21,font=('arial',26,'bold'), textvariable=Dactor)
        self.txtDactor.grid(row=1,column=1,sticky=W)
        
        self.rootPatient=Label(UpperFrameLeft,font=('arial',18,'bold'), text="Patient",padx=1,pady=2,bg='Blue',fg='white')
        self.rootPatient.grid(row=2,column=0,sticky=W)
        self.txtPatient=Entry(UpperFrameLeft,width=21,font=('arial',26,'bold'), textvariable=Patient)
        self.txtPatient.grid(row=2,column=1,sticky=W)

        
        
        self.rootDiseaseName=Label(UpperFrameLeft,font=('arial',18,'bold'), text="DiseaseName",padx=1,pady=2,bg='Blue',fg='white')
        self.rootDiseaseName.grid(row=3,column=0,sticky=W)
        self.txtDiseaseName=Entry(UpperFrameLeft,width=21,font=('arial',26,'bold'), textvariable=DiseaseName)
        self.txtDiseaseName.grid(row=3,column=1,sticky=W)
        
        #========================================================RightFrame_Bottom=========================================================================#
        self.rootDate=Label(LowerFrameRight,font=('arial',18,'bold'), text="Date",padx=1,pady=2,bg='Blue',fg='white')
        self.rootDate.grid(row=0,column=0,sticky=W)
        self.txtDate=Entry(LowerFrameRight,width=22,font=('arial',26,'bold'), textvariable=PayDate)
        self.txtDate.grid(row=0,column=1,sticky=W)
        
        self.rootCompleteFees=Label(LowerFrameRight,font=('arial',18,'bold'), text="CompleteFees",padx=1,pady=2,bg='Blue',fg='white')
        self.rootCompleteFees.grid(row=1,column=0,sticky=W)
        self.txtCompleteFees=Entry(LowerFrameRight,width=21,font=('arial',26,'bold'), textvariable=CompleteFees)
        self.txtCompleteFees.grid(row=1,column=1,sticky=W)
        
        self.rootDeduction=Label(LowerFrameRight,font=('arial',18,'bold'), text="Deduction",padx=1,pady=2,bg='Blue',fg='white')
        self.rootDeduction.grid(row=2,column=0,sticky=W)
        self.txtDeduction=Entry(LowerFrameRight,width=21,font=('arial',26,'bold'), textvariable=Deduction)
        self.txtDeduction.grid(row=2,column=1,sticky=W)
        
        self.rootNetPay=Label(LowerFrameRight,font=('arial',18,'bold'), text="NetPay",padx=1,pady=2,bg='Blue',fg='white')
        self.rootNetPay.grid(row=3,column=0,sticky=W)
        self.txtNetPay=Entry(LowerFrameRight,width=21,font=('arial',26,'bold'), textvariable=NetPay)
        self.txtNetPay.grid(row=3,column=1,sticky=W)

        #=======================================================LeftFrame_Bottom==========================================================================#
        self.rootPayment=Label(LowerFrameLeft,font=('arial',18,'bold'), text="Payment",padx=1,pady=2,bg='Blue',fg='white')
        self.rootPayment.grid(row=0,column=0,sticky=W)
        self.cboPayment=ttk.Combobox(LowerFrameLeft,textvariable=Payment,state='readonly',font=('arial',22,'bold'),width=19)
        self.cboPayment['value']=('Select Payment','250','500','750','1000')
        self.cboPayment.current(0)
        self.cboPayment.grid(row=0,column=1,pady=2)
        
      
        
        self.rootPayingFees=Label(LowerFrameLeft,font=('arial',18,'bold'), text="PayingFees",padx=1,pady=2,bg='Blue',fg='white')
        self.rootPayingFees.grid(row=2,column=0,sticky=W)
        self.txtPayingFees=Entry(LowerFrameLeft,width=21,font=('arial',26,'bold'), textvariable=NonDiscountFees)
        self.txtPayingFees.grid(row=2,column=1,sticky=W)

        
        
        self.rootPayAfterDiscoun=Label(LowerFrameLeft,font=('arial',18,'bold'), text="PayAfterDiscount",padx=1,pady=2,bg='Blue',fg='white')
        self.rootPayAfterDiscoun.grid(row=3,column=0,sticky=W)
        self.txtPayAfterDiscoun=Entry(LowerFrameLeft,width=21,font=('arial',26,'bold'), textvariable=PayAfterDiscount)
        self.txtPayAfterDiscoun.grid(row=3,column=1,sticky=W)


        #=============================================================Buttons=============================================================================#
        self.btnTotal=Button(BottomFrame,padx=37,pady=6,bd=4,fg="white",font=('arial',19,'bold'),width=24,bg='Blue',text='Total Fees',command=TotalFees).grid(row=0,column=0)
        self.btnTotal=Button(BottomFrame,padx=37,pady=6,bd=4,fg="white",font=('arial',19,'bold'),width=24,bg='Blue',text='Reset',command=Reset).grid(row=0,column=1)
        self.btnTotal=Button(BottomFrame,padx=37,pady=6,bd=4,fg="white",font=('arial',19,'bold'),width=24,bg='Blue',text='LogOut',command=Exit).grid(row=0,column=2)
       
        #=================================================================MAIN=========================================================================#



 
if __name__=='__main__':
    root=Tk()
    application=ReasonForMedication(root)
    root.mainloop()
        
        
