from tkinter import*
from tkinter import messagebox
from tkinter import scrolledtext
from cx_Oracle import*
import bs4
import requests
import socket
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly


class NegativeRnoException(Exception):
	def __init__(self,rno):
		pass
class NameErrorException(Exception):
	def __str__(self,name):
		pass
class NamelenErrorException(Exception):
	def __str__(self,name):
		pass
class MksRangeErrorException(Exception):
	def __str__(self,mks):
		pass
class RnoStringException(Exception):
	def __str__(self,rno):
		pass
class MksStringErrorException(Exception):
	def __str__(self,mks):
		pass


def f1():
	root.withdraw()
	adst.deiconify()
def f2():
	adst.withdraw()
	root.deiconify()
def f4():
	vist.withdraw()
	root.deiconify()
def f3():
	stdata.delete(1.0,END)
	root.withdraw()
	vist.deiconify()
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select rno,name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		msg=""
		for d in data:
			msg=msg+"rno="+str(d[0])+ "  name="+str(d[1])+  " mks="+str(d[2]) +"\n"
		stdata.insert(INSERT,msg)
	except DatabaseError as e:
		messagebox.showerror("invalid",e)
	finally:
		if con is not None:
			con.close()
def f5():
	con=None
	try:
		con=connect("system/abc123")
		rno=int(entAddRno.get())
		name=entAddName.get()
		mks=int(entAddMks.get())
		cursor=con.cursor()
		sql="insert into students values ('%d','%s','%d')"
		args=(rno,name,mks)
		if rno<0:
			raise NegativeRnoException("Rno cannot be negative")
		if name.isdigit():
			raise NameErrorException("only string")

		if len(name)<2:
			raise NamelenErrorException("len cannot be less than two")
		cursor.execute(sql %args)
		if name.isalpha():
			pass
		else:
			raise NameErrorException("only string")
		if (mks<0 or mks>100):
			raise MksRangeErrorException("invaid marks")
		#if mks.isalpha():
		#	raise MksRangeErrorException("oops invalid marks")
	
		con.commit()
		msg=str(cursor.rowcount)+ "record inserted"
		messagebox.showinfo("correct",msg)
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMks.delete(0,END)
		entAddRno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("invalid"," rno already exists")
		entAddRno.delete(0,END)
		entAddName.delete(0,END)
		entAddMks.delete(0,END)
		entAddRno.focus()
	except NegativeRnoException as e:
		messagebox.showerror("Wrong",e)
		entAddRno.delete(0,END)
		entAddRno.focus()
	except NameErrorException as e:
		con.rollback()
		msg="Name:String only"
		messagebox.showerror("invalid",msg)
		entAddName.delete(0,END)
		entAddName.focus()
	except NamelenErrorException as e:
		con.rollback()
		msg="length of name cannot be less than two"
		messagebox.showerror("invalid",msg)
		entAddName.delete(0,END)
		entAddName.focus()
	except MksRangeErrorException as e:
		con.rollback()
		msg="marks should be in range of 0 to 100"
		messagebox.showerror("invalid",msg)
		entAddMks.delete(0,END)
		entAddMks.focus()
	except ValueError as e:
		con.rollback()
		msg="oops there is some mistake in rno or mks"
		messagebox.showerror("invalid",msg)
		entAddRno.delete(0,END)
		entAddMks.delete(0,END)
		entAddRno.focus()
		
	finally:
		if con is not None:
			con.close()
def f6():
	root.withdraw()
	upst.deiconify()
def f7():
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="update students set name='%s',mks='%d' where rno='%d'"
		name=entUpdateName.get()
		mks=int(entUpdateMks.get())
		rno=int(entUpdateRno.get())
		args=(name,mks,rno)
		if rno<0:
			raise NegativeRnoException("Rno cannot be negative")
		if len(name)<2:
			raise NamelenErrorException("len cannot be less than two")
		if name.isdigit():
			raise NameErrorException("only string")
		if name.isalpha():
			pass
		else:
			raise NameErrorException("only string")
		if (mks<0 or mks>100):
			raise MksRangeErrorException("invaid marks")
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+ "record updated"
		messagebox.showinfo("correct",msg)
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateMks.delete(0,END)
		entUpdateRno.focus()
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("invalid",e)
		entUpdateRno.delete(0,END)
		entUpdateName.delete(0,END)
		entUpdateMks.delete(0,END)
		entUpdateRno.focus()
	except NegativeRnoException as e:
		messagebox.showerror("Wrong",e)
		entUpdateRno.delete(0,END)
		entUpdateRno.focus()
	except ValueError as e:
		con.rollback()
		msg="oops invalid rno or mks"
		messagebox.showerror("invalid",msg)
		entUpdateRno.delete(0,END)
		entUpdateMks.delete(0,END)
		entUpdateRno.focus()
	except NameError as e:
		con.rollback()
		msg="Name:String only"
		messagebox.showerror("invalid",msg)
		entUpdateName.delete(0,END)
		entUpdateName.focus()
	except NamelenErrorException as e:
		con.rollback()
		msg="length of name cannot be less than two"
		messagebox.showerror("invalid",msg)
		entUpdateName.delete(0,END)
		entUpdateName.focus()
	except MksRangeErrorException as e:
		con.rollback()
		msg="marks should be in range of 0 to 100"
		messagebox.showerror("invalid",msg)
		entUpdateMks.delete(0,END)
		entUpdateMks.focus()

	finally:
		if con is not None:
			con.close()
def f8():
	upst.withdraw()
	root.deiconify()
def f9():
	root.withdraw()
	delst.deiconify()
def f10():
	delst.withdraw()
	root.deiconify()
def f11():
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="delete from students where rno='%d'"
		rno=int(entDeleteRno.get())
		args=(rno)
		if rno<0:
			raise NegativeRnoException("Rno cannot be negative")
		cursor.execute(sql % args)
		con.commit()
		msg=str(cursor.rowcount)+ "record deleted"
		messagebox.showinfo("correct",msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
		
	except DatabaseError as e:
		con.rollback()
		messagebox.showerror("invalid",e)
	except NegativeRnoException as e:
		messagebox.showerror("Wrong",e)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	except ValueError as e:
		con.rollback()
		msg="Integer only"
		messagebox.showerror("invalid",msg)
		entDeleteRno.delete(0,END)
		entDeleteRno.focus()
	finally:		
		if con is not None:
			con.close()


def f14():
	graphStu.withdraw()
	root.deiconify()
def f16():
	root.withdraw()
	graphStu.deiconify()
def f15():
	con=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats=[]
		tmks=[]
		tname=[]
		for d in data:
			stats.append((d[1],d[0]))
			tmks.append(d[1])
			tname.append(d[0])
		#stats.sort(reverse=True)
		#mks=[]
		#name=[]
		#for s in range(5):
		#	sdata=stats[s]
		#	mks.append(sdata[0])
		#	name.append(sdata[1])

		plt.plot(tname,tmks,marker='o',markersize=10,label='MARKS')
		plt.xlabel("NAMES")
		plt.ylabel("MARKS")
		plt.ylim(0,100)
		plt.title("SEM PERFORMANCE")
		plt.legend(loc='lower left',shadow=True)
		plt.grid()
		plt.show()
	except Exception as e:
		messagebox.showerror(e)
	finally:
		if con is not None:
			con.close()
def f17():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats1=[]
		tmks1=[]
		tname1=[]
		for d in data:
			stats1.append((d[1],d[0]))
			tmks1.append(d[1])
			tname1.append(d[0])
		#stats1.sort(reverse=True)
		#mks1=[]
		#name1=[]
		#for s in range(5):
		#	sdata=stats1[s]
		#	mks1.append(sdata[0])
		#	name1.append(sdata[1]) 

		
	

		
		plt.bar(tname1,tmks1,color = ['green','purple','blue','pink','yellow'])
		plt.xlabel("NAMES")
		plt.ylabel("MARKS")
		plt.title("Student Report")
		plt.grid()
		plt.show()
	finally:
		if con is not None:
			con.close()
def f18():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats2=[]
		tmks2=[]
		tname2=[]
		for d in data:
			stats2.append((d[1],d[0]))
			tmks2.append(d[1])
			tname2.append(d[0])
		#stats2.sort(reverse=True)
		#mks2=[]
		#name2=[]
		#for s in range(5):
		#	sdata=stats2[s]
		#	mks2.append(sdata[0])
		#	name2.append(sdata[1])
		plt.pie(tmks2,labels=tname2,radius=1.2,shadow=True,startangle=45,colors=['pink','#0000FF','#FF9999','teal'],autopct='%.2f%%')

		plt.show()
	finally:
		if con is not None:
			con.close()
def f19():
	root.withdraw()
	FFStu.deiconify()

def f20():
	FFStu.withdraw()
	graphStu.deiconify()
def f21():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats3=[]
		tmks3=[]
		tname3=[]
		for d in data:
			stats3.append((d[1],d[0]))
			tmks3.append(d[1])
			tname3.append(d[0])
		stats3.sort(reverse=True)
		mks3=[]
		name3=[]
		for s in range(5):
			sdata=stats3[s]
		plt.legend(loc='lower left',shadow=True)
		plt.grid()
		plt.show()
	except Exception as e:
		messagebox.showerror(e)
	finally:
		if con is not None:
			con.close()
def f22():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats4=[]
		tmks4=[]
		tname4=[]
		for d in data:
			stats4.append((d[1],d[0]))
			tmks4.append(d[1])
			tname4.append(d[0])
		stats4.sort(reverse=True)
		mks4=[]
		name4=[]
		for s in range(5):
			sdata=stats4[s]
			mks4.append(sdata[0])
			name4.append(sdata[1]) 

		
	

		
		plt.bar(name4,mks4,color = ['green','purple','blue'])
		plt.xlabel("NAMES")
		plt.ylabel("MARKS")
		plt.title("Student Report")
		plt.grid()
		plt.show()
	finally:
		if con is not None:
			con.close()
def f23():
	con=None
	cursor=None
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats5=[]
		tmks5=[]
		tname5=[]
		for d in data:
			stats5.append((d[1],d[0]))
			tmks5.append(d[1])
			tname5.append(d[0])
		stats5.sort(reverse=True)
		mks5=[]
		name5=[]
		for s in range(5):
			sdata=stats5[s]
			mks5.append(sdata[0])
			name5.append(sdata[1])
		plt.pie(mks5,labels=name5,radius=1.2,explode=[0,0.4,0,0.1,0],shadow=True,startangle=45,colors=['pink','#0000FF','#FF9999','teal'],autopct='%.2f%%')

		plt.show()
	finally:
		if con is not None:
			con.close()

def f25():
	con=None
	cursor=None
	import itertools
	try:
		con=connect("system/abc123")
		cursor=con.cursor()
		sql="select name,mks from students"
		cursor.execute(sql)
		data=cursor.fetchall()
		stats5=[]
		tmks5=[]
		tname5=[]
		for d in data:
			stats5.append((d[1],d[0]))
			tmks5.append(d[1])
			tname5.append(d[0])
		#stats5.sort(reverse=True)
		#mks5=[]
		#name5=[]
		#for s in range(5):
		#	sdata=stats5[s]
		#	mks5.append(sdata[0])
		#	name5.append(sdata[1])
		colors = itertools.cycle(["r", "b", "g"])
		for y in tmks5:
    			plt.scatter(tname5,tmks5,color=next(colors),linewidth=1)
		plt.xlabel("name")
		plt.ylabel("marks")
		plt.show()
	finally:
		if con is not None:
			con.close()
	
			

			
	

root=Tk()
root.title("S.M.S")
root.iconbitmap(r'travel_pBc_icon.ico')
root.geometry("800x500+300+100")
root.configure(background='indianred1')

res=requests.get("https://www.brainyquote.com/quote_of_the_day.html")

soup=bs4.BeautifulSoup(res.text,'lxml')

quote=soup.find('img',{"class":"p-qotd"})

text=quote['alt']
lblText=Label(root,text=text,font="Times 10 bold",bg='indianred1')
lblText.pack(padx=10,pady=10)

try:
	city='mumbai'
	socket.create_connection(("www.google.com",80))
	a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q="+city
	a3="&appid=c6e315d09197cec231495138183954bd"
	api_address= a1 + a2 + a3
	res1=requests.get(api_address)
	data=res1.json()
	temp=data['main']['temp']
	lblTemp=Label(root,text='Temperature '+str(temp),relief='solid',font=("Courier",16,'bold'),bg='indianred1')
	lblTemp.pack(pady=10)
	
	

except OSError:
	messagebox.showerror("check network")



btnAdd=Button(root,text="Add",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f1)
btnView=Button(root,text="View",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f3)
btnUpdate=Button(root,text="Update",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f6)
btnDelete=Button(root,text="Delete",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f9)
btnGraph=Button(root,text="Graph",width=10,font=("arial",16,'bold'),bg='#ADD8E6',command=f16)

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)

