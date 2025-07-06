from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import (
    FormulaType, SymbolType, Symbol, LogicalFormula, LogicalFormulaSymbol,
    InferenceRule, InferenceRuleArgument, InferenceRulePremise,
    Theorem, Proof, ProofInference, ProofInferenceArgument, ProofUnresolvedAssumption
)
from .serializers import (
    FormulaTypeSerializer, SymbolTypeSerializer, SymbolSerializer, LogicalFormulaSerializer, LogicalFormulaSymbolSerializer,
    InferenceRuleSerializer, InferenceRuleArgumentSerializer, InferenceRulePremiseSerializer,
    TheoremSerializer, ProofSerializer, ProofInferenceSerializer, ProofInferenceArgumentSerializer, ProofUnresolvedAssumptionSerializer
)


class FormulaTypeViewSet(ReadOnlyModelViewSet):
    queryset = FormulaType.objects.all()
    serializer_class = FormulaTypeSerializer


class SymbolTypeViewSet(ReadOnlyModelViewSet):
    queryset = SymbolType.objects.all()
    serializer_class = SymbolTypeSerializer


class SymbolViewSet(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer


class LogicalFormulaViewSet(viewsets.ModelViewSet):
    queryset = LogicalFormula.objects.all()
    serializer_class = LogicalFormulaSerializer


class LogicalFormulaSymbolViewSet(viewsets.ModelViewSet):
    queryset = LogicalFormulaSymbol.objects.all()
    serializer_class = LogicalFormulaSymbolSerializer


class InferenceRuleViewSet(viewsets.ModelViewSet):
    queryset = InferenceRule.objects.all()
    serializer_class = InferenceRuleSerializer


class InferenceRuleArgumentViewSet(viewsets.ModelViewSet):
    queryset = InferenceRuleArgument.objects.all()
    serializer_class = InferenceRuleArgumentSerializer


class InferenceRulePremiseViewSet(viewsets.ModelViewSet):
    queryset = InferenceRulePremise.objects.all()
    serializer_class = InferenceRulePremiseSerializer


class TheoremViewSet(viewsets.ModelViewSet):
    queryset = Theorem.objects.all()
    serializer_class = TheoremSerializer


class ProofViewSet(viewsets.ModelViewSet):
    queryset = Proof.objects.all()
    serializer_class = ProofSerializer


class ProofInferenceViewSet(viewsets.ModelViewSet):
    queryset = ProofInference.objects.all()
    serializer_class = ProofInferenceSerializer


class ProofInferenceArgumentViewSet(viewsets.ModelViewSet):
    queryset = ProofInferenceArgument.objects.all()
    serializer_class = ProofInferenceArgumentSerializer


class ProofUnresolvedAssumptionViewSet(viewsets.ModelViewSet):
    queryset = ProofUnresolvedAssumption.objects.all()
    serializer_class = ProofUnresolvedAssumptionSerializer
