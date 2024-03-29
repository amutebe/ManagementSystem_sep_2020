from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from random import randint,randrange
from django import forms
from django.conf import settings
from multiselectfield import MultiSelectField
from itsms_20000.models import component
from accounts.utils import *



##################################
from django.core.exceptions import ValidationError




# Create your models here.
def car_no():
    now = datetime.now()
    return str((date.today()).strftime("%d%m%Y"))+str(randrange(100, 299))


def correction_no():
    now = datetime.now()
    return str((date.today()).strftime("%d%m%Y"))+str(randrange(100, 299))

class providers(models.Model):

    description=models.CharField("Provider Name", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class improvementplan(models.Model):

    description=models.CharField("Improvement plan:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class planofaction(models.Model):

    description=models.CharField("Plan of action", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
class document_standard(models.Model):

    description=models.CharField("ISO Standard Clause:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class document_type(models.Model):

    description=models.CharField("Document type", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class document_format(models.Model):

    description=models.CharField("Document format", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
class document_location(models.Model):

    description=models.CharField("Document location", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class equipment(models.Model):

    description=models.CharField("Equipment", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class schedule(models.Model):

    description=models.CharField("Maintenence schedule", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class classification(models.Model):

    description=models.CharField("Incident Classification", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
class correction(models.Model):

    description=models.CharField("Correction/Containment:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class rootcause(models.Model):

    description=models.CharField("Root Cause", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class mod9001_document_manager(models.Model):
    document_date=models.DateField("Date:")
    document_number=models.CharField("Document no.:",max_length=200,default="BCL-Q-"+car_no(),primary_key=True)
    standard= models.ForeignKey('document_standard',on_delete=models.CASCADE,verbose_name='Standard',related_name='standard')
    Origin=(('1','Internal'),('2','External'))
    origin=models.CharField(max_length=200,null=True, choices=Origin)
    doc_type= models.ForeignKey('document_type',on_delete=models.CASCADE,verbose_name='Document Type:',related_name='type')
    document_id =models.TextField("Document ID:",null=True,blank=True)
    doc_name =models.TextField("Document Name:",null=True,blank=True)

    clause =models.TextField("Standard Clause:",null=True,blank=True)
    format= models.ForeignKey('document_format',on_delete=models.CASCADE,verbose_name='Format:',related_name='format')
    version =models.TextField("Version No:",null=True,blank=True)
    location= models.ForeignKey('document_location',on_delete=models.CASCADE,verbose_name='Location:',related_name='location')
    specifyl =models.TextField("Specify location:",null=True,blank=True)
    author =models.TextField("Author:",null=True,blank=True)
   
   
    owner= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Owner:',related_name='owner')
    Retention=(('1','1 Year'),('2','2 Years'),('3','3 years'),('4','4 Years'),('5','5 years'),('6','more than 5 Yeas'))
    retention=models.CharField("Retention time:",max_length=200,null=True, choices=Retention)
    Status=(('1','Current'),('2','Obsolete'))
    status=models.CharField(max_length=200,null=True, choices=Status)
    document = models.FileField("Upload document:",upload_to='documents/',null=True,validators=[validate_file_size])
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)
class mod9001_calibration(models.Model):
    calibration_date=models.DateField("Date:")
    calibration_number=models.CharField("Calibration no.:",max_length=200,default="BCL-C-"+car_no(),primary_key=True)
    type =models.TextField("Calibration type:",null=True,blank=True, help_text='Calibration type')
    device_id =models.TextField("Device ID:",null=True,blank=True, help_text='Device ID')
    manufacturer =models.TextField("Manufacturer:",null=True,blank=True, help_text='Device Manufacturer')
    range =models.TextField("Range:",null=True,blank=True, help_text='Range')
    calibrated_by= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Done by:',related_name='doneby')
    standard= models.ForeignKey('document_standard',on_delete=models.CASCADE,verbose_name='Standard:',related_name='calstandard')
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='cal_entered_by',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)
class maintenance(models.Model):
    maintenance_number=models.CharField("Maintenance no.:",max_length=200,default="BCL-M-"+car_no(),primary_key=True)
    date_today=models.DateField("Date:")
    equipment= models.ForeignKey('equipment',on_delete=models.CASCADE,verbose_name='Equipment:',related_name='Equipment')
    id =models.TextField("ID:",null=True,blank=True, help_text='Enter ID or Serial #')
    manufacturer =models.TextField("Manufacturer:",null=True,blank=True, help_text='Manufacturer')
    date=models.DateField("Manufacture Date:")
    location =models.TextField("Location:",null=True,blank=True, help_text='Location')
    user= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='user:',related_name='user')
    schedule= models.ForeignKey('Schedule',on_delete=models.CASCADE,verbose_name='Schedule:',related_name='Schedule')
    detials =models.TextField("Details:",null=True,blank=True, help_text='Details')
    maintenanceby=(('1','Internal technician'),('2','External technician'))
    maintenanceby=models.CharField(max_length=200,null=False, choices=maintenanceby)
    name =models.TextField("Name of Techncian:",null=True,blank=True, help_text='Name')
    parts =models.TextField("Parts replaced:",null=True,blank=True, help_text='Parts replaced')
    notes =models.TextField("Notes:",null=True,blank=True, help_text='Notes')
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='maintenance_entered_by',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)
class prod_description(models.Model):

    description=models.CharField("Program Description", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description 


class status(models.Model):

    description=models.CharField("Status", max_length=50,null=True,blank=True,)
    def __str__(self):
        return self.description 

class qmsstatus(models.Model):

    description=models.CharField("Status", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class noteffective(models.Model):
    description=models.CharField("Reason not effective", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class train_desc(models.Model):
    description=models.CharField("Training Description", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class train_objective(models.Model):
    description=models.CharField("Training Objective", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class train_status(models.Model):
    description=models.CharField("Training Status", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class incident_type(models.Model):
    
    description=models.CharField("Type of feedback", max_length=200,null=True,blank=True)
    def __str__(self):
        return self.description

class costs(models.Model):
    
    description=models.CharField("Incident cost", max_length=200,null=True,blank=True)
    def __str__(self):
        return self.description




class incident_description(models.Model):
    description=models.CharField("Incident Description", max_length=200,null=True,blank=True)
    incident_type= models.ForeignKey('incident_type',on_delete=models.CASCADE,verbose_name='Incident Type:',related_name='incidentype')
    def __str__(self):
        return self.description

class process(models.Model):
    description=models.CharField("Process", max_length=200,null=True,blank=True)
    dept= models.ForeignKey('accounts.Department',on_delete=models.CASCADE,verbose_name='Department:',null=True,blank=True)
    owner =models.TextField("Process Owner:",null=True,blank=True, help_text='Process owner')

    def __str__(self):
        return self.description


class mod9001_qmsplanner(models.Model):
    planner_number=models.CharField("Planner no.:",max_length=200,default="BCL-QP-"+car_no(),primary_key=True)
    plan_date=models.DateField("Plan Date:")
    #planner = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='qms_by',on_delete=models.CASCADE)
    planner=models.ForeignKey('accounts.employees',on_delete=models.SET_NULL,null=True,verbose_name='Planner:',related_name='qms_by')
    planner_user_id= models.CharField("Planner Sytem UserID.:", max_length=20, null=True, blank=True)       
    planner_user_title= models.CharField("Planner Title.:", max_length=20, null=True, blank=True)     
       
    
    start=models.DateField("Start Date:")
    end=models.DateField("End Date:")
    description= models.ForeignKey('prod_description',on_delete=models.CASCADE,verbose_name='Program description:',related_name='progdesc')
    details =models.TextField("Additional Description:",null=True,blank=True, help_text='Additional Description')
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.CASCADE,verbose_name='Status:',null=True,blank=True)
    rejected=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    approval_date=models.DateField("Date Approved:",null=True,blank=True)
    approved_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='qmsApprov_by',on_delete=models.CASCADE)
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.CASCADE,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    due=models.DateField("When:",null=True,blank=True)
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.CASCADE,null=True,verbose_name='Verification Status:')
    completion=models.DateField("Completion Date:",null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='qms_entered_by',on_delete=models.CASCADE)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)    
    date_today=models.DateField("Date created:",default=datetime.now)
    def __str__(self):
        return self.planner_number
class mod9001_trainingplanner(models.Model):
    plan_number=models.CharField("Plan no.:",max_length=200,default="Comp-TP-"+car_no(),primary_key=True)
    planner=models.ForeignKey('accounts.employees',null=True, blank=True,on_delete=models.CASCADE,verbose_name='Planner:',related_name='tainingplanner_by')
    planner_user_id= models.CharField("Planner Sytem UserID.:", max_length=20, null=True, blank=True)
    planner_user_title= models.CharField("Planner Title:", max_length=20, null=True, blank=True)                  
    trainng_date=models.DateField("Training Date:",null=True)
    TYPE=(('1','Planned'),('2','Not Planned'))
    type=models.CharField(max_length=200, choices=TYPE)
    description = models.ForeignKey('train_desc',null=True, blank=True, related_name='train_desc',on_delete=models.CASCADE)
    details=models.TextField("Additional description:",null=True,blank=True)
    other=models.TextField("Other training description:",null=True,blank=True)
    TrainAudience=(('1','Employee'),('2','Other'))
    trainaudience=models.CharField(max_length=200,null=True, choices=TrainAudience)
    trainee=models.ForeignKey('accounts.employees',null=True, blank=True,on_delete=models.CASCADE,verbose_name='Trainee:')
     
    other_audience=models.TextField("Other Training Audience:",null=True,blank=True)
    start=models.DateField("Start Date:")
    end=models.DateField("End Date:")
    LOCATION=(('1','Company Premise'),('2','Other'))
    trainlocation=models.CharField(max_length=200,null=True, choices=LOCATION)
    other_location=models.TextField("Other Location:",null=True,blank=True)
    trainer=models.TextField("Trainer:",null=True,blank=True)
    resources=models.TextField("Resource:",null=True,blank=True)
    objective = models.ForeignKey('train_objective',null=True, blank=True, related_name='train_objective',on_delete=models.CASCADE)
    comments=models.TextField("Comment:",null=True,blank=True)
    reason=models.TextField("Give Reason:",null=True,blank=True)
    rescheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    completion=models.DateField("Completion Date:",null=True,blank=True)
     
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.CASCADE,verbose_name='Status:',null=True,blank=True)
    rejected=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    approval_date=models.DateField("Date Approved:",null=True,blank=True)
    approved_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='trainplannerApprov_by',on_delete=models.CASCADE)
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.CASCADE,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    due=models.DateField("When:",null=True,blank=True)
    trainplannerstatus=models.ForeignKey(qmsstatus, on_delete=models.CASCADE,null=True,verbose_name='Verification Status:')

    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='planner_entered_by',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True) 

    def __str__(self):
        return self.plan_number




class mod9001_trainingregister(models.Model):
    training_number=models.CharField("Training no.:",max_length=200,default="Comp-TR-"+car_no(),primary_key=True)
    plan_number=models.ForeignKey(mod9001_trainingplanner,on_delete=models.CASCADE,verbose_name='Planner No.:',related_name='plannerid')
   
    train_date=models.DateField("Training Date:",null=True)
    Nature=(('1','Planned'),('2','Not Planned'))
    nature=models.CharField(max_length=200,null=True, choices=Nature)
    training_desc=models.TextField("Training Description:",null=True,blank=True)
    trainingplanid=models.TextField("Training Plan ID:",null=True,blank=True)
    training=models.TextField("Training:",null=True,blank=True)
    location=models.TextField("Location:",null=True,blank=True)
    trainer = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='reg_by',on_delete=models.CASCADE)
    #trainee=models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Trainee:',related_name='trainee')
    trainee=models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Trainee :',null=True,blank=True)
    tainee_dept=models.ForeignKey('accounts.Department', on_delete=models.CASCADE,verbose_name='Trainee Department ID:',related_name='traineeDepartment')
    completion_date=models.DateField("Completion Date:")
    yesno=(('1','Yes'),('2','No'))
    job=models.CharField("Job performance level raised ",max_length=200,null=True, choices=yesno)
    skills=models.CharField("Training skills applied",max_length=200,null=True, choices=yesno)
    indicators=models.CharField("Indicators exist proving that the employee benefited from training",max_length=200,null=True, choices=yesno)
    able=models.CharField("Employee Able to train others",max_length=200,null=True, choices=yesno)
    decision=(('1','Effective'),('2','Not Effective'))
    decision=models.CharField("Evaluation Decision:",max_length=200,null=True, choices=decision)
    reasond=models.ForeignKey('noteffective', on_delete=models.CASCADE,verbose_name='If Not Effective, give reason:',related_name='noteffectreason',null=True,blank=True)
    reasonother=models.TextField("Other reasons:",null=True,blank=True)
    actionplan=models.ForeignKey('planofaction', on_delete=models.CASCADE,verbose_name='Plan of action:',related_name='planofaction',null=True,blank=True)
    actionplanother=models.TextField("Additional description:",null=True,blank=True)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='assignedto',verbose_name='Assigned to:',on_delete=models.CASCADE)
    timeline=models.DateField("Timeline:",null=True,blank=True)     
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.CASCADE,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.CASCADE,null=True,verbose_name='Verification Status:')
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.CASCADE,verbose_name='Status:',null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    completion=models.DateField("Completion Date:",null=True,blank=True)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)   
        
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='training_entered_by',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)


class mod9001_customeregistration(models.Model):
    name="Customer Registration"
    plan_number=models.CharField("Plan no.:",max_length=200,primary_key=True)
    date_posted=models.DateField("Date Posted:",null=True)
    name=models.TextField("Customer Name:",null=True,blank=True)
    manager=models.TextField("Account Manager:",null=True,blank=True)
    contact=models.TextField("Customer Contact Person:",null=True,blank=True)
    phone=models.TextField("Customer Business Phone No:",null=True,blank=True)
    email=models.EmailField("Customer Business Email: ",null=True,blank=True)
    address=models.TextField("Customer Business Address: ",null=True,blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='customer_entered_by',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)


class mod9001_supplieregistration(models.Model):
    name="Supplier Registration"
    supplier_number=models.CharField("Supplier no.:",max_length=200,primary_key=True)
    date_posted=models.DateField("Date Posted:",null=True)
    name=models.TextField("Supplier Name:",null=True,blank=True)
    #name = models.ForeignKey(providers,null=True, blank=True, related_name='providers',on_delete=models.CASCADE)
    manager=models.TextField("Account Manager:",null=True,blank=True)
    contact=models.TextField("Customer Contact Person:",null=True,blank=True)
    phone=models.TextField("Customer Business Phone No:",null=True,blank=True)
    email=models.EmailField("Customer Business Email: ",null=True,blank=True)
    address=models.TextField("Customer Business Address: ",null=True,blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='supplier_entered_by',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    def __str__(self):
        return self.name


####################INCIDENT LOG#####################################

class mod9001_incidentregister(models.Model):
    incident_number=models.CharField("Incident No.:",max_length=200,primary_key=True)
    date=models.DateField("Date:",default=datetime.now,null=False)
    time=models.TimeField("Time (24Hr):",null=True)
    reporter= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Reported by:',null=True,blank=True)
       
    REFERENCE=(('1','Project'),('2','Process'),('3','Other'))
    reference=models.CharField("Reference",max_length=200, choices=REFERENCE)
    processname=models.ForeignKey('process', on_delete=models.CASCADE,verbose_name='If Process, name:',null=True,blank=True)
    incidentype=models.ForeignKey('incident_type', on_delete=models.CASCADE,verbose_name='incidentype:',null=True,blank=True)
    incident_description=models.ForeignKey('incident_description', on_delete=models.CASCADE,verbose_name='Incident description:',null=True,blank=True)
    other=models.TextField("Details",null=True, blank=True)
    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='register_entered_byy',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    analysis_flag=models.TextField("Incident Analysis Done?",null=True,blank=True,default='No', help_text='To be uses while filtering incidents pending analysis')
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)   
    
    
    def __str__(self):
        return self.incident_number


#####################INCIDENT ANALYSIS######################################
class mod9001_incidentregisterStaff(models.Model):
    incident_number=models.OneToOneField('mod9001_incidentregister', on_delete=models.CASCADE,verbose_name='Incident Number:',null=True,blank=True)
    date=models.DateField("Date:",default=datetime.now,null=False)   
    classification=models.ForeignKey('classification', on_delete=models.CASCADE,verbose_name='Incident Classification:',null=True,blank=True)
    rootcause=models.ForeignKey('rootcause', on_delete=models.CASCADE,verbose_name='Root Cause:',null=True,blank=True)
    otherootcause=models.TextField("Other Root Cause:",null=True, blank=True)
    #correction=(('1','Redo/Rework'),('2','Replace'),('3','Refund'),('4','Repair'),('5','Suspend'),('6','Customer Concession obtained'),('7','Escalated'),('8','Other'))    
    #correction=models.CharField(verbose_name='Short Term Correction/Containment:',max_length=50, null=True,blank=True,choices=correction)
    correction=models.ForeignKey('correction', on_delete=models.CASCADE,verbose_name='Correction/Containment:',null=True,blank=True)

    escalated = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,verbose_name='Responsible:', related_name='escalated',on_delete=models.CASCADE)
    description=models.TextField("Additional Description:",null=True, blank=True)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, verbose_name='Assigned:',related_name='asigned',on_delete=models.CASCADE)
    #date=models.DateField("Date:",default=datetime.now)
    completion=models.DateField("Completion Date:",null=True,blank=True)
    costs=(('1','Financial'),('2','Operational'),('3','Legal/Regulatory'),('4','Brand/Reputation'))
    #MY_CHOICES = (('item_key1', 'Item title 1.1'),('item_key2', 'Item title 1.2'),('item_key3', 'Item title 1.3'),('item_key4', 'Item title 1.4'),('item_key5', 'Item title 1.5'))
    cost = MultiSelectField('Incident Cost',choices=costs)
    currency=(('1','UGX'),('2','USD'),('3','Kshs'),('4','GBP'))
    currency=models.CharField(verbose_name='Currency:',max_length=50, null=True,blank=True,choices=currency)

    costdescription=models.IntegerField("Cost Amount:",null=True,blank=True)

    lesson=models.TextField("Lesson learnt:",null=True, blank=True)
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.CASCADE,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True)
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.CASCADE,null=True,verbose_name='Verification Status:')
    
  
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    #assignedto= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name='Assigned to:',null=True,blank=True)
    completedby= models.ForeignKey('accounts.employees',on_delete=models.SET_NULL,verbose_name='Completed by:',null=True,blank=True)
    
    due=models.DateField("When:",null=True,blank=True)      
    #comp_status=models.TextField("Compliant Status:",null=True, blank=True)
    component_affected= models.ForeignKey(component,on_delete=models.SET_NULL,verbose_name='Affected Component:',null=True,blank=True)
    report_number=models.TextField("Report No.:",null=True, blank=True)
    error=models.TextField("Known Error:",null=True, blank=True)    
    solution=models.TextField("Solution:",null=True, blank=True)    
    remark=models.TextField("Remarks:",null=True, blank=True) 
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)  

    entered_by = models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='incidentstaff',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.CASCADE,verbose_name='Status:',null=True,blank=True)
    document = models.FileField("Upload Support Document:",upload_to='documents/',null=True,blank=True,validators=[validate_file_size_verification])
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)    
    
    
    
    def __str__(self):
        return self.incident_number

    

