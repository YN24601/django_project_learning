from django.shortcuts import render
# from django.urls import reverse, reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.models import Teacher
from classroom.forms import ContactForm

'''
# Create your views here.
def home_view(request):
    return render(request, 'classroom/home.html')
'''

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
# create a new instance
    model = Teacher
    # fields = ['name', 'subject']
    fields = '__all__'
    # by default, it will look for a template called teacher_form.html
    # template_name = 'classroom/teacher_form.html'

    # success_url = '/classroom/thank_you'
    success_url = '/classroom/list_teachers'
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherListView(ListView):
    model = Teacher
    # by default, it will look for a template called teacher_list.html
    # template_name = 'classroom/teacher_list.html'

    # queryset = Teacher.objects.all()
    queryset = Teacher.objects.order_by('name')

class TeacherDetailView(DetailView):
    model = Teacher
    # by default, it will look for a template called teacher_detail.html
    # PK --> {{teacher}}

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['subject']
    # by default, it will look for a template called teacher_form.html
    # which is same as CreateView
    # success_url = '/classroom/list_teachers'
    success_url = reverse_lazy('classroom:list_teachers')

class TeacherDeleteView(DeleteView):
    model = Teacher
    # by default, it will look for a template called teacher_confirm_delete.html
    # success_url = '/classroom/list_teachers'
    success_url = reverse_lazy('classroom:list_teachers')
    

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    
    # go to thank you page after form is submitted
    # it is a URL, NOT a template
    success_url = '/classroom/thank_you'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print(form.cleaned_data)
        return super().form_valid(form)
