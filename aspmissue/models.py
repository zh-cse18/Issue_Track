from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
class Supplier(models.Model):
    suppliername = models.CharField(max_length=200, null=True)
    pmname = models.CharField(max_length=200, null=True, blank=True)
    supplier_description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.suppliername


class ModelType(models.Model):
    typename = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.typename


class ModelName(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    modeltype = models.ForeignKey(ModelType, on_delete=models.CASCADE, null=True, blank=True)
    modelname = models.CharField(max_length=200)
    modeldescription = models.CharField(max_length=200, null=True)
    isFinished = models.BooleanField(default=False,blank=True,null=True)

    def __str__(self):
        return self.modelname


class SoftwareType(models.Model):
    softwaretype = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.softwaretype


class Software(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True)
    modelname = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True, blank=True)
    software_type = models.ForeignKey(SoftwareType, on_delete=models.CASCADE, null=True)
    software_name = models.CharField(max_length=200, null=True, blank=True)
    software_full_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.software_full_name

class MajorIssue(models.Model):
    modelname = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True, blank=True)
    total_issue = (
        ('Camera Blur', 'Camera Blur'),
        ('Camera Noise', 'Camera Noise'),
        ('Sound Noise', 'Sound Noise'),
        ('Sound Low Multimedia', 'Sound Low Multimedia'),
        ('Sound Echo', 'Sound Echo'),
        ('Phone Hang issue in normal use','phone hang issue in normal use'),
        ('Message layout not standard', 'message layout not standard'),
        ('Blacklist not working', 'blacklist not working'),
        ('Emergency number not working', 'emergency number not working'),
        ('Pocco launcher overlap issue', 'pocco launcher overlap issue'),
        ('Wallpaper  theme can’t change', 'wallpaper theme can’t change'),
        ('Call disconnecting', 'call disconnecting'),
        ('MMI code can not run', 'MMI code can’t run'),
        ('Loopback sound is broken', 'loopback sound is broken'),
        ('Earphone controller can work', 'Earphone controller can’t work'),
        ('Cantanct can’t sync', 'contact can’t sync'),
        ('VoLTE call  can’t support', 'VoLTE call can not support'),
        ('Display blinked', 'Display blinked'),
        ('Pattern can’t work', 'Pattern can’t work'),
        ('Proximity sensor can not work', 'proximity sensor can not work'),
        ('Sound mute', 'sound mute'),
        ('Gps can not work', 'Gps can not work'),
        ('GPS is not working in ride sharing', 'GPS is not working in ride sharing'),
        ('Metting application can’t connect on pc', 'metting application can’t connect on pc'),
        ('Front Camera Noise in Low Light', 'Front Camera Noise in Low Light'),
        ('Audio Low Voice call','Audio Low Voice call'),
        ('Call Drop','Call Drop'),
        ('Fingerprint not working','Fingerprint not working'),
        ('Bokeh Mode not working','Bokeh Mode not working'),
        ('Face unlock not working','Face unlock not working'),
        ('Anti theft, data protection missing', 'Anti theft, data protection missing'),
        ('Face unlock lacks / slow','Face unlock lacks / slow'),
        ('Cast screen is not working','Cast screen is not working'),
        ('High RAM consumption','High RAM consumption'),
        ('app close issue','app close issue'),
        ('default ringtone should Neon','default ringtone should Neon'),
        ('Three finger gesture screenshot not working','Three finger gesture screenshot not working'),
        ('Gesture Navigation not working','Gesture Navigation not working'),
        ('Wide-Angle mode not presence', 'Wide-Angle mode not presence'),
        ('Depth control not work accurately in Bokeh and portrait mode',
         'Depth control not work accurately in Bokeh and portrait mode'),
        ('Notch settings is missing in display', 'Notch settings is missing in display'),
        ('Sales tracker not found', 'Sales tracker not found'),
        ('Network Fluctuated','Network Fluctuated'),
        ('Screen pinning  is not working','screen pinning is not working'),
        ('Fingerprint unlock is not working',' Fingerprint unlock is not working'),
        ('Overheating Game','Overheating Game'),
        ('Camera HDR not working','Camera HDR not working'),
        ('Contact move/copy not working','Contact move/copy not working'),
        ('App Clone issue','App Clone issue'),
        ('Bluetooth connect issue', 'Bluetooth connect issue'),
        ('Alarm not working','Alarm not working'),
        ('Google service issue','Google service issue'),
        ('App fullscreen issue','App fullscreen issue'),
        ('Adaptive brightness issue','Adaptive brightness issue'),
        ('Dark theme switch issue','Dark theme switch issue'),
        ('Draw over apps issue','Draw over apps issue'),
        ('DND mode not work','DND mode not work'),
        ('Gesture navigation should set as default','Gesture navigation should set as default'),
        ('3rd party calling app sound clarity noisy','3rd party calling app  sound clarity noisy'),
        ('fingerprint response slow','fingerprint response slow'),
        ('face unlock response slow','face unlock response slow'),
        ('screen pinning missing','screen pinning missing'),
        ('split screen not working','split screen not working'),
        ('PIP mode not working','PIP mode not working'),
        ('smart control is not working properly','smart control is not working properly'),
        ('Gaming FPS dropping','Gaming FPS dropping'),
        ('Excessive heat generated while gaming','Excessive heat generated while gaming'),
        ('Device hang issue while gaming','Device hang issue while gaming'),
        ('Data connection  going null upon calling','Data connection  going null upon calling'),
        ('VOLTE calling issue', 'VOLTE calling issue'),
        ('device over hit on heavy usage','device over hit on heavy usage'),
        ('camera images lacks clarity and sharpness','camera images lacks clarity and sharpness'),
        ('swipe up problem','swipe up problem'),
        ('youtube playback screen freeze issue','youtube playback screen freeze issue'),
        ('Call recording sound is too low','Call recording sound is too low'),
        ('Hang issue in normal use','Hang issue in normal use'),
        ('Camera hang issue','Camera hang issue'),

    )

    issue =MultiSelectField(max_length=2000,choices=total_issue,blank=True,null=True)
    def __str__(self):
        return self.modelname.modelname

