from django.shortcuts import render
import math

# Create your views here.
def start(request):
    return render(request,'start.html' )

def about(request):
    return render(request,'about.html' )

def contactdeveloper(request):
    return render(request,'contactdeveloper.html' )

def home(request):
    global counthome
    counthome = 0
    counthome += 1
    global counthomecalc
    counthomecalc = 0
    return render(request,'home.html' )

def homecalc(request):
    global counthomecalc
    counthomecalc = 0
    counthomecalc += 1
    global counthome
    counthome = 0
    return render(request,'home.html')


def page(request):

    coursepattern = request.GET['coursepattern']
    branch = request.GET['branch']
    semindex = int(request.GET['semindex'])
    global Gcoursepattern
    Gcoursepattern = coursepattern
    global Gbranch
    Gbranch = branch
    global Gsemindex
    Gsemindex = semindex
    global countFE_SE
    countFE_SE = 0        #for FE & SE 2015 pattern - insem : endsem = 50:50 instead of 30:70
    global countproject
    countproject = 0       #for BE 8th sem Project - Total 200 - insem : endsem = 100:100

    msgMarksOutOfL = []
    msgProjectOutOfL = []
    msgprojectL = []
    
    if coursepattern == "2015":
        if branch == "mech":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Engineering Graphics I','Basic Electrical / Electronics Engineering','Basic Civil & Environmental Engineering'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Mechanical Engineering','Engineering Mechanics','Basic Electronics / Electrical Engineering'],                #Sem2
                        ['Engineering Mathematics – III','Manufacturing Process-I','Thermodynamics','Material Science','Strength of Materials'],     #Sem3
                        ['Fluid Mechanics','Theory of Machines – I','Engineering Metallurgy','Applied Thermodynamics','Electrical and Electronics Engineering'],     #Sem4
                        ['Design of Machine Elements-I','Heat Transfer','Theory of Machines-II','Turbo Machines','Metrology and Quality Control'],     #Sem5  
                        ['Numerical Methods and Optimization','Design of Machine Elements-II','Refrigeration and Air Conditioning','Mechatronics','Manufacturing Process-II'],   #Sem6
                        ['Hydraulics and Pneumatics','CAD CAM Automation','Dynamics of Machinery','FEA / CFD / HVAC','Automobile Engg / Operation Research / Energy Audit & Management'],    #Sem7
                        ['Energy Engineering','Mechanical System Design','Tribology / Industrial Engg / Robotics','Advanced Manufacturing Processes / Solar & Wind Energy / Product Design and Development','Project']]   #Sem8
            credit = [  [5,5,4,4,4],       #Sem1
                        [4,5,4,5,4],
                        [5,3,4,3,4],
                        [4,4,3,4,3],
                        [4,4,3,3,3],
                        [4,4,3,3,3],
                        [3,3,4,3,3],
                        [3,4,3,3,5] ]     #Sem8

            subjectL = subject[semindex]
            creditL = credit[semindex]                          
    
        elif branch == "cs":
            subject =  [['Engineering Mathematics I','Engineering Physics / Chemistry','Engineering Graphics I','Basic Electrical / Electronics Engineering','Basic Civil & Environmental Engineering'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Mechanical Engineering','Engineering Mechanics','Basic Electronics / Electrical Engineering'],
                        ['Discrete Mathematics','Digital Electronics and Logic Design','Data Structures and Algorithms','Computer Organization and Architecture','Object Oriented Programming'],
                        ['Engineering Mathematics III','Computer Graphics','Advanced Data Structures','Microprocessor','Principles of Programming Languages'],
                        ['Theory of Computation','Database Management Systems (DBMS)','Software Engineering & Project Management','Information Systems & Engineering Economics','Computer Networks (CN)'],
                        ['Design & Analysis of Algorithms','Systems Programming & Operating System (SP & OS)','Embedded Systems & Internet of Things (ES & IoT)','Software Modeling and Design','Web Technology'],
                        ['High Performance Computing','Artificial Intelligence and Robotics','Data Analytics','Elective I','Elective II'],
                        ['Machine Learning','Information and Cyber Security','Elective III','Elective IV','Project'] ]                  
            credit =   [[5,5,4,4,4],      #Sem1
                        [4,5,4,5,4],
                        [4,4,4,4,4],
                        [5,4,4,4,3],
                        [3,3,3,3,4],
                        [4,4,4,3,3],
                        [4,3,3,3,3],
                        [3,3,3,3,5]]      #Sem8
            subjectL = subject[semindex]
            creditL = credit[semindex]

        elif branch == "it":
            subject =  [['Engineering Mathematics I','Engineering Physics / Chemistry','Engineering Graphics I','Basic Electrical / Electronics Engineering','Basic Civil & Environmental Engineering'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Mechanical Engineering','Engineering Mechanics','Basic Electronics / Electrical Engineering'],
                        ['Discrete Structures','Computer Organization & Architecture','Digital Electronics and Logic Design','Fundamentals of Data Structures','Problem Solving and Object Oriented programming'],
                        ['Engineering Mathematics -III','Computer Graphics','Processor Architecture and Interfacing','Data Structures & Files','Foundations of Communication and Computer Network'],
                        ['Theory of Computation','Database Management Systems','Software Engineering &Project Management','Operating System','Human-Computer Interaction'],
                        ['Computer Network Technology','Systems Programming','Design and Analysis of Algorithms','Cloud Computing','Data Science & Big Data Analytics'],
                        ['Information and Cyber Security','Machine Learning and Applications','Software Design and Modeling','Elective-I (WC / NLP / UE / MCS / BA&I)','Elective-II (SDN / SC / STQA / CC / Gamification)'],
                        ['Distributed Computing System','Ubiquitous Computing','Elective-III (IOR / ISR / MT / IWP / CO)','Elective-IV (RTDC / PC / CV / SMA)','Project']]             
            credit =   [[5,5,4,4,4],       #Sem1
                        [4,5,4,5,4],
                        [4,4,4,4,4],
                        [5,3,4,4,4],
                        [4,4,3,4,3],
                        [3,4,4,3,4],
                        [3,4,3,3,3],
                        [3,3,4,3,5]]
            subjectL = subject[semindex]
            creditL = credit[semindex]

        elif branch == "civil":
            subject =  [['Engineering Mathematics I','Engineering Physics / Chemistry','Engineering Graphics I','Basic Electrical / Electronics Engineering','Basic Civil & Environmental Engineering'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Mechanical Engineering','Engineering Mechanics','Basic Electronics / Electrical Engineering'],
                        ['Building Technology and Materials','Engineering Mathematics III','Surveying','Strength of Materials','Geotechnical Engineering'],
                        ['Fluid Mechanics I','Architectural Planning and Design of Buildings','Structural Analysis I','Engineering Geology','Concrete Technology'],
                        ['Hydrology & water resource Engineering.','Infrastructure Engineering and Construction Techniques','Structural Design I','Structural Analysis II','Fluid Mechanics I'],
                        ['Advanced Surveying','Project Management & Engineering Economics','Foundation Engineering','Structural Design II','Enviornmental Engineering I'],
                        ['Environmental Engineering II','Transportation Engineering','Structural Design & Drawing III','Elective I','Elective II'],
                        ['Dams and Hydraulic Structures','Quantity Surveying, Contracts & Tenders','Elective III','Elective IV','Project']]                    
            credit =   [[5,5,4,4,4],       #Sem1
                        [4,5,4,5,4],
                        [4,5,4,4,4],
                        [4,4,4,4,4],
                        [3,4,4,3,4],
                        [3,4,3,4,4],
                        [3,3,4,3,3],
                        [3,3,3,3,5]]
            subjectL = subject[semindex]
            creditL = credit[semindex]
        
        elif branch == "entc":
            subject =  [['Engineering Mathematics I','Engineering Physics / Chemistry','Engineering Graphics I','Basic Electrical / Electronics Engineering','Basic Civil & Environmental Engineering'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Mechanical Engineering','Engineering Mechanics','Basic Electronics / Electrical Engineering'],
                        ['Signals & Systems','Electronic Devices & Circuits','Electrical Circuits and Machines','Data Structures and Algorithms','Digital Electronics'],
                        ['Engineering Mathematics III','Integrated Circuits','Control Systems','Analog Communication','Object Oriented Programming'],
                        ['Digital Communication','Digital Signal Processing','Digital Signal Processing','Microcontrollers','Mechatronics'],
                        ['Power Electronics','Information Theory, Coding and Communication Networks','Business Management','Advanced Processors','System Programming and Operating Systems'],
                        ['VLSI Design & Technology','Computer Networks & Security','Radiation & Microwave Techniques','Elective I (DIVP/IDC/ES&RTOS/IOT)','Elective II (Wavelets/EPD/OT/AI/EA)'],
                        ['Mobile Communication','Broadband Communication Systems','Elective III (ML/PLC&A/ASP/SDR/AVE)','Elective IV (Robotics/BE/WSN/RES)','Project']]                    
            credit =   [[5,5,4,4,4],       #Sem1
                        [4,5,4,5,4],
                        [4,4,3,4,4],
                        [5,4,3,3,3],
                        [3,3,4,3,3],
                        [3,4,3,3,3],
                        [3,4,3,3,3],
                        [3,4,3,3,5]]
            subjectL = subject[semindex]
            creditL = credit[semindex]
        
        elif branch == "electrical":
            subject =  [['Engineering Mathematics I','Engineering Physics / Chemistry','Engineering Graphics I','Basic Electrical / Electronics Engineering','Basic Civil & Environmental Engineering'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Mechanical Engineering','Engineering Mechanics','Basic Electronics / Electrical Engineering'],
                        ['Power Generation Technologies','Engineering Mathematics- III','Material Science','Analog & Digital Electronics','Electrical Measurements & Instrumentation'],
                        ['Power System I','Electrical Machines I','Network Analysis','Numerical Methods & Computer Programming','Fundamentals of Microcontroller & Applications'],
                        ['Industrial and Technology Management','Advance Microcontroller and its Applications','Electrical Machines II','Power Electronics','Electrical Installation, Maintenance and Testing'],
                        ['Power System II','Control System I','Utilization of Electrical Energy','Design of Electrical Machines','Energy Audit and Management'],
                        ['Power System Operation and Control','PLC and SCADA Applications','Elective I','Elective II','Control System II'],
                        ['Switchgear and Protection','Power Electronic Controlled Drives','Elective III','Elective IV','Project']]
                                
            credit =   [[5,5,4,4,4],       #Sem1
                        [4,5,4,5,4],
                        [4,4,4,4,4],
                        [4,4,4,4,4],
                        [3,4,4,4,3],
                        [4,4,3,4,3],
                        [3,4,3,3,3],
                        [3,4,3,3,5]]
                                
            subjectL = subject[semindex]
            creditL = credit[semindex]

        if semindex == 0 or semindex == 1 or semindex == 2 or semindex == 3:
            countFE_SE += 1
        if semindex == 7:
            countproject += 1

    if coursepattern == "2019":
        if branch == "mech":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Systems in Mechanical Engineering','Basic Electrical / Electronics Engineering','Programming and Problem Solving / Engineering Mechanics'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Electronics / Electrical Engineering','Programming & Problem Solving / Engineering Mechanics','Engineering Graphics'],                #Sem2
                        ['Solid Mechanics','Solid Modeling and Drafting','Engineering Thermodynamics','Engineering Materials and Metallurgy','Electrical and Electronics Engineering'],
                        ['Engineering Mathematics - III','Kinematics of Machinery','Applied Thermodynamics','Fluid Mechanics','Manufacturing Processes']]
            credit = [  [4,5,4,4,4],       #Sem1
                        [5,5,4,4,3],
                        [5,4,4,4,4],
                        [4,4,4,4,3] ]
            try:    #same try except for all 2019 sebjects... remaining
                subjectL = subject[semindex]
                creditL = credit[semindex]
            except Exception :
                return render(request,'errorpage.html') 

        elif branch == "cs":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Systems in Mechanical Engineering','Basic Electrical / Electronics Engineering','Programming and Problem Solving / Engineering Mechanics'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Electronics / Electrical Engineering','Programming & Problem Solving / Engineering Mechanics','Engineering Graphics'],                #Sem2
                        ['Discrete Mathematics','Fundamentals od data Structures','Object Oriented Programming','Computer Graphics','Digital Electronics & Logic Design'],
                        ['Engineering Mathematics- III','Data Structures and Algorithms','Software Engineering','Microprcessor','Principle of Programming Languages']]
            credit = [  [4,5,4,4,4],       #Sem1
                        [5,5,4,4,3],
                        [3,3,3,3,3],
                        [4,3,3,3,3] ]
            try:    #same try except for all 2019 sebjects... remaining
                subjectL = subject[semindex]
                creditL = credit[semindex]
            except Exception :
                return render(request,'errorpage.html') 

        elif branch == "it":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Systems in Mechanical Engineering','Basic Electrical / Electronics Engineering','Programming and Problem Solving / Engineering Mechanics'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Electronics / Electrical Engineering','Programming & Problem Solving / Engineering Mechanics','Engineering Graphics'],                #Sem2
                        ['Discrete Mathematics','Logic Design and Computer Organization','Data Structures and Algorithms','Object Oriented Programming','Basics of Computer Network'],
                        ['Engineering Mathematics- III','Processor Architecture','Database Management System','Computer Graphics','Software Engineering']]
            credit = [  [4,5,4,4,4],       #Sem1
                        [5,5,4,4,3],
                        [3,3,3,3,3],
                        [4,3,3,3,3] ]
            try:    #same try except for all 2019 sebjects... remaining
                subjectL = subject[semindex]
                creditL = credit[semindex]
            except Exception :
                return render(request,'errorpage.html') 
        
        elif branch == "civil":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Systems in Mechanical Engineering','Basic Electrical / Electronics Engineering','Programming and Problem Solving / Engineering Mechanics'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Electronics / Electrical Engineering','Programming & Problem Solving / Engineering Mechanics','Engineering Graphics'],                #Sem2
                        ['Building Technology and Architectural Planning','Mechanics of structure','Fluid Mechanics','Engineering Mathematics III','Engineering Geology'],
                        ['Geotechnical Engineering','Survey','Concrete Technology','Structural Analysis','Project management']]
            credit = [  [4,5,4,4,4],       #Sem1
                        [5,5,4,4,3],
                        [3,3,3,4,3],
                        [3,3,3,4,3] ]
            try:    #same try except for all 2019 sebjects... remaining
                subjectL = subject[semindex]
                creditL = credit[semindex]
            except Exception :
                return render(request,'errorpage.html') 

        elif branch == "entc":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Systems in Mechanical Engineering','Basic Electrical / Electronics Engineering','Programming and Problem Solving / Engineering Mechanics'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Electronics / Electrical Engineering','Programming & Problem Solving / Engineering Mechanics','Engineering Graphics'],                #Sem2
                        ['Engineering Mathematics III','Electronic Circuits','Digital Circuits','Electrical Circuits','Data structures'],
                        ['Signals & Systems','Control Systems','Principles of Communication Systems','Object Oriented Programming','Employability Skill Development'] ]
            credit = [  [4,5,4,4,4],       #Sem1
                        [5,5,4,4,3],
                        [5,3,3,3,3],
                        [4,3,3,3,3] ]
            try:    #same try except for all 2019 sebjects... remaining
                subjectL = subject[semindex]
                creditL = credit[semindex]
            except Exception :
                return render(request,'errorpage.html') 

        elif branch == "electrical":
            subject = [ ['Engineering Mathematics I','Engineering Physics / Chemistry','Systems in Mechanical Engineering','Basic Electrical / Electronics Engineering','Programming and Problem Solving / Engineering Mechanics'],     #Sem1
                        ['Engineering Mathematics II','Engineering Physics / Chemistry','Basic Electronics / Electrical Engineering','Programming & Problem Solving / Engineering Mechanics','Engineering Graphics'],                #Sem2
                        ['Engineering Mathematics-III','Power Generation Technologies','Material Science','Analog and Digital Electronics','Electrical Measurement & Instrumentation'],
                        ['Power System-I','Electrical Machines-I','Network Analysis','Numerical Methods & Computer Programming','Fundamental of Microcontroller and Applications'] ]
            credit = [  [4,5,4,4,4],       #Sem1
                        [5,5,4,4,3],
                        [3,3,3,3,3],
                        [3,3,3,3,3] ]
            try:    #same try except for all 2019 sebjects... remaining
                subjectL = subject[semindex]
                creditL = credit[semindex]
            except Exception :
                return render(request,'errorpage.html') 
            
    global GsubjectL
    GsubjectL = subjectL
    global GcreditL
    GcreditL = creditL

    if counthome != 0:
        return render(request,'page.html', {'subjectL' : subjectL,'creditL':creditL,'a': coursepattern,'b': branch})
    #--------------------------------------------------------------------------
    else:
        if countFE_SE != 0:
            msgMarksOutOfL.append(50)      #------------------------------- Msg Sem 1 2 3 4 of 2015 pattern, online 50 : Endsem 50 
            msgMarksOutOfL.append(50)
            msgProjectOutOfL.append(50)
            msgProjectOutOfL.append(50)
            

        elif countproject != 0:
            msgprojectL.append('Note : Project is for 200 Marks. 100 Marks for Term Work (~Insem) & 100 Marks for Oral (~Endsem). Enter Marks Accordingly')   #----------- Msg Project 100 : 100
            msgMarksOutOfL.append(30)
            msgMarksOutOfL.append(70)
            msgProjectOutOfL.append(100)
            msgProjectOutOfL.append(100)
            
        else:
            msgMarksOutOfL.append(30)      #----------------------- Msg for normal condition. Insem 30 : Endsem 70 
            msgMarksOutOfL.append(70)
            msgProjectOutOfL.append(30)
            msgProjectOutOfL.append(70)
            
        return render(request,'pagecalc.html', {'subjectL' : subjectL,'creditL':creditL,'a': coursepattern,'b': branch, 'msgMarksOutOfL':msgMarksOutOfL, 'msgProjectOutOfL':msgProjectOutOfL,'msgprojectL':msgprojectL })
