from django.db import models
import uuid
from django.core.exceptions import ValidationError

class FormulaType(models.Model):
  """論理式種類（項・命題）"""
  name = models.CharField(max_length=100, unique=True, verbose_name="種類名")

  def __str__(self):
    return self.name
      
  class Meta:
    verbose_name = "論理式種類"
    verbose_name_plural = "論理式種類"

class SymbolType(models.Model):
  """記号種類（例：自由変数、関数記号、述語記号…）"""
  name = models.CharField(max_length=100, unique=True, verbose_name="種類名")
  formula_type = models.ForeignKey(
    FormulaType,
    on_delete=models.PROTECT,
    verbose_name="論理式種類ID")
  is_quantifier = models.BooleanField(default=False, verbose_name="量化記号かどうか")

  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "記号種類"
    verbose_name_plural = "記号種類"
        
class Symbol(models.Model):
  """個々の数学記号(例：+, =, x, P)"""
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255, verbose_name="記号名")
  symbol_type = models.ForeignKey(
    SymbolType,
    on_delete=models.PROTECT,
    verbose_name="記号種類ID")
  arity = models.IntegerField(verbose_name="引数の数")
  argument_formula_type = models.ForeignKey(
    FormulaType,
    on_delete=models.PROTECT,
    blank=True,
    null=True,
    verbose_name="引数の論理式種類ID")
  notes = models.TextField(blank=True, verbose_name="備考")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return self.name

  def _clean(self):
    if self.arity == 0 and self.argument_formula_type is not None:
      raise ValidationError({
        'argument_formula_type': '引数の数が0の場合は、引数の論理式種類を指定できません。',
        'arity': '引数の数が0の場合は、引数の論理式種類を指定できません。'
      })
    if self.arity != 0 and self.argument_formula_type is None:
      raise ValidationError({
        'argument_formula_type': '引数の数が0でない場合は、引数の論理式種類を指定する必要があります。',
        'arity': '引数の数が0でない場合は、引数の論理式種類を指定する必要があります。'
      })

  def save(self, *args, **kwargs):
    self._clean()
    super().save(*args, **kwargs)

  class Meta:
    verbose_name = "記号"
    verbose_name_plural = "記号"

class LogicalFormula(models.Model):
  """論理式"""
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  representation = models.TextField(verbose_name="文字列表現(LaTeX)", blank=False)
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  @property
  def formula_type(self):
    """連番0の記号のformula_typeを返す"""
    try:
      first_symbol = self.symbols.get(sequence=0)  # type: ignore
      return first_symbol.symbol.symbol_type.formula_type
    except LogicalFormulaSymbol.DoesNotExist as e:
      e.args = (
        f"論理式 {self.representation} には連番0の記号が存在しません。"
        "論理式には必ず連番0の記号が必要です。",
        *e.args
      )
      raise

  def __str__(self):
    return self.representation

  class Meta:
    verbose_name = "論理式"
    verbose_name_plural = "論理式"

class LogicalFormulaSymbol(models.Model):
  """論理式記号列"""
  logical_formula = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    related_name='symbols',
    verbose_name="論理式ID")
  sequence = models.IntegerField(verbose_name="連番")
  symbol = models.ForeignKey(Symbol, on_delete=models.PROTECT, verbose_name="記号ID")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return f"[{self.symbol.name}]"

  class Meta:
    unique_together = [('logical_formula', 'sequence')]
    verbose_name = "論理式記号列"
    verbose_name_plural = "論理式記号列"

class InferenceRule(models.Model):
  """推論規則(例：modus ponens, ∧導入, …)"""
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=255, verbose_name="推論規則名")
  result_formula = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    verbose_name="結論論理式ID")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return self.name
  
  class Meta:
    verbose_name = "推論規則"
    verbose_name_plural = "推論規則"

class InferenceRuleArgument(models.Model):
  """推論規則引数"""
  inference_rule = models.ForeignKey(
    InferenceRule,
    on_delete=models.PROTECT,
    verbose_name="推論規則ID")
  sequence = models.IntegerField(verbose_name="連番")
  symbol = models.ForeignKey(Symbol, on_delete=models.PROTECT, verbose_name="記号ID")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return f"[{self.symbol.name}]"

  class Meta:
    unique_together = [('inference_rule', 'sequence')]
    verbose_name = "推論規則引数"
    verbose_name_plural = "推論規則引数"

