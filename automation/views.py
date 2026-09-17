from django.shortcuts import render, redirect
from .models import Lead, Automation


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def chatboard(request):
    return render(request, "chatboard.html")


def leads(request):

    all_leads = Lead.objects.all().order_by("-created_at")

    return render(
        request,
        "leads.html",
        {
            "leads": all_leads
        }
    )


def generate_leads(request):

    if request.method == "POST":

        sample_leads = [
            {
                "name": "Ali Hassan",
                "email": "ali@example.com",
                "interest": "AI Automation",
                "status": "New",
            },
            {
                "name": "Ayesha Khan",
                "email": "ayesha@example.com",
                "interest": "AI Chatbot",
                "status": "New",
            },
            {
                "name": "Usman Ahmed",
                "email": "usman@example.com",
                "interest": "Business Software",
                "status": "Qualified",
            },
        ]

        for lead in sample_leads:

            Lead.objects.create(
                name=lead["name"],
                email=lead["email"],
                interest=lead["interest"],
                status=lead["status"],
            )

        return redirect("leads")

    return redirect("leads")


def automations(request):
    return render(request, "automations.html")


def create_automation(request):
    return render(request, "create_automation.html")


def analytics(request):
    return render(request, "analytics.html")


def projects(request):
    return render(request, "projects.html")


def settings_page(request):
    return render(request, "settings.html")
def automations(request):
    all_automations = Automation.objects.all().order_by("-created_at")

    return render(
        request,
        "automations.html",
        {"automations": all_automations}
    )


def create_automation(request):

    if request.method == "POST":

        name = request.POST.get("name")
        description = request.POST.get("description")
        trigger = request.POST.get("trigger")
        action = request.POST.get("action")

        if name and description and trigger and action:

            Automation.objects.create(
                name=name,
                description=description,
                trigger=trigger,
                action=action,
                status="Active"
            )

            return redirect("automations")

    return render(request, "create_automation.html")
from django.shortcuts import render, redirect, get_object_or_404
from .models import Lead, Automation


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def chatboard(request):
    return render(request, "chatboard.html")


# =========================
# LEADS
# =========================

def leads(request):
    all_leads = Lead.objects.all().order_by("-created_at")

    return render(
        request,
        "leads.html",
        {"leads": all_leads}
    )


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Lead

def add_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company = request.POST.get('company', '').strip()
        status = request.POST.get('status', 'new')
        notes = request.POST.get('notes', '').strip()

        if not name:
            messages.error(request, 'Name is required.')
            return render(request, 'add_lead.html', {
                'status_choices': Lead.STATUS_CHOICES,
                'form_data': request.POST,
            })

        Lead.objects.create(
            name=name,
            email=email or None,
            phone=phone or None,
            company=company or None,
            status=status,
            notes=notes or None,
        )
        messages.success(request, f'Lead "{name}" added successfully!')
        return redirect('leads')

    return render(request, 'add_lead.html', {
        'status_choices': Lead.STATUS_CHOICES,
    })

def view_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    return render(request, 'view_lead.html', {'lead': lead})

def edit_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    if request.method == 'POST':
        lead.name = request.POST.get('name')
        lead.email = request.POST.get('email')
        lead.phone = request.POST.get('phone')
        lead.save()
        return redirect('leads')
    return render(request, 'edit_lead.html', {'lead': lead})

def delete_lead(request, lead_id):
    lead = get_object_or_404(Lead, id=lead_id)
    if request.method == 'POST':
        lead.delete()
    return redirect('leads')


# =========================
# AUTOMATIONS
# =========================

def automations(request):

    all_automations = Automation.objects.all().order_by("-created_at")

    return render(
        request,
        "automations.html",
        {"automations": all_automations}
    )


def create_automation(request):

    if request.method == "POST":

        name = request.POST.get("name")
        description = request.POST.get("description")
        trigger = request.POST.get("trigger")
        action = request.POST.get("action")

        if name and description and trigger and action:

            Automation.objects.create(
                name=name,
                description=description,
                trigger=trigger,
                action=action,
                status="Active"
            )

            return redirect("automations")

    return render(request, "create_automation.html")


def analytics(request):
    return render(request, "analytics.html")


def projects(request):
    return render(request, "projects.html")


def settings_page(request):
    return render(request, "settings.html")