#==============================================================================================
###################### START-- Part 1 -- Estimate Marks for entered Pointer ###################
#==============================================================================================
def main(request):

    try:
        pointerT = float(request.GET['pointerT'])
    except Exception:
        pass
    
    sd1 = int(request.GET['sd1'])
    sd2 = int(request.GET['sd2'])
    sd3 = int(request.GET['sd3'])
    sd4 = int(request.GET['sd4'])
    sd5 = int(request.GET['sd5'])

    sc1 = GcreditL[0]
    sc2 = GcreditL[1]
    sc3 = GcreditL[2]
    sc4 = GcreditL[3]
    sc5 = GcreditL[4]

    marksubL = []
    insem = []
    endsem = [] 
    totalL = []
    credT = sc1+sc2+sc3+sc4+sc5
    sdL = [sd1,sd2,sd3,sd4,sd5]

    coursepattern = Gcoursepattern
    semindex = Gsemindex

    def CalcAndDisplay(pointerD):
        pointerClosest = min(pointerD,key = lambda x:abs(x-pointerT))
        gradepointSol = pointerD.get(pointerClosest)
        
        def get_marks(x):
            if x == 10:
                return 82
            if x == 9:
                return 71
            if x == 8:
                return 63
            if x == 7:
                return 56
            if x == 6:
                return 51
            if x == 5:
                return 46
            if x == 4:
                return 41
            
        markSub1 = get_marks(gradepointSol[0])
        markSub2 = get_marks(gradepointSol[1])
        markSub3 = get_marks(gradepointSol[2])
        markSub4 = get_marks(gradepointSol[3])
        markSub5 = get_marks(gradepointSol[4])
        
        marksubL.append(markSub1)
        marksubL.append(markSub2)
        marksubL.append(markSub3)
        marksubL.append(markSub4)
        marksubL.append(markSub5)
       
        if countFE_SE != 0:
            for i in marksubL:
                insem.append(math.ceil(i * 0.5))
            for i in marksubL:
                endsem.append(math.ceil(i * 0.5))

        elif countproject != 0:
            for i in range (4):
                insem.append(math.ceil(marksubL[i] * 0.3))
            for i in range (4):
                endsem.append(math.ceil(marksubL[i] * 0.7))
            insem.append(math.ceil(marksubL[4]))      # for Project insem : endsem = 100:100
            endsem.append(math.ceil(marksubL[4]))
            
        else:
            for i in marksubL:
                insem.append(math.ceil(i * 0.3))
            for i in marksubL:
                endsem.append(math.ceil(i * 0.7))

        for i in range(5):
            totalL.append(insem[i]+endsem[i])
          
