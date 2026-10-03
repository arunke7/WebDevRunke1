import streamlit as st

def quiz():
    st.header("Where is your next vacation?")
    st.image("https://imgcdn.stablediffusionweb.com/2024/5/8/7cf909a8-8912-4cf6-ac76-76ed9edd36e1.jpg", width=300)
    

quiz()

def question1():
    st.subheader("1. What do you like the most?")
    select1=st.selectbox("",["Select One","Beach","City","Mountains"], key="q1_455557")
    if select1=="Select One":
        return None
    if select1=="Beach":
        st.write("Beach")
        return("Beach")  
    if select1=="City":
        st.write("City")
        return("City")
    if select1=="Mountains":
        st.write("Mountains")
        return("Mountains")
        
   

q1=question1()
def question2():
    st.subheader ("2. How many vacations have you been on?")
    vacay=st.slider("",0,100)#new
    if vacay>10:
        return("Expert")
    if vacay<=10:
        return("Beginner")
q2=question2()

def question3():
    st.subheader("3. What is your favorite color?")
    select=st.selectbox("", ["Select One", "Blue", "Green", "Red", "Yellow","Orange","Purple","Pink" ]) #new
    if select=="Select One":
        return None
    if select=="Blue" or select=="Purple" or select=="Green":
        return("Cool")
    elif select=="Red" or select=="Orange" or select=="Yellow" or select=="Pink":
        return("Warm")
    
q3=question3()


def question4():
    st.subheader("4. What is your favorite season?")
    st.image("https://tse1.mm.bing.net/th/id/OIP.2TtCpojI6S5kpVP5dWC7bQHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",width=200)
    answera=st.button("Winter")
    answerb=st.button("Spring")
    answerc=st.button("Summer")
    answerd=st.button("Fall")
    if answera==True:
        st.write("Winter")
        return("Winter")
    if answerb==True:
        st.write("Spring")
        return("Spring")
    if answerc==True:
        st.write("Summer")
        return("Summer")
    if answerd==True:
        st.write("Fall")
        return("Fall")

q4=question4()

def question5():
    st.subheader("5. How many bags are you bringing?")
    select=st.radio("", ["Select One","1", "2", "3", "4","5" ],key="455")
    if select=="Select One":
        return None
    if select=="3" or select=="4" or select=="5":
        return("Heavy")
    else:
        return("Light")
q5=question5()
def answer(q1,q2,q3,q4,q5):
    if q1==None or q2==None or q3==None or q4==None or q5==None:
        st.subheader("Please Finish answering the questions.")
        return(None)
    if q1=="Beach":
        if q2=="Expert":
            if q3=="Cool":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Cox Bay")
                    if q5=="Light":
                        return("Cox Beach")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Inchydoney")
                    if q5=="Light":
                        return("Cox Bay")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Binz")
                    if q5=="Light":
                        return("Inchydoney")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Bar Harbor")
                    if q5=="Light":
                        return("Bar Harbor")
            if q3=="Warm":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Cox Bay")
                    if q5=="Light":
                        return("Cox Bay")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Newport")
                    if q5=="Light":
                        return("Newport")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Trunk Bay")
                    if q5=="Light":
                        return("Trunk Bay")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Bar Harbor")
                    if q5=="Light":
                        return("Mackinac")
        if q2=="Beginner":
            if q3=="Cool":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Cox Bay")
                    if q5=="Light":
                        return("Cox Bay")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Inchydoney")
                    if q5=="Light":
                        return("Cox Bay")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Binz Beach")
                    if q5=="Light":
                        return("Inchydoney")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Bar Harbor")
                    if q5=="Light":
                        return("Bar Harbor")
            if q3=="Warm":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Cox Bay")
                    if q5=="Light":
                        return("Cox Bay")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Newport")
                    if q5=="Light":
                        return("Newport")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Trunk Bay")
                    if q5=="Light":
                        return("Trunk Bay")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Bar Harbor")
                    if q5=="Light":
                        return("Mackinac")
    if q1=="City":
        if q2=="Expert":
            if q3=="Cool":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Edinburg")
                    if q5=="Light":
                        return("Edinburg")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Lisbon")
                    if q5=="Light":
                        return("Madrid")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Madrid")
                    if q5=="Light":
                        return("Lisbon")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Denver")
                    if q5=="Light":
                        return("Copenhagen")
            if q3=="Warm":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Denver")
                    if q5=="Light":
                        return("Copenhagen")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Seattle")
                    if q5=="Light":
                        return("Seattle")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Madrid")
                    if q5=="Light":
                        return("Seattle")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Copenhagen")
                    if q5=="Light":
                        return("Denver")
        if q2=="Beginner":
            if q3=="Cool":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Yakutsk")
                    if q5=="Light":
                        return("Yakutsk")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Lisbon")
                    if q5=="Light":
                        return("Madrid")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Dubai")
                    if q5=="Light":
                        return("Dubai")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Denver")
                    if q5=="Light":
                        return("Copenhagen")
            if q3=="Warm":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Yakutsk")
                    if q5=="Light":
                        return("Copenhagen")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Seattle")
                    if q5=="Light":
                        return("Seattle")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Dubai")
                    if q5=="Light":
                        return("Seattle")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Copenhagen")
                    if q5=="Light":
                        return("Denver")
    if q1=="Mountains":
        if q2=="Expert":
            if q3=="Cool":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Aspen")
                    if q5=="Light":
                        return("Alps")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Lisbon")
                    if q5=="Light":
                        return("Madrid")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Madrid")
                    if q5=="Light":
                        return("Lisbon")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Denver")
                    if q5=="Light":
                        return("Copenhagen")
            if q3=="Warm":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Denver")
                    if q5=="Light":
                        return("Copenhagen")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Seattle")
                    if q5=="Light":
                        return("Seattle")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Madrid")
                    if q5=="Light":
                        return("Seattle")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Copenhagen")
                    if q5=="Light":
                        return("Denver")
        if q2=="Beginner":
            if q3=="Cool":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Aspen")
                    if q5=="Light":
                        return("Alps")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Fuji")
                    if q5=="Light":
                        return("Fuji")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Rainier")
                    if q5=="Light":
                        return("Rainier")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Adirondacks")
                    if q5=="Light":
                        return("Adirondacks")
            if q3=="Warm":
                if q4=="Winter":
                    if q5=="Heavy":
                        return("Yakutsk")
                    if q5=="Light":
                        return("Copenhagen")
                if q4=="Spring":
                    if q5=="Heavy":
                        return("Himulayas")
                    if q5=="Light":
                        return("Himulayas")
                if q4=="Summer":
                    if q5=="Heavy":
                        return("Rainier")
                    if q5=="Light":
                        return("Rainier")
                if q4=="Fall":
                    if q5=="Heavy":
                        return("Adirondacks")
                    if q5=="Light":
                        return("Adirondacks")
