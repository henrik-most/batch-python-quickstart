# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 10:47:23 2021

@author: Administrator
"""

import pandas, os, joblib


def fSaveModel(clf, sPath):
    joblib.dump(clf,sPath)

def fFileLoader(sPath):
    return joblib.load(sPath)


def fCreateTestLeftside(sSupplier, sLeftSide):
    df_temp=pandas.DataFrame(columns=["Tutkittava"])
    df_temp.loc[len(df_temp)]=sSupplier
    print("Created test left side")
    fSaveModel(df_temp, sLeftSide)


def fReadTestLeftside(sLeftSide):
    df_temp=fFileLoader(sLeftSide)
    print("loaded test_left_side")
    return(df_temp["Tutkittava"][0])
    


if __name__=="__main__":
    sModelsPath='/mnt/batch/tasks/fsmounts/batch/models'
    sExportZip="export.zip"
    sLeftSide="left_side.sav"
    sResultDir='/mnt/batch/tasks/fsmounts/batch/invoice-results'
    sResultFile="predicted_result.pkl.z"
    sResultPath=os.path.join(sResultDir,sResultFile)
    
    #supplier=os.environ.get(_SUPPLIER)
    #print(supplier)

    #invoice=os.environ.get(_INVOICE_NAME)
    #print(invoice)

    # Testing if all folders exist    
    if os.path.isdir(sModelsPath):
        print("Model folder found")
    else:
        print("Error in model folder. Check dir locations")
        
        
    if os.path.isfile(sExportZip):
        print("Export found")
    else:
        print("Error in Export. Check dir locations")
        
    
    # Testing pandas and yTEST    
    fCreateTestLeftside("yTEST", sLeftSide)
    sReceivedSupplier=fReadTestLeftside(sLeftSide)
    
    if(sReceivedSupplier!="yTEST"):
        print("Error in receiving yTEST. Ensure dirs and check that pandas works.")
        print("Potentially ignore this error if not using testCase")
    else:
        print("yTEST passed")


    if os.path.isdir(sResultDir):
        print("ResultDir found")
    else:
        print("Error in ResultDir. Check dir locations")
        raise # Exiting, so the next writing session will not fail.
    

    # Ensuring that model exists
    sModelPath=os.path.join(sModelsPath,sReceivedSupplier+"_ALV_pred.sav")
    if(os.path.isfile(sModelPath)):
        print("Model file exists")
        df_result=pandas.DataFrame(columns=["Date"])
        df_result.loc[0]=datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        fSaveModel(df_result, sResultPath)
    
    
    
    
    
    
    
    
    