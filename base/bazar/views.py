from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product, Section
from django.core.paginator import Paginator
from .forms import ProductForm, SectionForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
PAGINATOR_PER_PAGE = 10

@login_required
def get_products(request):
    products = Product.objects.all()

    return render(
        request,
        "bazar/product/product_view.html",
        {"products": paginator_wrapper(products, request)},
    )

@login_required
def get_sections(request):
    sections = Section.objects.all()
    return render(
        request,
        "bazar/section/section_view.html",
        {"sections": paginator_wrapper(sections, request)},
    )


def paginator_wrapper(view, request):
    paginator = Paginator(view, PAGINATOR_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def handle_create(request, form_class, template_name, redirect_url):
    error = ""
    form = form_class(request.POST)
    if form.is_valid():
        form.save()
        return redirect(redirect_url)
    else:
        error = "Перевірте дані"

    return render(request, template_name, {"form": form, "error": error})


def create_product(request):
    return handle_create(
        request, ProductForm, "bazar/product/create_product.html", "product_view"
    )


def create_section(request):
    return handle_create(
        request, SectionForm, "bazar/section/create_section.html", "section_view"
    )


class ProductDetailView(DetailView):
    model = Product
    template_name = "bazar/product/product_detail_view.html"
    context_object_name = "product"


class SectionDetailView(DetailView):
    model = Section
    template_name = "bazar/section/section_detail_view.html"
    context_object_name = "section"


class ProductUpdateView(UpdateView):
    model = Product
    template_name = "bazar/product/product_update.html"
    success_url = reverse_lazy("product_view")
    form_class = ProductForm


class SectionUpdateView(UpdateView):
    model = Section
    template_name = "bazar/section/section_update.html"
    success_url = reverse_lazy("section_view")
    form_class = SectionForm


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'bazar/product/product_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy("product_view")


class SectionDeleteView(DeleteView):
    model = Section
    template_name = 'bazar/section/section_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('section_view')

    