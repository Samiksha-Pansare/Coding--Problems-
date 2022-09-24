from pyrsistent import m


def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    p_count=0
    e_count=0
    o_count=0
    max=""
    for i in range(0,len(patient_medical_speciality_list)):
        #print(i)
        if(i%2!=0):
            #print(patient_medical_speciality_list[i])
            if(patient_medical_speciality_list[i]=="P"):
                p_count=p_count+1
            elif(patient_medical_speciality_list[i]=="E"):
                e_count = e_count+1
            elif(patient_medical_speciality_list[i]=="O"):
                o_count=o_count+1
        #print(p_count,o_count,e_count)
        if(p_count>e_count):
            if(p_count>o_count):
                max="P"
            else:
                max="O"
        elif(o_count>e_count):
            max="O"
        else:
            max="E"
        #print("Max",max)
    return medical_speciality.get(max)

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
#print(speciality)