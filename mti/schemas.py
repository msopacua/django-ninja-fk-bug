from ninja import ModelSchema

from .models import ReportCard, LinesOfCode


class ReportCardSchema(ModelSchema):
    class Meta:
        model = ReportCard
        fields = '__all__'


class LinesOfCodeSchema(ModelSchema):
    class Meta:
        model = LinesOfCode
        fields = '__all__'
