# -*- coding: utf-8 -*-
print("------------------------------------------------------")
print("---------------- Metadata Information ----------------")
print("------------------------------------------------------")
print("")

print("In the name of God")
print("Project: AutoCML: Automatic Comparative Machine Learning in COVID-19 Screening Model")
print("Creator: Mohammad Reza Saraei")
print("Contact: m.r.saraei@seraj.ac.ir")
print("University: Seraj Institute of Higher Education")
print("Supervisor: Dr. Saman Rajebi")
print("Created Date: May 20, 2022")
print("") 


print("----------------------------------------------------")
print("------------------ Import Libraries ----------------")
print("----------------------------------------------------")
print("")

# Import Libraries for Python
import pandas as pd

print("----------------------------------------------------")
print("------------------ Data Ingestion ------------------")
print("----------------------------------------------------")
print("")

# Import DataFrames (.csv) by Pandas Library
df_PLS = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Screening\Encoded Data\CoV19_PLS_Encoded.csv")
df_CLS = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Screening\Encoded Data\CoV19_CLS_Encoded.csv")
df_EHR = pd.read_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Screening\Encoded Data\CoV19_EHR_Encoded.csv")

# Fusion of DataFrames (.csv) 
df = pd.concat([df_PLS, df_CLS, df_EHR], axis = 1)                  
# df = np.concatenate((df_PhS, df_ClS, df_EHR), axis = 1)

# Delete Column "Gender" from Dataframe
df = df.drop("Gender", axis = 1)

print("------------------------------------------------------")
print("----------------- Data Annotation --------------------")
print("------------------------------------------------------")
print("")

# [0 = Suspected]
# [1 = Probable]

df['Target'] = 0     
# range(0, len(df))

def target(row):
    if (row['LoT_S'] == 2):
        return "1"  
    elif ((row['Ch_P'] == 1) | (row['LoS_M_C'] == 1)) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Cough'] == 2) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif (row['Hypoxemia'] == 3) & (row['Dyspnea'] == 1) & (row['Fatigue'] == 2) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Headache'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Fatigue'] == 2) & (row['Headache'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Fatigue'] == 2) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"    
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Fatigue'] == 2) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"        
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Headache'] == 1) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"       
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['Headache'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"       
    elif ((row['Pyrexia'] == 1) | (row['Pyrexia'] == 2) | (row['Pyrexia'] == 3) | (row['Pyrexia'] == 4)) & (row['GI'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"           
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"            
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"                
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"                   
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"                    
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & (row['Headache'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"        
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"        
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Fatigue'] == 2) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"        
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Headache'] == 1) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Hypoxemia'] == 1) | (row['Hypoxemia'] == 2) | (row['Hypoxemia'] == 3)) & (row['Headache'] == 1) & (row['Dyspnea'] == 1 & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3)))):
        return "1"    
    elif (row['Hypoxemia'] == 1) & (row['GI'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1" 
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & (row['Headache'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Fatigue'] == 2) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"   
    elif ((row['Cough'] == 1) | (row['Cough'] == 3)) & (row['Headache'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"   
    elif (row['Fatigue'] == 2) & (row['Headache'] == 1) & (row['GI'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif (row['Fatigue'] == 2) & (row['Headache'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif (row['Fatigue'] == 2) & (row['GI'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    elif (row['Headache'] == 1) & (row['GI'] == 1) & (row['Dyspnea'] == 1) & ((row['Contact'] == 1) | (row['Age'] == 1) | ((row['Anamnesis'] == 1) | (row['Anamnesis'] == 2) | (row['Anamnesis'] == 3))):
        return "1"
    else:
        return "0"

df = df.assign(Target=df.apply(target, axis = 1))

print("")

print("----------------------------------------------------")
print("----------------- Saving Outputs -------------------")
print("----------------------------------------------------")
print("")

# Save DataFrame After Encoding
df.to_csv(r"D:\My Papers\2020 - 2030\Journal Paper\Journal of Communications Technology and Electronics [IF=0.5] (2022)\CoV19 Dataset\Screening\Annotated Data\CoV19_Data_Annotated.csv", index = False)

print("----------------------------------------------------")
print("--------- Thank you for waiting, Good Luck ---------")
print("---------- Signature: Mohammad Reza Saraei ---------")
print("----------------------------------------------------")