#Add

adst=Toplevel(root)
adst.title("Add Stu.")
adst.iconbitmap(r'travel_pBc_icon.ico')
adst.geometry("500x500+300+100")
adst.configure(background='coral1')
adst.withdraw()

lblAddRno=Label(adst,text="Enter Rno",font=("arial",16,'bold'),bg='coral1')
lblAddName=Label(adst,text="Enter Name",font=("arial",16,'bold'),bg='coral1')
lblAddMks=Label(adst,text="Enter Marks",font=("arial",16,'bold'),bg='coral1')
entAddRno=Entry(adst,bd=5,font=("arial",16,'bold'))
entAddName=Entry(adst,bd=5,font=("arial",16,'bold'))
entAddMks=Entry(adst,bd=5,font=("arial",16,'bold'))
btnAddSave=Button(adst,text="Save",font=("arial",16,'bold'),command=f5)
btnAddBack=Button(adst,text="Back",font=("arial",16,'bold'),command=f2)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMks.pack(pady=10)
entAddMks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

#view
vist=Toplevel(root)
vist.title("View Stu.")
vist.iconbitmap(r'travel_pBc_icon.ico')
vist.geometry("500x500+300+100")
vist.configure(background='mediumpurple1')
vist.withdraw()

stdata=scrolledtext.ScrolledText(vist,width=40,height=20)
#stdata.configure(state='disabled')
btnViewBack=Button(vist,text='Back',font=("arial",16,'bold'),command=f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)

