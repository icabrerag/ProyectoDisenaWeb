from django.test import TestCase

# Create your tests here.
class mis_tests (unittest.TestCase):


    def plan_list(request, pk):
        plan = get_object_or_404(plan, pk=pk)
        return render(request, 'plan_list.html', {'plan': plan })