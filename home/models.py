import uuid
from Profile.models import CustomUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at  = models.DateTimeField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True, null=True)

    class Meta:
        abstract = True

class Instructer(BaseModel):
    instructer_name = models.CharField(max_length=199, blank=False, null=False, default="")
    instructer_profile = models.ImageField(upload_to="instructers", blank=False, null=False)
    instructer_about = models.TextField(default="")

    def __str__(self) -> str:
        return str(self.instructer_name)
    
    class Meta:
        verbose_name = "Instructer's"

class CourseCategory(BaseModel):
    name = models.CharField(max_length=199, null=True, blank=True, default="")

    def __str__(self) -> str:
        return str(self.name)
    
    class Meta:
        verbose_name = "Course Categorie's"

class Courses(BaseModel):
    course_banner = models.ImageField(upload_to="courses", blank=False, null=False)
    course_title = models.CharField(max_length=299, default="unspecified", blank=False, null=False)
    rating = models.FloatField(blank=True, null=True, max_length=3, default=0.0)
    course_taglines = ArrayField(models.TextField(default="", null=False), blank=False)
    course_overview = models.TextField(default="", null=False)
    benifits = ArrayField(models.TextField(default="", null=False), blank=False)
    pricing = models.DecimalField(blank=False, default=0.0, max_digits=5, decimal_places=2)
    currencies = (('inr','INR'),('usd','USD'))
    base_currency = models.CharField(choices=currencies, blank=False, default="None", max_length=3)
    teacher = models.ManyToManyField(Instructer, default="", related_name="instructors", blank=False)
    category = models.ForeignKey(CourseCategory, blank=False, null=False, default="", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.course_title)
    
    class Meta:
        verbose_name = "Courses Information"

class CourseIncludes(BaseModel):
    title = models.CharField(max_length=299, default="", null=False, blank=False)
    icons = (
        ('play_circle','Play Circle'),
        ('newspaper','Newspaper'),
        ('cloud_download','Cloud Download'),
        ('all_inclusive','Infinity Logo'),
        ('devices','Devices'),
        ('edit_document','Edit Documents'),
        ('emoji_events','Emoji Events')
        )
    icon = models.CharField(max_length=49, null=True, blank=True, default="", choices=icons)
    connected_course = models.ForeignKey(Courses, blank=False, null=False, default="", on_delete=models.CASCADE,related_name="included")
    
    def __str__(self) -> str:
        return str(self.title)
    
    class Meta:
        verbose_name = "Course Include's"

class HomeModel(BaseModel):
    company_logo = models.ImageField(upload_to="company", blank=True, null=True)
    company_banner = models.ImageField(upload_to="company", blank=True, null=True)
    home_head = models.CharField(max_length=499, default="", blank=False, null=False)
    home_about = models.TextField(default="", null=False)
    showcase = models.ManyToManyField(Courses, blank=False, default="", related_name="showcased_courses")

    def __str__(self) -> str:
        return str(self.home_head)
    
    class Meta:
        verbose_name = "Home Page Data"

class Blog(BaseModel):
    title = models.CharField(max_length=299, default="", blank=False, null=False)
    description = models.TextField(default="")
    banner = models.ImageField(upload_to="blogs", blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)
    
    class Meta:
        verbose_name = "Blog's"