#----------------------END----------------------

#---------------ALGORITHM 3 LOGIC-----------------
    if (sd1==sd2 and sd2==sd3 and sd3==sd4 and sd4==sd5):
        
        pointSt = math.ceil(pointerT)
        
        z = pointSt

        dscr3L = [z,z,z,z,z]
        scL3 = [sc1,sc2,sc3,sc4,sc5]
        sol = []
        pointerD3 = {}
        
        sol.append( [ z,z,z,z,z ] )
        
        for i in range (5):  
            if scL3[i] == 3:
                dscr3L[i] = z-1
                scL3[i] += 3
                sol.append( [ dscr3L[0],dscr3L[1],dscr3L[2],dscr3L[3],dscr3L[4] ] )
            
        for i in range (5):   
            if scL3[i] == 4:
                dscr3L[i] = z-1
                scL3[i] += 3
                sol.append( [ dscr3L[0],dscr3L[1],dscr3L[2],dscr3L[3],dscr3L[4] ] )
            
        for i in range (5):         
            if scL3[i] == 5:
                dscr3L[i] = z-1
                scL3[i] += 3
                sol.append( [ dscr3L[0],dscr3L[1],dscr3L[2],dscr3L[3],dscr3L[4] ] )
                
        for i in range (len(sol)):
            pointerTemp3 = ((sc1*sol[i][0]+sc2*sol[i][1]+sc3*sol[i][2]+sc4*sol[i][3]+sc5*sol[i][4] )/credT)
            pointerHold3 = round(pointerTemp3,2) 
            pointerD3.update({pointerHold3 : [sol[i][0],sol[i][1],sol[i][2],sol[i][3],sol[i][4]] } )
            