class IssueSummary(models.Model):
    model = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True)
    software = models.ForeignKey(Software, on_delete=models.CASCADE, null=True)
    issue_analysis_version_wise = models.CharField(max_length=200, null=True)
    total_issue = models.IntegerField(max_length=2000, null=True)
    expected_software_date = models.DateField(null=True, blank=True)
    pre_version_actual_software_date =  models.DateField(null=True)
    actual_software_date = models.DateField(null=True)
    feedback_expected_date = models.DateField(null=True)
    feedback_actual_date = models.DateField(null=True)
    new_issue = models.IntegerField(max_length=200, null=True)
    reopen_issue = models.IntegerField(max_length=200, null=True)
    is_mp = models.BooleanField(default=False)
    closed_issue = models.IntegerField(max_length=200, null=True)
    delay_team = (
        ('PM', 'PM'),
        ('QC', 'QC'),
        ('Supplier', 'Supplier'),
    )
    supplier_can_not_fixed = models.IntegerField(max_length=200, null=True, blank=True)
    issue_clsoed_by_pm = models.IntegerField(max_length=200, null=True, blank=True)
    delay = models.CharField(max_length=50, choices=delay_team, null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    delay_by_pm = models.CharField(max_length=200, null=True, blank=True)
    delay_by_qc = models.CharField(max_length=200, null=True, blank=True)	
    mejor_issue = models.ForeignKey(MajorIssue, on_delete=models.CASCADE, null=True, blank=True)
    diff_two_version = models.CharField(max_length=200, null=True, blank=True)


    def save(self, *args, **kwargs):
        if self.expected_software_date is not None:
            self.delay_by_pm = self.actual_software_date - self.expected_software_date
        elif self.expected_software_date is None:
            self.delay_by_pm = self.feedback_actual_date - self.actual_software_date
        if self.feedback_expected_date is not None:
            self.delay_by_qc = self.feedback_actual_date - self.feedback_expected_date
        self.diff_two_version = self.actual_software_date -self.pre_version_actual_software_date
        super(IssueSummary, self).save(*args, **kwargs)

    def __str__(self):
        return self.issue_analysis_version_wise

    issue_sum = IssueSummary.objects.all()
    print(issue_sum)


     
class IssueAnalysis(models.Model):
    model = models.ForeignKey(ModelName, on_delete=models.CASCADE, null=True)
    issue_name = models.CharField(max_length=200, null=True)
    imei = models.CharField(max_length=200, null=True)
    issue_source = models.CharField(max_length=200, null=True)
    problem = models.CharField(max_length=2000, null=True)
    qc_findings = models.TextField(null=True)
    hw_findings = models.TextField(null=True)
    root_cause = models.TextField(null=True, blank=True)
    evidence = models.FileField(upload_to='')
    posted_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.issue_name + " " + self.model.modelname


