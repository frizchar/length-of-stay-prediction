# length-of-stay prediction
### Overview
We predict the length-of-stay (LOS) of hospital inpatients.<br>
The problem is treated as a classification problem using the [xgboost](https://github.com/dmlc/xgboost/releases) algorithm and considering the following two classes:<br>
- class 1 = **'1 or 2 days'**<br>
- class 2 = **'3+ days'**<br>

&rarr; LOS = 1 ( _class 1 = '1 or 2 days'_ ) is considered when _admission date = release date_.<br>
&rarr; LOS = 2 ( _class 1 = '1 or 2 days'_ ) is considered when _admission date = release date + 1 day_.<br>
&rarr; LOS = 3 ( _class 2 = '3+ days'_ ) is considered when _admission date = release date + 2 days_.<br>
etc.

The code is written in Python.

### Folder structure
- folder **evaluate** includes the evaluation code
- folder **deploy** includes the deployment code

### Dependencies
The required packages are included in file ```requirements.txt```.<br>
Python interpreter version used for this project: **3.9.4**

### Predictors
1. sex : categorical variable := sex of patient
1. family : categorical variable := family status id of patient
1. ter : categorical variable := prefecture id of patient's residence
1. wayin : categorical variable := type of patient's admission
1. asfal1 : categorical variable := id of patient's 1st health insurance
1. has_asfal2 : categorical variable := boolean flag on whether the patient has 2nd health insurance or not
1. has_asfal3 : categorical variable := boolean flag on whether the patient has 3rd health insurance or not
1. icd10groupid : categorical variable := id of ICD10 group assigned to patient on admission
1. specialty : categorical variable := id of the doctor's specialty
1. weekday : numerical variable := day of week (0,1,..6) on admission
1. hh24 : numerical variable := hour of day (00,01,02,...,23) on admission
1. age : numerical variable := patient age on admission day