#---------------------END----------------------
        
        CalcAndDisplay(pointerD3)
    
    else:
    #---------------ALGORITHM 1 LOGIC-----------------
        pointerD = {}
        
        for st in range (10,5,-1):
            
            algo1 = [st,st,st,st,st,st,st,st,st]
            algo2 = [st-1,st-2,st-1,st-2,st-1,st-2,st-3,st-3,st-3]
            algo3 = [st-2,st-3,st-3,st-4,st-4,st-5,st-4,st-5,st-6]
            
            for j in range (9):
                
                dscrL = []
                for i in range(5):
                    if (sdL[i]==1):
                        dscrL.append(algo1[j])
                    elif (sdL[i]==2):
                        dscrL.append(algo2[j])
                    else:
                        dscrL.append(algo3[j])
                        
                pointerTemp = ((sc1*dscrL[0]+sc2*dscrL[1]+sc3*dscrL[2]+sc4*dscrL[3]+sc5*dscrL[4])/credT)
                pointerHold = round(pointerTemp,2) 
                pointerD.update({pointerHold : [dscrL[0],dscrL[1],dscrL[2],dscrL[3],dscrL[4]] } )
        
        pointerClosest1 = min(pointerD,key = lambda x:abs(x-pointerT))    
        
#---------------------END----------------------
    
        if ((pointerT-0.2) < pointerClosest1  < (pointerT+0.2)):
            
            CalcAndDisplay(pointerD)
        
        else:
    #---------------ALGORITHM 2 LOGIC-----------------
            pointerD2 = {}

            z = 10
            
            dscr2L = [z,z,z,z,z]
            sdL2 = [sd1,sd2,sd3,sd4,sd5]
            sol = []
            
            for i in range(5):
                if sdL2[i] == 3:
                    dscr2L[i] = z-1
                    sdL2[i] += 2
                    sol.append( [ dscr2L[0],dscr2L[1],dscr2L[2],dscr2L[3],dscr2L[4] ] )
                    
            for i in range(5):
                if sdL2[i] == 2:
                    dscr2L[i] = z-1
                    sdL2[i] += 2
                    sol.append( [ dscr2L[0],dscr2L[1],dscr2L[2],dscr2L[3],dscr2L[4] ] )
            
            for i in range(5):
                if sdL2[i] == 5:
                    dscr2L[i] = z-2
                    sdL2[i] += 2    
                    sol.append( [ dscr2L[0],dscr2L[1],dscr2L[2],dscr2L[3],dscr2L[4] ] )
            
            for i in range (len(sol)):
                pointerTemp2 = ((sc1*sol[i][0]+sc2*sol[i][1]+sc3*sol[i][2]+sc4*sol[i][3]+sc5*sol[i][4] )/credT)
                pointerHold2 = round(pointerTemp2,2) 
                pointerD2.update({pointerHold2 : [sol[i][0],sol[i][1],sol[i][2],sol[i][3],sol[i][4]] } )
            
            pointerClosest2 = min(pointerD2,key = lambda x:abs(x-pointerT))
            
    #---------------------END----------------------
            
            if ((pointerT-0.25) < pointerClosest2  < (pointerT+0.25)): 
                
                CalcAndDisplay(pointerD2)
            else:
                CalcAndDisplay(pointerD)
