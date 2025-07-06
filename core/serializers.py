from rest_framework import serializers
from .models import (
    FormulaType, SymbolType, Symbol, LogicalFormula, LogicalFormulaSymbol,
    InferenceRule, InferenceRuleArgument, InferenceRulePremise,
    Theorem, Proof, ProofInference, ProofInferenceArgument, ProofUnresolvedAssumption
)


class FormulaTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormulaType
        fields = '__all__'


class SymbolTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymbolType
        fields = '__all__'


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = '__all__'


class LogicalFormulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogicalFormula
        fields = '__all__'


class LogicalFormulaSymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = LogicalFormulaSymbol
        fields = '__all__'


class InferenceRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InferenceRule
        fields = '__all__'


class InferenceRuleArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = InferenceRuleArgument
        fields = '__all__'


class InferenceRulePremiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InferenceRulePremise
        fields = '__all__'


class TheoremSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theorem
        fields = '__all__'


class ProofSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proof
        fields = '__all__'


class ProofInferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofInference
        fields = '__all__'


class ProofInferenceArgumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofInferenceArgument
        fields = '__all__'


class ProofUnresolvedAssumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProofUnresolvedAssumption
        fields = '__all__' 