class mod9001_processtable(models.Model):
    process_number=models.CharField("Process ID:",max_length=200,default="Comp-Pr-"+car_no(),primary_key=True)
    date=models.DateTimeField("Date Registered:",null=True)
    category=(('1','Key Process'),('2','Support Process'),('3','Outsourced Process'),('4','Other'))
    processcategory=models.CharField("Process Category",max_length=200, choices=category)
    process=models.ForeignKey('process', on_delete=models.CASCADE,verbose_name='procestable:',null=True,blank=True)
    purpose=models.TextField("Purpose",null=True, blank=True)
    owner= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Owner:',related_name='own')

class providerparameters(models.Model):
    id=models.CharField("ID:",max_length=50,primary_key=True)
    desc=models.TextField("Description:")
    def __str__(self):
        return self.desc

class adaptability(models.Model):
    id=models.CharField("ID:",max_length=50,primary_key=True)
    desc=models.TextField("Description:")
    def __str__(self):
        return self.riskseverity_desc


class mod9001_providerassessment(models.Model):
    emp_perfrev_no=models.CharField("Performance Review No.:",max_length=200,default="Comp-EA-Q-"+car_no(),primary_key=True)
    planner_number=models.ForeignKey(mod9001_qmsplanner, on_delete=models.CASCADE,verbose_name='QMS planner number:',null=True,blank=True)
   
    date=models.DateTimeField("Date:",null=True)
    provider=(('1','External provider'),('2','Internal provider'))
    Provider=models.CharField("Provider Type",max_length=200, choices=provider)
    organisation=models.ForeignKey(mod9001_supplieregistration, on_delete=models.CASCADE,verbose_name='External Provider Organisation:',related_name='suppliers',null=True,blank=True)
    assesment_date=models.DateField("Last Assessment Date:",null=True)
    start=models.DateField("Start Date:")
    end=models.DateField("End Date:")
    appraise= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Appraisee:(Internal Provider)',related_name='appraise',null=True,blank=True)
    appraiseename=models.CharField("Appraisee Name:(External Provider)",max_length=25,null=True,blank=True)

    #year_in_school = models.CharField(max_length=10,choices='mod9001_supplieregistration.name',verbose_name='Test:')   
    #purpose=models.TextField("Purpose",null=True, blank=True)
    #owner= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Owner:',related_name='own')
    jobknowledge=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='1.Response Time:',related_name='jobknowledg',null=True,blank=True)
    adaptability=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='2.Resolution Time:',related_name='adaptabilit',null=True,blank=True)
    problemsolve=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='3.Quality:',related_name='problemsolve',null=True,blank=True)
    initiativeness=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='4.Technical/Product Expertise:',related_name='initiative',null=True,blank=True)
    planning=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='5.Returns/Rejects:',related_name='plannin',null=True,blank=True)
    work=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='6.Delivery Rating:',related_name='problemsolv',null=True,blank=True)
    
   # skills=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='7.	Interpersonal Skills:',related_name='skill',null=True,blank=True)
    Communication=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='7.Complaints:',related_name='communicatin',null=True,blank=True)
    supervision=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='8.Pricing:',related_name='supervisio',null=True,blank=True)
    #availability=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='9.	Availability:',related_name='availabilit',null=True,blank=True)
    #professionalism=models.ForeignKey(providerparameters, on_delete=models.CASCADE,verbose_name='11. Professional Contribution:',related_name='professionalis',null=True,blank=True)
    rank=models.CharField("Final Ranking: (Scores 1 to 8 are required)",max_length=25,null=True,blank=True)
    comment=models.TextField("Comment",null=True, blank=True)
    #nonconformity=(('1','Support/Resource'),('2','Planning'),('3','IITS(Information, Instructions, Training, Supervision)'),('4','Performance monitoring'),('5','Evaluation'),('6','Risk/Vulnerability Assessment'),('7','Leadership'),('8','Other'))
    #nonconformity=models.CharField("Reason: cause of nonconformity",max_length=200, choices=nonconformity,null=True,blank=True)
    jobknowledg=(('1','Technical/Professional skills required'),('2','Application'),('3','Support and training'))
    jobknowledg = MultiSelectField('1.Knowledge/Expertise',choices=jobknowledg,null=True,blank=True)

    flexibility=(('1','Relaibility'),('2','Response to Change'))
    flexibility = MultiSelectField('2. Adaptability & Flexibility',choices=flexibility,null=True,blank=True)

    problemsolving=(('1','Response promptness'),('2','Level of Judgement'),('3','Solution Quality'))
    problemsolving = MultiSelectField('3. Problem solving',choices=problemsolving,null=True,blank=True)

    Initiativenes=(('1','Idea Development'),('2','Effective use of resources'))
    Initiativenes = MultiSelectField('4. Initiativeness & Resourcefulness',choices=Initiativenes,null=True,blank=True)

    planing=(('1','Establishing Priorities'),('2','Meeting Deadlines'),('3','Planning of Tasks'))
    planing = MultiSelectField('5. Planning & Organisation',choices=planing,null=True,blank=True)

    workqualit=(('1','Meeting Company Objectives'),('2','Task Completeness'),('3','Accuracy'))
    workquality = MultiSelectField('6. Work Quality & Quantity',choices=workqualit,null=True,blank=True)

    #skill=(('1','Relationship with Co-workers'),('2','Clients or Team spirit and general work attitude'))
    #interskills = MultiSelectField('7. Interpersonal Skills',choices=skill,null=True,blank=True)

    communication=(('1','Oral and Written'),('2','Clarity of Information shared'),('3','Accuracy of Information shared'))
    communication = MultiSelectField('7. Communication',choices=communication,null=True,blank=True)

    supervisionm=(('1','Work/task scheduling'),('2','Self-Supervision'))
    supervisionmagt = MultiSelectField('8. Supervision & Management',choices=supervisionm,null=True,blank=True)

    availabilit=(('1','Time keeping'),('2','Commitment'))
    availabilit = MultiSelectField('9. Availability',choices=availabilit,null=True,blank=True)

    #professional=(('1','Attendance of Professional Meetings'),('2','Provision of Professional education/talks'))
    #professional = MultiSelectField('11. Professional Contribution',choices=professional,null=True,blank=True)
 
    nonconfdetails=models.TextField("Additional description",null=True, blank=True)

    costs=(('1','Financial'),('2','Operational'),('3','Legal/Regulatory'),('4','Brand/Reputation'))
    cost = MultiSelectField('Cost',choices=costs,null=True,blank=True)
    currency=(('1','UGX'),('2','USD'),('3','Kshs'),('4','GBP'))
    currency=models.CharField(verbose_name='Currency:',max_length=50, null=True,blank=True,choices=currency)
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.CASCADE,verbose_name='Status:',null=True,blank=True)
 
    
    costdescription=models.IntegerField("Cost Amount:",null=True,blank=True)

    lesson=models.TextField("Lesson learnt:",null=True, blank=True)
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.CASCADE,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
     
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.CASCADE,null=True,verbose_name='Verification Status:')
    
    completion=models.DateField("Completion Date:",null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
   
    assigned= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Assessor:',null=True,blank=True)
  
    due=models.DateField("When:",null=True,blank=True)

    entered_by= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='providerentered',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)
