from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    FormulaTypeViewSet, SymbolTypeViewSet, SymbolViewSet, LogicalFormulaViewSet, LogicalFormulaSymbolViewSet,
    InferenceRuleViewSet, InferenceRuleArgumentViewSet, InferenceRulePremiseViewSet,
    TheoremViewSet, ProofViewSet, ProofInferenceViewSet, ProofInferenceArgumentViewSet, ProofUnresolvedAssumptionViewSet
)

router = DefaultRouter()
router.register(r'formulatype', FormulaTypeViewSet)
router.register(r'symboltype', SymbolTypeViewSet)
router.register(r'symbol', SymbolViewSet)
router.register(r'logicalformula', LogicalFormulaViewSet)
router.register(r'logicalformulasymbol', LogicalFormulaSymbolViewSet)
router.register(r'inferencerule', InferenceRuleViewSet)
router.register(r'inferenceruleargument', InferenceRuleArgumentViewSet)
router.register(r'inferencerulepremise', InferenceRulePremiseViewSet)
router.register(r'theorem', TheoremViewSet)
router.register(r'proof', ProofViewSet)
router.register(r'proofinference', ProofInferenceViewSet)
router.register(r'proofinferenceargument', ProofInferenceArgumentViewSet)
router.register(r'proofunresolvedassumption', ProofUnresolvedAssumptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 