#=============================================================================================              
###################### END -- Part 1 -- Estimate Marks for entered Pointer ###################
#=============================================================================================
    msgprojectL = []
    msgMarksOutOfL = []

    if countFE_SE != 0:
        msgMarksOutOfL.append('Out of 50 marks')      #------------------------------- Msg Sem 1 2 3 4 of 2015 pattern, online 50 : Endsem 50 ----- for Marks Estimation ie. 1st app
        msgMarksOutOfL.append('Out of 50 marks')

    elif countproject != 0:
        msgprojectL.append('Project is for 200 Marks. 100 Marks for Term Work (~Insem) & 100 Marks for Oral (~Endsem).')   #----------- Msg Project 100 : 100 ----- for Marks Estimation ie. 1st app
        msgMarksOutOfL.append('Out of 30 marks')
        msgMarksOutOfL.append('Out of 70 marks')
    else:
        msgMarksOutOfL.append('Out of 30 marks')      #----------------------- Msg for normal condition. Insem 30 : Endsem 70 ----- for Marks Estimation ie. 1st app
        msgMarksOutOfL.append('Out of 70 marks')

   
    return render(request,'result.html', {'subjectL':GsubjectL, 'insem': insem, 'endsem':endsem, 'totalL':totalL,'x':coursepattern, 'y':semindex, 'msgMarksOutOfL':msgMarksOutOfL,'msgprojectL':msgprojectL, 'pointer':pointerT } )
