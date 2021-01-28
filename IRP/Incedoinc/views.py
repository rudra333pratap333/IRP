from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Employee, Job, Candidate, Feedback #CandidateJobInfo

from datetime import datetime
# Create your views here.
def index(request):
    return HttpResponse('Welcome to Incedo Portal')

def search_candidate(request):
    return HttpResponseRedirect(reverse("feedback", args=(9,)))


def feedback(request, req_id):
    if request.method == "POST":
        comment = request.POST['description']
        #candidate_email = Candidate.objects.get()
        #candidate_email = Candidate.objects.get(emailId='rudra@gmail.com')
        #interviewer_code = Employee.objects.get(incedoCode=201201)
        #time_stamp = datetime.timestamp(datetime.now())

        candidate_email = request.POST['candidate_email']
        interviewer_code = request.POST['interviewer_code']
        #level_ = request.POST['level_']
        status_ = request.POST['status_']
        ratingPython_ = request.POST['ratingPython_']
        ratingJava_ = request.POST['ratingJava_']
        ratingCPP_ = request.POST['ratingCPP_']
        ratingSQL_ = request.POST['ratingSQL_']

        Feedback.objects.create(candidateEmail=Candidate.objects.get(emailId=candidate_email),
                                interviewerCode=Employee.objects.get(incedoCode=interviewer_code),
                                level=int(req_id)+1,
                                status=status_,
                                ratingPython=ratingPython_,
                                ratingJava=ratingJava_,
                                ratingCPP=ratingCPP_,
                                ratingSQL=ratingSQL_,
                                comments=comment,)
        return HttpResponseRedirect(reverse('test_name'))

    try:
        prv_feedback = Feedback.objects.get(level=req_id)
        print(prv_feedback)

    except Feedback.DoesNotExist:
        raise Http404('Feedback does not exist')


    context = {
        'feedback': prv_feedback,
        'candidate': Candidate.objects.get()
    }
    return render(request, 'registration/feedback.html', context)




    '''
    if request.method=='POST':
        comments = request.POST['description']
        return render(request, "registration/search_candidate.html") # redirect
    else:
        comtext = {
            'candiate': Candidate.objects.all(),
            'feedback':Feedback.objects.
        }
        return render(request, 'registration/feedback.html', req_id)
        '''

def test(request):
    return HttpResponse('inside the test')
