from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


"""this handles the sprints which will have an optional name and description
and a unique end date."""

class Sprint(models.Model):

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end


"""this handles the tasks within a given sprint.
tasks have name, optional description, backlog, user assigned to each task,
      start date, end date, due date, and states like: not started,
      in progress, testing, and done."""

class Task(models.Model):

    TO_DO = 1
    IN_PROGRESS = 2
    TESTING = 3
    DONE = 4

    STATUS_CHOICES = (
        (TO_DO, _('Not Started')),
        (IN_PROGRESS, _('In Progress')),
        (TESTING, _('Testing')),
        (DONE, _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=TO_DO)
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)
    started = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