finala=answer(q1,q2,q3,q4,q5)



def result(finala):
    if finala is None:
        return
    st.balloons()#new
    if finala=="Inchydoney":
        st.subheader("You are going to Inchydoney, Ireland!")
        st.image("Images/Ichydoney.jpg", width=150)
    if finala=="Fuji":
        st.subheader("You are going to Mount Fuji, Japan!")
        st.image("Images/Fuji.jpg", width=150)
    if finala=="Adirondacks":
        st.subheader("You are goung to Adirondacks, NY!")
        st.image("Images/Adirondacks.jpg", width=150)
    if finala=="Alps":
        st.subheader("You are going to Western Alps, France!")
        st.image("Images/Alps.jpg", width=150)
    if finala=="Aspen":
        st.subheader("You are going to Aspen, CO!")
        st.image("Images/Aspen.jpg",width=150)
    if finala=="Bar Harbor":
        st.subheader("You are going to Bar Harbor, ME!")
        st.image("Images/Bar Harbor.jpg",width=150)
    if finala=="Binz":
        st.subheader("You are going to Binz, Germany!")
        st.image("Images/Binz.jpg", width=150)
    if finala=="Copenhagen":
        st.subheader("You are going to Copenhagen, Denmark!")
        st.image("Images/Copenhagen.jpg",width=150)
    if finala=="Cox Bay":
        st.subheader("You are going to Cox Bay, Canada!")
        st.image("Images/Cox Bay.jpg",width=150)
    if finala=="Denver":
        st.subheader("You are going to Denver, CO!")
        st.image("Images/Denver.jpg", width=150)
    if finala=="Dubai":
        st.subheader("You are going to Dubai, Dubai!")
        st.image("Images/Dubai.jpg",width=150)
    if finala=="Edinburg":
        st.subheader("You are going to Edinburgh, Scotland!")
        st.image("Images/Edinburg.jpg", width=150)
    if finala=="Himalayas":
        st.subheader("You are going to Himalayas, India!")
        st.image("Images/Himalayas.jpg",width=150)
    if finala=="Lisbon":
        st.subheader("You are going to Lisbon, Portugal!")
        st.image("Images/Lisbon.jpg",width=150)
    if finala=="Mackinac":
        st.subheader("You are going to Mackinac Island, MI!")
        st.image("Images/Mackinac.jpg",width=150)
    if finala=="Madrid":
        st.subheader("You are going to Madrid, Spain!")
        st.image("Images/Madrid.jpg",width=150)
    if finala=="Newport":
        st.subheader("You are going to Newport, RI!")
        st.image("Images/Newport.jpg",width=150)
    if finala=="Rainier":
        st.subheader("You are going to Mount Rainier, WA!")
        st.image("Images/Rainier.jpg",width=150)
    if finala=="Seattle":
        st.subheader("You are going to Seattle, WA!")
        st.image("Images/Seattle.jpg",width=150)
    if finala=="Trunk Bay":
        st.subheader("You are going to Trunk Bay, St.John!")
        st.image("Images/Trunk Bay.jpg",width=150)
    if finala=="Yakutsk":
        st.subheader("You are going to Yakutsk, Russia!")
        st.image("Images/Yakutsk.jpg",width=150)
        
result(finala)        
            

                      
    
