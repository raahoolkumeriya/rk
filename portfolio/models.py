# -*- coding: utf-8 -*-
from django.db import models
import datetime
import readtime
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Projects(models.Model):
    """
    Project model
    """
    CATEGORY_CHOICES = (
        ('Web Apps', 'Web Apps'),
        ('Machine Learning', 'Machine Learning'),
        ('APIs', 'APIs'),
        ('Command Line Applications', 'Command Line Applications'),
        ('Data Visualization', 'Data Visualization'),
        ('Graphical User Interfaces', 'Graphical User Interfaces'),
        ('Artificial Intelligence', 'Artificial Intelligence'),
        ('DevOps', 'DevOps'),
        ('Data Science', 'Data Science'),
        ('Other', 'Other'),
    )
    title = models.CharField(max_length=255)
    summary = models.TextField(max_length=1000, blank=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    category = models.CharField(
        max_length=50, choices=CATEGORY_CHOICES,
        default='Other')
    urllink = models.URLField(max_length=255)
    startdate = models.DateField()
    enddate = models.DateField(blank=True, null=True)
    technology = models.CharField(max_length=255)
    sourcecode = models.URLField(max_length=255)
    description = RichTextField()
    image = models.URLField(max_length=500, blank=True, null=True)
    publish = models.BooleanField(default=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Projects, self).save(*args, **kwargs)

    def get_readtime(self):
        result = readtime.of_text(self.description)
        return result.text

    class Meta:
        verbose_name = "Project Entry"
        verbose_name_plural = "Project Entries"
        ordering = ["category", "-pub_date"]


class AwardsAndAchievements(models.Model):
    """
    Award and Achievements
    """
    title = models.CharField(max_length=255)
    received = models.DateField()

    def __str__(self):
        return self.title

    def get_formated_date(self):
        """
        Returns the date in the format of 'Month Year'
        """
        return self.received.strftime('%B %Y')

    class Meta:
        verbose_name = "Award and Achievement Entry"
        verbose_name_plural = "Award and Achievement Entries"


class Notes(models.Model):
    """
    Notes are stored in the database as a text field.
    """
    note = models.CharField(max_length=255)
    description = RichTextField()
    tags = models.CharField(max_length=255, blank=True)
    gisturl = models.URLField(max_length=255)

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = "Note Entry"
        verbose_name_plural = "Note Entries"


class Summary(models.Model):
    """
    Summary is a single line of text that summarizes the projects.
    """
    summary = RichTextField()
    summary_image = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.summary

    class Meta:
        verbose_name = "Summary Entry"
        verbose_name_plural = "Summary Entries"


class Experience(models.Model):
    """
    Experience details.
    """
    title = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    experience = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Experience Entry"
        verbose_name_plural = "Experience Entries"


class Contact(models.Model):
    """
    Contact is a single line of text that summarizes the projects.
    """
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message_date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    def __str__(self):
        return self.email