class InferenceRulePremise(models.Model):
  """推論規則仮定"""
  inference_rule = models.ForeignKey(
    InferenceRule,
    on_delete=models.PROTECT,
    verbose_name="推論規則ID")
  sequence = models.IntegerField(verbose_name="連番")
  logical_formula = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    verbose_name="論理式ID")
  solvable_proposition = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    blank=True,
    null=True,
    verbose_name="解消可能命題ID")
  is_solvable_proposition_mandatory = models.BooleanField(
    default=None,
    blank=True,
    null=True,
    verbose_name="解消可能命題の解消が必須かどうか")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def _clean(self):
    if self.solvable_proposition is None and self.is_solvable_proposition_mandatory is not None:
      raise ValidationError({
        'solvable_proposition': '解消可能命題が指定されていない場合は、解消必須フラグを指定できません。',
        'is_solvable_proposition_mandatory': '解消可能命題が指定されていない場合は、解消必須フラグを指定できません。'
      })
    if self.solvable_proposition is not None and self.is_solvable_proposition_mandatory is None:
      raise ValidationError({
        'solvable_proposition': '解消可能命題が指定されている場合は、解消必須フラグを指定する必要があります。',
        'is_solvable_proposition_mandatory': '解消可能命題が指定されている場合は、解消必須フラグを指定する必要があります。'
      })

  def save(self, *args, **kwargs):
    self._clean()
    super().save(*args, **kwargs)

  def __str__(self):
    return f"[{self.inference_rule.name}] {self.sequence}"

  class Meta:
    unique_together = [('inference_rule', 'sequence')]
    verbose_name = "推論規則仮定"
    verbose_name_plural = "推論規則仮定"

class Theorem(models.Model):
  """定理"""
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.TextField(max_length=255, verbose_name="定理名", blank=True, null=True)
  meaning = models.TextField(verbose_name="定理の意味", blank=True, null=True)
  conclusion = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    verbose_name="結論論理式ID")
  assumptions = models.ManyToManyField(
    LogicalFormula,
    verbose_name="仮定論理式ID",
    blank=True)
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
  
  def __str__(self):
    return self.name

  class Meta:
    verbose_name = "定理"
    verbose_name_plural = "定理"

class Proof(models.Model):
  """証明"""
  theorem = models.ForeignKey(
    Theorem,
    on_delete=models.CASCADE,
    verbose_name="定理ID")
  sequence = models.IntegerField(verbose_name="連番")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return f"Proof {self.sequence} for '{self.theorem.name}'"

  class Meta:
    unique_together = [('theorem', 'sequence')]
    verbose_name = "証明"
    verbose_name_plural = "証明"

class ProofInference(models.Model):
  """証明推論"""
  proof = models.ForeignKey(
    Proof,
    on_delete=models.CASCADE,
    verbose_name="証明ID")
  sequence = models.IntegerField(verbose_name="連番")
  inference_rule = models.ForeignKey(
    InferenceRule,
    on_delete=models.PROTECT,
    verbose_name="推論規則ID")
  conclusion_formula = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    verbose_name="結論論理式ID")
  from_nodes = models.ManyToManyField(
    'self',
    symmetrical=False,
    related_name='to_nodes',
    blank=True,
    verbose_name="先行する推論ステップ")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return f"Proof {self.proof.sequence} Step {self.sequence}: Rule '{self.inference_rule.name}'"

  class Meta:
    unique_together = [('proof', 'sequence')]
    verbose_name = "証明推論"
    verbose_name_plural = "証明推論"

class ProofInferenceArgument(models.Model):
  """証明推論引数"""
  proof_inference = models.ForeignKey(
    ProofInference,
    on_delete=models.CASCADE,
    verbose_name="証明推論ID")
  sequence = models.IntegerField(verbose_name="連番")
  argument_formula = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    verbose_name="引数論理式ID")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")

  def __str__(self):
    return f"Argument {self.sequence} for Proof {self.proof_inference.proof.sequence} Step {self.proof_inference.sequence}: {self.argument_formula.representation}"

  class Meta:
    unique_together = [('proof_inference', 'sequence')]
    verbose_name = "証明推論引数"
    verbose_name_plural = "証明推論引数"

class ProofUnresolvedAssumption(models.Model):
  """証明未解消仮定"""
  proof = models.ForeignKey(
    Proof,
    on_delete=models.CASCADE,
    verbose_name="証明ID")
  sequence = models.IntegerField(verbose_name="連番")
  formula = models.ForeignKey(
    LogicalFormula,
    on_delete=models.PROTECT,
    verbose_name="仮定論理式ID")
  added_by_inference = models.ForeignKey(
    ProofInference,
    on_delete=models.CASCADE,
    verbose_name="導入した推論ステップ")
  resolved_by_inference = models.ForeignKey(
    ProofInference,
    on_delete=models.PROTECT,
    blank=True,
    null=True,
    verbose_name="解消した推論ステップ")
  created_at = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
  updated_at = models.DateTimeField(auto_now=True, verbose_name="更新日時")
  
  def __str__(self):
    status = "Resolved" if self.resolved_by_inference else "Unresolved"
    return f"Assumption {self.sequence} ({status}) in Proof {self.proof.sequence}"

  class Meta:
    unique_together = [('proof', 'sequence')]
    verbose_name = "証明未解消仮定"
    verbose_name_plural = "証明未解消仮定"
