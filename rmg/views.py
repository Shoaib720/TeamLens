from django.shortcuts import render, redirect, get_object_or_404
from .models import ProfileUpdate, ProfileUpdateHistory
from .forms import ResourceForm

# Create your views here.
def index(request):
    updates = ProfileUpdate.objects.filter(
        marked_deleted=False
    ).exclude(
        status__in=['Fulfilled', 'Inactivated']
    ).order_by('-updated_at')
    instance = None
    
    if request.method == 'POST':
        update_id = request.POST.get('id')  # Hidden field from the form
        if update_id:
            instance = get_object_or_404(ProfileUpdate, pk=update_id)
            form = ResourceForm(request.POST, instance=instance)
        else:
            form = ResourceForm(request.POST)

        if form.is_valid():
            saved_instance = form.save()
            print(saved_instance)
            ProfileUpdateHistory.objects.create(
                resource=saved_instance,
                cv_name=saved_instance.cv_name,
                requirement_name=saved_instance.requirement_name,
                status=saved_instance.status,
                comments=saved_instance.comments,
                change_type='update' if update_id else 'create'
            )
            return redirect('index')
    else:
        update_id = request.GET.get('edit')  # when edit link is clicked
        if update_id:
            instance = get_object_or_404(ProfileUpdate, pk=update_id)
            form = ResourceForm(instance=instance)
        else:
            form = ResourceForm()
            
    return render(request, 'rmg/index.html', {
        'form': form,
        'updates': updates,
        'editing': instance is not None,
        'editing_id': instance.id if instance else '',
    })

def edit_profile_allocation(request, pk):
    update = ProfileUpdate.objects.get(pk=pk)
    form = ResourceForm(instance=update)

    if request.method == 'POST':
        form = ResourceForm(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'rmg/edit.html', {'form': form, 'update': update})

def delete_profile_allocation(request, pk):
    update = get_object_or_404(ProfileUpdate, pk=pk)
    update.marked_deleted = True
    update.save()
    ProfileUpdateHistory.objects.create(
        resource=update,
        cv_name=update.cv_name,
        requirement_name=update.requirement_name,
        status=update.status,
        comments=update.comments,
        change_type='delete'  # Still considered an update
    )
    return redirect('index')