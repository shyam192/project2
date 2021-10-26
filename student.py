import csv                           #package or librarie

def write_into_csv(info_list):                      #creating a function to write a file or create a file    
    
    with open('student_info.csv','a',newline='') as csv_file:   #a apend mode #w+ write mode new li ne each string sepraed by a row                         #opening a file to do file handling process                        
        writer=csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","age","mobile_no","e-mail"])
            
        writer.writerow(info_list)

if __name__=='__main__':           #progrmas will start from here
    condition=True
    student_num=1

    while(condition):
        student_info=input("Enter student {} details   Format(name,age m_no,email id):".format(student_num))
        
        #split function  from string class : it takes the string and split the string according to our given data
        
        student_info_list=student_info.split(' ')
        
        #print("student details: "+str(student_info_list))
        
        print("\nStudent {} details :\nName: {}\nAge:{}\nContact_number: {}\nEMAiL-ID: {}".format(student_num,student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))

        choice_check=input("IS THE INFORMARTIPON CORRECT ?(YES/NO)")
        if choice_check=="yes":
            
            write_into_csv(student_info_list)

            condition_check=input("PRESS YES IF YOU WANT TO ENTER ANOTHER STUDENT DETAILS OTHERWISE NO (YES/NO):")
            if condition_check=="yes":
                condition=True
                student_num=student_num+1
            elif condition_check=="no":
                condition=False             #input  completed
        else:
            print("please re enter the  information!")
             

