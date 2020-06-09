from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import HangSanXuat, HangHoa, BaiViet


def index(request):
    return HttpResponse('xin chao')


def handle_uploaded_file(f, tenfile):
    with open(tenfile, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class IndexView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        so_1 = request.POST.get('so1')
        so_2 = request.POST.get('so2')
        kq = int(so_1) + int(so_2)
        print()
        handle_uploaded_file(request.FILES['file1'], 'ten1.jpg')
        du_lieu = {
            'ketqua': kq
        }
        return render(request, 'index.html', du_lieu)


class TinhToanView(View):
    def get(self, request):
        so_1 = request.GET.get('so1')
        so_2 = request.GET.get('so2')
        kq = int(so_1) + int(so_2)
        ketqu = str(kq) + ' - theo kieu get'
        du_lieu = {
            'ketqua': ketqu
        }
        return render(request, 'index.html', du_lieu)


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index_views')
        else:
            return HttpResponse('login that bai')


class FormView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        hang_san_xuat = HangSanXuat.objects.all()
        context = {
            'hang_sx': hang_san_xuat
        }
        return render(request, 'form.html', context)

    def post(self, request):
        th = request.POST.get('tenhang')
        gt = request.POST.get('giatien')
        hsx = request.POST.get('hangsx')
        h = HangSanXuat.objects.get(id=hsx)
        HangHoa.objects.create(ten_hang=th, gia_tien=gt, hang=h)
        hang_san_xuat = HangSanXuat.objects.all()

        context = {
            'hang_sx': hang_san_xuat,
            'message': 'them thanh cong'
        }
        return render(request, 'form.html', context)


class ViewBaiViet(View):

    def get(self, request, slugg):
        p = BaiViet.objects.get(slug=slugg)
        return render(request, 'post.html', {'p': p})


class ListBaiViet(View):
    def get(self, request):
        lp = BaiViet.objects.all()
        context = {
            'bv': lp
        }
        return render(request, 'list_post.html', context)