#update
upst=Toplevel(root)
upst.title("Update Stu.")
upst.iconbitmap(r'travel_pBc_icon.ico')
upst.geometry("500x500+300+100")
upst.configure(background='MediumOrchid1')
upst.withdraw()

lblUpdateRno=Label(upst,text="Enter Rno",width=10,font=("arial",16,'bold'),background='MediumOrchid1')
entUpdateRno=Entry(upst,bd=5,width=10,font=("arial",16,'bold'))
lblUpdateName=Label(upst,text="Enter Name",width=10,font=("arial",16,'bold'),background='MediumOrchid1')
entUpdateName=Entry(upst,bd=5,width=10,font=("arial",16,'bold'))
lblUpdateMks=Label(upst,text="Enter Marks",width=10,font=("arial",16,'bold'),background='MediumOrchid1')
entUpdateMks=Entry(upst,bd=5,width=10,font=("arial",16,'bold'))
btnUpSave=Button(upst,text="Save",width=10,font=("arial",16,'bold'),command=f7)
btnUpBack=Button(upst,text="Back",width=10,font=("arial",16,'bold'),command=f8)

lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
lblUpdateMks.pack(pady=10)
entUpdateMks.pack(pady=10)
btnUpSave.pack(pady=10)
btnUpBack.pack(pady=10)

#delete
delst=Toplevel(root)
delst.title("Delete S")
delst.iconbitmap(r'travel_pBc_icon.ico')
delst.geometry("500x400+300+200")
delst.configure(background='salmon1')
delst.withdraw()

lblDeleteRno=Label(delst,text="enter Rno",width=10,font=("arial",16,'bold'),background='salmon1')
entDeleteRno=Entry(delst,bd=5,width=10,font=("arial",16,'bold'))
btnDelete=Button(delst,text="Delete",width=10,font=("arial",16,'bold'),command=f11)
btnDelBack=Button(delst,text="Back",width=10,font=("arial",16,'bold'),command=f10)
lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDelete.pack(pady=10)
btnDelBack.pack(pady=10)

#graph
graphStu=Toplevel(root)
graphStu.title("Graph S")
graphStu.geometry("500x400+300+200")
graphStu.configure(background='medium purple1')
btngraphL=Button(graphStu,text="Line",width=10,font=("Helvetica",16,'bold'),bg='light pink1',fg='gray2',command=f15)
btngraphB=Button(graphStu,text="Bar",width=10,font=("Helvetica",16,'bold'),bg='light pink1',fg='gray2',command=f17)
btngraphP=Button(graphStu,text="Pie",width=10,font=("Helvetica",16,'bold'),bg='light pink1',fg='gray2',command=f18)
btngraphS=Button(graphStu,text="Scatter",width=10,font=("Helvetica",16,'bold'),bg='light pink1',fg='gray2',command=f25)
btngraphFF=Button(graphStu,text="Top Five",width=10,font=("Helvetica",16,'bold'),bg='light pink1',fg='gray2',command=f19)
btngraphStuBack=Button(graphStu,text="Back",width=10,font=("Helvetica",16,'bold'),bg='light pink1',fg='gray2',command=f14)
btngraphL.pack(pady=10)
btngraphB.pack(pady=10)
btngraphP.pack(pady=10)
btngraphS.pack(pady=10)
btngraphFF.pack(pady=10)
btngraphStuBack.pack(pady=10)
graphStu.withdraw()

#topfive
FFStu=Toplevel(root)
FFStu.title("Graph of top five")
FFStu.geometry("500x400+300+200")
FFStu.configure(background='orchid3')
btnFFStul=Button(FFStu,text="Line",width=10,font=("arial",16,'bold'),command=f21)
btnFFStub=Button(FFStu,text="Bar",width=10,font=("arial",16,'bold'),command=f22)
btnFFStup=Button(FFStu,text="Pie",width=10,font=("arial",16,'bold'),command=f23)
btnFFStuBack=Button(FFStu,text="Back",width=10,font=("arial",16,'bold'),command=f20)
btnFFStul.pack(pady=10)
btnFFStub.pack(pady=10)
btnFFStup.pack(pady=10)
btnFFStuBack.pack(pady=10)
FFStu.withdraw()
root.mainloop()
