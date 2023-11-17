from __future__ import annotations

import typing as t

from cuid2 import cuid_wrapper
from django import forms
from django.db.models.fields import CharField

cuid_generator: t.Callable[[], str] = cuid_wrapper()


class CuidFormField(forms.CharField):
    def __init__(self, **kwargs):
        super().__init__(max_length=32, widget=forms.HiddenInput, disabled=True, required=False)

class CuidField(CharField):
    def __init__(self, max_length=32, **kwargs) -> None:
        kwargs["primary_key"] = True
        kwargs["default"] = cuid_generator
        super().__init__(max_length=max_length, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs["max_length"] = self.max_length
        del kwargs["primary_key"]
        del kwargs["default"]
        return name, path, args, kwargs

    def formfield(
        self,
        form_class = None,
        choices_form_class = None,
        **kwargs,
    ):
        defaults = {
            "form_class": form_class or CuidFormField
        }
        defaults.update(choices_form_class=choices_form_class, **kwargs)
        return super().formfield(**defaults)