#==============================================================================================
#################### START -- Part 2 -- Estimate Pointer from entered Marks ###################
#==============================================================================================
def maincalc(request):

    inM1 = int(request.GET['inM1'])
    endM1 = int(request.GET['endM1'])
    inM2 = int(request.GET['inM2'])
    endM2 = int(request.GET['endM2'])
    inM3 = int(request.GET['inM3'])
    endM3 = int(request.GET['endM3'])
    inM4 = int(request.GET['inM4'])
    endM4 = int(request.GET['endM4'])
    inM5 = int(request.GET['inM5'])
    endM5 = int(request.GET['endM5'])

    insemL = [inM1,inM2,inM3,inM4,inM5]
    endsemL = [endM1,endM2,endM3,endM4,endM5]
    
    msgprojectL = []
    msgMarksOutOfL = []

    m1 = inM1 + endM1
    m2 = inM2 + endM2
    m3 = inM3 + endM3
    m4 = inM4 + endM4
    m5 = inM5 + endM5
    m_5 = m5

    if Gsemindex == 7:
        m5 = m5/2
        
    else:
        m5 = m5
#----------------------------------------------- To display Outof marks text in resultcalc page use only if needed.
    if countFE_SE != 0:
        msgMarksOutOfL.append('Out of 50')      #------------------------------- Msg Sem 1 2 3 4 of 2015 pattern, online 50 : Endsem 50 
        msgMarksOutOfL.append('Out of 50')

    elif countproject != 0:
        msgprojectL.append('Project is for 200 Marks. 100 Marks for Term Work (~Insem) & 100 Marks for Oral (~Endsem).')   #----------- Msg Project 100 : 100
        msgMarksOutOfL.append('Out of 30')
        msgMarksOutOfL.append('Out of 70')
    else:
        msgMarksOutOfL.append('Out of 30')      #----------------------- Msg for normal condition. Insem 30 : Endsem 70 
        msgMarksOutOfL.append('Out of 70')
