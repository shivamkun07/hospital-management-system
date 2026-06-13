
import customtkinter as ctk
from tkinter import ttk, messagebox
import sqlite3

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

TABLES = {
    "Patients": ("patients", ["patient_id","name","age","gender","phone","blood_group"]),
    "Doctors": ("doctors", ["doctor_id","name","specialization","fee"]),
    "Nurses": ("nurses", ["nurse_id","name","department","shift"]),
    "Appointments": ("appointments", ["appointment_id","patient_id","doctor_id","date","slot","status"]),
    "Medicines": ("medicines", ["medicine_id","name","stock","price","expiry"]),
    "Records": ("medical_records", ["record_id","patient_id","diagnosis","prescription","notes"]),
    "Reports": ("lab_reports", ["report_id","patient_id","test_name","result","date"]),
    "Bills": ("bills", ["bill_id","patient_id","consultation","medicine","lab","total"]),
}

class HospitalGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Hospital Management System")
        self.geometry("1500x850")

        self.conn = sqlite3.connect("hospital.db")
        self.cur = self.conn.cursor()

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar()
        self.dashboard()

    def sidebar(self):
        s = ctk.CTkFrame(self,width=220)
        s.grid(row=0,column=0,sticky="ns")
        ctk.CTkLabel(s,text="🏥 Hospital ",font=("Arial",28,"bold")).pack(pady=20)

        ctk.CTkButton(s,text="Dashboard",command=self.dashboard).pack(fill="x",padx=10,pady=5)

        for name in TABLES:
            ctk.CTkButton(
                s,text=name,
                command=lambda n=name:self.module(n)
            ).pack(fill="x",padx=10,pady=5)

    def clear(self):
        if hasattr(self,"content"):
            self.content.destroy()
        self.content=ctk.CTkFrame(self)
        self.content.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)

    def count(self, table):
        try:
            self.cur.execute(f"select count(*) from {table}")
            return self.cur.fetchone()[0]
        except:
            return 0

    def dashboard(self):
        self.clear()
        ctk.CTkLabel(self.content,text="Dashboard",font=("Arial",32,"bold")).pack(pady=20)

        row=ctk.CTkFrame(self.content)
        row.pack()

        cards=[
            ("Patients","patients","Patients"),
            ("Doctors","doctors","Doctors"),
            ("Nurses","nurses","Nurses"),
            ("Appointments","appointments","Appointments")
        ]

        for title,table,module in cards:
            ctk.CTkButton(
                row,
                width=220,
                height=120,
                text=f"{title}\n\n{self.count(table)}",
                command=lambda m=module:self.module(m)
            ).pack(side="left",padx=15,pady=15)

    def module(self,name):
        table, cols = TABLES[name]

        self.clear()
        self.current_table = table
        self.current_cols = cols

        ctk.CTkLabel(self.content,text=name,font=("Arial",28,"bold")).pack(pady=10)

        form=ctk.CTkFrame(self.content)
        form.pack(fill="x",padx=10,pady=10)

        self.entries={}

        for i,col in enumerate(cols):
            e=ctk.CTkEntry(form,placeholder_text=col)
            e.grid(row=0,column=i,padx=4,pady=5)
            self.entries[col]=e

        ctk.CTkButton(form,text="Add",command=self.add_record).grid(row=1,column=0,pady=5)
        ctk.CTkButton(form,text="Update Selected",command=self.update_record).grid(row=1,column=1,pady=5)
        ctk.CTkButton(form,text="Delete Selected",command=self.delete_record).grid(row=1,column=2,pady=5)
        ctk.CTkButton(form,text="Refresh",command=lambda:self.module(name)).grid(row=1,column=3,pady=5)

        self.search=ctk.CTkEntry(form,placeholder_text="Search")
        self.search.grid(row=1,column=4,padx=5)
        ctk.CTkButton(form,text="Search",command=self.search_record).grid(row=1,column=5)

        self.tree=ttk.Treeview(self.content,columns=cols,show="headings")
        for c in cols:
            self.tree.heading(c,text=c)
            self.tree.column(c,width=140)
        self.tree.pack(fill="both",expand=True,padx=10,pady=10)

        self.tree.bind("<<TreeviewSelect>>", self.fill_entries)

        self.load_data()

    def load_data(self, rows=None):
        for i in self.tree.get_children():
            self.tree.delete(i)

        if rows is None:
            self.cur.execute(f"select * from {self.current_table}")
            rows=self.cur.fetchall()

        for r in rows:
            self.tree.insert("", "end", values=r)

    def add_record(self):
        vals=[self.entries[c].get() for c in self.current_cols]
        q="INSERT INTO {} VALUES({})".format(
            self.current_table,
            ",".join(["?"]*len(vals))
        )
        try:
            self.cur.execute(q, vals)
            self.conn.commit()
            self.load_data()
        except Exception as e:
            messagebox.showerror("Error",str(e))

    def delete_record(self):
        sel=self.tree.focus()
        if not sel:return
        pk=self.tree.item(sel)["values"][0]
        pkcol=self.current_cols[0]
        self.cur.execute(
            f"DELETE FROM {self.current_table} WHERE {pkcol}=?",
            (pk,)
        )
        self.conn.commit()
        self.load_data()

    def update_record(self):
        sel=self.tree.focus()
        if not sel:return

        vals=[self.entries[c].get() for c in self.current_cols]
        pk=vals[0]

        set_clause=",".join([f"{c}=?" for c in self.current_cols[1:]])

        q=f"UPDATE {self.current_table} SET {set_clause} WHERE {self.current_cols[0]}=?"

        self.cur.execute(q, vals[1:]+[pk])
        self.conn.commit()
        self.load_data()

    def fill_entries(self,event=None):
        sel=self.tree.focus()
        if not sel:return
        vals=self.tree.item(sel)["values"]

        for col,val in zip(self.current_cols, vals):
            self.entries[col].delete(0,"end")
            self.entries[col].insert(0,str(val))

    def search_record(self):
        txt=self.search.get().strip()
        if not txt:
            self.load_data()
            return

        q=" OR ".join([f"{c} LIKE ?" for c in self.current_cols])
        params=["%"+txt+"%"]*len(self.current_cols)

        self.cur.execute(
            f"SELECT * FROM {self.current_table} WHERE {q}",
            params
        )

        self.load_data(self.cur.fetchall())

if __name__=="__main__":
    app=HospitalGUI()
    app.mainloop()
