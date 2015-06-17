from django.views import generic
from django.shortcuts import redirect
from django.conf import settings
from django.core.urlresolvers import reverse_lazy

from .forms import ArticleCreateForm
from .models import Article


class ArticleListView(generic.ListView):

    template_model = 'blog/article_list.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 3
    ordering = '-create_at'


class ArticleDetailView(generic.DetailView):

    template_model = 'blog/article_detail.html'
    model = Article
    context_object_name = 'article'


class ArticleCreateView(generic.CreateView):

    template_model = 'blog/article_form.html'
    model = Article
    form_class = ArticleCreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.add_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Crear articulo'
        context['nombre_btn'] = 'Crear'
        # devolvemos el contexto
        return context

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(generic.UpdateView):

    template_model = 'blog/article_form.html'
    model = Article
    form_class = ArticleCreateForm

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.change_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto de la clase base
        context = super().get_context_data(**kwargs)
        # añadimos nuevas variables de contexto al diccionario
        context['title'] = 'Editar articulo'
        context['nombre_btn'] = 'Editar'
        # devolvemos el contexto
        return context


class ArticleDeleteView(generic.DeleteView):

    template_name = 'blog/confirmar_eliminacion.html'
    success_url = reverse_lazy('blog.article_list')
    model = Article

    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perms('blog.delete_article'):
            return redirect(settings.LOGIN_URL)
        return super().dispatch(request, *args, **kwargs)
