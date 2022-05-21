from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    #    UpdateView,
    DeleteView,
)

from django.forms import modelform_factory, modelformset_factory

from .models import Medication, Presentation


class MedicationsIndexView(LoginRequiredMixin, ListView):
    """
    It shows a list of all the medications in the database.
    Offers actions to alter the medications:
    - Create a new medication
    - Edit an existing medication
    - Delete an existing medication
    """

    model = Medication
    context_object_name = "medications"
    template_name = "medications/index.html"


def create_medication(request):
    """
    It creates a new medication.
    """

    MedicationForm = modelform_factory(
        Medication,
        fields=("name", "description"),
    )
    PresentationFormSet = modelformset_factory(
        Presentation,
        fields=("type", "measure_unit", "measure"),
        can_delete=True,
    )

    if request.method == "POST":
        medication_form = MedicationForm(request.POST)
        presentation_formset = PresentationFormSet(request.POST, request.FILES)

        if medication_form.is_valid() and presentation_formset.is_valid():
            medication = medication_form.save()
            # Get the presentations' models from the formset
            # but delete those marked for deletion
            presentations = presentation_formset.save(commit=False)

            # Set the medication to the presentations
            for presentation in presentations:
                presentation.medication = medication
                presentation.save()

            messages.success(
                request, "The medication has been created successfully."
            )
            return redirect("medications:index")
    else:
        medication_form = MedicationForm()
        presentation_formset = PresentationFormSet(
            queryset=Presentation.objects.none()
        )

    return render(
        request,
        "medications/create_medication.html",
        {
            "medication_form": medication_form,
            "presentation_formset": presentation_formset,
        },
    )


class DeleteMedicationView(LoginRequiredMixin, DeleteView):
    """
    Deletes a medication given its id.
    """

    model = Medication

    def get_success_url(self):
        messages.success(
            self.request, "El medicamento ha sido eliminado exitosamente."
        )
        return reverse_lazy("medications:index")
