import pytest

from .models import ReportCard, LinesOfCode, Student, Developer
from .schemas import ReportCardSchema, LinesOfCodeSchema


@pytest.mark.django_db
def test_mutlitable_inheritance():
    student = Student.objects.create(name='Alice')
    report_card = ReportCard.objects.create(student=student, average=7)

    schema = ReportCardSchema.from_orm(report_card)
    assert schema.average == 7

@pytest.mark.django_db
def test_abstract():
    developer = Developer.objects.create(name='Bob')
    lines_of_code = LinesOfCode.objects.create(developer=developer, average=10000)

    schema = LinesOfCodeSchema.from_orm(lines_of_code)
    assert schema.average == 10000


