from django.db import models
from django.utils.text import slugify

class Banner(models.Model):
    PAGE_CHOICES = (
        ('HOME', 'Home Page'),
        ('ABOUT', 'About Page'),
        ('SERVICES', 'Services Page'),
        ('CONTACT', 'Contact Page'),
        ('INDUSTRIES', 'Industries Page'),
        ('CAREERS', 'Careers Page'),
        ('BLOG', 'Blog Page'),
    )
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='banners/')
    link = models.URLField(blank=True)
    active = models.BooleanField(default=True)
    page = models.CharField(max_length=20, choices=PAGE_CHOICES, default='HOME')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} ({self.get_page_display()})"

class ServiceCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    icon = models.ImageField(upload_to='services/', blank=True, null=True) # Or use a charfield for icon class
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Service Categories"
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Industry(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    icon = models.ImageField(upload_to='industries/icons/', blank=True, null=True)
    banner_image = models.ImageField(upload_to='industries/banners/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Industries"
        ordering = ['order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class IndustrySection(models.Model):
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='industries/sections/', blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.industry.name} - {self.title}"

class CareerJob(models.Model):
    JOB_TYPES = (
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
    )
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='Full-time')
    description = models.TextField()
    requirements = models.TextField()
    posted_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-posted_date']

    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/')
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class LeadershipMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='leadership/')
    linkedin_url = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Partner(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='partners/')
    website = models.URLField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class CompanyValue(models.Model):
    title = models.CharField(max_length=200)
    icon = models.ImageField(upload_to='values/', blank=True, null=True)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class VisionMission(models.Model):
    TYPES = (
        ('Vision', 'Vision'),
        ('Mission', 'Mission'),
    )
    type = models.CharField(max_length=20, choices=TYPES, unique=True)
    content = models.TextField()

    class Meta:
        verbose_name = "Vision & Mission"
        verbose_name_plural = "Vision & Mission"

    def __str__(self):
        return self.type

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    attachment = models.FileField(upload_to='contact_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Message from {self.name}"

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=200, default="KMATI")
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=50)
    address = models.TextField()
    facebook_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    def __str__(self):
        return "Site Configuration"