#------------------------------------------------ end Use only if needed
    totalL = [m1,m2,m3,m4,m_5] 

    def get_credit(x):
        if 80 <= x <= 100:
            return 10
        if 70 <= x <= 79:
            return 9
        if 60 <= x <= 69:
            return 8
        if 55 <= x <= 59:
            return 7
        if 50 <= x <= 54:
            return 6
        if 45 <= x <= 49:
            return 5
        if 40 <= x <= 44:
            return 4
    
    cp1 = get_credit(m1)      # cp1 -- Credit Point Scored for Subject 1 (Out of 10)
    cp2 = get_credit(m2)
    cp3 = get_credit(m3)
    cp4 = get_credit(m4)
    cp5 = get_credit(m5) 

    global GcreditL
    creditL = GcreditL        # creditL -- Alloted Credits of each Subject (3,4,5)

    cpT1 = cp1 * creditL[0]    # cpT1 -- Total Credit Points Scored for Subject 1 (Out of 50 or 40 or 30)
    cpT2 = cp2 * creditL[1]
    cpT3 = cp3 * creditL[2]
    cpT4 = cp4 * creditL[3]
    cpT5 = cp5 * creditL[4]

    totalScoredcp = cpT1 + cpT2 + cpT3 + cpT4 + cpT5

    totalAllotedcp = (creditL[0]+creditL[1]+creditL[2]+creditL[3]+creditL[4])# *10

    pointerScored = round(totalScoredcp/totalAllotedcp,2)# *10

    percent = round(pointerScored * 8.8,2)
#=============================================================================================
###################### END -- Part 2 -- Estimate Pointer from entered Marks ##################
#=============================================================================================
    return render(request,'resultcalc.html', {'pointer':pointerScored ,'insemL':insemL,'endsemL':endsemL,'totalL':totalL, 'subjectL':GsubjectL, 'msgMarksOutOfL':msgMarksOutOfL,'msgprojectL':msgprojectL, 'percent':percent })