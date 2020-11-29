#!/usr/bin/env python
# coding: utf-8

# In[224]:


#for dealing with csv files
import csv
#for getting the filenames
import os


# In[225]:


def get_location(str):
    b=len(str)-1
    while(str[b] ==' '):
        b-=1;
    a=b
    while(str[a] != ' '):
        a-=1;
    try:
        # Some transactions don't have valid or any location at all
        x=int(str[a:b+1])
        return "None"
    except :
        return str[a:b+1].lower()


# In[226]:


def get_transaction_detail(di,row):
    for x in di:
        if "Transaction" in x:
            str=di[x]
            break
    # str is the Transaction Detail
    p=len(str)
    x=row['Transaction']
    # Checking if International, as then we also have to get Currency
    if "International" in x:
        # last word is Currency and rest id Transaction Description
        p=str.rfind(' ')
        row['Transaction Description']=str[:p]
        row['Currency']=str[p:]
    else:
        # if Domestic, then Transaction Description is Unchanged
        row['Transaction Description']=str;
    
    # obtaining location from the Transaction Details
    row['Location']=get_location(str[:p])
    
    


# In[227]:


def get_amount(di,row,line):
    if len(line) >len(di):
        # Location & Transaction values are noy correct
        location_found=0
        for x in di:
            if location_found:
                location=di[x]
                for y in di:
                    if 'Transaction' in y:
                        di[y]=di[y]+' '+location
                        break
                break
            if 'Transaction' in x:
                location_found=1
        # Credit and Debit will be not in their corresponding columns
        if 'Amount' in di:
            di['Amount']=line[-1]
        else:
            di['Debit']=line[-1]
            di['Credit']=""
            
    if "Amount" in di:
        if "r" in di["Amount"]:
            row['Credit']=int(di["Amount"][:-2])
            row['Debit']=0
        else:
            row['Debit']=di["Amount"]
            row['Credit']=0
    else:
        row['Credit']=di['Credit']
        row['Debit']=di['Debit']
        if row['Credit']=="":
            row['Credit']=0;
        if row['Debit']=="":
            row['Debit']=0;


# In[228]:


def change_date(str):
    if '#' in str:
        # Date is not specified
        return "00000000"
    str=str.replace('/','-')
    a=str.find('-')
    b=str.rfind('-')
    return (str[b:]+str[a:b]+str[:a])


# In[229]:


def StandardizeStatement(input_file,output_file):
    with open(input_file,'r',encoding='utf-8-sig') as input:
        with open(output_file,'w',newline='') as output:
            fields=['Date','Transaction Description','Debit','Credit','Currency','CardName','Transaction','Location']
            input=csv.reader(input)
            input=list(input)
            output=csv.DictWriter(output,fieldnames=fields)
            output.writeheader()
            
            #The values of this dictionary will be transfered to every row of output file
            row=dict.fromkeys(fields)
            
            #Currency = INR , will be used in Domestic 
            row['Credit']=0
            row['Debit']=0
            row['Currency']="INR"
            
            #This dictionary will be used for different indices/headings of input files
            di={}
            
            # This heading var will be set after seeing heading Domestic/International 
            heading=0
            
            # Iterating Over our input file
            for line in input:
                # Check if Row is Empty or Not
                if any(line):
                    if heading or (len([x for x in line if "Date" in x])):
                        # Looking For Heading of each Section, i.e if new section has started or not
                        di=dict.fromkeys(line)
                        heading=0
                    elif line[0] == '':
                        #check if name or Transaxtion detail
                        i=1
                        while(line[i]==''):
                            i+=1
                        if "Transaction" in line[i]:
                            heading=1
                            row['Transaction'] = line[i]
                        else:
                            row['CardName']=line[i]
                    else:
                        i=0
                        #enter the row values in di dictionary
                        for x in di:
                            di[x]=line[i]
                            i+=1
                        
                        #Getting Date from di, we are iterating over dictionary as there are tab spaces in names 
                        for x in di:
                            if "Date" in x:
                                row["Date"]=di[x]
                                break
                                
                        # Getting Credit and Debit from Amount
                        get_amount(di,row,line)
                        
                        # Getting Transaction related information
                        get_transaction_detail(di,row)
                        
                        # Writing the row into our output file, after obtaining all the values
                        output.writerow(row)
                    


# In[230]:


def SortByDate(file):    
    with open(file,'r',encoding='utf-8-sig') as input:
        input=csv.reader(input)
        input=list(input)
        # Passing The entire Data except the index column
        input[1:]=sorted(input[1:],key= lambda x: change_date(x[0]))
    with open(file,'w',encoding='utf-8-sig',newline="") as output:
        output=csv.writer(output)
        for line in input:
            # Standardizing The Delimiter for dates 
            line[0]=line[0].replace('/','-')
            output.writerow(line)
        
        
    


# In[231]:




if __name__ == '__main__':
    # For Checking on Various other files, simply put those files in input directory
    # When the program is run, it will automatically collect all the files in Input directory
    # And produce the Corresponding Standardized Output File with proper name
    # Sending Files one by one to our function
    for filename in os.listdir('input'):
        input='input/'+filename
        output='output/'+filename.replace('Input','Output')
        StandardizeStatement(input,output)
        SortByDate(output)
    
    
    
    


# In[ ]:




