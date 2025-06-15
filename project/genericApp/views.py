from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from .models import Detail
from .forms import DetailForm
from django.contrib import messages

class IndexView(ListView):
    template_name='genericApp/index.html'
    context_object_name='data'
    
    def get_queryset(self):
        return Detail.objects.all()
    
    
class CreateData(CreateView):
    template_name='genericApp/form.html'
    model=Detail
    form_class=DetailForm
    success_url='/generic'
    
    def form_valid(self, form):
        age=form.cleaned_data.get('age')
        if age>100 or age<0:
            form.add_error('age',"age milana ni yar")
            return self.form_invalid(form)
        
        messages.success(self.request,'success')
        
        return super().form_valid(form)
    
class UpdateData(UpdateView):
    template_name='genericApp/form.html'
    model=Detail
    form_class=DetailForm
    success_url='/generic'
    
class DeleteData(DeleteView):
    model=Detail
    success_url='/generic'
    
    
print("kai data haleko xu la mail")
print(("sujan branch change"))

print("sujan ko ho la branch")