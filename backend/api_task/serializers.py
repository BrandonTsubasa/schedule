from rest_framework import serializers
from core.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('task_id', 'task_name', 'user_name', 'status',
                  'priority', 'created_date', 'start_date', 'end_date')
        read_only_fields = ('task_id',)
