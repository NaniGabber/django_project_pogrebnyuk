from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Product, Section
from django.core.paginator import Paginator
from .forms import ProductForm, SectionForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

PAGINATOR_PER_PAGE = 15


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


@staff_member_required
def handle_create(request, form_class, template_name, redirect_url):
    error = ""
    form = form_class(request.POST)
    if form.is_valid():
        form.save()
        return redirect(redirect_url)
    else:
        error = "Перевірте дані"

    return render(request, template_name, {"form": form, "error": error})


@staff_member_required
def create_product(request):
    return handle_create(
        request, ProductForm, "bazar/product/create_product.html", "product_view"
    )


@staff_member_required
def create_section(request):
    return handle_create(
        request, SectionForm, "bazar/section/create_section.html", "section_view"
    )


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "bazar/product/product_detail_view.html"
    context_object_name = "product"

class SectionDetailView(LoginRequiredMixin, DetailView):
    model = Section
    template_name = "bazar/section/section_detail_view.html"
    context_object_name = "section"

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    template_name = "bazar/product/product_update.html"
    success_url = reverse_lazy("product_view")
    form_class = ProductForm

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.info(self.request, "Only a superadmin or a staff user (administrator) is allowed to update product.")
        return redirect("product")



class SectionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Section
    template_name = "bazar/section/section_update.html"
    success_url = reverse_lazy("section_view")
    form_class = SectionForm

    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        messages.info(self.request, "Only a superadmin or a staff user (administrator) is allowed to update section.")
        return redirect("product")


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "bazar/product/product_delete.html"
    context_object_name = "product"
    success_url = reverse_lazy("product_view")

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.info(self.request, "Only a superadmin or a staff user (administrator) is allowed to delete product.")
        return redirect("product")

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(
            request, f"'{self.object.title}' has been deleted successfully"
        )
        return response


class SectionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Section
    template_name = "bazar/section/section_delete.html"
    context_object_name = "section"
    success_url = reverse_lazy("section_view")

    def test_func(self):
        return self.request.user.is_superuser
    
    def handle_no_permission(self):
        messages.info(self.request, "Only a superadmin or a staff user (administrator) is allowed to delete section.")
        return redirect("product")