class car_source(models.Model):

    description=models.CharField("CAR Source:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
    
class element(models.Model):

    description=models.CharField("Element:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description

class containment(models.Model):

    description=models.CharField("Containment Action:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class root_cause(models.Model):

    description=models.CharField("Root Cause Analysis:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class decision(models.Model):

    description=models.CharField("Decision or Action plan:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description



##########################CORRECTIVE ACTION #############################################################

class mod9001_correctiveaction(models.Model):
    car_no=models.CharField("CAR No.:",max_length=200,default="Comp-CAR-Q-"+ correction_no(),primary_key=True)
    date=models.DateField("CAR Date:",null=True)
    process=models.ForeignKey('process', on_delete=models.CASCADE,verbose_name='Process:',null=True,blank=True)
    car_source=models.ForeignKey('car_source', on_delete=models.CASCADE,verbose_name='CAR source:',null=True,blank=True)
    element=models.ForeignKey('element', on_delete=models.CASCADE,verbose_name='Element:',null=True,blank=True)
    reference=models.TextField("Reference",null=True, blank=True)      
    findings=(('1','Non Conformity'),('2','Observation'))
    finding=models.CharField("Finding",max_length=200, choices=findings)
    addesc=models.TextField("Additional Description",null=True, blank=True)
    requesto= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Request to:',null=True,blank=True)
    entered_by= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='correctiveactionentered',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    car_flag=models.TextField("CAR planning Done?",null=True,blank=True,default='No', help_text='To be uses while filtering CARs pending planning')
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)      
    
    
    def __str__(self):
        return self.car_no

class mod9001_planning(models.Model):
    #car_no=models.OneToOneField('mod9001_correctiveaction', on_delete=models.CASCADE,verbose_name='CAR ID:',null=True,blank=True)
    car_no=models.OneToOneField('mod9001_correctiveaction', on_delete=models.CASCADE,verbose_name='CarNo:',null=True,blank=True)
    containment=models.ForeignKey('containment', on_delete=models.CASCADE,verbose_name='containment:',null=True,blank=True)
    rootcause=models.ForeignKey('root_cause', on_delete=models.CASCADE,verbose_name='rootcause:',null=True,blank=True)
    rootcause_desc=models.TextField("Root Cause Description",null=True, blank=True)
    decision=models.ForeignKey('decision', on_delete=models.CASCADE,verbose_name='decision:',null=True,blank=True)
    details=models.TextField("Additional Details",null=True, blank=True)   
    proposedby= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Proposed by:',related_name='proposed_to',null=True,blank=True)
    proposedby_user_id= models.CharField("ProposedBy Sytem UserID.:", max_length=20, null=True, blank=True) 
    
    assignedto= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Assigned to:',related_name='asigned_to',null=True,blank=True)
    due=models.DateTimeField("When:",null=True)
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.CASCADE,verbose_name='Status:',null=True,blank=True)
    rejected=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    approval_date=models.DateField("Date Approved:",null=True,blank=True)
    approved_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='Approved_by',on_delete=models.CASCADE)
    entered_by= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True, related_name='planningentered',on_delete=models.CASCADE)
    date_today=models.DateField("Date created:",default=datetime.now)
    verification=models.ForeignKey('accounts.carsverification', on_delete=models.CASCADE,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True)
    planner_user_id= models.CharField("Planner Sytem UserID.:", max_length=20, null=True, blank=True)       
    planner_user_title= models.CharField("Planner Title.:", max_length=20, null=True, blank=True)    
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.CASCADE,null=True,verbose_name='Verification Status:')
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)    
    completion=models.DateField("Completion Date:",null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    comment=models.TextField("Comment:",null=True,blank=True, help_text='')
    def __str__(self):
        return self.car_no
          
################CHANGE REQUEST #########################
class change_type(models.Model):

    description=models.CharField("Change type:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class change_type_desc(models.Model):

    description=models.CharField("Change type details:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class changeRequest_reason(models.Model):

    description=models.CharField("Reason:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
class evaluation(models.Model):

    description=models.CharField("Evaluation:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description


class mod9001_changeRegister(models.Model):
    req_no=models.CharField("Request No.:",max_length=200,default="Comp-RFC-Q-"+ correction_no(),primary_key=True)
    date=models.DateField("Date:",null=True)    
    raisedby= models.ForeignKey('accounts.employees',on_delete=models.CASCADE,verbose_name='Raised by:',related_name='raised_by',null=True,blank=True)  
    raisedby_user_id= models.CharField("RaisedBy Sytem UserID.:", max_length=20, null=True, blank=True)    
    trigger=models.ForeignKey('car_source', on_delete=models.CASCADE,verbose_name='Source:',null=True,blank=True)
    reference=models.TextField("Reference",null=True, blank=True)      
    process=models.ForeignKey('process', on_delete=models.CASCADE,verbose_name='Process:',null=True,blank=True)
    changetype=models.ForeignKey('change_type', on_delete=models.CASCADE,verbose_name='Change Type:',null=True,blank=True)
    changetype_desc=models.ForeignKey('change_type_desc', on_delete=models.SET_NULL,verbose_name='Change Type Desc:',null=True,blank=True)
    
    changedesc=models.TextField("Additional Description",null=True, blank=True)    
    #evaluation=models.ForeignKey('evaluation', on_delete=models.SET_NULL,verbose_name='evaluation:',null=True,blank=True)
    Evaluation=(('1','Change affects existing products or services'),('2','Change absolutely necessary'),('3','Change impacts existing documents'),('4','Personnel training/re-training required'))
    evaluation = MultiSelectField('Evaluation',choices=Evaluation,null=True,blank=True)
    evaldesc=models.TextField("Additional Description",null=True, blank=True) 
    costs=(('1','Financial'),('2','Operational'),('3','Legal/Regulatory'),('4','Brand/Reputation'),('5','Product/Service'),('6','Customer Satisfaction'))
    cost = MultiSelectField('Risks or Business Impacts',choices=costs,null=True,blank=True)
    costdesc=models.TextField("Risks/Business Impacts Details",null=True, blank=True) 
    
    
    
    currency=(('1','UGX'),('2','USD'),('3','Kshs'),('4','GBP'))
    currency=models.CharField(verbose_name='Currency:',max_length=50, null=True,blank=True,choices=currency)
    costdescription=models.IntegerField("Cost Amount:",null=True,blank=True)
    reason=models.ForeignKey('changeRequest_reason', on_delete=models.SET_NULL,verbose_name='Change Request Reason:',null=True,blank=True)
    reason_details=models.TextField("Details",null=True, blank=True)       
    
    add_desc=models.TextField("Details",null=True, blank=True)    
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.SET_NULL,verbose_name='Status:',null=True,blank=True)
 
    rejected=models.TextField("Reason for rejecting:",null=True,blank=True, help_text='If rejected, please give a reason')
    approval_date=models.DateField("Date Approved:",null=True,blank=True)
    approved_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.SET_NULL, related_name='Approved_by2')
    entered_by= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.SET_NULL, related_name='enter_by')
    date_today=models.DateField("Date created:",default=datetime.now)
    verification=models.ForeignKey('accounts.carsverification', on_delete=models.SET_NULL,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True)
  
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.SET_NULL,null=True,verbose_name='Verification Status:')
    
    completion=models.DateField("Completion Date:",null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True) 

    proposedby= models.ForeignKey('accounts.employees',on_delete=models.SET_NULL,verbose_name='Proposed by:',related_name='proposed',null=True,blank=True)
    assignedto= models.ForeignKey('accounts.employees',on_delete=models.SET_NULL,verbose_name='Assigned to:',related_name='asigned',null=True,blank=True)
    due=models.DateTimeField("Due Date:",null=True)    
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)   

