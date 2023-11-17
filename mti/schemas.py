from ninja import ModelSchema

from .models import ReportCard, LinesOfCode


class ReportCardSchema(ModelSchema):
    class Config:
        model = ReportCard
        model_fields = '__all__'


class LinesOfCodeSchema(ModelSchema):
    class Config:
        model = LinesOfCode
        model_fields = '__all__'
