from django.db import models


class TodoList(models.Model):
   name = models.CharField(max_length=100, null=False)

   def __str__(self):
        return "%s" % (self.name)


class Todo(models.Model):
   name = models.CharField(max_length=100, null=False)
   checked = models.BooleanField(default=False, null=False)
   todo_list = models.ForeignKey(TodoList,
                                 related_name='todos',
                                 on_delete=models.CASCADE)
   def __str__(self):
        return "%s %s" % (self.name, self.checked)