######################CUSTOMER COMPLAINT########################
class complaint_type(models.Model):

    description=models.CharField("Complaint Type:", max_length=50,null=True,blank=True)
    def __str__(self):
        return self.description
class mod9001_customerComplaint(models.Model):
    comp_no=models.CharField("Complaint No.:",max_length=200,default="Comp-COMP-Q-"+ correction_no(),primary_key=True)
    date=models.DateField("Date:",default=datetime.now,null=False)
    time=models.TimeField("Time (24Hr):",null=True)
    complaint=models.TextField("Complainant:",null=True, blank=True)   
    organisation=models.ForeignKey('accounts.customer', on_delete=models.SET_NULL,verbose_name='Customer Organisation:',related_name='org',null=True,blank=True)
    process=models.ForeignKey('process', on_delete=models.SET_NULL,verbose_name='Process:',null=True,blank=True)    
    type=models.ForeignKey('complaint_type', on_delete=models.SET_NULL,verbose_name='Complaint Type:',null=True,blank=True) 
    complaint_desc=models.TextField("Complaint Description",null=True, blank=True)
    reoccurance=(('1','Yes'),('2','No'))
    re_occurance=models.CharField(verbose_name='Re-Occurance:',max_length=50, null=True,blank=True,choices=reoccurance)
    classification=models.ForeignKey('classification', on_delete=models.SET_NULL,verbose_name='Complaint Classification:',null=True,blank=True)
    correction=models.ForeignKey('correction', on_delete=models.SET_NULL,verbose_name='Correction/Containment:',null=True,blank=True)
    add_desc=models.TextField("Additional Description",null=True, blank=True)       
    assignedto= models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,verbose_name='Assigned to:',null=True,blank=True)
    completedby= models.ForeignKey('accounts.employees',on_delete=models.SET_NULL,verbose_name='Completed by:',null=True,blank=True)
    
    due=models.DateField("When:",null=True)    
    entered_by= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.SET_NULL, related_name='entered')
    date_today=models.DateField("Date created:",default=datetime.now)
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.SET_NULL,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True)
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.SET_NULL,null=True,verbose_name='Verification Status:')
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.SET_NULL,verbose_name='Status:',null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    completion=models.DateField("Completion Date:",null=True,blank=True)
    analysis_flag=models.TextField("Complaint Analysis Done?",null=True,blank=True,default='No', help_text='To be uses while filtering complaints pending analysis')
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)    
    document = models.FileField("Upload Support Document:",upload_to='documents/',null=True,blank=True,validators=[validate_file_size_verification])
    uploaded_at = models.DateTimeField(auto_now_add=True,null=True)  
   

