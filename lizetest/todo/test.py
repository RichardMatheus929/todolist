from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import Task, Category, User

class DeleteTaskComplete(TestCase):
    def setUp(self):

        self.client = APIClient()

        self.user_teste = User.objects.create(
            username='Richard_teste',
            name='Richard'
        )
        self.category_teste = Category.objects.create(
            name="Categoria_teste",
            author=self.user_teste
        )
        self.task_teste_completed = Task.objects.create(
            title="Tesko",
            description="Task completa para testar a exclusão",
            category=self.category_teste,
            completed=True,
            author=self.user_teste
        )
        self.task_teste_incomplete = Task.objects.create(
            title="Tesko",
            description="Task completa para testar a exclusão",
            category=self.category_teste,
            completed=False,
            author=self.user_teste
        )

    def test_delete_completed_task(self):
        response = self.client.get(reverse('todo:task_delete', kwargs={'task_id': self.task_teste_completed.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sucess'], False)

    def test_delete_incomplete_task(self):
        response = self.client.get(reverse('todo:task_delete', kwargs={'task_id': self.task_teste_incomplete.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sucess'], True)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(id=self.task_teste_incomplete.id)

class CompleteTask(TestCase):
    def setUp(self):

        self.client = APIClient()

        self.user_teste = User.objects.create(
            username='Richard_teste',
            name='Richard'
        )
        self.category_teste = Category.objects.create(
            name="Categoria_teste",
            author=self.user_teste
        )
        self.task_teste = Task.objects.create(
            title="Tesko",
            description="Task completa para testar a exclusão",
            category=self.category_teste,
            completed=False,
            author=self.user_teste
        )

    def test_completar_task(self):
        self.assertEqual(self.task_teste.completed,False)
        self.client.get(reverse('todo:task_alter', kwargs={'task_id': self.task_teste.id}))
        is_complete = Task.objects.get(id=self.task_teste.id).completed
        self.assertEqual(is_complete,True)


        








