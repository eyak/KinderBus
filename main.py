import streamlit as st
from settings import *
import datetime
from model import Registration, Kid

def run():
    st.write('Ring My Bell')

    regs = Registration.all()
    kids = Kid.all()

    tab0, tab1 = st.tabs(["Register", "List"])

    doRegister(tab0, regs, kids)
    doList(tab1, regs, kids)

def doRegister(target, regs, kids):
    selKid = target.selectbox("Name", kids, format_func=lambda x: x.name)
    selDate = target.date_input("Date")
    selDirection = target.selectbox("Direction", ["Go", "Return"])
    selAction = target.selectbox("Action", ["Register", "Cancel"])

    if target.button("Register"):
        reg = Registration(name=[selKid], date=selDate, action=selAction, direction=selDirection) 
        reg.save()
        target.write("OK!")

def doList(target, regs, kids):
    dates = sorted(set([r.date for r in regs]))
    # find the index of today in dates
    today = datetime.date.today()
    todayIndex = dates.index(today)
    selDate = target.selectbox("Date", dates, index=todayIndex)

    if target.button("Refresh"):
        st.rerun()

    
    for direction in ["Go", "Return"]:
        target.header(direction)
        kidsLatest = {}
        dirRegs = [reg for reg in regs if reg.date == selDate and reg.direction == direction]
        for reg in dirRegs:
            kidid = reg.name[0].id
            #target.write(kid)
            if kidid not in kidsLatest:
                kidsLatest[kidid] = (reg.created, reg.action)
            else:
                lastReg, lastAction = kidsLatest[kidid]

                if reg.created > lastReg:
                    kidsLatest[kidid] = (reg.created, reg.action)
        
        going = []
        canceled = []
        for kidid, (created, action) in kidsLatest.items():
            kid = Kid.from_id(kidid)
            if action == "Register":
                going.append(kid.name)
            else:
                canceled.append(kid.name)
        
        target.markdown(f"### Registered {len(going)}")
        for index, name in enumerate(sorted(going)):
            target.write(f'{index+1} {name}')
        target.markdown(f'### Canceled {len(canceled)}')
        for index, name in enumerate(sorted(canceled)):
            target.write(f'{index+1} {name}')

        target.write("----")
        
                
        
if __name__ == "__main__":
    run()