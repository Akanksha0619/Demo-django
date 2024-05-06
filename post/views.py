
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from .forms import PostForm
from .models import *
from django.shortcuts import render, get_object_or_404
from .forms import FeedbackForm
from django.contrib.auth import authenticate

from .models import ContactMessage





# Create your views here.

def index(request):
    return render(request, 'index.html')
def home(request):
    context = {
        'posts': Job.objects.all()
    }
    return render(request, 'home.html', context)


class PostListView(ListView):
    model = Job
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Job
    template_name = 'post_detail.html'



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    form_class = PostForm  # Use the customized form
    template_name = 'post_update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Job
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # Redirect to the user's profile page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def posts_by_date(request, date):
    # Retrieve all posts uploaded on the given date
    posts = Job.objects.filter(date_posted__date=date)
    return render(request, 'posts_by_date.html', {'posts': posts, 'date': date})



def user_profile_and_posts(request, user_id):
    user = get_object_or_404(User, id=user_id)
    posts = Job.objects.filter(author=user)
    return render(request, 'user_profile_and_posts.html', {'user': user, 'posts': posts})



def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "Feedback submitted successfully!"
            form = FeedbackForm()  # Reset form for new feedback
    else:
        form = FeedbackForm()
        success_message = None

    return render(request, 'feedback_form.html', {'form': form, 'success_message': success_message})


def feedback_list(request):
    feedbacks = Feedback.objects.all()  # Fetch all feedback objects
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks})





def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact.html', {'contacts': contacts})



def preparation_view(request):
    return render(request, 'preparation.html')


def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        enrollment_number = request.POST.get('enrollment_number', '')
        branch = request.POST.get('branch', '')
        message = request.POST.get('message', '')

        # Create a new ContactMessage object and save it to the database
        ContactMessage.objects.create(
            name=name,
            enrollment_number=enrollment_number,
            branch=branch,
            message=message
        )

        # Render the same contact_form.html with a thank you message
        return render(request, 'contact_form.html', {'thank_you_message': 'Thank you! Your message has been submitted.'})

    return render(request, 'contact_form.html')




def message_list(request):
    messages = ContactMessage.objects.all()
    return render(request, 'message_list.html', {'messages': messages})


from .models import Job

from django.db.models import Q

def job_search(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        min_salary = request.POST.get('min_salary')
        max_salary = request.POST.get('max_salary')
        position = request.POST.get('position')
        skills = request.POST.get('skills')

        # Filtering jobs based on user preferences
        filtered_jobs = Job.objects.all()
        if location:
            filtered_jobs = filtered_jobs.filter(location=location)
        if min_salary:
            # Remove currency symbol and commas before converting to integer
            min_salary = int(min_salary.replace('₹', '').replace(',', ''))
            filtered_jobs = filtered_jobs.filter(salary__gte=min_salary)
        if max_salary:
            # Remove currency symbol and commas before converting to integer
            max_salary = int(max_salary.replace('₹', '').replace(',', ''))
            filtered_jobs = filtered_jobs.filter(salary__lte=max_salary)
        if position:
            filtered_jobs = filtered_jobs.filter(position=position)
        if skills:
            # Split skills into a list and create Q objects for each skill
            skill_list = skills.split(',')
            query = Q()
            for skill in skill_list:
                query |= Q(required_skills__icontains=skill.strip())
            filtered_jobs = filtered_jobs.filter(query)

        # Recommendation based on matching data
        if skills:
            recommended_jobs = Job.objects.filter(Q(required_skills__icontains=skills) |
                                                   Q(position__icontains=skills)).exclude(id__in=filtered_jobs)
        else:
            recommended_jobs = Job.objects.none()

        context = {'jobs': filtered_jobs, 'recommended_jobs': recommended_jobs}
        return render(request, 'job_search_results.html', context)

    return render(request, 'job_search.html')
