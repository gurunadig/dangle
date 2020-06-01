from django.db import models



class Profile(models.Model):
    # user = models.OneToOneField(user, null=True, on_delete=models.CASCADE) 
    dob = models.DateField(max_length=8)    
    clocation = models.CharField(max_length=30)
    qualification = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    university = models.CharField(max_length=30)
    College = models.CharField(max_length=30)
    course_type = models.CharField(max_length=30)
    passing_year = models.CharField(max_length=30)
    experience = models.CharField(max_length=30)
    cctc = models.CharField(max_length=30)
    ectc = models.CharField(max_length=30)
    industry = models.CharField(max_length=30)
    skills = models.CharField(max_length=30)
    job_category = models.CharField(max_length=30)
    job_type = models.CharField(max_length=30)
	
def __str__(self):
	return self.dob


class Job(models.Model):
	
	job_title = models.CharField(max_length=30)
	job_description = models.CharField(max_length=30)
	job_location = models.CharField(max_length=30)
	company_name = models.CharField(max_length=30)
	Designation = models.CharField(max_length=30)
	qualification = models.CharField(max_length=30)
	course = models.CharField(max_length=30)
	specialization = models.CharField(max_length=30)
	course_type = models.CharField(max_length=30)
	passing_year = models.CharField(max_length=30)
	experience = models.CharField(max_length=30)
	salary = models.CharField(max_length=30)
	industry = models.CharField(max_length=30)
	skills = models.CharField(max_length=30)
	job_category = models.CharField(max_length=30)
	job_type = models.CharField(max_length=30)
	# apply = models.ManyToManyField(Account, related_name='applyjob')
	
	def __str__(self):
		return self.job_title