class mod9001_customerSatisfaction(models.Model):
    satis_no=models.CharField("Satisfaction Survey No.:",max_length=200,default="Comp-CS-Q-"+ correction_no(),primary_key=True)
    date=models.DateField("Date created:",default=datetime.now,null=False)
    organisation=models.ForeignKey('accounts.customer', on_delete=models.SET_NULL,verbose_name='Customer Organisation:',null=True,blank=True)
    #year=models.DateField("Survey Period:",null=True)
    start=models.DateField("Start Date:",null=True, blank=True)
    end=models.DateField("End Date:",null=True, blank=True)
    responsetime=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='1. Time Management:',related_name='resptime',null=True,blank=True)
    resolution=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='2. Knowledge of the products:',related_name='resotime',null=True,blank=True)
    delivery=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='3. Complaint Handling/ Resolution:',related_name='delivtime',null=True,blank=True)
    communication=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='4. Response to support:',related_name='comm',null=True,blank=True)
    compliant=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='5. Service Reporting:',related_name='handlin',null=True,blank=True)
    quality=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='6. Professionalism:',related_name='serv',null=True,blank=True)
    
    infosecurity=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='7. Overall quality of our products/ services:',related_name='securit',null=True,blank=True)
    #customerservice=models.ForeignKey(providerparameters, on_delete=models.SET_NULL,verbose_name='8. Customer Services:',related_name='cus',null=True,blank=True)
   
    rank=models.CharField("Final Rating:(Scores 1 to 7 are required)",max_length=25,null=True,blank=True)
    rankdesc_survey=models.CharField("",max_length=25,null=True,blank=True)

    comment=models.TextField("Comment",null=False, blank=False)
      
    improvement=(('1','Time Management'),('2','Knowledge of the products'),('3','Complaint Handling/ Resolution'),('4','Response to support'),('5','Service Reporting'),('6','Professionalism'),('7','Overall quality of our products/ services'),('8','Other'))
    improvplan = MultiSelectField('Improvement Plan',choices=improvement,null=True,blank=True) 
    details=models.TextField("Additional Details",null=True, blank=True)   
    assignedto= models.ForeignKey('accounts.employees',on_delete=models.SET_NULL,verbose_name='Assigned to:',null=True,blank=True)
    due=models.DateField("When:",null=True)    
    entered_by= models.ForeignKey(settings.AUTH_USER_MODEL,null=True, blank=True,on_delete=models.SET_NULL, related_name='ente')
    date_today=models.DateField("Date created:",default=datetime.now)
 
    verification=models.ForeignKey('issues_9001.RISK_OPPverification', on_delete=models.SET_NULL,verbose_name='Verification:',null=True,blank=True)
    verification_status=models.CharField(max_length=200, null=True,blank=True)
    verification_failed=models.TextField("Reason for rejecting:",null=True,blank=True)
    qmsstatus=models.ForeignKey(qmsstatus, on_delete=models.SET_NULL,null=True,verbose_name='Verification Status:')
    status=models.ForeignKey('issues_9001.approval_status', on_delete=models.SET_NULL,verbose_name='Status:',null=True,blank=True)
    scheduled=models.DateField("Rescheduled Date:",null=True,blank=True)
    completion=models.DateField("Completion Date:",null=True,blank=True)
    record_group=models.CharField("Data Group",max_length=20,null=True,blank=True)  
   







    












   
    
    
    
















