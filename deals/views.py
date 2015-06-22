from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Deal
from .forms import DealForm

class IndexView(generic.ListView):
    context_object_name = 'latest_deals_list'

    def get_queryset(self):
        return Deal.objects.order_by('-created_date')[:10]

class DetailView(generic.DetailView):
    model = Deal

def add_model(request):

    form = DealForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        deal = form.save()
        return HttpResponseRedirect(reverse('deals:detail', args=(deal.id,)));

    return render(request, "deals/deal_form.html", {'form': form, 'title': 'Add New Deal'})

def update_model(request, pk):

    deal = get_object_or_404(Deal, pk=pk)

    form = DealForm(request.POST or None, instance=deal)
    if form.is_valid():
        deal = form.save()
        return HttpResponseRedirect(reverse('deals:detail', args=(deal.id,)));

    return render(request, "deals/deal_form.html", {'form': form, 'title': 'Editing "' + deal.title + '"'})

def delete_model(request, pk):

    deal = get_object_or_404(Deal, pk=pk)

    if request.method == 'POST':
        deal.delete()
        return HttpResponseRedirect(reverse('deals:index'));

    return render(request, "deals/deal_confirm_delete.html", {'object': deal, 'title': 'Confirm deleting "' + deal.title + '"'})

def vote(request, pk):

    deal = get_object_or_404(Deal, pk=pk)

    if request.method == 'POST' and request.POST['vote']:
        if request.POST['vote'] == '1':
            deal.votes_up += 1
        if request.POST['vote'] == '0':
            deal.votes_down += 1
        deal.save()

    return HttpResponseRedirect(reverse('deals:detail', args=(deal.id,)));