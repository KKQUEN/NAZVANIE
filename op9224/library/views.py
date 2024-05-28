from .models import Poem
from django.shortcuts import render, reverse
from django.views.generic import TemplateView, CreateView


class CreatePoem(CreateView):
    model = Poem  # Модель, экземпляр которой мы создаём
    fields = ['author', 'title', 'lyrics']  # Отображаемые поля
    template_name = "library/create_poem.html"  # путь до файла с разметкой

    def get_success_url(self):
        # функция, возвращающая url при успешном заполнении формы
        return reverse("home")


class HomeView(TemplateView):
    template_name = "library/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['poems'] = Poem.objects.all()
        return context
