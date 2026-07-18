from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Commission, Artwork
from .forms import CommissionForm
from .serializers import ArtworkSerializer, CommissionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def home(request):
    all_commissions = Commission.objects.all()
    pending = Commission.objects.filter(status='pending')
    pending_CA = Commission.objects.filter(status='pending', priority='CA')
    active = Commission.objects.exclude(status='cancelled')
    top_priority = Commission.objects.filter(
        status='pending'
    ).exclude(
        priority='CA'
    ).order_by('-created_at')
    first_five = Commission.objects.all()[:5]
    names_only = Commission.objects.values('name', 'email', 'status')
    has_pending = Commission.objects.filter(status='pending').exists()
    total = Commission.objects.count()

    context = {
        'all_commissions': all_commissions,
        'pending': pending,
        'pending_CA': pending_CA,
        'active': active,
        'top_priority': top_priority,
        'first_five': first_five,
        'names_only': names_only,
        'has_pending': has_pending,
        'total': total,
    }
    return render(request, 'studio/home.html', context)

def commission_detail(request, id):
    commission = get_object_or_404(Commission, id=id)
    context = {'commission': commission}
    return render(request, 'studio/commission_detail.html', context)

def submit_commission(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CommissionForm()
    context = {'form': form}
    return render(request, 'studio/submit_commission.html', context)

def success(request):
    return render(request, 'studio/success.html')


# ============ API VIEWS ============

@api_view(['GET'])
def api_artworks(request):
    artworks = Artwork.objects.filter(status='available')
    serializer = ArtworkSerializer(artworks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_artwork_detail(request, id):
    artwork = get_object_or_404(Artwork, id=id)
    serializer = ArtworkSerializer(artwork)
    return Response(serializer.data)

@csrf_exempt
@api_view(['POST'])
def api_submit_commission(request):
    serializer = CommissionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {'message': 'Commission submitted successfully'},
            status=status.HTTP_201_CREATED
        )
    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )