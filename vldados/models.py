# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agrfin(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dc = models.CharField(db_column='DC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlpgto = models.FloatField(db_column='VLPGTO', blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(db_column='BANCO', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtpgto = models.DateTimeField(db_column='DTPGTO', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtbaixa = models.DateTimeField(db_column='DTBAIXA', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='GRUPO', blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cobranca = models.BooleanField(db_column='COBRANCA', blank=True, null=True)  # Field name made lowercase.
    dt_docto = models.DateTimeField(db_column='DT_DOCTO', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    nrobanco = models.CharField(db_column='NROBANCO', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bdev = models.BooleanField(db_column='BDEV', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlvencto = models.FloatField(db_column='VLVENCTO', blank=True, null=True)  # Field name made lowercase.
    pgcobranca = models.BooleanField(db_column='PGCOBRANCA', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    ccusto = models.CharField(db_column='CCUSTO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nominal = models.CharField(db_column='NOMINAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desdobra = models.CharField(db_column='DESDOBRA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.
    dtbanco = models.DateTimeField(db_column='DTBANCO', blank=True, null=True)  # Field name made lowercase.
    rem = models.IntegerField(db_column='REM', blank=True, null=True)  # Field name made lowercase.
    ret = models.IntegerField(db_column='RET', blank=True, null=True)  # Field name made lowercase.
    vldesc = models.FloatField(db_column='VLDESC', blank=True, null=True)  # Field name made lowercase.
    vlacresc = models.FloatField(db_column='VLACRESC', blank=True, null=True)  # Field name made lowercase.
    nregext = models.IntegerField(db_column='NREGEXT', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfecha = models.IntegerField(db_column='NFECHA', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    norc = models.IntegerField(db_column='NORC', blank=True, null=True)  # Field name made lowercase.
    agchq = models.CharField(db_column='AGCHQ', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contachq = models.CharField(db_column='CONTACHQ', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cnpjcpfchq = models.CharField(db_column='CNPJCPFCHQ', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    gnf = models.CharField(db_column='GNF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    npedout = models.IntegerField(db_column='NPEDOUT', blank=True, null=True)  # Field name made lowercase.
    rem_banco = models.BooleanField(db_column='REM_BANCO', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    aut = models.CharField(db_column='AUT', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCODE', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AGRFIN'


class Alunos(models.Model):
    nreg = models.IntegerField(db_column='NREG')  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (CODIGO, NREG) found, that is not supported. The first column is selected.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    escola = models.CharField(db_column='ESCOLA', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtnasc = models.DateTimeField(db_column='DTNASC', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ALUNOS'
        unique_together = (('codigo', 'nreg'),)


class Analcgr(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='EDITION', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tenv = models.FloatField(db_column='TENV', blank=True, null=True)  # Field name made lowercase.
    tret = models.FloatField(db_column='TRET', blank=True, null=True)  # Field name made lowercase.
    tvendas = models.FloatField(db_column='TVENDAS', blank=True, null=True)  # Field name made lowercase.
    taj = models.FloatField(db_column='TAJ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ANALCGR'


class Apostilas(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomeinst = models.CharField(db_column='NOMEINST', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aluno = models.IntegerField(db_column='ALUNO', blank=True, null=True)  # Field name made lowercase.
    nomealuno = models.CharField(db_column='NOMEALUNO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'APOSTILAS'


class Assin(models.Model):
    codassin = models.IntegerField(db_column='CODASSIN', primary_key=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    dtinicio = models.DateTimeField(db_column='DTINICIO', blank=True, null=True)  # Field name made lowercase.
    dtfim = models.DateTimeField(db_column='DTFIM', blank=True, null=True)  # Field name made lowercase.
    qtex = models.IntegerField(db_column='QTEX', blank=True, null=True)  # Field name made lowercase.
    period = models.CharField(db_column='PERIOD', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    ultrec = models.CharField(db_column='ULTREC', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtultrec = models.DateTimeField(db_column='DTULTREC', blank=True, null=True)  # Field name made lowercase.
    ativo = models.CharField(db_column='ATIVO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    qtdias = models.IntegerField(db_column='QTDIAS', blank=True, null=True)  # Field name made lowercase.
    exinicio = models.CharField(db_column='EXINICIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    exfim = models.CharField(db_column='EXFIM', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    historico = models.TextField(db_column='HISTORICO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtultpub = models.DateTimeField(db_column='DTULTPUB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ASSIN'


class Atendente(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bonus = models.FloatField(db_column='BONUS', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATENDENTE'


class AtribMp(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, PORTAL, CODIGO) found, that is not supported. The first column is selected.
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    visivel = models.BooleanField(db_column='VISIVEL', blank=True, null=True)  # Field name made lowercase.
    campo_vl = models.CharField(db_column='CAMPO_VL', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    padrao = models.CharField(db_column='PADRAO', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ATRIB_MP'
        unique_together = (('filial', 'portal', 'codigo'),)


class Auditoria(models.Model):
    dtev = models.DateTimeField(db_column='DTEV', primary_key=True)  # Field name made lowercase. The composite primary key (DTEV, TPEV) found, that is not supported. The first column is selected.
    tpev = models.CharField(db_column='TPEV', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    motivo = models.TextField(db_column='MOTIVO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUDITORIA'
        unique_together = (('dtev', 'tpev'),)


class Auximpb2W(models.Model):
    stped = models.CharField(db_column='STPED', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.CharField(db_column='NPED', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.CharField(db_column='NSITE', primary_key=True, max_length=15, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ref = models.CharField(db_column='REF', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tel1 = models.CharField(db_column='TEL1', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tel2 = models.CharField(db_column='TEL2', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tel3 = models.CharField(db_column='TEL3', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codbarras = models.CharField(db_column='CODBARRAS', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    frete = models.FloatField(db_column='FRETE', blank=True, null=True)  # Field name made lowercase.
    dtprev = models.DateTimeField(db_column='DTPREV', blank=True, null=True)  # Field name made lowercase.
    dtenvio = models.DateTimeField(db_column='DTENVIO', blank=True, null=True)  # Field name made lowercase.
    cp1 = models.CharField(db_column='CP1', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cp2 = models.CharField(db_column='CP2', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='INFO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    metodo = models.CharField(db_column='METODO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp2 = models.CharField(db_column='TRANSP2', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUXIMPB2W'


class Auxped(models.Model):
    nint = models.AutoField(db_column='NINT', primary_key=True)  # Field name made lowercase.
    nreg = models.IntegerField(db_column='NREG', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    st = models.CharField(db_column='ST', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    origem = models.CharField(db_column='ORIGEM', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregant = models.IntegerField(db_column='NREGANT', blank=True, null=True)  # Field name made lowercase.
    opant = models.CharField(db_column='OPANT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfant = models.CharField(db_column='NFANT', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    aliqicmsst = models.FloatField(db_column='ALIQICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.FloatField(db_column='ALIQIPI', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    vicms = models.FloatField(db_column='VICMS', blank=True, null=True)  # Field name made lowercase.
    vst = models.FloatField(db_column='VST', blank=True, null=True)  # Field name made lowercase.
    vipi = models.FloatField(db_column='VIPI', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    vfrete = models.FloatField(db_column='VFRETE', blank=True, null=True)  # Field name made lowercase.
    vseg = models.FloatField(db_column='VSEG', blank=True, null=True)  # Field name made lowercase.
    voutro = models.FloatField(db_column='VOUTRO', blank=True, null=True)  # Field name made lowercase.
    orig = models.CharField(db_column='ORIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CSTIPI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    vpis = models.FloatField(db_column='VPIS', blank=True, null=True)  # Field name made lowercase.
    vcofins = models.FloatField(db_column='VCOFINS', blank=True, null=True)  # Field name made lowercase.
    qtde_xml = models.IntegerField(db_column='QTDE_XML', blank=True, null=True)  # Field name made lowercase.
    redicms = models.FloatField(db_column='REDICMS', blank=True, null=True)  # Field name made lowercase.
    conf = models.CharField(db_column='CONF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUXPED'


class Auxplan(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    autor = models.CharField(db_column='AUTOR', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    pr_mkt = models.FloatField(db_column='PR_MKT', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='ANO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    edicao = models.CharField(db_column='EDICAO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtpag = models.IntegerField(db_column='QTPAG', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    altura = models.FloatField(db_column='ALTURA', blank=True, null=True)  # Field name made lowercase.
    largura = models.FloatField(db_column='LARGURA', blank=True, null=True)  # Field name made lowercase.
    lombada = models.FloatField(db_column='LOMBADA', blank=True, null=True)  # Field name made lowercase.
    formato = models.CharField(db_column='FORMATO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj1 = models.CharField(db_column='SUBJ1', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='ASSUNTO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    moeda = models.CharField(db_column='MOEDA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    binding = models.CharField(db_column='BINDING', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    editora = models.CharField(db_column='EDITORA', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sinopse = models.TextField(db_column='SINOPSE', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    link_img = models.CharField(db_column='LINK_IMG', max_length=150, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cad_ok = models.BooleanField(db_column='CAD_OK', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    statcd = models.CharField(db_column='STATCD', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj2 = models.CharField(db_column='SUBJ2', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj3 = models.CharField(db_column='SUBJ3', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    idioma = models.CharField(db_column='IDIOMA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codff = models.CharField(db_column='CODFF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    local = models.CharField(db_column='LOCAL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    sinc = models.IntegerField(db_column='SINC', blank=True, null=True)  # Field name made lowercase.
    disp_ff = models.IntegerField(db_column='DISP_FF', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    secao = models.CharField(db_column='SECAO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_ext = models.CharField(db_column='COD_EXT', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUXPLAN'


class Auxprod(models.Model):
    isbn = models.CharField(db_column='ISBN', primary_key=True, max_length=13, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    editora = models.CharField(db_column='EDITORA', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='ASSUNTO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    autor = models.CharField(db_column='AUTOR', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    edicao = models.CharField(db_column='EDICAO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='ANO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    link_img = models.CharField(db_column='LINK_IMG', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bindig = models.CharField(db_column='BINDIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    formato = models.CharField(db_column='FORMATO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    altura = models.FloatField(db_column='ALTURA', blank=True, null=True)  # Field name made lowercase.
    largura = models.FloatField(db_column='LARGURA', blank=True, null=True)  # Field name made lowercase.
    lombada = models.FloatField(db_column='LOMBADA', blank=True, null=True)  # Field name made lowercase.
    peso = models.IntegerField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    qtpag = models.IntegerField(db_column='QTPAG', blank=True, null=True)  # Field name made lowercase.
    disp = models.IntegerField(db_column='DISP', blank=True, null=True)  # Field name made lowercase.
    sinopse = models.TextField(db_column='SINOPSE', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    cod_ff = models.CharField(db_column='COD_FF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dt_ff = models.DateTimeField(db_column='DT_FF', blank=True, null=True)  # Field name made lowercase.
    sinc = models.IntegerField(db_column='SINC', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUXPROD'


class Auxsinc(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    erro = models.CharField(db_column='ERRO', max_length=250, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_portal = models.IntegerField(db_column='COD_PORTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUXSINC'


class Auxsped(models.Model):
    nlinha = models.IntegerField(db_column='NLINHA', primary_key=True)  # Field name made lowercase.
    c1 = models.CharField(db_column='C1', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c2 = models.CharField(db_column='C2', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c3 = models.CharField(db_column='C3', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c4 = models.CharField(db_column='C4', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c5 = models.CharField(db_column='C5', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c6 = models.CharField(db_column='C6', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c7 = models.CharField(db_column='C7', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c8 = models.CharField(db_column='C8', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c9 = models.CharField(db_column='C9', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c10 = models.CharField(db_column='C10', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    c11 = models.CharField(db_column='C11', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AUXSPED'


class Axatped(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    locest = models.CharField(db_column='LOCEST', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomeff = models.CharField(db_column='NOMEFF', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomecli = models.CharField(db_column='NOMECLI', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conf = models.CharField(db_column='CONF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXATPED'


class Axcheque(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='GRUPO', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nominal = models.CharField(db_column='NOMINAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtpgto = models.DateTimeField(db_column='DTPGTO', blank=True, null=True)  # Field name made lowercase.
    vlpgto = models.FloatField(db_column='VLPGTO', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ccusto = models.CharField(db_column='CCUSTO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desdobra = models.CharField(db_column='DESDOBRA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtbanco = models.DateTimeField(db_column='DTBANCO', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    regext = models.IntegerField(db_column='REGEXT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXCHEQUE'


class Axcomiss(models.Model):
    vendedor = models.CharField(db_column='VENDEDOR', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendas = models.FloatField(db_column='VENDAS', blank=True, null=True)  # Field name made lowercase.
    comis = models.FloatField(db_column='COMIS', blank=True, null=True)  # Field name made lowercase.
    num = models.IntegerField(db_column='NUM', blank=True, null=True)  # Field name made lowercase.
    perc = models.FloatField(db_column='PERC', blank=True, null=True)  # Field name made lowercase.
    cgc = models.CharField(db_column='CGC', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXCOMISS'


class Axcomissoes(models.Model):
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telres = models.CharField(db_column='TELRES', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtbaixa = models.DateTimeField(db_column='DTBAIXA', blank=True, null=True)  # Field name made lowercase.
    dtpgto = models.DateTimeField(db_column='DTPGTO', blank=True, null=True)  # Field name made lowercase.
    vlpgto = models.FloatField(db_column='VLPGTO', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXCOMISSOES'


class Axer(models.Model):
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    qtde = models.IntegerField(blank=True, null=True)
    prunit = models.FloatField(blank=True, null=True)
    title = models.CharField(max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    author = models.CharField(max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    edition = models.CharField(max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    ano = models.CharField(max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    di = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    sellpr = models.FloatField(blank=True, null=True)
    tpprod = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    prcusto = models.FloatField(blank=True, null=True)
    isbn1 = models.CharField(db_column='ISBN1', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    op = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    nreg = models.IntegerField(blank=True, null=True)
    vendedor = models.CharField(max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    moeda = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    prlista = models.FloatField(blank=True, null=True)
    list = models.FloatField(blank=True, null=True)
    publisher = models.CharField(max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    fi = models.CharField(db_column='Fi', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXER'


class Axetiq(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    autor = models.CharField(db_column='AUTOR', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=25, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    moeda = models.CharField(db_column='MOEDA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXETIQ'


class Axfcx(models.Model):
    grupo = models.CharField(db_column='GRUPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vencto = models.DateTimeField(db_column='VENCTO', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    subgr = models.CharField(db_column='SUBGR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    total = models.FloatField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXFCX'


class Axitsep(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    locest = models.CharField(db_column='LOCEST', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomeff = models.CharField(db_column='NOMEFF', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomecli = models.CharField(db_column='NOMECLI', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.
    napanha = models.IntegerField(db_column='NAPANHA', blank=True, null=True)  # Field name made lowercase.
    separado = models.CharField(db_column='SEPARADO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXITSEP'


class Axlkp(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fornec = models.CharField(db_column='FORNEC', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    evento = models.CharField(db_column='EVENTO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(db_column='BANCO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fpg2 = models.CharField(db_column='FPG2', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    secao = models.CharField(db_column='SECAO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    espec = models.CharField(db_column='ESPEC', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf2 = models.CharField(db_column='UF2', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    setbol = models.CharField(db_column='SETBOL', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    moeda = models.CharField(db_column='MOEDA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpcli = models.CharField(db_column='TPCLI', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsite = models.IntegerField(db_column='STSITE', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXLKP'


class Axper(models.Model):
    inicio = models.DateTimeField(db_column='INICIO', blank=True, null=True)  # Field name made lowercase.
    fim = models.DateTimeField(db_column='FIM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXPER'


class Axpesq(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXPESQ'


class Axpgto(models.Model):
    tipo = models.CharField(db_column='TIPO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dias = models.FloatField(db_column='DIAS', blank=True, null=True)  # Field name made lowercase.
    txadm = models.FloatField(db_column='TXADM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXPGTO'


class Axrec(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    juros = models.FloatField(db_column='JUROS', blank=True, null=True)  # Field name made lowercase.
    multa = models.FloatField(db_column='MULTA', blank=True, null=True)  # Field name made lowercase.
    valorpg = models.FloatField(db_column='VALORPG', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='GRUPO', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregext = models.IntegerField(db_column='NREGEXT', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nrobanco = models.CharField(db_column='NROBANCO', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desc_p_unica = models.FloatField(db_column='DESC_P_UNICA', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dt_docto = models.DateTimeField(db_column='DT_DOCTO', blank=True, null=True)  # Field name made lowercase.
    dtpgto = models.DateTimeField(db_column='DTPGTO', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    aut = models.CharField(db_column='AUT', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXREC'


class Axreclv(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    npedff = models.IntegerField(db_column='NPEDFF', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    locest = models.CharField(db_column='LOCEST', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    secao = models.CharField(db_column='SECAO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXRECLV'


class AxrecMkt(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    canal = models.CharField(db_column='CANAL', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_mkt = models.CharField(db_column='COD_MKT', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    frete = models.FloatField(db_column='FRETE', blank=True, null=True)  # Field name made lowercase.
    outros = models.FloatField(db_column='OUTROS', blank=True, null=True)  # Field name made lowercase.
    parcela = models.CharField(db_column='PARCELA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvenda = models.DateTimeField(db_column='DTVENDA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXREC_MKT'


class Axrelnf(models.Model):
    dtcad = models.DateTimeField(blank=True, null=True)
    dtemissao = models.DateTimeField(blank=True, null=True)
    natop = models.CharField(max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    codfiscal = models.CharField(max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    es = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    serie = models.CharField(max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    tpnf = models.CharField(max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    vlfrete = models.FloatField(blank=True, null=True)
    uf = models.CharField(max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    vlcontabil = models.FloatField(blank=True, null=True)
    baseicms = models.FloatField(blank=True, null=True)
    impicms = models.FloatField(blank=True, null=True)
    impipi = models.FloatField(blank=True, null=True)
    baseicmsst = models.FloatField(blank=True, null=True)
    impicmsst = models.FloatField(blank=True, null=True)
    cliforn = models.CharField(max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    nome = models.CharField(max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    razsocial = models.CharField(max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    fj = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    cgc = models.CharField(max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    inscr = models.CharField(max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXRELNF'


class Axrembol(models.Model):
    parc = models.IntegerField(db_column='PARC', primary_key=True)  # Field name made lowercase.
    qtdia = models.IntegerField(db_column='QTDIA', blank=True, null=True)  # Field name made lowercase.
    vldia = models.FloatField(db_column='VLDIA', blank=True, null=True)  # Field name made lowercase.
    impdia = models.CharField(db_column='IMPDIA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtatr1 = models.IntegerField(db_column='QTATR1', blank=True, null=True)  # Field name made lowercase.
    vlatr1 = models.FloatField(db_column='VLATR1', blank=True, null=True)  # Field name made lowercase.
    impatr1 = models.CharField(db_column='IMPATR1', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtatr2 = models.IntegerField(db_column='QTATR2', blank=True, null=True)  # Field name made lowercase.
    vlatr2 = models.FloatField(db_column='VLATR2', blank=True, null=True)  # Field name made lowercase.
    impatr2 = models.CharField(db_column='IMPATR2', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXREMBOL'


class Axrep(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='EDITION', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='SUPPLIER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    disp = models.IntegerField(db_column='DISP', blank=True, null=True)  # Field name made lowercase.
    qtped = models.IntegerField(db_column='QTPED', blank=True, null=True)  # Field name made lowercase.
    estmin = models.IntegerField(db_column='ESTMIN', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    ped = models.CharField(db_column='PED', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    exame = models.IntegerField(db_column='EXAME', blank=True, null=True)  # Field name made lowercase.
    ev = models.IntegerField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn1 = models.CharField(db_column='ISBN1', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tconsig = models.IntegerField(db_column='TCONSIG', blank=True, null=True)  # Field name made lowercase.
    devsimb = models.IntegerField(db_column='DEVSIMB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXREP'


class Axsaldo(models.Model):
    conta = models.CharField(db_column='CONTA', primary_key=True, max_length=9, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    anterior = models.FloatField(db_column='ANTERIOR', blank=True, null=True)  # Field name made lowercase.
    entrada = models.FloatField(db_column='ENTRADA', blank=True, null=True)  # Field name made lowercase.
    saida = models.FloatField(db_column='SAIDA', blank=True, null=True)  # Field name made lowercase.
    disp = models.FloatField(db_column='DISP', blank=True, null=True)  # Field name made lowercase.
    banco = models.FloatField(db_column='BANCO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXSALDO'


class Axsincvd(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (NBOOK, NREG) found, that is not supported. The first column is selected.
    nreg = models.IntegerField(db_column='NREG')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXSINCVD'
        unique_together = (('nbook', 'nreg'),)


class Axvendas(models.Model):
    dtvenda = models.DateTimeField(db_column='DTVENDA', primary_key=True)  # Field name made lowercase.
    qtdev = models.IntegerField(db_column='QTDEV', blank=True, null=True)  # Field name made lowercase.
    dev = models.FloatField(db_column='DEV', blank=True, null=True)  # Field name made lowercase.
    qtvenda = models.IntegerField(db_column='QTVENDA', blank=True, null=True)  # Field name made lowercase.
    venda = models.FloatField(db_column='VENDA', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='ANO', blank=True, null=True)  # Field name made lowercase.
    mes = models.IntegerField(db_column='MES', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AXVENDAS'


class Bancos(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BANCOS'


class Base(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    ramal = models.CharField(db_column='RAMAL', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    bdatual = models.DateTimeField(db_column='BDATUAL', blank=True, null=True)  # Field name made lowercase.
    ultarq = models.IntegerField(db_column='ULTARQ', blank=True, null=True)  # Field name made lowercase.
    dtsincr = models.DateTimeField(db_column='DTSINCR', blank=True, null=True)  # Field name made lowercase.
    svl = models.IntegerField(db_column='SVL', blank=True, null=True)  # Field name made lowercase.
    ultpedsite = models.IntegerField(db_column='ULTPEDSITE', blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='MARGEM', blank=True, null=True)  # Field name made lowercase.
    versao = models.CharField(db_column='VERSAO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    simulanfe = models.BooleanField(db_column='SIMULANFE', blank=True, null=True)  # Field name made lowercase.
    arqsql = models.IntegerField(db_column='ARQSQL', blank=True, null=True)  # Field name made lowercase.
    tsinc = models.IntegerField(db_column='TSINC', blank=True, null=True)  # Field name made lowercase.
    retsimbcgr = models.BooleanField(db_column='RETSIMBCGR', blank=True, null=True)  # Field name made lowercase.
    sincprod = models.BooleanField(db_column='SINCPROD', blank=True, null=True)  # Field name made lowercase.
    sincfin = models.BooleanField(db_column='SINCFIN', blank=True, null=True)  # Field name made lowercase.
    imp_localizador = models.BooleanField(db_column='IMP_LOCALIZADOR', blank=True, null=True)  # Field name made lowercase.
    vlnfe = models.BooleanField(db_column='VLNFE', blank=True, null=True)  # Field name made lowercase.
    parc_unica = models.BooleanField(db_column='PARC_UNICA', blank=True, null=True)  # Field name made lowercase.
    carne = models.BooleanField(db_column='CARNE', blank=True, null=True)  # Field name made lowercase.
    capicom = models.BooleanField(db_column='CAPICOM', blank=True, null=True)  # Field name made lowercase.
    cod_vlplace = models.CharField(db_column='COD_VLPLACE', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    agrupafilial = models.BooleanField(db_column='AGRUPAFILIAL', blank=True, null=True)  # Field name made lowercase.
    tsinc_vlplace = models.IntegerField(db_column='TSINC_VLPLACE', blank=True, null=True)  # Field name made lowercase.
    filial_vlplace = models.CharField(db_column='FILIAL_VLPLACE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BASE'


class Bisac(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=11, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=200, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_bisac = models.CharField(db_column='COD_BISAC', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BISAC'


class Cabfcx(models.Model):
    grupo = models.CharField(db_column='GRUPO', primary_key=True, max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (GRUPO, FPG) found, that is not supported. The first column is selected.
    fpg = models.CharField(db_column='FPG', max_length=30, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CABFCX'
        unique_together = (('grupo', 'fpg'),)


class CadEv(models.Model):
    cod_ev = models.IntegerField(db_column='COD_EV', primary_key=True)  # Field name made lowercase.
    id_estante = models.CharField(db_column='ID_ESTANTE', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    autor = models.CharField(db_column='AUTOR', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='ANO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    edicao = models.CharField(db_column='EDICAO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    estante = models.CharField(db_column='ESTANTE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    binding = models.CharField(db_column='BINDING', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    editora = models.CharField(db_column='EDITORA', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conservacao = models.TextField(db_column='CONSERVACAO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volume = models.CharField(db_column='VOLUME', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    statcd = models.CharField(db_column='STATCD', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    local = models.CharField(db_column='LOCAL', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    nreg_orc = models.IntegerField(db_column='NREG_ORC', blank=True, null=True)  # Field name made lowercase.
    sinopse = models.TextField(db_column='SINOPSE', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    idioma = models.CharField(db_column='IDIOMA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAD_EV'


class Caixa(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    dc = models.CharField(db_column='DC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sangria = models.CharField(db_column='SANGRIA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    norc = models.IntegerField(db_column='NORC', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAIXA'


class CanalMp(models.Model):
    canal = models.CharField(db_column='CANAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CANAL_MP'


class Cartacorr(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CARTACORR'


class CatExt(models.Model):
    categoria = models.CharField(db_column='CATEGORIA', primary_key=True, max_length=100, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CAT_EXT'


class Cce(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    seq = models.IntegerField(db_column='SEQ')  # Field name made lowercase.
    dtemissao = models.DateTimeField(db_column='DTEMISSAO', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    correcao = models.TextField(db_column='CORRECAO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    xml = models.CharField(db_column='XML', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CCE'


class Ccusto(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transf = models.CharField(db_column='TRANSF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    gritem = models.CharField(db_column='GRITEM', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fluxo = models.CharField(db_column='FLUXO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codctb = models.CharField(db_column='CODCTB', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CCUSTO'


class CcMkt(models.Model):
    evento = models.CharField(db_column='EVENTO', primary_key=True, max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (EVENTO, CCUSTO) found, that is not supported. The first column is selected.
    ccusto = models.CharField(db_column='CCUSTO', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CC_MKT'
        unique_together = (('evento', 'ccusto'),)


class Cfdesc(models.Model):
    cliforn = models.CharField(db_column='CLIFORN', primary_key=True, max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (CLIFORN, FORNEC) found, that is not supported. The first column is selected.
    fornec = models.CharField(db_column='FORNEC', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    desccf = models.FloatField(db_column='DESCCF', blank=True, null=True)  # Field name made lowercase.
    condpg = models.CharField(db_column='CONDPG', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFDESC'
        unique_together = (('cliforn', 'fornec'),)


class Cfg(models.Model):
    nrohd = models.CharField(db_column='NROHD', primary_key=True, max_length=50, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (NROHD, FILIAL) found, that is not supported. The first column is selected.
    ifundo = models.CharField(db_column='IFUNDO', max_length=255, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cfundo = models.CharField(db_column='CFUNDO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    imprnf = models.CharField(db_column='IMPRNF', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impped = models.CharField(db_column='IMPPED', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modimp = models.CharField(db_column='MODIMP', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    snfisc = models.IntegerField(db_column='SNFISC', blank=True, null=True)  # Field name made lowercase.
    scupom = models.CharField(db_column='SCUPOM', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncaixa = models.CharField(db_column='NCAIXA', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    mcupom = models.CharField(db_column='MCUPOM', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    portac = models.CharField(db_column='PORTAC', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    impetiq = models.CharField(db_column='IMPETIQ', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modetiq = models.CharField(db_column='MODETIQ', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    md5 = models.CharField(db_column='MD5', max_length=32, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    superpremium = models.BooleanField(db_column='SUPERPREMIUM', blank=True, null=True)  # Field name made lowercase.
    dtspremium = models.DateTimeField(db_column='DTSPREMIUM', blank=True, null=True)  # Field name made lowercase.
    hdserv = models.BooleanField(db_column='HDSERV', blank=True, null=True)  # Field name made lowercase.
    nomecomputador = models.CharField(db_column='NOMECOMPUTADOR', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    certificadodigital = models.CharField(db_column='CERTIFICADODIGITAL', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serienfce = models.CharField(db_column='SERIENFCE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pagped = models.CharField(db_column='PAGPED', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    textobtn = models.BooleanField(db_column='TEXTOBTN', blank=True, null=True)  # Field name made lowercase.
    tpnfconsumidor = models.CharField(db_column='TPNFCONSUMIDOR', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    seriesat = models.IntegerField(db_column='SERIESAT', blank=True, null=True)  # Field name made lowercase.
    csc = models.CharField(db_column='CSC', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    paginacodimp = models.IntegerField(db_column='PAGINACODIMP', blank=True, null=True)  # Field name made lowercase.
    largurabobinaimp = models.IntegerField(db_column='LARGURABOBINAIMP', blank=True, null=True)  # Field name made lowercase.
    margemtopoimp = models.IntegerField(db_column='MARGEMTOPOIMP', blank=True, null=True)  # Field name made lowercase.
    margemfundoimp = models.IntegerField(db_column='MARGEMFUNDOIMP', blank=True, null=True)  # Field name made lowercase.
    margemesquerdaimp = models.IntegerField(db_column='MARGEMESQUERDAIMP', blank=True, null=True)  # Field name made lowercase.
    margemdireitaimp = models.IntegerField(db_column='MARGEMDIREITAIMP', blank=True, null=True)  # Field name made lowercase.
    imprconsumidor = models.CharField(db_column='IMPRCONSUMIDOR', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    miniimpconsumidor = models.BooleanField(db_column='MINIIMPCONSUMIDOR', blank=True, null=True)  # Field name made lowercase.
    idcsc = models.CharField(db_column='IDCSC', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    salto_cupom = models.IntegerField(db_column='SALTO_CUPOM', blank=True, null=True)  # Field name made lowercase.
    imprime1linha = models.BooleanField(db_column='IMPRIME1LINHA', blank=True, null=True)  # Field name made lowercase.
    ver_hist = models.BooleanField(db_column='VER_HIST', blank=True, null=True)  # Field name made lowercase.
    tipo_menu = models.IntegerField(db_column='TIPO_MENU', blank=True, null=True)  # Field name made lowercase.
    estilo_menu = models.IntegerField(db_column='ESTILO_MENU', blank=True, null=True)  # Field name made lowercase.
    mini_impped = models.CharField(db_column='MINI_IMPPED', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    largura = models.IntegerField(db_column='LARGURA', blank=True, null=True)  # Field name made lowercase.
    senha_cert = models.CharField(db_column='SENHA_CERT', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    esphera = models.BooleanField(db_column='ESPHERA', blank=True, null=True)  # Field name made lowercase.
    dtesphera = models.DateTimeField(db_column='DTESPHERA', blank=True, null=True)  # Field name made lowercase.
    lib = models.CharField(db_column='LIB', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFG'
        unique_together = (('nrohd', 'filial'),)


class Cflv(models.Model):
    cliforn = models.CharField(db_column='CLIFORN', primary_key=True, max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (CLIFORN, NBOOK) found, that is not supported. The first column is selected.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    desccf = models.FloatField(db_column='DESCCF', blank=True, null=True)  # Field name made lowercase.
    condpg = models.CharField(db_column='CONDPG', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFLV'
        unique_together = (('cliforn', 'nbook'),)


class Cfop(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ent_estado = models.CharField(db_column='ENT_ESTADO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ent_fora = models.CharField(db_column='ENT_FORA', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ent_exterior = models.CharField(db_column='ENT_EXTERIOR', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sai_estado = models.CharField(db_column='SAI_ESTADO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sai_fora = models.CharField(db_column='SAI_FORA', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sai_exterior = models.CharField(db_column='SAI_EXTERIOR', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isentopf = models.CharField(db_column='ISENTOPF', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stestado = models.CharField(db_column='STESTADO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stfora = models.CharField(db_column='STFORA', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CFOP'


class Cheque(models.Model):
    grupo = models.IntegerField(db_column='GRUPO', primary_key=True)  # Field name made lowercase.
    nominal = models.CharField(db_column='NOMINAL', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncheque = models.CharField(db_column='NCHEQUE', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    linha1 = models.CharField(db_column='LINHA1', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    linha2 = models.CharField(db_column='LINHA2', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    dtbanco = models.DateTimeField(db_column='DTBANCO', blank=True, null=True)  # Field name made lowercase.
    desd = models.BooleanField(db_column='DESD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHEQUE'


class Cliforn(models.Model):
    tipo = models.CharField(db_column='TIPO', primary_key=True, max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (TIPO, CODIGO) found, that is not supported. The first column is selected.
    codigo = models.CharField(db_column='CODIGO', max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgc = models.CharField(db_column='CGC', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.CharField(db_column='ATIVO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fj = models.CharField(db_column='FJ', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    razsocial = models.CharField(db_column='RAZSOCIAL', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telres = models.CharField(db_column='TELRES', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telcom = models.CharField(db_column='TELCOM', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tel2 = models.CharField(db_column='TEL2', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ramal = models.CharField(db_column='RAMAL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    inscr = models.CharField(db_column='INSCR', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='CONTATO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj1 = models.CharField(db_column='SUBJ1', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj2 = models.CharField(db_column='SUBJ2', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endc = models.CharField(db_column='ENDC', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairroc = models.CharField(db_column='BAIRROC', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidc = models.CharField(db_column='CIDC', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cepc = models.CharField(db_column='CEPC', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ufc = models.CharField(db_column='UFC', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telc = models.CharField(db_column='TELC', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contatoc = models.CharField(db_column='CONTATOC', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fretecta = models.CharField(db_column='FRETECTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='CARGO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filiacao = models.CharField(db_column='FILIACAO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    condpg = models.CharField(db_column='CONDPG', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descn = models.FloatField(db_column='DESCN', blank=True, null=True)  # Field name made lowercase.
    desci = models.FloatField(db_column='DESCI', blank=True, null=True)  # Field name made lowercase.
    desccli = models.FloatField(db_column='DESCCLI', blank=True, null=True)  # Field name made lowercase.
    limite = models.FloatField(db_column='LIMITE', blank=True, null=True)  # Field name made lowercase.
    spc = models.BooleanField(db_column='SPC', blank=True, null=True)  # Field name made lowercase.
    setbol = models.CharField(db_column='SETBOL', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo_cli = models.CharField(db_column='TIPO_CLI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cadlocal = models.CharField(db_column='CADLOCAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    dtnasc = models.DateTimeField(db_column='DTNASC', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    distrib = models.CharField(db_column='DISTRIB', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ddd = models.CharField(db_column='DDD', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compradir = models.BooleanField(db_column='COMPRADIR', blank=True, null=True)  # Field name made lowercase.
    fatmin = models.FloatField(db_column='FATMIN', blank=True, null=True)  # Field name made lowercase.
    pais = models.IntegerField(db_column='PAIS', blank=True, null=True)  # Field name made lowercase.
    paisc = models.IntegerField(db_column='PAISC', blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='COMPLEMENTO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codmun = models.IntegerField(db_column='CODMUN', blank=True, null=True)  # Field name made lowercase.
    emailnfe = models.CharField(db_column='EMAILNFE', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    im = models.CharField(db_column='IM', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    suframa = models.CharField(db_column='SUFRAMA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ipi = models.BooleanField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    simples = models.BooleanField(db_column='SIMPLES', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sbscard = models.IntegerField(db_column='SBSCARD', blank=True, null=True)  # Field name made lowercase.
    contribuinte = models.BooleanField(db_column='CONTRIBUINTE', blank=True, null=True)  # Field name made lowercase.
    estrangeiro = models.BooleanField(db_column='ESTRANGEIRO', blank=True, null=True)  # Field name made lowercase.
    arred = models.IntegerField(db_column='ARRED', blank=True, null=True)  # Field name made lowercase.
    emailbol = models.CharField(db_column='EMAILBOL', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome_ev = models.CharField(db_column='NOME_EV', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tp_cobranca = models.IntegerField(db_column='TP_COBRANCA', blank=True, null=True)  # Field name made lowercase.
    at_cobranca = models.CharField(db_column='AT_COBRANCA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_mercos = models.IntegerField(db_column='COD_MERCOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CLIFORN'
        unique_together = (('tipo', 'codigo'),)


class Comcli(models.Model):
    vendedor = models.CharField(db_column='VENDEDOR', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (VENDEDOR, CLIENTE, DESCMAX) found, that is not supported. The first column is selected.
    cliente = models.CharField(db_column='CLIENTE', max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    descmin = models.FloatField(db_column='DESCMIN', blank=True, null=True)  # Field name made lowercase.
    descmax = models.FloatField(db_column='DESCMAX')  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMCLI'
        unique_together = (('vendedor', 'cliente', 'descmax'),)


class Comeditora(models.Model):
    vendedor = models.CharField(db_column='VENDEDOR', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (VENDEDOR, EDITORA, DESCMAX) found, that is not supported. The first column is selected.
    editora = models.CharField(db_column='EDITORA', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    descmin = models.FloatField(db_column='DESCMIN', blank=True, null=True)  # Field name made lowercase.
    descmax = models.FloatField(db_column='DESCMAX')  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMEDITORA'
        unique_together = (('vendedor', 'editora', 'descmax'),)


class Comprod(models.Model):
    vendedor = models.CharField(db_column='VENDEDOR', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (VENDEDOR, NBOOK, DESCMAX) found, that is not supported. The first column is selected.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    descmin = models.FloatField(db_column='DESCMIN', blank=True, null=True)  # Field name made lowercase.
    descmax = models.FloatField(db_column='DESCMAX')  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMPROD'
        unique_together = (('vendedor', 'nbook', 'descmax'),)


class Comsecao(models.Model):
    vendedor = models.CharField(db_column='VENDEDOR', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (VENDEDOR, SECAO, DESCMAX) found, that is not supported. The first column is selected.
    secao = models.CharField(db_column='SECAO', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    descmin = models.FloatField(db_column='DESCMIN', blank=True, null=True)  # Field name made lowercase.
    descmax = models.FloatField(db_column='DESCMAX')  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COMSECAO'
        unique_together = (('vendedor', 'secao', 'descmax'),)


class Configbol(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CODIGO) found, that is not supported. The first column is selected.
    codigo = models.CharField(db_column='CODIGO', max_length=7, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    lpp = models.IntegerField(db_column='LPP', blank=True, null=True)  # Field name made lowercase.
    nlinhas = models.IntegerField(db_column='NLINHAS', blank=True, null=True)  # Field name made lowercase.
    llocal = models.IntegerField(db_column='LLOCAL', blank=True, null=True)  # Field name made lowercase.
    clocal = models.IntegerField(db_column='CLOCAL', blank=True, null=True)  # Field name made lowercase.
    ldtvencto = models.IntegerField(db_column='LDTVENCTO', blank=True, null=True)  # Field name made lowercase.
    cdtvencto = models.IntegerField(db_column='CDTVENCTO', blank=True, null=True)  # Field name made lowercase.
    ldtdoc = models.IntegerField(db_column='LDTDOC', blank=True, null=True)  # Field name made lowercase.
    cdtdoc = models.IntegerField(db_column='CDTDOC', blank=True, null=True)  # Field name made lowercase.
    lndoc = models.IntegerField(db_column='LNDOC', blank=True, null=True)  # Field name made lowercase.
    cndoc = models.IntegerField(db_column='CNDOC', blank=True, null=True)  # Field name made lowercase.
    lvldoc = models.IntegerField(db_column='LVLDOC', blank=True, null=True)  # Field name made lowercase.
    cvldoc = models.IntegerField(db_column='CVLDOC', blank=True, null=True)  # Field name made lowercase.
    linst1 = models.IntegerField(db_column='LINST1', blank=True, null=True)  # Field name made lowercase.
    cinst1 = models.IntegerField(db_column='CINST1', blank=True, null=True)  # Field name made lowercase.
    linst2 = models.IntegerField(db_column='LINST2', blank=True, null=True)  # Field name made lowercase.
    cinst2 = models.IntegerField(db_column='CINST2', blank=True, null=True)  # Field name made lowercase.
    linst3 = models.IntegerField(db_column='LINST3', blank=True, null=True)  # Field name made lowercase.
    cinst3 = models.IntegerField(db_column='CINST3', blank=True, null=True)  # Field name made lowercase.
    lsacado = models.IntegerField(db_column='LSACADO', blank=True, null=True)  # Field name made lowercase.
    csacado = models.IntegerField(db_column='CSACADO', blank=True, null=True)  # Field name made lowercase.
    lend = models.IntegerField(db_column='LEND', blank=True, null=True)  # Field name made lowercase.
    cend = models.IntegerField(db_column='CEND', blank=True, null=True)  # Field name made lowercase.
    lcep = models.IntegerField(db_column='LCEP', blank=True, null=True)  # Field name made lowercase.
    ccep = models.IntegerField(db_column='CCEP', blank=True, null=True)  # Field name made lowercase.
    localpg = models.CharField(db_column='LOCALPG', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    agencia = models.CharField(db_column='AGENCIA', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    multa = models.FloatField(db_column='MULTA', blank=True, null=True)  # Field name made lowercase.
    juros = models.FloatField(db_column='JUROS', blank=True, null=True)  # Field name made lowercase.
    linst4 = models.IntegerField(db_column='LINST4', blank=True, null=True)  # Field name made lowercase.
    cinst4 = models.IntegerField(db_column='CINST4', blank=True, null=True)  # Field name made lowercase.
    convenio = models.CharField(db_column='CONVENIO', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    carteira = models.CharField(db_column='CARTEIRA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    variacao = models.CharField(db_column='VARIACAO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tdias = models.CharField(db_column='TDIAS', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    diasprot = models.IntegerField(db_column='DIASPROT', blank=True, null=True)  # Field name made lowercase.
    seq = models.FloatField(db_column='SEQ', blank=True, null=True)  # Field name made lowercase.
    tipoimp = models.CharField(db_column='TIPOIMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impbol = models.CharField(db_column='IMPBOL', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ultarq = models.IntegerField(db_column='ULTARQ', blank=True, null=True)  # Field name made lowercase.
    tipobol = models.CharField(db_column='TIPOBOL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cob_reg = models.BooleanField(db_column='COB_REG', blank=True, null=True)  # Field name made lowercase.
    protestar = models.BooleanField(db_column='PROTESTAR', blank=True, null=True)  # Field name made lowercase.
    benef = models.CharField(db_column='BENEF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pix = models.BooleanField(db_column='PIX', blank=True, null=True)  # Field name made lowercase.
    tipo_pix = models.IntegerField(db_column='TIPO_PIX', blank=True, null=True)  # Field name made lowercase.
    chave_pix = models.CharField(db_column='CHAVE_PIX', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONFIGBOL'
        unique_together = (('filial', 'codigo'),)


class Conservacao(models.Model):
    descricao = models.CharField(db_column='DESCRICAO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    marca = models.BooleanField(db_column='MARCA', blank=True, null=True)  # Field name made lowercase.
    ordem = models.IntegerField(db_column='ORDEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONSERVACAO'


class Conta(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=9, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    numbco = models.CharField(db_column='NUMBCO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numage = models.CharField(db_column='NUMAGE', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomeage = models.CharField(db_column='NOMEAGE', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    setch = models.CharField(db_column='SETCH', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    setbol = models.CharField(db_column='SETBOL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codctb = models.CharField(db_column='CODCTB', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpconta = models.CharField(db_column='TPCONTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTA'


class Contador(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='COMPLEMENTO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codmun = models.IntegerField(db_column='CODMUN', blank=True, null=True)  # Field name made lowercase.
    telcom = models.CharField(db_column='TELCOM', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgc = models.CharField(db_column='CGC', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    crc = models.CharField(db_column='CRC', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    autxml = models.BooleanField(db_column='AUTXML', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTADOR'


class Contatos(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    depto = models.CharField(db_column='DEPTO', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='CARGO', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtnasc = models.DateTimeField(db_column='DTNASC', blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='TELEFONE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    celular = models.CharField(db_column='CELULAR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codcontato = models.IntegerField(db_column='CODCONTATO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTATOS'


class Correios(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CONTRATO) found, that is not supported. The first column is selected.
    contrato = models.CharField(db_column='CONTRATO', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    cartao = models.CharField(db_column='CARTAO', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_adm = models.CharField(db_column='COD_ADM', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modico = models.CharField(db_column='MODICO', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sufixo = models.CharField(db_column='SUFIXO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtmodico = models.IntegerField(db_column='QTMODICO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CORREIOS'
        unique_together = (('filial', 'contrato'),)


class Cpvd(models.Model):
    editora = models.CharField(db_column='EDITORA', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (EDITORA, NBOOK) found, that is not supported. The first column is selected.
    neditora = models.CharField(db_column='NEDITORA', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtcompra = models.IntegerField(db_column='QTCOMPRA', blank=True, null=True)  # Field name made lowercase.
    vlcompra = models.FloatField(db_column='VLCOMPRA', blank=True, null=True)  # Field name made lowercase.
    qtvenda = models.IntegerField(db_column='QTVENDA', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    isbn1 = models.CharField(db_column='ISBN1', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CPVD'
        unique_together = (('editora', 'nbook'),)


class Credcl(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlnf = models.FloatField(db_column='VLNF', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregfin = models.IntegerField(db_column='NREGFIN', blank=True, null=True)  # Field name made lowercase.
    nregcx = models.IntegerField(db_column='NREGCX', blank=True, null=True)  # Field name made lowercase.
    credito = models.FloatField(db_column='CREDITO', blank=True, null=True)  # Field name made lowercase.
    vlbaixa = models.FloatField(db_column='VLBAIXA', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CREDCL'


class Credff(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlnf = models.FloatField(db_column='VLNF', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregfin = models.IntegerField(db_column='NREGFIN', blank=True, null=True)  # Field name made lowercase.
    credito = models.FloatField(db_column='CREDITO', blank=True, null=True)  # Field name made lowercase.
    vlbaixa = models.FloatField(db_column='VLBAIXA', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregcx = models.IntegerField(db_column='NREGCX', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CREDFF'


class Ctdiraut(models.Model):
    contrato = models.IntegerField(db_column='CONTRATO', primary_key=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTDIRAUT'


class Ctg(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (NBOOK, FILIAL) found, that is not supported. The first column is selected.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    lj = models.IntegerField(db_column='LJ', blank=True, null=True)  # Field name made lowercase.
    dep = models.IntegerField(db_column='DEP', blank=True, null=True)  # Field name made lowercase.
    lj2 = models.IntegerField(db_column='LJ2', blank=True, null=True)  # Field name made lowercase.
    dep2 = models.IntegerField(db_column='DEP2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTG'
        unique_together = (('nbook', 'filial'),)


class Ctr(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='HORA', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    parc = models.SmallIntegerField(db_column='PARC', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vloutros = models.FloatField(db_column='VLOUTROS', blank=True, null=True)  # Field name made lowercase.
    vlipi = models.FloatField(db_column='VLIPI', blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs1 = models.CharField(db_column='OBS1', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs2 = models.CharField(db_column='OBS2', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fretecta = models.CharField(db_column='FRETECTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtcompl = models.IntegerField(db_column='QTCOMPL', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(db_column='ESPECIE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    peso = models.CharField(db_column='PESO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pliq = models.CharField(db_column='PLIQ', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    boleto = models.CharField(db_column='BOLETO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    obsnf = models.TextField(db_column='OBSNF', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dt_docto = models.DateTimeField(db_column='DT_DOCTO', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bx = models.CharField(db_column='BX', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    rastreamento = models.CharField(db_column='RASTREAMENTO', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.FloatField(db_column='VLFRETE', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    narq = models.IntegerField(db_column='NARQ', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    vlicms = models.FloatField(db_column='VLICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    vlicmsst = models.FloatField(db_column='VLICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    vlacess = models.FloatField(db_column='VLACESS', blank=True, null=True)  # Field name made lowercase.
    vlseg = models.FloatField(db_column='VLSEG', blank=True, null=True)  # Field name made lowercase.
    iimp = models.FloatField(db_column='IIMP', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    cpfcnpj = models.CharField(db_column='CPFCNPJ', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    atualizar = models.CharField(db_column='ATUALIZAR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aluno = models.IntegerField(db_column='ALUNO', blank=True, null=True)  # Field name made lowercase.
    npedcli = models.CharField(db_column='NPEDCLI', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    st_log = models.IntegerField(db_column='ST_LOG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTR'


class Ctrcx(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CAIXA, NFECHA) found, that is not supported. The first column is selected.
    caixa = models.CharField(db_column='CAIXA', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nfecha = models.IntegerField(db_column='NFECHA')  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    operador = models.CharField(db_column='OPERADOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    horafim = models.DateTimeField(db_column='HORAFIM', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    fechado = models.BooleanField(db_column='FECHADO', blank=True, null=True)  # Field name made lowercase.
    conferente = models.CharField(db_column='CONFERENTE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRCX'
        unique_together = (('filial', 'caixa', 'nfecha'),)


class Ctrdfe(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, TPNF, SERIE) found, that is not supported. The first column is selected.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    numero = models.IntegerField(db_column='NUMERO', blank=True, null=True)  # Field name made lowercase.
    imp = models.BooleanField(db_column='IMP', blank=True, null=True)  # Field name made lowercase.
    cons_indev = models.DateTimeField(db_column='CONS_INDEV', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRDFE'
        unique_together = (('filial', 'tpnf', 'serie'),)


class Ctrinv(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    moeda = models.CharField(db_column='MOEDA', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    via = models.CharField(db_column='VIA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtcompl = models.IntegerField(db_column='QTCOMPL', blank=True, null=True)  # Field name made lowercase.
    peso = models.CharField(db_column='PESO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(db_column='ESPECIE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    venda = models.CharField(db_column='VENDA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    txcambio = models.FloatField(db_column='TXCAMBIO', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.FloatField(db_column='VLFRETE', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vloutros = models.FloatField(db_column='VLOUTROS', blank=True, null=True)  # Field name made lowercase.
    npedvd = models.IntegerField(db_column='NPEDVD', blank=True, null=True)  # Field name made lowercase.
    pesoliq = models.CharField(db_column='PESOLIQ', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRINV'


class Ctrlista(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    atualpr = models.BooleanField(db_column='ATUALPR', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    atualizar = models.CharField(db_column='ATUALIZAR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRLISTA'


class Ctrnf(models.Model):
    serie = models.CharField(db_column='SERIE', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    imp = models.BooleanField(db_column='IMP', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfce = models.IntegerField(db_column='NFCE', blank=True, null=True)  # Field name made lowercase.
    impnfce = models.BooleanField(db_column='IMPNFCE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRNF'


class Ctrout(models.Model):
    nped = models.AutoField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='HORA', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    parc = models.SmallIntegerField(db_column='PARC', blank=True, null=True)  # Field name made lowercase.
    docout = models.CharField(db_column='DOCOUT', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vloutros = models.FloatField(db_column='VLOUTROS', blank=True, null=True)  # Field name made lowercase.
    vlipi = models.FloatField(db_column='VLIPI', blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs1 = models.CharField(db_column='OBS1', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs2 = models.CharField(db_column='OBS2', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fretecta = models.CharField(db_column='FRETECTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtcompl = models.IntegerField(db_column='QTCOMPL', blank=True, null=True)  # Field name made lowercase.
    especie = models.CharField(db_column='ESPECIE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    peso = models.CharField(db_column='PESO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pliq = models.CharField(db_column='PLIQ', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    boleto = models.CharField(db_column='BOLETO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    obsnf = models.TextField(db_column='OBSNF', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dt_docto = models.DateTimeField(db_column='DT_DOCTO', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bx = models.CharField(db_column='BX', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    rastreamento = models.CharField(db_column='RASTREAMENTO', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.FloatField(db_column='VLFRETE', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    lista_tipodoc_modelo_docfisc = models.IntegerField(db_column='LISTA_TIPODOC_MODELO_DOCFISC', blank=True, null=True)  # Field name made lowercase.
    narq = models.IntegerField(db_column='NARQ', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    vlicms = models.FloatField(db_column='VLICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    vlicmsst = models.FloatField(db_column='VLICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    vlacess = models.FloatField(db_column='VLACESS', blank=True, null=True)  # Field name made lowercase.
    vlseg = models.FloatField(db_column='VLSEG', blank=True, null=True)  # Field name made lowercase.
    cpfcnpj = models.CharField(db_column='CPFCNPJ', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    iimp = models.FloatField(db_column='IIMP', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    atualizar = models.CharField(db_column='ATUALIZAR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aluno = models.IntegerField(db_column='ALUNO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTROUT'


class Ctrped(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='HORA', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    env = models.CharField(db_column='ENV', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vloutros = models.FloatField(db_column='VLOUTROS', blank=True, null=True)  # Field name made lowercase.
    vlipi = models.FloatField(db_column='VLIPI', blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs1 = models.CharField(db_column='OBS1', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs2 = models.CharField(db_column='OBS2', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fretecta = models.CharField(db_column='FRETECTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    stsite = models.IntegerField(db_column='STSITE', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    parc = models.IntegerField(db_column='PARC', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    validade = models.CharField(db_column='VALIDADE', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    rastreamento = models.CharField(db_column='RASTREAMENTO', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    autoriza = models.CharField(db_column='AUTORIZA', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtautoriza = models.DateTimeField(db_column='DTAUTORIZA', blank=True, null=True)  # Field name made lowercase.
    usautoriza = models.CharField(db_column='USAUTORIZA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    estorno = models.IntegerField(db_column='ESTORNO', blank=True, null=True)  # Field name made lowercase.
    conf = models.CharField(db_column='CONF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    narq = models.IntegerField(db_column='NARQ', blank=True, null=True)  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    atualizar = models.CharField(db_column='ATUALIZAR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aluno = models.IntegerField(db_column='ALUNO', blank=True, null=True)  # Field name made lowercase.
    travapr = models.BooleanField(db_column='TRAVAPR', blank=True, null=True)  # Field name made lowercase.
    cod_mktplace = models.CharField(db_column='COD_MKTPLACE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtentrega = models.DateTimeField(db_column='DTENTREGA', blank=True, null=True)  # Field name made lowercase.
    priori = models.IntegerField(db_column='PRIORI', blank=True, null=True)  # Field name made lowercase.
    vlacess = models.FloatField(db_column='VLACESS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRPED'


class Ctrrec(models.Model):
    recibo = models.IntegerField(db_column='RECIBO', primary_key=True)  # Field name made lowercase.
    cliente = models.CharField(max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcanc = models.DateTimeField(db_column='DTCANC', blank=True, null=True)  # Field name made lowercase.
    uscanc = models.CharField(db_column='USCANC', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRREC'


class Ctrver(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=13, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    versao = models.CharField(db_column='VERSAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtversao = models.DateTimeField(db_column='DTVERSAO', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    chave = models.CharField(db_column='CHAVE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTRVER'


class Desd(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ccusto = models.CharField(db_column='CCUSTO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    nf = models.CharField(db_column='NF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DESD'


class Di(models.Model):
    nreg = models.IntegerField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nint = models.IntegerField(db_column='NINT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtdi = models.DateTimeField(db_column='DTDI', blank=True, null=True)  # Field name made lowercase.
    locdesemb = models.CharField(db_column='LOCDESEMB', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtdesemb = models.DateTimeField(db_column='DTDESEMB', blank=True, null=True)  # Field name made lowercase.
    codexp = models.CharField(db_column='CODEXP', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    adicao = models.IntegerField(db_column='ADICAO', blank=True, null=True)  # Field name made lowercase.
    seqadicao = models.IntegerField(db_column='SEQADICAO', blank=True, null=True)  # Field name made lowercase.
    codfab = models.CharField(db_column='CODFAB', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vldesc = models.FloatField(db_column='VLDESC', blank=True, null=True)  # Field name made lowercase.
    tpviatransp = models.IntegerField(db_column='TPVIATRANSP', blank=True, null=True)  # Field name made lowercase.
    vafrmm = models.FloatField(db_column='VAFRMM', blank=True, null=True)  # Field name made lowercase.
    tpintermedio = models.IntegerField(db_column='TPINTERMEDIO', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ufterceiro = models.CharField(db_column='UFTERCEIRO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndraw = models.IntegerField(db_column='NDRAW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DI'


class Difped(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregant = models.IntegerField(db_column='NREGANT', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlistaped = models.FloatField(db_column='PRLISTAPED', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunitped = models.FloatField(db_column='PRUNITPED', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIFPED'


class Docout(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtemissao = models.DateTimeField(db_column='DTEMISSAO', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codfiscal = models.CharField(db_column='CODFISCAL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bx = models.CharField(db_column='BX', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    natop = models.CharField(db_column='NATOP', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlcontabil = models.FloatField(db_column='VLCONTABIL', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    impicms = models.FloatField(db_column='IMPICMS', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    impipi = models.FloatField(db_column='IMPIPI', blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.FloatField(db_column='VLFRETE', blank=True, null=True)  # Field name made lowercase.
    vlseg = models.FloatField(db_column='VLSEG', blank=True, null=True)  # Field name made lowercase.
    vlacess = models.FloatField(db_column='VLACESS', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs1 = models.CharField(db_column='OBS1', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs2 = models.CharField(db_column='OBS2', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    fretecta = models.CharField(db_column='FRETECTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obsnf = models.TextField(db_column='OBSNF', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipocf = models.CharField(db_column='TIPOCF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nossanf = models.BooleanField(db_column='NOSSANF')  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    lista_tipodoc_modelo_docfisc = models.IntegerField(db_column='LISTA_TIPODOC_MODELO_DOCFISC', blank=True, null=True)  # Field name made lowercase.
    statusnf = models.IntegerField(db_column='STATUSNF', blank=True, null=True)  # Field name made lowercase.
    xml = models.CharField(db_column='XML', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    chavexml = models.CharField(db_column='CHAVEXML', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    impicmsst = models.FloatField(db_column='IMPICMSST', blank=True, null=True)  # Field name made lowercase.
    iimp = models.FloatField(db_column='IIMP', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    totprod = models.FloatField(db_column='TOTPROD', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    tpcte = models.IntegerField(db_column='TPCTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOCOUT'


class Dolar(models.Model):
    data = models.DateTimeField(db_column='DATA', primary_key=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DOLAR'


class EditMp(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    estmin = models.IntegerField(db_column='ESTMIN', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    cross_s_estoque = models.IntegerField(db_column='CROSS_S_ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    catavento = models.CharField(db_column='CATAVENTO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_li = models.IntegerField(db_column='COD_LI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CODIGO) found, that is not supported. The first column is selected.
    cod_tray = models.IntegerField(db_column='COD_TRAY', blank=True, null=True)  # Field name made lowercase.
    li = models.BooleanField(db_column='LI', blank=True, null=True)  # Field name made lowercase.
    desc_li = models.FloatField(db_column='DESC_LI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EDIT_MP'
        unique_together = (('filial', 'codigo'),)


class EdExt(models.Model):
    editora = models.CharField(db_column='EDITORA', primary_key=True, max_length=100, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ED_EXT'


class Empresa(models.Model):
    razsocial = models.CharField(db_column='RAZSOCIAL', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telcom = models.CharField(db_column='TELCOM', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telres = models.CharField(db_column='TELRES', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgc = models.CharField(db_column='CGC', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    inscr = models.CharField(db_column='INSCR', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='CONTATO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ltimbre1 = models.CharField(db_column='LTIMBRE1', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ltimbre2 = models.CharField(db_column='LTIMBRE2', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ltimbre3 = models.CharField(db_column='LTIMBRE3', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    rodape = models.CharField(db_column='RODAPE', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    corfundo = models.CharField(db_column='CORFUNDO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    logo = models.CharField(db_column='LOGO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    timbre = models.CharField(db_column='TIMBRE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fator = models.FloatField(db_column='FATOR', blank=True, null=True)  # Field name made lowercase.
    servidor = models.CharField(db_column='SERVIDOR', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    servpop3 = models.CharField(db_column='SERVPOP3', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    servemail = models.CharField(db_column='SERVEMAIL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impnf = models.CharField(db_column='IMPNF', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtnf = models.SmallIntegerField(db_column='QTNF', blank=True, null=True)  # Field name made lowercase.
    modcupom = models.CharField(db_column='MODCUPOM', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impped = models.CharField(db_column='IMPPED', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modped = models.CharField(db_column='MODPED', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    vlbatual = models.IntegerField(db_column='VLBATUAL', blank=True, null=True)  # Field name made lowercase.
    tipoarq = models.CharField(db_column='TIPOARQ', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ordemped = models.CharField(db_column='ORDEMPED', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pedff = models.CharField(db_column='PEDFF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlnf = models.CharField(db_column='VLNF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortnped = models.BooleanField(db_column='SHORTNPED', blank=True, null=True)  # Field name made lowercase.
    somaest = models.BooleanField(db_column='SOMAEST', blank=True, null=True)  # Field name made lowercase.
    ematriz = models.CharField(db_column='EMATRIZ', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bloqatraso = models.BooleanField(db_column='BLOQATRASO', blank=True, null=True)  # Field name made lowercase.
    tolatraso = models.IntegerField(db_column='TOLATRASO', blank=True, null=True)  # Field name made lowercase.
    ldiainadim = models.IntegerField(db_column='LDIAINADIM', blank=True, null=True)  # Field name made lowercase.
    descricaoped = models.CharField(db_column='DESCRICAOPED', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfcod = models.CharField(db_column='NFCOD', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descnf = models.CharField(db_column='DESCNF', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliente = models.BooleanField(db_column='CLIENTE', blank=True, null=True)  # Field name made lowercase.
    nped = models.BooleanField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.BooleanField(db_column='VENDEDOR', blank=True, null=True)  # Field name made lowercase.
    lentrega = models.BooleanField(db_column='LENTREGA', blank=True, null=True)  # Field name made lowercase.
    obsfixanf = models.TextField(db_column='OBSFIXANF', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    frmpgto = models.CharField(db_column='FRMPGTO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impbolvd = models.BooleanField(db_column='IMPBOLVD', blank=True, null=True)  # Field name made lowercase.
    ctg = models.DateTimeField(db_column='CTG', blank=True, null=True)  # Field name made lowercase.
    mostrarcsg = models.BooleanField(db_column='MOSTRARCSG', blank=True, null=True)  # Field name made lowercase.
    bloqndisp = models.BooleanField(db_column='BLOQNDISP', blank=True, null=True)  # Field name made lowercase.
    numctg = models.IntegerField(db_column='NUMCTG', blank=True, null=True)  # Field name made lowercase.
    ftp = models.CharField(db_column='FTP', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    userftp = models.CharField(db_column='USERFTP', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senhaftp = models.CharField(db_column='SENHAFTP', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortnnf = models.BooleanField(db_column='SHORTNNF', blank=True, null=True)  # Field name made lowercase.
    dirftp = models.CharField(db_column='DIRFTP', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sodisp = models.BooleanField(db_column='SODISP', blank=True, null=True)  # Field name made lowercase.
    dtsincr = models.DateTimeField(db_column='DTSINCR', blank=True, null=True)  # Field name made lowercase.
    svl = models.IntegerField(db_column='SVL', blank=True, null=True)  # Field name made lowercase.
    ultpedsite = models.IntegerField(db_column='ULTPEDSITE', blank=True, null=True)  # Field name made lowercase.
    impetiqvd = models.BooleanField(db_column='IMPETIQVD', blank=True, null=True)  # Field name made lowercase.
    descmax = models.FloatField(db_column='DESCMAX', blank=True, null=True)  # Field name made lowercase.
    parcmax = models.IntegerField(db_column='PARCMAX', blank=True, null=True)  # Field name made lowercase.
    autobrig = models.BooleanField(db_column='AUTOBRIG', blank=True, null=True)  # Field name made lowercase.
    altprlista = models.BooleanField(db_column='ALTPRLISTA', blank=True, null=True)  # Field name made lowercase.
    contatoe = models.CharField(db_column='CONTATOE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ende = models.CharField(db_column='ENDE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cepe = models.CharField(db_column='CEPE', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cide = models.CharField(db_column='CIDE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ufe = models.CharField(db_column='UFE', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tele = models.CharField(db_column='TELE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlbolsite = models.FloatField(db_column='VLBOLSITE', blank=True, null=True)  # Field name made lowercase.
    agruparel = models.BooleanField(db_column='AGRUPAREL', blank=True, null=True)  # Field name made lowercase.
    impcp = models.BooleanField(db_column='IMPCP', blank=True, null=True)  # Field name made lowercase.
    ssl = models.BooleanField(db_column='SSL', blank=True, null=True)  # Field name made lowercase.
    portasmtp = models.IntegerField(db_column='PORTASMTP', blank=True, null=True)  # Field name made lowercase.
    ftppassivo = models.BooleanField(db_column='FTPPASSIVO', blank=True, null=True)  # Field name made lowercase.
    calcpesonf = models.BooleanField(db_column='CALCPESONF', blank=True, null=True)  # Field name made lowercase.
    travafiscal = models.DateTimeField(db_column='TRAVAFISCAL', blank=True, null=True)  # Field name made lowercase.
    codmun = models.IntegerField(db_column='CODMUN', blank=True, null=True)  # Field name made lowercase.
    coduf = models.IntegerField(db_column='CODUF', blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='COMPLEMENTO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfe = models.BooleanField(db_column='NFE', blank=True, null=True)  # Field name made lowercase.
    homologacao = models.BooleanField(db_column='HOMOLOGACAO', blank=True, null=True)  # Field name made lowercase.
    contingencia = models.IntegerField(db_column='CONTINGENCIA', blank=True, null=True)  # Field name made lowercase.
    dirnfe = models.CharField(db_column='DIRNFE', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    timbreweb = models.CharField(db_column='TIMBREWEB', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    timbrenfe = models.CharField(db_column='TIMBRENFE', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    crt = models.IntegerField(db_column='CRT', blank=True, null=True)  # Field name made lowercase.
    pedirsinal = models.BooleanField(db_column='PEDIRSINAL', blank=True, null=True)  # Field name made lowercase.
    sinalobrig = models.BooleanField(db_column='SINALOBRIG', blank=True, null=True)  # Field name made lowercase.
    tema = models.CharField(db_column='TEMA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impxml = models.BooleanField(db_column='IMPXML', blank=True, null=True)  # Field name made lowercase.
    checaprorc = models.BooleanField(db_column='CHECAPRORC', blank=True, null=True)  # Field name made lowercase.
    altprdevff = models.BooleanField(db_column='ALTPRDEVFF', blank=True, null=True)  # Field name made lowercase.
    prvdicms = models.BooleanField(db_column='PRVDICMS', blank=True, null=True)  # Field name made lowercase.
    infdp = models.BooleanField(db_column='INFDP', blank=True, null=True)  # Field name made lowercase.
    fatconf = models.BooleanField(db_column='FATCONF', blank=True, null=True)  # Field name made lowercase.
    im = models.CharField(db_column='IM', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    suframa = models.CharField(db_column='SUFRAMA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contador = models.CharField(db_column='CONTADOR', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cnae = models.CharField(db_column='CNAE', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtinicio = models.DateTimeField(db_column='DTINICIO', blank=True, null=True)  # Field name made lowercase.
    parcmin = models.FloatField(db_column='PARCMIN', blank=True, null=True)  # Field name made lowercase.
    dtinventario = models.DateTimeField(db_column='DTINVENTARIO', blank=True, null=True)  # Field name made lowercase.
    tpinventario = models.IntegerField(db_column='TPINVENTARIO', blank=True, null=True)  # Field name made lowercase.
    decimaisprunitdanfe = models.IntegerField(db_column='DECIMAISPRUNITDANFE', blank=True, null=True)  # Field name made lowercase.
    cadcfcompleto = models.BooleanField(db_column='CADCFCOMPLETO', blank=True, null=True)  # Field name made lowercase.
    padrao_descricao_nfe = models.IntegerField(db_column='PADRAO_DESCRICAO_NFE', blank=True, null=True)  # Field name made lowercase.
    nfce = models.BooleanField(db_column='NFCE', blank=True, null=True)  # Field name made lowercase.
    gravar_sair_atorc = models.BooleanField(db_column='GRAVAR_SAIR_ATORC', blank=True, null=True)  # Field name made lowercase.
    ftp_site = models.CharField(db_column='FTP_SITE', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    userftp_site = models.CharField(db_column='USERFTP_SITE', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senhaftp_site = models.CharField(db_column='SENHAFTP_SITE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dirftp_site = models.CharField(db_column='DIRFTP_SITE', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ftppassivo_site = models.BooleanField(db_column='FTPPASSIVO_SITE', blank=True, null=True)  # Field name made lowercase.
    vlb_site = models.IntegerField(db_column='VLB_SITE', blank=True, null=True)  # Field name made lowercase.
    mod_danfe = models.IntegerField(db_column='MOD_DANFE', blank=True, null=True)  # Field name made lowercase.
    tp_bal = models.IntegerField(db_column='TP_BAL', blank=True, null=True)  # Field name made lowercase.
    gr_bal = models.CharField(db_column='GR_BAL', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obsfixanfce = models.TextField(db_column='OBSFIXANFCE', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    versao_dfe = models.CharField(db_column='VERSAO_DFE', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usar_leitorcb = models.BooleanField(db_column='USAR_LEITORCB', blank=True, null=True)  # Field name made lowercase.
    offline = models.BooleanField(db_column='OFFLINE', blank=True, null=True)  # Field name made lowercase.
    encomenda = models.BooleanField(db_column='ENCOMENDA', blank=True, null=True)  # Field name made lowercase.
    transf_orc_ped = models.BooleanField(db_column='TRANSF_ORC_PED', blank=True, null=True)  # Field name made lowercase.
    dt_est_corte = models.DateTimeField(db_column='DT_EST_CORTE', blank=True, null=True)  # Field name made lowercase.
    cont_nfce = models.IntegerField(db_column='CONT_NFCE', blank=True, null=True)  # Field name made lowercase.
    descr_ev = models.TextField(db_column='DESCR_EV', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dt_escolar = models.DateTimeField(db_column='DT_ESCOLAR', blank=True, null=True)  # Field name made lowercase.
    nfe_br_dp = models.BooleanField(db_column='NFE_BR_DP', blank=True, null=True)  # Field name made lowercase.
    dt_inv_anual = models.DateTimeField(db_column='DT_INV_ANUAL', blank=True, null=True)  # Field name made lowercase.
    email_nfe = models.BooleanField(db_column='EMAIL_NFE', blank=True, null=True)  # Field name made lowercase.
    danfe_simplificado = models.BooleanField(db_column='DANFE_SIMPLIFICADO', blank=True, null=True)  # Field name made lowercase.
    nume = models.CharField(db_column='NUME', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairroe = models.CharField(db_column='BAIRROE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    comple = models.CharField(db_column='COMPLE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codmune = models.CharField(db_column='CODMUNE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    exped_online = models.BooleanField(db_column='EXPED_ONLINE', blank=True, null=True)  # Field name made lowercase.
    vlnfe_simplif = models.BooleanField(db_column='VLNFE_SIMPLIF', blank=True, null=True)  # Field name made lowercase.
    ftp_log = models.CharField(db_column='FTP_LOG', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dir_log = models.CharField(db_column='DIR_LOG', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    porta_log = models.IntegerField(db_column='PORTA_LOG', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPRESA'


class Entrega(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ende = models.CharField(db_column='ENDE', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairroe = models.CharField(db_column='BAIRROE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cide = models.CharField(db_column='CIDE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ufe = models.CharField(db_column='UFE', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cepe = models.CharField(db_column='CEPE', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tele = models.CharField(db_column='TELE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contatoe = models.CharField(db_column='CONTATOE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    paise = models.IntegerField(db_column='PAISE', blank=True, null=True)  # Field name made lowercase.
    nume = models.CharField(db_column='NUME', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    comple = models.CharField(db_column='COMPLE', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codmune = models.IntegerField(db_column='CODMUNE', blank=True, null=True)  # Field name made lowercase.
    codentrega = models.IntegerField(db_column='CODENTREGA', blank=True, null=True)  # Field name made lowercase.
    nregext = models.IntegerField(db_column='NREGEXT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENTREGA'


class Envassin(models.Model):
    codassin = models.IntegerField(db_column='CODASSIN', primary_key=True)  # Field name made lowercase. The composite primary key (CODASSIN, EXEMPLAR) found, that is not supported. The first column is selected.
    exemplar = models.IntegerField(db_column='EXEMPLAR')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtenv = models.DateTimeField(db_column='DTENV', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    impr = models.CharField(db_column='IMPR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtrec = models.DateTimeField(db_column='DTREC', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ENVASSIN'
        unique_together = (('codassin', 'exemplar'),)


class Espec(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=45, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estante = models.CharField(db_column='ESTANTE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    wpress = models.IntegerField(db_column='WPRESS', blank=True, null=True)  # Field name made lowercase.
    catavento = models.CharField(db_column='CATAVENTO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    li = models.IntegerField(db_column='LI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESPEC'


class EspecMp(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CODIGO) found, that is not supported. The first column is selected.
    codigo = models.CharField(db_column='CODIGO', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_li = models.IntegerField(db_column='COD_LI', blank=True, null=True)  # Field name made lowercase.
    cod_wpress = models.IntegerField(db_column='COD_WPRESS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESPEC_MP'
        unique_together = (('filial', 'codigo'),)


class Estantes(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTANTES'


class Estoque(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (NBOOK, FILIAL) found, that is not supported. The first column is selected.
    disp = models.IntegerField(db_column='DISP', blank=True, null=True)  # Field name made lowercase.
    reserva = models.IntegerField(db_column='RESERVA', blank=True, null=True)  # Field name made lowercase.
    qtped = models.IntegerField(db_column='QTPED', blank=True, null=True)  # Field name made lowercase.
    exame = models.IntegerField(db_column='EXAME', blank=True, null=True)  # Field name made lowercase.
    consig = models.IntegerField(db_column='CONSIG', blank=True, null=True)  # Field name made lowercase.
    dtatu = models.DateTimeField(db_column='DTATU', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dp = models.IntegerField(db_column='DP', blank=True, null=True)  # Field name made lowercase.
    ev = models.IntegerField(db_column='EV', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    locest = models.CharField(db_column='LOCEST', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.
    atualizar = models.CharField(db_column='Atualizar', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_ff = models.CharField(db_column='COD_FF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    disp_ff = models.IntegerField(db_column='DISP_FF', blank=True, null=True)  # Field name made lowercase.
    li = models.BooleanField(db_column='LI', blank=True, null=True)  # Field name made lowercase.
    cad_ok = models.BooleanField(db_column='CAD_OK', blank=True, null=True)  # Field name made lowercase.
    codprod_ff = models.IntegerField(db_column='CODPROD_FF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTOQUE'
        unique_together = (('nbook', 'filial'),)


class Estorno(models.Model):
    nsite = models.IntegerField(db_column='NSITE', primary_key=True)  # Field name made lowercase.
    dtestorno = models.DateTimeField(db_column='DTESTORNO', blank=True, null=True)  # Field name made lowercase.
    nrestorno = models.CharField(db_column='NRESTORNO', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlestorno = models.FloatField(db_column='VLESTORNO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ESTORNO'


class Etiquetas(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    nsite = models.CharField(db_column='NSITE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    etiqueta = models.CharField(db_column='ETIQUETA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    plp = models.CharField(db_column='PLP', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    servico = models.CharField(db_column='SERVICO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    st = models.IntegerField(db_column='ST', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETIQUETAS'


class EtiqMp(models.Model):
    nped = models.CharField(db_column='NPED', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    entrega = models.IntegerField(db_column='ENTREGA', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    st = models.IntegerField(db_column='ST', blank=True, null=True)  # Field name made lowercase.
    etiqueta = models.CharField(db_column='ETIQUETA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    plp = models.CharField(db_column='PLP', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    megarota = models.CharField(db_column='MEGAROTA', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    rota = models.CharField(db_column='ROTA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtprometida = models.CharField(db_column='DTPROMETIDA', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, PORTAL, NPED) found, that is not supported. The first column is selected.
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    servico = models.CharField(db_column='SERVICO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETIQ_MP'
        unique_together = (('filial', 'portal', 'nped'),)


class Fcp(models.Model):
    uf = models.CharField(db_column='UF', primary_key=True, max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (UF, NCM) found, that is not supported. The first column is selected.
    ncm = models.CharField(db_column='NCM', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    fcp = models.FloatField(db_column='FCP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FCP'
        unique_together = (('uf', 'ncm'),)


class Feriados(models.Model):
    dtferiado = models.DateTimeField(db_column='DTFERIADO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FERIADOS'


class Ffext(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    servidor = models.CharField(db_column='SERVIDOR', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomebd = models.CharField(db_column='NOMEBD', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estmin = models.IntegerField(db_column='ESTMIN', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    cod_cliente = models.CharField(db_column='COD_CLIENTE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    prioridade = models.IntegerField(db_column='PRIORIDADE', blank=True, null=True)  # Field name made lowercase.
    ult_cod = models.IntegerField(db_column='ULT_COD', blank=True, null=True)  # Field name made lowercase.
    pedaut = models.BooleanField(db_column='PEDAUT', blank=True, null=True)  # Field name made lowercase.
    cod_transp = models.IntegerField(db_column='COD_TRANSP', blank=True, null=True)  # Field name made lowercase.
    dropshipping = models.BooleanField(db_column='DROPSHIPPING', blank=True, null=True)  # Field name made lowercase.
    sinc = models.IntegerField(db_column='SINC', blank=True, null=True)  # Field name made lowercase.
    token = models.CharField(db_column='TOKEN', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sincplace = models.BooleanField(db_column='SINCPLACE', blank=True, null=True)  # Field name made lowercase.
    dt_token = models.DateTimeField(db_column='DT_TOKEN', blank=True, null=True)  # Field name made lowercase.
    dt_estff = models.DateTimeField(db_column='DT_ESTFF', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CODIGO) found, that is not supported. The first column is selected.
    ajpreco = models.BooleanField(db_column='AJPRECO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FFEXT'
        unique_together = (('filial', 'codigo'),)


class Fluxo(models.Model):
    dc = models.CharField(db_column='DC', primary_key=True, max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (DC, GRUPO, CCUSTO) found, that is not supported. The first column is selected.
    grupo = models.CharField(db_column='GRUPO', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    ccusto = models.CharField(db_column='CCUSTO', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    p1 = models.FloatField(db_column='P1', blank=True, null=True)  # Field name made lowercase.
    p2 = models.FloatField(db_column='P2', blank=True, null=True)  # Field name made lowercase.
    p3 = models.FloatField(db_column='P3', blank=True, null=True)  # Field name made lowercase.
    p4 = models.FloatField(db_column='P4', blank=True, null=True)  # Field name made lowercase.
    p5 = models.FloatField(db_column='P5', blank=True, null=True)  # Field name made lowercase.
    p6 = models.FloatField(db_column='P6', blank=True, null=True)  # Field name made lowercase.
    p7 = models.FloatField(db_column='P7', blank=True, null=True)  # Field name made lowercase.
    p8 = models.FloatField(db_column='P8', blank=True, null=True)  # Field name made lowercase.
    p9 = models.FloatField(db_column='P9', blank=True, null=True)  # Field name made lowercase.
    p10 = models.FloatField(db_column='P10', blank=True, null=True)  # Field name made lowercase.
    p11 = models.FloatField(db_column='P11', blank=True, null=True)  # Field name made lowercase.
    p12 = models.FloatField(db_column='P12', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FLUXO'
        unique_together = (('dc', 'grupo', 'ccusto'),)


class Fpg(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    parc = models.CharField(db_column='PARC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipopg = models.CharField(db_column='TIPOPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descto = models.CharField(db_column='DESCTO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cupom = models.CharField(db_column='CUPOM', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ctarec = models.BooleanField(db_column='CTAREC', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dc = models.CharField(db_column='DC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    prazo1 = models.IntegerField(db_column='PRAZO1', blank=True, null=True)  # Field name made lowercase.
    prazo2 = models.IntegerField(db_column='PRAZO2', blank=True, null=True)  # Field name made lowercase.
    taxa1 = models.FloatField(db_column='TAXA1', blank=True, null=True)  # Field name made lowercase.
    taxa2 = models.FloatField(db_column='TAXA2', blank=True, null=True)  # Field name made lowercase.
    textoecf = models.CharField(db_column='TEXTOECF', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpcartao = models.CharField(db_column='TPCARTAO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    cnpj_credenciadora = models.CharField(db_column='CNPJ_CREDENCIADORA', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpag = models.CharField(db_column='TPAG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tband = models.CharField(db_column='TBAND', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    loja_mkt = models.CharField(db_column='LOJA_MKT', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cnpj_intermediadora = models.CharField(db_column='CNPJ_INTERMEDIADORA', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FPG'


class Fpgnfe(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FPGNFE'


class Fichacf(models.Model):
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nreg = models.IntegerField(db_column='NREG', blank=True, null=True)  # Field name made lowercase.
    dc = models.CharField(db_column='DC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    deb = models.FloatField(db_column='DEB', blank=True, null=True)  # Field name made lowercase.
    cred = models.FloatField(db_column='CRED', blank=True, null=True)  # Field name made lowercase.
    saldo = models.FloatField(db_column='SALDO', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FichaCF'


class Fichalv(models.Model):
    data = models.DateTimeField(db_column='DATA', primary_key=True)  # Field name made lowercase. The composite primary key (DATA, NPED, OP) found, that is not supported. The first column is selected.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    entra = models.IntegerField(db_column='ENTRA', blank=True, null=True)  # Field name made lowercase.
    saida = models.IntegerField(db_column='SAIDA', blank=True, null=True)  # Field name made lowercase.
    saldo = models.IntegerField(db_column='SALDO', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.BooleanField(db_column='BAIXA', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FichaLv'
        unique_together = (('data', 'nped', 'op'),)


class Fichacl(models.Model):
    data = models.DateTimeField(db_column='DATA', primary_key=True)  # Field name made lowercase. The composite primary key (DATA, NPED, OP) found, that is not supported. The first column is selected.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.BooleanField(db_column='BAIXA', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Fichacl'
        unique_together = (('data', 'nped', 'op'),)


class Hist(models.Model):
    mes = models.IntegerField(db_column='MES', primary_key=True)  # Field name made lowercase.
    nmes = models.CharField(db_column='NMES', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano1 = models.CharField(db_column='ANO1', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano2 = models.CharField(db_column='ANO2', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano3 = models.CharField(db_column='ANO3', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano4 = models.CharField(db_column='ANO4', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano5 = models.CharField(db_column='ANO5', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HIST'


class Histver(models.Model):
    sfw = models.CharField(db_column='SFW', primary_key=True, max_length=15, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (SFW, VERSAO) found, that is not supported. The first column is selected.
    versao = models.CharField(db_column='VERSAO', max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    dtversao = models.DateTimeField(db_column='DTVERSAO', blank=True, null=True)  # Field name made lowercase.
    historico = models.TextField(db_column='HISTORICO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HISTVER'
        unique_together = (('sfw', 'versao'),)


class Ibpt(models.Model):
    ncm = models.CharField(db_column='NCM', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    cest = models.CharField(db_column='CEST', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nac_fed = models.FloatField(db_column='NAC_FED', blank=True, null=True)  # Field name made lowercase.
    imp_fed = models.FloatField(db_column='IMP_FED', blank=True, null=True)  # Field name made lowercase.
    est = models.FloatField(db_column='EST', blank=True, null=True)  # Field name made lowercase.
    mun = models.FloatField(db_column='MUN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'IBPT'


class Invoice(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'INVOICE'


class Itdiraut(models.Model):
    contrato = models.IntegerField(db_column='CONTRATO', primary_key=True)  # Field name made lowercase. The composite primary key (CONTRATO, AUTOR) found, that is not supported. The first column is selected.
    autor = models.CharField(db_column='AUTOR', max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    percdir = models.FloatField(db_column='PERCDIR', blank=True, null=True)  # Field name made lowercase.
    acerto = models.CharField(db_column='ACERTO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    obs = models.TextField(db_column='OBS', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ITDIRAUT'
        unique_together = (('contrato', 'autor'),)


class Lista(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA'


class ListaTipodocModeloDocfisc(models.Model):
    codigo = models.AutoField(db_column='CODIGO')  # Field name made lowercase.
    tipodoc = models.IntegerField(db_column='TIPODOC', primary_key=True)  # Field name made lowercase. The composite primary key (TIPODOC, MODELO_DOCFISC) found, that is not supported. The first column is selected.
    modelo_docfisc = models.CharField(db_column='MODELO_DOCFISC', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LISTA_TIPODOC_MODELO_DOCFISC'
        unique_together = (('tipodoc', 'modelo_docfisc'),)


class LogpedMp(models.Model):
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    cod_mktplace = models.CharField(db_column='COD_MKTPLACE', max_length=30, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    dtsinc = models.DateTimeField(db_column='DTSINC', blank=True, null=True)  # Field name made lowercase.
    erro = models.CharField(db_column='ERRO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, PORTAL, COD_MKTPLACE) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'LOGPED_MP'
        unique_together = (('filial', 'portal', 'cod_mktplace'),)


class LogprodMp(models.Model):
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    erro = models.CharField(db_column='ERRO', max_length=250, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, PORTAL, NBOOK) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'LOGPROD_MP'
        unique_together = (('filial', 'portal', 'nbook'),)


class Logsite(models.Model):
    nsite = models.IntegerField(db_column='NSITE', primary_key=True)  # Field name made lowercase. The composite primary key (NSITE, DTSTATUS, STSITE) found, that is not supported. The first column is selected.
    dtstatus = models.DateTimeField(db_column='DTSTATUS')  # Field name made lowercase.
    stsite = models.IntegerField(db_column='STSITE')  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    arq = models.IntegerField(db_column='ARQ', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOGSITE'
        unique_together = (('nsite', 'dtstatus', 'stsite'),)


class Logus(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    dtop = models.DateTimeField(db_column='DTOP', blank=True, null=True)  # Field name made lowercase.
    usuario = models.CharField(db_column='USUARIO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    li = models.BooleanField(db_column='LI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOGUS'


class LogFfext(models.Model):
    dtatual = models.DateTimeField(db_column='DTATUAL', primary_key=True)  # Field name made lowercase. The composite primary key (DTATUAL, ISBN) found, that is not supported. The first column is selected.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    cod_ff = models.CharField(db_column='COD_FF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    dt_ff = models.DateTimeField(db_column='DT_FF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOG_FFEXT'
        unique_together = (('dtatual', 'isbn'),)


class LogMp(models.Model):
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    dtsinc = models.DateTimeField(db_column='DTSINC')  # Field name made lowercase.
    historico = models.TextField(db_column='HISTORICO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, PORTAL, DTSINC) found, that is not supported. The first column is selected.

    class Meta:
        managed = False
        db_table = 'LOG_MP'
        unique_together = (('filial', 'portal', 'dtsinc'),)


class LogSincprod(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ean = models.CharField(db_column='EAN', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    st = models.CharField(db_column='ST', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prvenda = models.FloatField(db_column='PRVENDA', blank=True, null=True)  # Field name made lowercase.
    cod_ret = models.IntegerField(db_column='COD_RET', blank=True, null=True)  # Field name made lowercase.
    msg_ret = models.TextField(db_column='MSG_RET', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'LOG_SINCPROD'


class LvMp(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    isbn = models.CharField(db_column='ISBN', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    altura = models.FloatField(db_column='ALTURA', blank=True, null=True)  # Field name made lowercase.
    largura = models.FloatField(db_column='LARGURA', blank=True, null=True)  # Field name made lowercase.
    lombada = models.FloatField(db_column='LOMBADA', blank=True, null=True)  # Field name made lowercase.
    link_img = models.CharField(db_column='LINK_IMG', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sinopse = models.TextField(db_column='SINOPSE', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    cad_ok = models.BooleanField(db_column='CAD_OK', blank=True, null=True)  # Field name made lowercase.
    cond_usado = models.CharField(db_column='COND_USADO', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bisac = models.CharField(db_column='BISAC', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    amz = models.CharField(db_column='AMZ', max_length=11, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    idioma = models.CharField(db_column='IDIOMA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LV_MP'


class Maladir(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.CharField(db_column='NF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    assin = models.CharField(db_column='ASSIN', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='CONTATO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    peso = models.CharField(db_column='PESO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    rastreamento = models.CharField(db_column='RASTREAMENTO', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='PAIS', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    num = models.CharField(db_column='NUM', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MALADIR'


class ModeloDocfisc(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MODELO_DOCFISC'


class ModMp(models.Model):
    layout = models.CharField(db_column='LAYOUT', primary_key=True, max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (LAYOUT, NCOL) found, that is not supported. The first column is selected.
    ncol = models.IntegerField(db_column='NCOL')  # Field name made lowercase.
    col = models.CharField(db_column='COL', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tit1 = models.CharField(db_column='TIT1', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tit2 = models.CharField(db_column='TIT2', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tit3 = models.CharField(db_column='TIT3', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.TextField(db_column='DESCRICAO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    validacao = models.TextField(db_column='VALIDACAO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    st = models.IntegerField(db_column='ST', blank=True, null=True)  # Field name made lowercase.
    campo = models.CharField(db_column='CAMPO', max_length=25, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    formato = models.CharField(db_column='FORMATO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tam_max = models.IntegerField(db_column='TAM_MAX', blank=True, null=True)  # Field name made lowercase.
    valor_fixo = models.CharField(db_column='VALOR_FIXO', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vreduz = models.BooleanField(db_column='VREDUZ', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOD_MP'
        unique_together = (('layout', 'ncol'),)


class Moedas(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOEDAS'


class Movcli(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    nregant = models.IntegerField(db_column='NREGANT', blank=True, null=True)  # Field name made lowercase.
    nfant = models.CharField(db_column='NFANT', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    opant = models.CharField(db_column='OPANT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    aliqicmsst = models.FloatField(db_column='ALIQICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.FloatField(db_column='ALIQIPI', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sittribut = models.CharField(db_column='SITTRIBUT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    canc = models.BooleanField(db_column='CANC', blank=True, null=True)  # Field name made lowercase.
    vicms = models.FloatField(db_column='VICMS', blank=True, null=True)  # Field name made lowercase.
    vst = models.FloatField(db_column='VST', blank=True, null=True)  # Field name made lowercase.
    vipi = models.FloatField(db_column='VIPI', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    vfrete = models.FloatField(db_column='VFRETE', blank=True, null=True)  # Field name made lowercase.
    vseg = models.FloatField(db_column='VSEG', blank=True, null=True)  # Field name made lowercase.
    voutro = models.FloatField(db_column='VOUTRO', blank=True, null=True)  # Field name made lowercase.
    orig = models.CharField(db_column='ORIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CSTIPI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    vpis = models.FloatField(db_column='VPIS', blank=True, null=True)  # Field name made lowercase.
    vcofins = models.FloatField(db_column='VCOFINS', blank=True, null=True)  # Field name made lowercase.
    comissaovd = models.FloatField(db_column='COMISSAOVD', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregext = models.IntegerField(db_column='NREGEXT', blank=True, null=True)  # Field name made lowercase.
    redicms = models.FloatField(db_column='REDICMS', blank=True, null=True)  # Field name made lowercase.
    nf_ant = models.IntegerField(db_column='NF_ANT', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVCLI'


class Movcx(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    operador = models.CharField(db_column='OPERADOR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    horainicio = models.DateTimeField(db_column='HORAINICIO', blank=True, null=True)  # Field name made lowercase.
    horafim = models.DateTimeField(db_column='HORAFIM', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fechado = models.BooleanField(db_column='FECHADO', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    conferente = models.CharField(db_column='CONFERENTE', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVCX'


class Movest(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    titulo = models.CharField(db_column='TITULO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    editora = models.CharField(db_column='EDITORA', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sdant = models.IntegerField(db_column='SDANT', blank=True, null=True)  # Field name made lowercase.
    compra = models.IntegerField(db_column='COMPRA', blank=True, null=True)  # Field name made lowercase.
    consig = models.IntegerField(db_column='CONSIG', blank=True, null=True)  # Field name made lowercase.
    devcpr = models.IntegerField(db_column='DEVCPR', blank=True, null=True)  # Field name made lowercase.
    devcsg = models.IntegerField(db_column='DEVCSG', blank=True, null=True)  # Field name made lowercase.
    venda = models.IntegerField(db_column='VENDA', blank=True, null=True)  # Field name made lowercase.
    exame = models.IntegerField(db_column='EXAME', blank=True, null=True)  # Field name made lowercase.
    devvda = models.IntegerField(db_column='DEVVDA', blank=True, null=True)  # Field name made lowercase.
    devexa = models.IntegerField(db_column='DEVEXA', blank=True, null=True)  # Field name made lowercase.
    trfe = models.IntegerField(db_column='TRFE', blank=True, null=True)  # Field name made lowercase.
    trfs = models.IntegerField(db_column='TRFS', blank=True, null=True)  # Field name made lowercase.
    oute = models.IntegerField(db_column='OUTE', blank=True, null=True)  # Field name made lowercase.
    outs = models.IntegerField(db_column='OUTS', blank=True, null=True)  # Field name made lowercase.
    disp = models.IntegerField(db_column='DISP', blank=True, null=True)  # Field name made lowercase.
    preco = models.FloatField(db_column='PRECO', blank=True, null=True)  # Field name made lowercase.
    doacao = models.IntegerField(db_column='DOACAO', blank=True, null=True)  # Field name made lowercase.
    isbn1 = models.CharField(db_column='ISBN1', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVEST'


class MovestCsg(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, NBOOK, OP, CLIFORN) found, that is not supported. The first column is selected.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    editora = models.CharField(db_column='EDITORA', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVEST_CSG'
        unique_together = (('filial', 'nbook', 'op', 'cliforn'),)


class Movfil(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    nregant = models.IntegerField(db_column='NREGANT', blank=True, null=True)  # Field name made lowercase.
    nfant = models.CharField(db_column='NFANT', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    opant = models.CharField(db_column='OPANT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    aliqicmsst = models.FloatField(db_column='ALIQICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.FloatField(db_column='ALIQIPI', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vicms = models.FloatField(db_column='VICMS', blank=True, null=True)  # Field name made lowercase.
    vst = models.FloatField(db_column='VST', blank=True, null=True)  # Field name made lowercase.
    vipi = models.FloatField(db_column='VIPI', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    vfrete = models.FloatField(db_column='VFRETE', blank=True, null=True)  # Field name made lowercase.
    vseg = models.FloatField(db_column='VSEG', blank=True, null=True)  # Field name made lowercase.
    voutro = models.FloatField(db_column='VOUTRO', blank=True, null=True)  # Field name made lowercase.
    orig = models.CharField(db_column='ORIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CSTIPI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    vpis = models.FloatField(db_column='VPIS', blank=True, null=True)  # Field name made lowercase.
    vcofins = models.FloatField(db_column='VCOFINS', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    redicms = models.FloatField(db_column='REDICMS', blank=True, null=True)  # Field name made lowercase.
    nf_ant = models.IntegerField(db_column='NF_ANT', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVFIL'


class Movfin(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dc = models.CharField(db_column='DC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlpgto = models.FloatField(db_column='VLPGTO', blank=True, null=True)  # Field name made lowercase.
    banco = models.CharField(db_column='BANCO', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    compl = models.CharField(db_column='COMPL', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtpgto = models.DateTimeField(db_column='DTPGTO', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtbaixa = models.DateTimeField(db_column='DTBAIXA', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    grupo = models.IntegerField(db_column='GRUPO', blank=True, null=True)  # Field name made lowercase.
    imp = models.CharField(db_column='IMP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendedor = models.CharField(db_column='VENDEDOR', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cobranca = models.BooleanField(db_column='COBRANCA', blank=True, null=True)  # Field name made lowercase.
    dt_docto = models.DateTimeField(db_column='DT_DOCTO', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    nrobanco = models.CharField(db_column='NROBANCO', max_length=12, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bdev = models.BooleanField(db_column='BDEV', blank=True, null=True)  # Field name made lowercase.
    pgcobranca = models.BooleanField(db_column='PGCOBRANCA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlvencto = models.FloatField(db_column='VLVENCTO', blank=True, null=True)  # Field name made lowercase.
    conta = models.CharField(db_column='CONTA', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nsite = models.IntegerField(db_column='NSITE', blank=True, null=True)  # Field name made lowercase.
    ccusto = models.CharField(db_column='CCUSTO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nominal = models.CharField(db_column='NOMINAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desdobra = models.CharField(db_column='DESDOBRA', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.
    dtbanco = models.DateTimeField(db_column='DTBANCO', blank=True, null=True)  # Field name made lowercase.
    rem = models.IntegerField(db_column='REM', blank=True, null=True)  # Field name made lowercase.
    ret = models.IntegerField(db_column='RET', blank=True, null=True)  # Field name made lowercase.
    vldesc = models.FloatField(db_column='VLDESC', blank=True, null=True)  # Field name made lowercase.
    vlacresc = models.FloatField(db_column='VLACRESC', blank=True, null=True)  # Field name made lowercase.
    nregext = models.IntegerField(db_column='NREGEXT', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfecha = models.IntegerField(db_column='NFECHA', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    norc = models.IntegerField(db_column='NORC', blank=True, null=True)  # Field name made lowercase.
    agchq = models.CharField(db_column='AGCHQ', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contachq = models.CharField(db_column='CONTACHQ', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cnpjcpfchq = models.CharField(db_column='CNPJCPFCHQ', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    gnf = models.CharField(db_column='GNF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    npedout = models.IntegerField(db_column='NPEDOUT', blank=True, null=True)  # Field name made lowercase.
    rem_banco = models.BooleanField(db_column='REM_BANCO', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    bonus_cobranca = models.FloatField(db_column='BONUS_COBRANCA', blank=True, null=True)  # Field name made lowercase.
    at_cobranca = models.CharField(db_column='AT_COBRANCA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aut = models.CharField(db_column='AUT', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qrcode = models.CharField(db_column='QRCODE', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVFIN'


class Movfor(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    nregant = models.IntegerField(db_column='NREGANT', blank=True, null=True)  # Field name made lowercase.
    nfant = models.CharField(db_column='NFANT', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    opant = models.CharField(db_column='OPANT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    aliqicmsst = models.FloatField(db_column='ALIQICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.FloatField(db_column='ALIQIPI', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vicms = models.FloatField(db_column='VICMS', blank=True, null=True)  # Field name made lowercase.
    vst = models.FloatField(db_column='VST', blank=True, null=True)  # Field name made lowercase.
    vipi = models.FloatField(db_column='VIPI', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    vfrete = models.FloatField(db_column='VFRETE', blank=True, null=True)  # Field name made lowercase.
    vseg = models.FloatField(db_column='VSEG', blank=True, null=True)  # Field name made lowercase.
    voutro = models.FloatField(db_column='VOUTRO', blank=True, null=True)  # Field name made lowercase.
    orig = models.CharField(db_column='ORIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CSTIPI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    vpis = models.FloatField(db_column='VPIS', blank=True, null=True)  # Field name made lowercase.
    vcofins = models.FloatField(db_column='VCOFINS', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    redicms = models.FloatField(db_column='REDICMS', blank=True, null=True)  # Field name made lowercase.
    nf_ant = models.IntegerField(db_column='NF_ANT', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVFOR'


class Movout(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    numitem = models.IntegerField(db_column='NUMITEM')  # Field name made lowercase.
    prodserv = models.CharField(db_column='PRODSERV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    nregant = models.IntegerField(db_column='NREGANT', blank=True, null=True)  # Field name made lowercase.
    nfant = models.CharField(db_column='NFANT', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    opant = models.CharField(db_column='OPANT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    aliqicmsst = models.FloatField(db_column='ALIQICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.FloatField(db_column='ALIQIPI', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sittribut = models.CharField(db_column='SITTRIBUT', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    canc = models.BooleanField(db_column='CANC', blank=True, null=True)  # Field name made lowercase.
    vicms = models.FloatField(db_column='VICMS', blank=True, null=True)  # Field name made lowercase.
    vst = models.FloatField(db_column='VST', blank=True, null=True)  # Field name made lowercase.
    vipi = models.FloatField(db_column='VIPI', blank=True, null=True)  # Field name made lowercase.
    vfrete = models.FloatField(db_column='VFRETE', blank=True, null=True)  # Field name made lowercase.
    vseg = models.FloatField(db_column='VSEG', blank=True, null=True)  # Field name made lowercase.
    voutro = models.FloatField(db_column='VOUTRO', blank=True, null=True)  # Field name made lowercase.
    orig = models.CharField(db_column='ORIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CSTIPI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    vpis = models.FloatField(db_column='VPIS', blank=True, null=True)  # Field name made lowercase.
    vcofins = models.FloatField(db_column='VCOFINS', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    comissaovd = models.FloatField(db_column='COMISSAOVD', blank=True, null=True)  # Field name made lowercase.
    infad = models.CharField(db_column='INFAD', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codbarra = models.CharField(db_column='CODBARRA', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codexterno = models.CharField(db_column='CODEXTERNO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=140, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MOVOUT'


class Municipios(models.Model):
    coduf = models.IntegerField(db_column='CODUF', primary_key=True)  # Field name made lowercase. The composite primary key (CODUF, CODMUN) found, that is not supported. The first column is selected.
    codmun = models.IntegerField(db_column='CODMUN')  # Field name made lowercase.
    municipio = models.CharField(db_column='MUNICIPIO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MUNICIPIOS'
        unique_together = (('coduf', 'codmun'),)


class Nfexp(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    ufembarq = models.CharField(db_column='UFEMBARQ', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    locembarq = models.CharField(db_column='LOCEMBARQ', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFEXP'


class Nfinutil(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    dtemissao = models.DateTimeField(db_column='DTEMISSAO', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    xml = models.CharField(db_column='XML', max_length=44, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFINUTIL'


class Nfiscal(models.Model):
    nped = models.IntegerField(db_column='NPED', primary_key=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtemissao = models.DateTimeField(db_column='DTEMISSAO', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codfiscal = models.CharField(db_column='CODFISCAL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    natop = models.CharField(db_column='NATOP', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlcontabil = models.FloatField(db_column='VLCONTABIL', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    impicms = models.FloatField(db_column='IMPICMS', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    impipi = models.FloatField(db_column='IMPIPI', blank=True, null=True)  # Field name made lowercase.
    vlfrete = models.FloatField(db_column='VLFRETE', blank=True, null=True)  # Field name made lowercase.
    vlseg = models.FloatField(db_column='VLSEG', blank=True, null=True)  # Field name made lowercase.
    vlacess = models.FloatField(db_column='VLACESS', blank=True, null=True)  # Field name made lowercase.
    transp = models.CharField(db_column='TRANSP', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs1 = models.CharField(db_column='OBS1', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs2 = models.CharField(db_column='OBS2', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    fretecta = models.CharField(db_column='FRETECTA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obsnf = models.TextField(db_column='OBSNF', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipocf = models.CharField(db_column='TIPOCF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nossanf = models.BooleanField(db_column='NOSSANF', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    statusnf = models.IntegerField(db_column='STATUSNF', blank=True, null=True)  # Field name made lowercase.
    xml = models.CharField(db_column='XML', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    impicmsst = models.FloatField(db_column='IMPICMSST', blank=True, null=True)  # Field name made lowercase.
    iimp = models.FloatField(db_column='IIMP', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    totprod = models.FloatField(db_column='TOTPROD', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    retorno_sefaz = models.CharField(db_column='RETORNO_SEFAZ', max_length=255, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dhemissao = models.DateTimeField(db_column='DHEMISSAO', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NFISCAL'


class Opnfe(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OPNFE'


class Orc(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    env = models.BooleanField(db_column='ENV', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.
    logsite = models.IntegerField(db_column='LOGSITE', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nregext = models.IntegerField(db_column='NREGEXT', blank=True, null=True)  # Field name made lowercase.
    it_mktplace = models.CharField(db_column='IT_MKTPLACE', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORC'


class Orfaos(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    isbn1 = models.CharField(db_column='ISBN1', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    novo = models.CharField(db_column='NOVO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dtnf = models.DateTimeField(db_column='DTNF', blank=True, null=True)  # Field name made lowercase.
    nossanf = models.BooleanField(db_column='NOSSANF', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    xml = models.CharField(db_column='XML', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    arqmov = models.CharField(db_column='ARQMOV', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORFAOS'


class Outnf(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nf = models.CharField(db_column='NF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    descn = models.FloatField(db_column='DESCN', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpnf = models.CharField(db_column='TPNF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    serie = models.CharField(db_column='SERIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    mva = models.FloatField(db_column='MVA', blank=True, null=True)  # Field name made lowercase.
    vfrete = models.FloatField(db_column='VFRETE', blank=True, null=True)  # Field name made lowercase.
    vseg = models.FloatField(db_column='VSEG', blank=True, null=True)  # Field name made lowercase.
    voutro = models.FloatField(db_column='VOUTRO', blank=True, null=True)  # Field name made lowercase.
    ncm = models.CharField(db_column='NCM', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cfop = models.CharField(db_column='CFOP', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baseicms = models.FloatField(db_column='BASEICMS', blank=True, null=True)  # Field name made lowercase.
    aliqicms = models.FloatField(db_column='ALIQICMS', blank=True, null=True)  # Field name made lowercase.
    baseicmsst = models.FloatField(db_column='BASEICMSST', blank=True, null=True)  # Field name made lowercase.
    aliqicmsst = models.FloatField(db_column='ALIQICMSST', blank=True, null=True)  # Field name made lowercase.
    baseipi = models.FloatField(db_column='BASEIPI', blank=True, null=True)  # Field name made lowercase.
    aliqipi = models.FloatField(db_column='ALIQIPI', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    vicms = models.FloatField(db_column='VICMS', blank=True, null=True)  # Field name made lowercase.
    vst = models.FloatField(db_column='VST', blank=True, null=True)  # Field name made lowercase.
    vipi = models.FloatField(db_column='VIPI', blank=True, null=True)  # Field name made lowercase.
    orig = models.CharField(db_column='ORIG', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipi = models.CharField(db_column='CSTIPI', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    vpis = models.FloatField(db_column='VPIS', blank=True, null=True)  # Field name made lowercase.
    vcofins = models.FloatField(db_column='VCOFINS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUTNF'


class Paises(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bacen = models.IntegerField(db_column='BACEN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PAISES'


class Pedfil(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    env = models.BooleanField(db_column='ENV', blank=True, null=True)  # Field name made lowercase.
    qtsep = models.IntegerField(db_column='QTSEP', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PEDFIL'


class Pedfor(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    env = models.BooleanField(db_column='ENV', blank=True, null=True)  # Field name made lowercase.
    filorigem = models.CharField(db_column='FILORIGEM', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    norc = models.IntegerField(db_column='NORC', blank=True, null=True)  # Field name made lowercase.
    dtpedorc = models.DateTimeField(db_column='DTPEDORC', blank=True, null=True)  # Field name made lowercase.
    priori = models.IntegerField(db_column='PRIORI', blank=True, null=True)  # Field name made lowercase.
    prodff = models.IntegerField(db_column='PRODFF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PEDFOR'


class PrefBisac(models.Model):
    prefixo = models.CharField(db_column='PREFIXO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome_bisac = models.CharField(db_column='NOME_BISAC', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PREF_BISAC'


class Prodserv(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    codexterno = models.CharField(db_column='CODEXTERNO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cliforn = models.CharField(db_column='CLIFORN', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=140, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    moeda = models.CharField(db_column='MOEDA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    codbarra = models.CharField(db_column='CODBARRA', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PRODSERV'


class ProdLi(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sku = models.CharField(db_column='SKU', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.CharField(db_column='ATIVO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROD_LI'


class PropTray(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CODIGO) found, that is not supported. The first column is selected.
    codigo = models.IntegerField(db_column='CODIGO')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PROP_TRAY'
        unique_together = (('filial', 'codigo'),)


class R01(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CAIXA, NUMERODEFABRICACAO) found, that is not supported. The first column is selected.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    numerodefabricacao = models.CharField(db_column='NUMERODEFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipodeecf = models.CharField(db_column='TIPODEECF', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    marcadoecf = models.CharField(db_column='MARCADOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelodoecf = models.CharField(db_column='MODELODOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    versaodosb = models.CharField(db_column='VERSAODOSB', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    datadeinstalacaodosb = models.CharField(db_column='DATADEINSTALACAODOSB', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    horariodeinstalacaodosb = models.CharField(db_column='HORARIODEINSTALACAODOSB', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerosequencialdoecf = models.CharField(db_column='NUMEROSEQUENCIALDOECF', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cnpjdousuario = models.CharField(db_column='CNPJDOUSUARIO', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    iedousuario = models.CharField(db_column='IEDOUSUARIO', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cnpjdadesenvolvedora = models.CharField(db_column='CNPJDADESENVOLVEDORA', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    iedadesenvolvedora = models.CharField(db_column='IEDADESENVOLVEDORA', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    imdadesenvolvedora = models.CharField(db_column='IMDADESENVOLVEDORA', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    denominacaodaempresadesenvolvedora = models.CharField(db_column='DENOMINACAODAEMPRESADESENVOLVEDORA', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nomedopafecf = models.CharField(db_column='NOMEDOPAFECF', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    versaodopafecf = models.CharField(db_column='VERSAODOPAFECF', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    md5pafecf = models.CharField(db_column='MD5PAFECF', max_length=32, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    versaodaerpafecf = models.CharField(db_column='VERSAODAERPAFECF', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtestoque = models.DateTimeField(db_column='DTESTOQUE', blank=True, null=True)  # Field name made lowercase.
    nfiscal = models.CharField(db_column='NFISCAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R01'
        unique_together = (('filial', 'caixa', 'numerodefabricacao'),)


class R02(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CAIXA, NFABRICACAO, CRZ) found, that is not supported. The first column is selected.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    crz = models.CharField(db_column='CRZ', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nfabricacao = models.CharField(db_column='NFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modecf = models.CharField(db_column='MODECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nusuario = models.CharField(db_column='NUSUARIO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    coo = models.CharField(db_column='COO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cro = models.CharField(db_column='CRO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtmov = models.CharField(db_column='DTMOV', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtemissao = models.CharField(db_column='DTEMISSAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    hemissao = models.CharField(db_column='HEMISSAO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vdbrutadiaria = models.CharField(db_column='VDBRUTADIARIA', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    paramdescissqn = models.CharField(db_column='PARAMDESCISSQN', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    gt = models.FloatField(db_column='GT', blank=True, null=True)  # Field name made lowercase.
    coo_inicial = models.CharField(db_column='COO_INICIAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsinc = models.IntegerField(db_column='STSINC', blank=True, null=True)  # Field name made lowercase.
    nfiscal = models.CharField(db_column='NFISCAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R02'
        unique_together = (('filial', 'caixa', 'nfabricacao', 'crz'),)


class R03(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CAIXA, NUMERODEFABRICACAO, CRZ, TOTALIZADORPARCIAL) found, that is not supported. The first column is selected.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    crz = models.CharField(db_column='CRZ', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    numerodefabricacao = models.CharField(db_column='NUMERODEFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelodoecf = models.CharField(db_column='MODELODOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerodousuario = models.CharField(db_column='NUMERODOUSUARIO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    totalizadorparcial = models.CharField(db_column='TOTALIZADORPARCIAL', max_length=7, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    valoracumulado = models.FloatField(db_column='VALORACUMULADO', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsinc = models.IntegerField(db_column='STSINC', blank=True, null=True)  # Field name made lowercase.
    nfiscal = models.CharField(db_column='NFISCAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R03'
        unique_together = (('filial', 'caixa', 'numerodefabricacao', 'crz', 'totalizadorparcial'),)


class R04(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    ccf = models.CharField(db_column='CCF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerodefabricacao = models.CharField(db_column='NUMERODEFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelodoecf = models.CharField(db_column='MODELODOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerodousuario = models.CharField(db_column='NUMERODOUSUARIO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtped = models.DateTimeField(db_column='DTPED', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    nomecli = models.CharField(db_column='NOMECLI', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cpfcnpjcli = models.CharField(db_column='CPFCNPJCLI', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    canc = models.CharField(db_column='CANC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    hora = models.CharField(db_column='HORA', max_length=5, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsinc = models.IntegerField(db_column='STSINC', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R04'


class R05(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    ccf = models.CharField(db_column='CCF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nitem = models.CharField(db_column='NITEM', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    numerodefabricacao = models.CharField(db_column='NUMERODEFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelodoecf = models.CharField(db_column='MODELODOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerodousuario = models.CharField(db_column='NUMERODOUSUARIO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=14, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    vlunit = models.FloatField(db_column='VLUNIT', blank=True, null=True)  # Field name made lowercase.
    descitem = models.FloatField(db_column='DESCITEM', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    canc = models.CharField(db_column='CANC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    unidade = models.CharField(db_column='UNIDADE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    totalizadorparcial = models.CharField(db_column='TOTALIZADORPARCIAL', max_length=7, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsinc = models.IntegerField(db_column='STSINC', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R05'


class R06(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CAIXA, COO, NUMERODEFABRICACAO) found, that is not supported. The first column is selected.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    coo = models.CharField(db_column='COO', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    numerodefabricacao = models.CharField(db_column='NUMERODEFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelodoecf = models.CharField(db_column='MODELODOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerodousuario = models.CharField(db_column='NUMERODOUSUARIO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    gnf = models.CharField(db_column='GNF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    grg = models.CharField(db_column='GRG', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cdc = models.CharField(db_column='CDC', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    denominacao = models.CharField(db_column='DENOMINACAO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    datafinaldeemissao = models.CharField(db_column='DATAFINALDEEMISSAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    horafinaldeemissao = models.CharField(db_column='HORAFINALDEEMISSAO', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsinc = models.IntegerField(db_column='STSINC', blank=True, null=True)  # Field name made lowercase.
    nfiscal = models.CharField(db_column='NFISCAL', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R06'
        unique_together = (('filial', 'caixa', 'coo', 'numerodefabricacao'),)


class R07(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nreg = models.IntegerField(db_column='NREG')  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    ccf = models.CharField(db_column='CCF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    gnf = models.CharField(db_column='GNF', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlpgto = models.FloatField(db_column='VLPGTO', blank=True, null=True)  # Field name made lowercase.
    meiopgto = models.CharField(db_column='MEIOPGTO', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    indicadorestorno = models.CharField(db_column='INDICADORESTORNO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlestorno = models.FloatField(db_column='VLESTORNO', blank=True, null=True)  # Field name made lowercase.
    numerodefabricacao = models.CharField(db_column='NUMERODEFABRICACAO', max_length=20, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    mfadicional = models.CharField(db_column='MFADICIONAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelodoecf = models.CharField(db_column='MODELODOECF', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    numerodousuario = models.CharField(db_column='NUMERODOUSUARIO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stsinc = models.IntegerField(db_column='STSINC', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'R07'


class Recassin(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (NBOOK, EXEMPLAR) found, that is not supported. The first column is selected.
    exemplar = models.CharField(db_column='EXEMPLAR', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    dtrec = models.DateTimeField(db_column='DTREC', blank=True, null=True)  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    impr = models.CharField(db_column='IMPR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtpub = models.DateTimeField(db_column='DTPUB', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECASSIN'
        unique_together = (('nbook', 'exemplar'),)


class Recibos(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    recibo = models.IntegerField(db_column='RECIBO', blank=True, null=True)  # Field name made lowercase.
    cliente = models.CharField(db_column='CLIENTE', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    dc = models.CharField(db_column='DC', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ndocto = models.CharField(db_column='NDOCTO', max_length=16, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtvencto = models.DateTimeField(db_column='DTVENCTO', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    valorpg = models.FloatField(db_column='VALORPG', blank=True, null=True)  # Field name made lowercase.
    juros = models.FloatField(db_column='JUROS', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    nf = models.IntegerField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    nreg_fin = models.IntegerField(db_column='NREG_FIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RECIBOS'


class Reserva(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nped = models.IntegerField(db_column='NPED')  # Field name made lowercase.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    qtde = models.IntegerField(db_column='QTDE', blank=True, null=True)  # Field name made lowercase.
    prlista = models.FloatField(db_column='PRLISTA', blank=True, null=True)  # Field name made lowercase.
    prunit = models.FloatField(db_column='PRUNIT', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    baixa = models.CharField(db_column='BAIXA', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtbaixa = models.IntegerField(db_column='QTBAIXA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    env = models.BooleanField(db_column='ENV', blank=True, null=True)  # Field name made lowercase.
    desconto = models.FloatField(db_column='DESCONTO', blank=True, null=True)  # Field name made lowercase.
    vlvenda = models.FloatField(db_column='VLVENDA', blank=True, null=True)  # Field name made lowercase.
    shortn = models.CharField(db_column='SHORTN', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVA'


class Rkorc(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlorc = models.FloatField(db_column='VLORC', blank=True, null=True)  # Field name made lowercase.
    vlped = models.FloatField(db_column='VLPED', blank=True, null=True)  # Field name made lowercase.
    vlfat = models.FloatField(db_column='VLFAT', blank=True, null=True)  # Field name made lowercase.
    rend = models.FloatField(db_column='REND', blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='MARGEM', blank=True, null=True)  # Field name made lowercase.
    percmargem = models.FloatField(db_column='PERCMARGEM', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RKORC'


class Saldo(models.Model):
    conta = models.CharField(db_column='CONTA', primary_key=True, max_length=9, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (CONTA, DATA) found, that is not supported. The first column is selected.
    data = models.DateTimeField(db_column='DATA')  # Field name made lowercase.
    entrada = models.FloatField(db_column='ENTRADA', blank=True, null=True)  # Field name made lowercase.
    saida = models.FloatField(db_column='SAIDA', blank=True, null=True)  # Field name made lowercase.
    disp = models.FloatField(db_column='DISP', blank=True, null=True)  # Field name made lowercase.
    banco = models.FloatField(db_column='BANCO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SALDO'
        unique_together = (('conta', 'data'),)


class Sbsadv(models.Model):
    sbscard = models.IntegerField(db_column='SBSCARD', primary_key=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    saldo = models.IntegerField(db_column='SALDO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SBSADV'


class Secao(models.Model):
    codigo = models.CharField(db_column='CODIGO', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SECAO'


class Selos(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SELOS'


class Series(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    instituicao = models.CharField(db_column='INSTITUICAO', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    atualizar = models.CharField(db_column='ATUALIZAR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERIES'


class ServCorreios(models.Model):
    contrato = models.CharField(db_column='CONTRATO', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (CONTRATO, SERVICO) found, that is not supported. The first column is selected.
    servico = models.CharField(db_column='SERVICO', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SERV_CORREIOS'
        unique_together = (('contrato', 'servico'),)


class Setch(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    lpp = models.CharField(db_column='LPP', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nlinhas = models.FloatField(db_column='NLINHAS', blank=True, null=True)  # Field name made lowercase.
    lvalor = models.FloatField(db_column='LVALOR', blank=True, null=True)  # Field name made lowercase.
    cvalor = models.FloatField(db_column='CVALOR', blank=True, null=True)  # Field name made lowercase.
    tvalor = models.FloatField(db_column='TVALOR', blank=True, null=True)  # Field name made lowercase.
    lext1 = models.FloatField(db_column='LEXT1', blank=True, null=True)  # Field name made lowercase.
    cext1 = models.FloatField(db_column='CEXT1', blank=True, null=True)  # Field name made lowercase.
    text1 = models.FloatField(db_column='TEXT1', blank=True, null=True)  # Field name made lowercase.
    lext2 = models.FloatField(db_column='LEXT2', blank=True, null=True)  # Field name made lowercase.
    cext2 = models.FloatField(db_column='CEXT2', blank=True, null=True)  # Field name made lowercase.
    text2 = models.FloatField(db_column='TEXT2', blank=True, null=True)  # Field name made lowercase.
    lnominal = models.FloatField(db_column='LNOMINAL', blank=True, null=True)  # Field name made lowercase.
    cnominal = models.FloatField(db_column='CNOMINAL', blank=True, null=True)  # Field name made lowercase.
    tnominal = models.FloatField(db_column='TNOMINAL', blank=True, null=True)  # Field name made lowercase.
    lcidade = models.FloatField(db_column='LCIDADE', blank=True, null=True)  # Field name made lowercase.
    ccidade = models.FloatField(db_column='CCIDADE', blank=True, null=True)  # Field name made lowercase.
    txtcidade = models.CharField(db_column='TXTCIDADE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ldia = models.FloatField(db_column='LDIA', blank=True, null=True)  # Field name made lowercase.
    cdia = models.FloatField(db_column='CDIA', blank=True, null=True)  # Field name made lowercase.
    lmes = models.FloatField(db_column='LMES', blank=True, null=True)  # Field name made lowercase.
    cmes = models.FloatField(db_column='CMES', blank=True, null=True)  # Field name made lowercase.
    lano = models.FloatField(db_column='LANO', blank=True, null=True)  # Field name made lowercase.
    cano = models.FloatField(db_column='CANO', blank=True, null=True)  # Field name made lowercase.
    lsaltar = models.FloatField(db_column='LSALTAR', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SETCH'


class Setupecf(models.Model):
    nome = models.CharField(db_column='NOME', primary_key=True, max_length=30, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    inicia = models.CharField(db_column='INICIA', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SETUPECF'


class Setupnf(models.Model):
    item = models.IntegerField(db_column='ITEM', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='CODIGO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    linha = models.SmallIntegerField(db_column='LINHA', blank=True, null=True)  # Field name made lowercase.
    coluna = models.SmallIntegerField(db_column='COLUNA', blank=True, null=True)  # Field name made lowercase.
    tamanho = models.SmallIntegerField(db_column='TAMANHO', blank=True, null=True)  # Field name made lowercase.
    imp = models.BooleanField(db_column='IMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SETUPNF'


class Sgrsup(models.Model):
    nreg = models.AutoField(db_column='NREG', primary_key=True)  # Field name made lowercase.
    data = models.DateTimeField(db_column='DATA', blank=True, null=True)  # Field name made lowercase.
    hora = models.DateTimeField(db_column='HORA', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    valor = models.FloatField(db_column='VALOR', blank=True, null=True)  # Field name made lowercase.
    fpg = models.CharField(db_column='FPG', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    operador = models.CharField(db_column='OPERADOR', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    caixa = models.CharField(db_column='CAIXA', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=200, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nfecha = models.IntegerField(db_column='NFECHA', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SGRSUP'


class Sincev(models.Model):
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    cgr = models.CharField(db_column='CGR', max_length=8, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    escola = models.CharField(db_column='ESCOLA', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='TIPO', max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vlb = models.IntegerField(db_column='VLB', blank=True, null=True)  # Field name made lowercase.
    dtvlb = models.DateTimeField(db_column='DTVLB', blank=True, null=True)  # Field name made lowercase.
    cli = models.IntegerField(db_column='CLI', blank=True, null=True)  # Field name made lowercase.
    dtcli = models.DateTimeField(db_column='DTCLI', blank=True, null=True)  # Field name made lowercase.
    est = models.IntegerField(db_column='EST', blank=True, null=True)  # Field name made lowercase.
    dtest = models.DateTimeField(db_column='DTEST', blank=True, null=True)  # Field name made lowercase.
    lis = models.IntegerField(db_column='LIS', blank=True, null=True)  # Field name made lowercase.
    dtlis = models.DateTimeField(db_column='DTLIS', blank=True, null=True)  # Field name made lowercase.
    env = models.IntegerField(db_column='ENV', blank=True, null=True)  # Field name made lowercase.
    dtenv = models.DateTimeField(db_column='DTENV', blank=True, null=True)  # Field name made lowercase.
    orc = models.IntegerField(db_column='ORC', blank=True, null=True)  # Field name made lowercase.
    dtorc = models.DateTimeField(db_column='DTORC', blank=True, null=True)  # Field name made lowercase.
    vda = models.IntegerField(db_column='VDA', blank=True, null=True)  # Field name made lowercase.
    dtvda = models.DateTimeField(db_column='DTVDA', blank=True, null=True)  # Field name made lowercase.
    vcx = models.IntegerField(db_column='VCX', blank=True, null=True)  # Field name made lowercase.
    dtvcx = models.DateTimeField(db_column='DTVCX', blank=True, null=True)  # Field name made lowercase.
    ser = models.IntegerField(db_column='SER', blank=True, null=True)  # Field name made lowercase.
    dtser = models.DateTimeField(db_column='DTSER', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    nome_ev = models.CharField(db_column='NOME_EV', max_length=25, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aux = models.IntegerField(db_column='AUX', blank=True, null=True)  # Field name made lowercase.
    dtaux = models.DateTimeField(db_column='DTAUX', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SINCEV'


class Sincftp(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    vlb = models.IntegerField(db_column='VLB', blank=True, null=True)  # Field name made lowercase.
    dtvlb = models.DateTimeField(db_column='DTVLB', blank=True, null=True)  # Field name made lowercase.
    cli = models.IntegerField(db_column='CLI', blank=True, null=True)  # Field name made lowercase.
    dtcli = models.DateTimeField(db_column='DTCLI', blank=True, null=True)  # Field name made lowercase.
    est = models.IntegerField(db_column='EST', blank=True, null=True)  # Field name made lowercase.
    dtest = models.DateTimeField(db_column='DTEST', blank=True, null=True)  # Field name made lowercase.
    lis = models.IntegerField(db_column='LIS', blank=True, null=True)  # Field name made lowercase.
    dtlis = models.DateTimeField(db_column='DTLIS', blank=True, null=True)  # Field name made lowercase.
    fin = models.IntegerField(db_column='FIN', blank=True, null=True)  # Field name made lowercase.
    dtfin = models.DateTimeField(db_column='DTFIN', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SINCFTP'


class Sinopse(models.Model):
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    sinopse = models.TextField(db_column='SINOPSE', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SINOPSE'


class Status(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATUS'


class StpedMp(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, PORTAL, CODIGO) found, that is not supported. The first column is selected.
    portal = models.CharField(db_column='PORTAL', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    codigo = models.IntegerField(db_column='CODIGO')  # Field name made lowercase.
    op = models.CharField(db_column='OP', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STPED_MP'
        unique_together = (('filial', 'portal', 'codigo'),)


class Stsite(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=255, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STSITE'


class StMp(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, NBOOK) found, that is not supported. The first column is selected.
    nbook = models.CharField(db_column='NBOOK', max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    pr_mkt = models.FloatField(db_column='PR_MKT', blank=True, null=True)  # Field name made lowercase.
    li = models.IntegerField(db_column='LI', blank=True, null=True)  # Field name made lowercase.
    cod_li = models.IntegerField(db_column='COD_LI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ST_MP'
        unique_together = (('filial', 'nbook'),)


class StTray(models.Model):
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, CODIGO) found, that is not supported. The first column is selected.
    codigo = models.IntegerField(db_column='CODIGO')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ST_TRAY'
        unique_together = (('filial', 'codigo'),)


class Tabicms(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    aliq = models.FloatField(db_column='ALIQ', blank=True, null=True)  # Field name made lowercase.
    aliqorigem = models.FloatField(db_column='ALIQORIGEM', blank=True, null=True)  # Field name made lowercase.
    aliqint = models.FloatField(db_column='ALIQINT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TABICMS'


class TabMp(models.Model):
    cod_mp = models.CharField(db_column='COD_MP', max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome_mp = models.CharField(db_column='NOME_MP', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='LOGIN', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    sinc = models.BooleanField(db_column='SINC', blank=True, null=True)  # Field name made lowercase.
    cadastrados = models.IntegerField(db_column='CADASTRADOS', blank=True, null=True)  # Field name made lowercase.
    ativos = models.IntegerField(db_column='ATIVOS', blank=True, null=True)  # Field name made lowercase.
    inativos = models.IntegerField(db_column='INATIVOS', blank=True, null=True)  # Field name made lowercase.
    pendentes = models.IntegerField(db_column='PENDENTES', blank=True, null=True)  # Field name made lowercase.
    dv = models.CharField(db_column='DV', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tp_sku = models.IntegerField(db_column='TP_SKU', blank=True, null=True)  # Field name made lowercase.
    id_cli_mp = models.CharField(db_column='ID_CLI_MP', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    url_mp = models.CharField(db_column='URL_MP', max_length=150, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cross_estoque = models.IntegerField(db_column='CROSS_ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    cross_s_estoque = models.IntegerField(db_column='CROSS_S_ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    st_aprovado = models.CharField(db_column='ST_APROVADO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    so_livros = models.BooleanField(db_column='SO_LIVROS', blank=True, null=True)  # Field name made lowercase.
    so_novos = models.BooleanField(db_column='SO_NOVOS', blank=True, null=True)  # Field name made lowercase.
    usa_estff = models.BooleanField(db_column='USA_ESTFF', blank=True, null=True)  # Field name made lowercase.
    sinc_etiq = models.BooleanField(db_column='SINC_ETIQ', blank=True, null=True)  # Field name made lowercase.
    cad_ok = models.BooleanField(db_column='CAD_OK', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase. The composite primary key (FILIAL, COD_MP) found, that is not supported. The first column is selected.
    vl_min = models.FloatField(db_column='VL_MIN', blank=True, null=True)  # Field name made lowercase.
    pre_venda = models.BooleanField(db_column='PRE_VENDA', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TAB_MP'
        unique_together = (('filial', 'cod_mp'),)


class Tipodoc(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPODOC'


class TipoCliente(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=2, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_mercos = models.IntegerField(db_column='COD_MERCOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_CLIENTE'


class TipoProduto(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=3, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstnac = models.CharField(db_column='CSTNAC', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstimp = models.CharField(db_column='CSTIMP', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    classfisc = models.CharField(db_column='CLASSFISC', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    icms = models.FloatField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    ipi = models.FloatField(db_column='IPI', blank=True, null=True)  # Field name made lowercase.
    codtrib = models.CharField(db_column='CODTRIB', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    redicms = models.FloatField(db_column='REDICMS', blank=True, null=True)  # Field name made lowercase.
    st = models.FloatField(db_column='ST', blank=True, null=True)  # Field name made lowercase.
    cstipie = models.CharField(db_column='CSTIPIE', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstipis = models.CharField(db_column='CSTIPIS', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    csosn = models.CharField(db_column='CSOSN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    un = models.CharField(db_column='UN', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    origem = models.IntegerField(db_column='ORIGEM', blank=True, null=True)  # Field name made lowercase.
    margem = models.FloatField(db_column='MARGEM', blank=True, null=True)  # Field name made lowercase.
    cadlocal = models.CharField(db_column='CADLOCAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstpis = models.CharField(db_column='CSTPIS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofins = models.CharField(db_column='CSTCOFINS', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    pis = models.FloatField(db_column='PIS', blank=True, null=True)  # Field name made lowercase.
    cofins = models.FloatField(db_column='COFINS', blank=True, null=True)  # Field name made lowercase.
    ibpt = models.FloatField(db_column='IBPT', blank=True, null=True)  # Field name made lowercase.
    cstpise = models.CharField(db_column='CSTPISE', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cstcofinse = models.CharField(db_column='CSTCOFINSE', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    mva_am = models.FloatField(db_column='MVA_AM', blank=True, null=True)  # Field name made lowercase.
    mva_ac = models.FloatField(db_column='MVA_AC', blank=True, null=True)  # Field name made lowercase.
    mva_al = models.FloatField(db_column='MVA_AL', blank=True, null=True)  # Field name made lowercase.
    mva_ap = models.FloatField(db_column='MVA_AP', blank=True, null=True)  # Field name made lowercase.
    mva_ba = models.FloatField(db_column='MVA_BA', blank=True, null=True)  # Field name made lowercase.
    mva_ce = models.FloatField(db_column='MVA_CE', blank=True, null=True)  # Field name made lowercase.
    mva_df = models.FloatField(db_column='MVA_DF', blank=True, null=True)  # Field name made lowercase.
    mva_es = models.FloatField(db_column='MVA_ES', blank=True, null=True)  # Field name made lowercase.
    mva_ma = models.FloatField(db_column='MVA_MA', blank=True, null=True)  # Field name made lowercase.
    mva_go = models.FloatField(db_column='MVA_GO', blank=True, null=True)  # Field name made lowercase.
    mva_mt = models.FloatField(db_column='MVA_MT', blank=True, null=True)  # Field name made lowercase.
    mva_ms = models.FloatField(db_column='MVA_MS', blank=True, null=True)  # Field name made lowercase.
    mva_mg = models.FloatField(db_column='MVA_MG', blank=True, null=True)  # Field name made lowercase.
    mva_pa = models.FloatField(db_column='MVA_PA', blank=True, null=True)  # Field name made lowercase.
    mva_pb = models.FloatField(db_column='MVA_PB', blank=True, null=True)  # Field name made lowercase.
    mva_pr = models.FloatField(db_column='MVA_PR', blank=True, null=True)  # Field name made lowercase.
    mva_pe = models.FloatField(db_column='MVA_PE', blank=True, null=True)  # Field name made lowercase.
    mva_pi = models.FloatField(db_column='MVA_PI', blank=True, null=True)  # Field name made lowercase.
    mva_rj = models.FloatField(db_column='MVA_RJ', blank=True, null=True)  # Field name made lowercase.
    mva_rn = models.FloatField(db_column='MVA_RN', blank=True, null=True)  # Field name made lowercase.
    mva_ro = models.FloatField(db_column='MVA_RO', blank=True, null=True)  # Field name made lowercase.
    mva_rr = models.FloatField(db_column='MVA_RR', blank=True, null=True)  # Field name made lowercase.
    mva_rs = models.FloatField(db_column='MVA_RS', blank=True, null=True)  # Field name made lowercase.
    mva_sc = models.FloatField(db_column='MVA_SC', blank=True, null=True)  # Field name made lowercase.
    mva_se = models.FloatField(db_column='MVA_SE', blank=True, null=True)  # Field name made lowercase.
    mva_sp = models.FloatField(db_column='MVA_SP', blank=True, null=True)  # Field name made lowercase.
    mva_to = models.FloatField(db_column='MVA_TO', blank=True, null=True)  # Field name made lowercase.
    cest = models.CharField(db_column='CEST', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    arred = models.IntegerField(db_column='ARRED', blank=True, null=True)  # Field name made lowercase.
    ibpt_fed = models.FloatField(db_column='IBPT_FED', blank=True, null=True)  # Field name made lowercase.
    ibpt_mun = models.FloatField(db_column='IBPT_MUN', blank=True, null=True)  # Field name made lowercase.
    secao = models.IntegerField(db_column='SECAO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TIPO_PRODUTO'


class Tpop(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=1, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=30, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fora = models.CharField(db_column='FORA', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    exterior = models.CharField(db_column='EXTERIOR', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    es = models.CharField(db_column='ES', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isentopf = models.CharField(db_column='ISENTOPF', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stestado = models.CharField(db_column='STESTADO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    stfora = models.CharField(db_column='STFORA', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TPOP'


class Transp(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=5, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    endereco = models.CharField(db_column='ENDERECO', max_length=70, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='BAIRRO', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='CIDADE', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='ESTADO', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=9, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    telcom = models.CharField(db_column='TELCOM', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=15, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ramal = models.CharField(db_column='RAMAL', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cgc = models.CharField(db_column='CGC', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    inscr = models.CharField(db_column='INSCR', max_length=18, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    contato = models.CharField(db_column='CONTATO', max_length=25, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='OBS', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TRANSP'


class Us(models.Model):
    nome = models.CharField(db_column='NOME', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=255, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    vendas = models.BooleanField(db_column='VENDAS', blank=True, null=True)  # Field name made lowercase.
    pesq = models.BooleanField(db_column='PESQ', blank=True, null=True)  # Field name made lowercase.
    vcli = models.BooleanField(db_column='VCLI', blank=True, null=True)  # Field name made lowercase.
    exame = models.BooleanField(db_column='EXAME', blank=True, null=True)  # Field name made lowercase.
    dvenda = models.BooleanField(db_column='DVENDA', blank=True, null=True)  # Field name made lowercase.
    dexame = models.BooleanField(db_column='DEXAME', blank=True, null=True)  # Field name made lowercase.
    reserva = models.BooleanField(db_column='RESERVA', blank=True, null=True)  # Field name made lowercase.
    orc = models.BooleanField(db_column='ORC', blank=True, null=True)  # Field name made lowercase.
    vdef = models.BooleanField(db_column='VDEF', blank=True, null=True)  # Field name made lowercase.
    remef = models.BooleanField(db_column='REMEF', blank=True, null=True)  # Field name made lowercase.
    compras = models.BooleanField(db_column='COMPRAS', blank=True, null=True)  # Field name made lowercase.
    compra = models.BooleanField(db_column='COMPRA', blank=True, null=True)  # Field name made lowercase.
    csg = models.BooleanField(db_column='CSG', blank=True, null=True)  # Field name made lowercase.
    ccsg = models.BooleanField(db_column='CCSG', blank=True, null=True)  # Field name made lowercase.
    cautor = models.BooleanField(db_column='CAUTOR', blank=True, null=True)  # Field name made lowercase.
    dcsg = models.BooleanField(db_column='DCSG', blank=True, null=True)  # Field name made lowercase.
    dcompra = models.BooleanField(db_column='DCOMPRA', blank=True, null=True)  # Field name made lowercase.
    pedff = models.BooleanField(db_column='PEDFF', blank=True, null=True)  # Field name made lowercase.
    etiq = models.BooleanField(db_column='ETIQ', blank=True, null=True)  # Field name made lowercase.
    admfin = models.BooleanField(db_column='ADMFIN', blank=True, null=True)  # Field name made lowercase.
    fin = models.BooleanField(db_column='FIN', blank=True, null=True)  # Field name made lowercase.
    dolar = models.BooleanField(db_column='DOLAR', blank=True, null=True)  # Field name made lowercase.
    altvenda = models.BooleanField(db_column='ALTVENDA', blank=True, null=True)  # Field name made lowercase.
    ajest = models.BooleanField(db_column='AJEST', blank=True, null=True)  # Field name made lowercase.
    cancnf = models.BooleanField(db_column='CANCNF', blank=True, null=True)  # Field name made lowercase.
    congr = models.BooleanField(db_column='CONGR', blank=True, null=True)  # Field name made lowercase.
    oes = models.BooleanField(db_column='OES', blank=True, null=True)  # Field name made lowercase.
    ecf = models.BooleanField(db_column='ECF', blank=True, null=True)  # Field name made lowercase.
    transfil = models.BooleanField(db_column='TRANSFIL', blank=True, null=True)  # Field name made lowercase.
    cadastros = models.BooleanField(db_column='CADASTROS', blank=True, null=True)  # Field name made lowercase.
    cadliv = models.BooleanField(db_column='CADLIV', blank=True, null=True)  # Field name made lowercase.
    cadcli = models.BooleanField(db_column='CADCLI', blank=True, null=True)  # Field name made lowercase.
    cadforn = models.BooleanField(db_column='CADFORN', blank=True, null=True)  # Field name made lowercase.
    status = models.BooleanField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    espec = models.BooleanField(db_column='ESPEC', blank=True, null=True)  # Field name made lowercase.
    categ = models.BooleanField(db_column='CATEG', blank=True, null=True)  # Field name made lowercase.
    fpgto = models.BooleanField(db_column='FPGTO', blank=True, null=True)  # Field name made lowercase.
    transp = models.BooleanField(db_column='TRANSP', blank=True, null=True)  # Field name made lowercase.
    icms = models.BooleanField(db_column='ICMS', blank=True, null=True)  # Field name made lowercase.
    vendedores = models.BooleanField(db_column='VENDEDORES', blank=True, null=True)  # Field name made lowercase.
    bancos = models.BooleanField(db_column='BANCOS', blank=True, null=True)  # Field name made lowercase.
    cadp = models.BooleanField(db_column='CADP', blank=True, null=True)  # Field name made lowercase.
    consrel = models.BooleanField(db_column='CONSREL', blank=True, null=True)  # Field name made lowercase.
    fcx = models.BooleanField(db_column='FCX', blank=True, null=True)  # Field name made lowercase.
    resd = models.BooleanField(db_column='RESD', blank=True, null=True)  # Field name made lowercase.
    movd = models.BooleanField(db_column='MOVD', blank=True, null=True)  # Field name made lowercase.
    sangria = models.BooleanField(db_column='SANGRIA', blank=True, null=True)  # Field name made lowercase.
    cobr = models.BooleanField(db_column='COBR', blank=True, null=True)  # Field name made lowercase.
    crec = models.BooleanField(db_column='CREC', blank=True, null=True)  # Field name made lowercase.
    carta = models.BooleanField(db_column='CARTA', blank=True, null=True)  # Field name made lowercase.
    sdocli = models.BooleanField(db_column='SDOCLI', blank=True, null=True)  # Field name made lowercase.
    analise = models.BooleanField(db_column='ANALISE', blank=True, null=True)  # Field name made lowercase.
    avper = models.BooleanField(db_column='AVPER', blank=True, null=True)  # Field name made lowercase.
    avprod = models.BooleanField(db_column='AVPROD', blank=True, null=True)  # Field name made lowercase.
    avranking = models.BooleanField(db_column='AVRANKING', blank=True, null=True)  # Field name made lowercase.
    avcomiss = models.BooleanField(db_column='AVCOMISS', blank=True, null=True)  # Field name made lowercase.
    avres = models.BooleanField(db_column='AVRES', blank=True, null=True)  # Field name made lowercase.
    avfpg = models.BooleanField(db_column='AVFPG', blank=True, null=True)  # Field name made lowercase.
    estoque = models.BooleanField(db_column='ESTOQUE', blank=True, null=True)  # Field name made lowercase.
    estpos = models.BooleanField(db_column='ESTPOS', blank=True, null=True)  # Field name made lowercase.
    estdt = models.BooleanField(db_column='ESTDT', blank=True, null=True)  # Field name made lowercase.
    estneg = models.BooleanField(db_column='ESTNEG', blank=True, null=True)  # Field name made lowercase.
    estaj = models.BooleanField(db_column='ESTAJ', blank=True, null=True)  # Field name made lowercase.
    fichalv = models.BooleanField(db_column='FICHALV', blank=True, null=True)  # Field name made lowercase.
    fichacli = models.BooleanField(db_column='FICHACLI', blank=True, null=True)  # Field name made lowercase.
    lvexame = models.BooleanField(db_column='LVEXAME', blank=True, null=True)  # Field name made lowercase.
    lvres = models.BooleanField(db_column='LVRES', blank=True, null=True)  # Field name made lowercase.
    lvped = models.BooleanField(db_column='LVPED', blank=True, null=True)  # Field name made lowercase.
    lvcsg = models.BooleanField(db_column='LVCSG', blank=True, null=True)  # Field name made lowercase.
    listlv = models.BooleanField(db_column='LISTLV', blank=True, null=True)  # Field name made lowercase.
    listesp = models.BooleanField(db_column='LISTESP', blank=True, null=True)  # Field name made lowercase.
    listeditora = models.BooleanField(db_column='LISTEDITORA', blank=True, null=True)  # Field name made lowercase.
    cad = models.BooleanField(db_column='CAD', blank=True, null=True)  # Field name made lowercase.
    nf = models.BooleanField(db_column='NF', blank=True, null=True)  # Field name made lowercase.
    maladir = models.BooleanField(db_column='MALADIR', blank=True, null=True)  # Field name made lowercase.
    util = models.BooleanField(db_column='UTIL', blank=True, null=True)  # Field name made lowercase.
    usuario = models.BooleanField(db_column='USUARIO', blank=True, null=True)  # Field name made lowercase.
    nsenha = models.BooleanField(db_column='NSENHA', blank=True, null=True)  # Field name made lowercase.
    restsd = models.BooleanField(db_column='RESTSD', blank=True, null=True)  # Field name made lowercase.
    param = models.BooleanField(db_column='PARAM', blank=True, null=True)  # Field name made lowercase.
    confignf = models.BooleanField(db_column='CONFIGNF', blank=True, null=True)  # Field name made lowercase.
    impvlplus = models.BooleanField(db_column='IMPVLPLUS', blank=True, null=True)  # Field name made lowercase.
    impvlb = models.BooleanField(db_column='IMPVLB', blank=True, null=True)  # Field name made lowercase.
    impest = models.BooleanField(db_column='IMPEST', blank=True, null=True)  # Field name made lowercase.
    expdados = models.BooleanField(db_column='EXPDADOS', blank=True, null=True)  # Field name made lowercase.
    lib = models.BooleanField(db_column='LIB', blank=True, null=True)  # Field name made lowercase.
    sql_field = models.BooleanField(db_column='SQL_', blank=True, null=True)  # Field name made lowercase. Field renamed because it ended with '_'.
    bol = models.BooleanField(db_column='BOL', blank=True, null=True)  # Field name made lowercase.
    nfp = models.BooleanField(db_column='NFP', blank=True, null=True)  # Field name made lowercase.
    rvcli = models.BooleanField(db_column='RVCLI', blank=True, null=True)  # Field name made lowercase.
    lprest = models.BooleanField(db_column='LPREST', blank=True, null=True)  # Field name made lowercase.
    novos = models.BooleanField(db_column='NOVOS', blank=True, null=True)  # Field name made lowercase.
    setbol = models.BooleanField(db_column='SETBOL', blank=True, null=True)  # Field name made lowercase.
    expest = models.BooleanField(db_column='EXPEST', blank=True, null=True)  # Field name made lowercase.
    rcgrev = models.BooleanField(db_column='RCGREV', blank=True, null=True)  # Field name made lowercase.
    envcgr = models.BooleanField(db_column='ENVCGR', blank=True, null=True)  # Field name made lowercase.
    retcgr = models.BooleanField(db_column='RETCGR', blank=True, null=True)  # Field name made lowercase.
    impcgr = models.BooleanField(db_column='IMPCGR', blank=True, null=True)  # Field name made lowercase.
    impdcgr = models.BooleanField(db_column='IMPDCGR', blank=True, null=True)  # Field name made lowercase.
    expcgr = models.BooleanField(db_column='EXPCGR', blank=True, null=True)  # Field name made lowercase.
    vdcgr = models.BooleanField(db_column='VDCGR', blank=True, null=True)  # Field name made lowercase.
    audcgr = models.BooleanField(db_column='AUDCGR', blank=True, null=True)  # Field name made lowercase.
    nfpcgr = models.BooleanField(db_column='NFPCGR', blank=True, null=True)  # Field name made lowercase.
    lpcgr = models.BooleanField(db_column='LPCGR', blank=True, null=True)  # Field name made lowercase.
    lvcgr = models.BooleanField(db_column='LVCGR', blank=True, null=True)  # Field name made lowercase.
    movcgr = models.BooleanField(db_column='MOVCGR', blank=True, null=True)  # Field name made lowercase.
    etiqcgr = models.BooleanField(db_column='ETIQCGR', blank=True, null=True)  # Field name made lowercase.
    exped = models.BooleanField(db_column='EXPED', blank=True, null=True)  # Field name made lowercase.
    vdexa = models.BooleanField(db_column='VDEXA', blank=True, null=True)  # Field name made lowercase.
    dupl = models.BooleanField(db_column='DUPL', blank=True, null=True)  # Field name made lowercase.
    histlv = models.BooleanField(db_column='HISTLV', blank=True, null=True)  # Field name made lowercase.
    histcli = models.BooleanField(db_column='HISTCLI', blank=True, null=True)  # Field name made lowercase.
    invoice = models.BooleanField(db_column='INVOICE', blank=True, null=True)  # Field name made lowercase.
    movest = models.BooleanField(db_column='MOVEST', blank=True, null=True)  # Field name made lowercase.
    vendascli = models.BooleanField(db_column='VENDASCLI', blank=True, null=True)  # Field name made lowercase.
    histvd = models.BooleanField(db_column='HISTVD', blank=True, null=True)  # Field name made lowercase.
    avcgr = models.BooleanField(db_column='AVCGR', blank=True, null=True)  # Field name made lowercase.
    invent = models.BooleanField(db_column='INVENT', blank=True, null=True)  # Field name made lowercase.
    cpvd = models.BooleanField(db_column='CPVD', blank=True, null=True)  # Field name made lowercase.
    reldiv = models.BooleanField(db_column='RELDIV', blank=True, null=True)  # Field name made lowercase.
    expvdcg = models.BooleanField(db_column='EXPVDCG', blank=True, null=True)  # Field name made lowercase.
    consorc = models.BooleanField(db_column='CONSORC', blank=True, null=True)  # Field name made lowercase.
    assin = models.BooleanField(db_column='ASSIN', blank=True, null=True)  # Field name made lowercase.
    cadassin = models.BooleanField(db_column='CADASSIN', blank=True, null=True)  # Field name made lowercase.
    recassin = models.BooleanField(db_column='RECASSIN', blank=True, null=True)  # Field name made lowercase.
    envassin = models.BooleanField(db_column='ENVASSIN', blank=True, null=True)  # Field name made lowercase.
    expassin = models.BooleanField(db_column='EXPASSIN', blank=True, null=True)  # Field name made lowercase.
    exnrec = models.BooleanField(db_column='EXNREC', blank=True, null=True)  # Field name made lowercase.
    exnenv = models.BooleanField(db_column='EXNENV', blank=True, null=True)  # Field name made lowercase.
    renassin = models.BooleanField(db_column='RENASSIN', blank=True, null=True)  # Field name made lowercase.
    fichaclassin = models.BooleanField(db_column='FICHACLASSIN', blank=True, null=True)  # Field name made lowercase.
    fichaassin = models.BooleanField(db_column='FICHAASSIN', blank=True, null=True)  # Field name made lowercase.
    anassin = models.BooleanField(db_column='ANASSIN', blank=True, null=True)  # Field name made lowercase.
    zeracgr = models.BooleanField(db_column='ZERACGR', blank=True, null=True)  # Field name made lowercase.
    invcli = models.BooleanField(db_column='INVCLI', blank=True, null=True)  # Field name made lowercase.
    estmin = models.BooleanField(db_column='ESTMIN', blank=True, null=True)  # Field name made lowercase.
    estprom = models.BooleanField(db_column='ESTPROM', blank=True, null=True)  # Field name made lowercase.
    cadfil = models.BooleanField(db_column='CADFIL', blank=True, null=True)  # Field name made lowercase.
    clifat = models.BooleanField(db_column='CLIFAT', blank=True, null=True)  # Field name made lowercase.
    tipo_cliente = models.BooleanField(db_column='TIPO_CLIENTE', blank=True, null=True)  # Field name made lowercase.
    tipo_produto = models.BooleanField(db_column='TIPO_PRODUTO', blank=True, null=True)  # Field name made lowercase.
    impaut = models.BooleanField(db_column='IMPAUT', blank=True, null=True)  # Field name made lowercase.
    vendcred = models.BooleanField(db_column='VENDCRED', blank=True, null=True)  # Field name made lowercase.
    rembolcred = models.BooleanField(db_column='REMBOLCRED', blank=True, null=True)  # Field name made lowercase.
    retbolcred = models.BooleanField(db_column='RETBOLCRED', blank=True, null=True)  # Field name made lowercase.
    remcobcred = models.BooleanField(db_column='REMCOBCRED', blank=True, null=True)  # Field name made lowercase.
    retcobcred = models.BooleanField(db_column='RETCOBCRED', blank=True, null=True)  # Field name made lowercase.
    relcomisscred = models.BooleanField(db_column='RELCOMISSCRED', blank=True, null=True)  # Field name made lowercase.
    relesccred = models.BooleanField(db_column='RELESCCRED', blank=True, null=True)  # Field name made lowercase.
    crediario = models.BooleanField(db_column='CREDIARIO', blank=True, null=True)  # Field name made lowercase.
    expexcel = models.BooleanField(db_column='EXPEXCEL', blank=True, null=True)  # Field name made lowercase.
    balanco = models.BooleanField(db_column='BALANCO', blank=True, null=True)  # Field name made lowercase.
    relfisc = models.BooleanField(db_column='RELFISC', blank=True, null=True)  # Field name made lowercase.
    fichaff = models.BooleanField(db_column='FICHAFF', blank=True, null=True)  # Field name made lowercase.
    intsite = models.BooleanField(db_column='INTSITE', blank=True, null=True)  # Field name made lowercase.
    itpendfil = models.BooleanField(db_column='ITPENDFIL', blank=True, null=True)  # Field name made lowercase.
    cadpedfil = models.BooleanField(db_column='CADPEDFIL', blank=True, null=True)  # Field name made lowercase.
    transfe = models.BooleanField(db_column='TRANSFE', blank=True, null=True)  # Field name made lowercase.
    transfs = models.BooleanField(db_column='TRANSFS', blank=True, null=True)  # Field name made lowercase.
    impfil = models.BooleanField(db_column='IMPFIL', blank=True, null=True)  # Field name made lowercase.
    bxfil = models.BooleanField(db_column='BXFIL', blank=True, null=True)  # Field name made lowercase.
    pendfil = models.BooleanField(db_column='PENDFIL', blank=True, null=True)  # Field name made lowercase.
    estdisp = models.BooleanField(db_column='ESTDISP', blank=True, null=True)  # Field name made lowercase.
    agrupapg = models.BooleanField(db_column='AGRUPAPG', blank=True, null=True)  # Field name made lowercase.
    admin = models.BooleanField(db_column='ADMIN', blank=True, null=True)  # Field name made lowercase.
    loclv = models.BooleanField(db_column='LOCLV', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cadprod = models.BooleanField(db_column='CADPROD', blank=True, null=True)  # Field name made lowercase.
    perfil = models.BooleanField(db_column='PERFIL', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    servpop = models.CharField(db_column='SERVPOP', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    servsmtp = models.CharField(db_column='SERVSMTP', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    userid = models.CharField(db_column='USERID', max_length=50, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    senhaemail = models.CharField(db_column='SENHAEMAIL', max_length=80, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    trocanf = models.BooleanField(db_column='TROCANF', blank=True, null=True)  # Field name made lowercase.
    sincr = models.BooleanField(db_column='SINCR', blank=True, null=True)  # Field name made lowercase.
    editacli = models.BooleanField(db_column='EDITACLI', blank=True, null=True)  # Field name made lowercase.
    editafor = models.BooleanField(db_column='EDITAFOR', blank=True, null=True)  # Field name made lowercase.
    editafil = models.BooleanField(db_column='EDITAFIL', blank=True, null=True)  # Field name made lowercase.
    malacred = models.BooleanField(db_column='MALACRED', blank=True, null=True)  # Field name made lowercase.
    trocavd = models.BooleanField(db_column='TROCAVD', blank=True, null=True)  # Field name made lowercase.
    site = models.BooleanField(db_column='SITE', blank=True, null=True)  # Field name made lowercase.
    orcsite = models.BooleanField(db_column='ORCSITE', blank=True, null=True)  # Field name made lowercase.
    bxrecsite = models.BooleanField(db_column='BXRECSITE', blank=True, null=True)  # Field name made lowercase.
    atorcsite = models.BooleanField(db_column='ATORCSITE', blank=True, null=True)  # Field name made lowercase.
    pendsite = models.BooleanField(db_column='PENDSITE', blank=True, null=True)  # Field name made lowercase.
    avvend = models.BooleanField(db_column='AVVEND', blank=True, null=True)  # Field name made lowercase.
    relmargem = models.BooleanField(db_column='RELMARGEM', blank=True, null=True)  # Field name made lowercase.
    feriados = models.BooleanField(db_column='FERIADOS', blank=True, null=True)  # Field name made lowercase.
    estorno = models.BooleanField(db_column='ESTORNO', blank=True, null=True)  # Field name made lowercase.
    altsite = models.BooleanField(db_column='ALTSITE', blank=True, null=True)  # Field name made lowercase.
    clipvend = models.BooleanField(db_column='CLIPVEND', blank=True, null=True)  # Field name made lowercase.
    bkp = models.BooleanField(db_column='BKP', blank=True, null=True)  # Field name made lowercase.
    trocafpg = models.BooleanField(db_column='TROCAFPG', blank=True, null=True)  # Field name made lowercase.
    ranked = models.BooleanField(db_column='RANKED', blank=True, null=True)  # Field name made lowercase.
    analisecp = models.BooleanField(db_column='ANALISECP', blank=True, null=True)  # Field name made lowercase.
    listaed = models.BooleanField(db_column='LISTAED', blank=True, null=True)  # Field name made lowercase.
    difped = models.BooleanField(db_column='DIFPED', blank=True, null=True)  # Field name made lowercase.
    ssl = models.BooleanField(db_column='SSL', blank=True, null=True)  # Field name made lowercase.
    rotcx = models.BooleanField(db_column='ROTCX', blank=True, null=True)  # Field name made lowercase.
    vlcash = models.BooleanField(db_column='VLCASH', blank=True, null=True)  # Field name made lowercase.
    nfe = models.BooleanField(db_column='NFE', blank=True, null=True)  # Field name made lowercase.
    trocaprod = models.BooleanField(db_column='TROCAPROD', blank=True, null=True)  # Field name made lowercase.
    vendaspais = models.BooleanField(db_column='VENDASPAIS', blank=True, null=True)  # Field name made lowercase.
    portasmtp = models.IntegerField(db_column='PORTASMTP', blank=True, null=True)  # Field name made lowercase.
    travafiscal = models.BooleanField(db_column='TRAVAFISCAL', blank=True, null=True)  # Field name made lowercase.
    envestoque = models.BooleanField(db_column='ENVESTOQUE', blank=True, null=True)  # Field name made lowercase.
    reneg = models.BooleanField(db_column='RENEG', blank=True, null=True)  # Field name made lowercase.
    vdsecao = models.BooleanField(db_column='VDSECAO', blank=True, null=True)  # Field name made lowercase.
    evirtual = models.BooleanField(db_column='EVIRTUAL', blank=True, null=True)  # Field name made lowercase.
    atualizaprorc = models.BooleanField(db_column='ATUALIZAPRORC', blank=True, null=True)  # Field name made lowercase.
    depfechado = models.BooleanField(db_column='DEPFECHADO', blank=True, null=True)  # Field name made lowercase.
    retsimbcsg = models.BooleanField(db_column='RETSIMBCSG', blank=True, null=True)  # Field name made lowercase.
    lista = models.BooleanField(db_column='LISTA', blank=True, null=True)  # Field name made lowercase.
    cadsecao = models.BooleanField(db_column='CADSECAO', blank=True, null=True)  # Field name made lowercase.
    cupomcgr = models.BooleanField(db_column='CUPOMCGR', blank=True, null=True)  # Field name made lowercase.
    serie = models.BooleanField(db_column='SERIE', blank=True, null=True)  # Field name made lowercase.
    auditoria = models.BooleanField(db_column='AUDITORIA', blank=True, null=True)  # Field name made lowercase.
    dirautorais = models.BooleanField(db_column='DIRAUTORAIS', blank=True, null=True)  # Field name made lowercase.
    vdescola = models.BooleanField(db_column='VDESCOLA', blank=True, null=True)  # Field name made lowercase.
    param_maquina = models.BooleanField(db_column='PARAM_MAQUINA', blank=True, null=True)  # Field name made lowercase.
    acesso_multifilial = models.BooleanField(db_column='ACESSO_MULTIFILIAL', blank=True, null=True)  # Field name made lowercase.
    contas = models.BooleanField(db_column='CONTAS', blank=True, null=True)  # Field name made lowercase.
    doacaocred = models.BooleanField(db_column='DOACAOCRED', blank=True, null=True)  # Field name made lowercase.
    vd_dev = models.BooleanField(db_column='VD_DEV', blank=True, null=True)  # Field name made lowercase.
    cgr_cx = models.BooleanField(db_column='CGR_CX', blank=True, null=True)  # Field name made lowercase.
    rel_rk = models.BooleanField(db_column='REL_RK', blank=True, null=True)  # Field name made lowercase.
    rel_hist = models.BooleanField(db_column='REL_HIST', blank=True, null=True)  # Field name made lowercase.
    rel_comiss = models.BooleanField(db_column='REL_COMISS', blank=True, null=True)  # Field name made lowercase.
    fil_pend = models.BooleanField(db_column='FIL_PEND', blank=True, null=True)  # Field name made lowercase.
    nome_email = models.CharField(db_column='NOME_EMAIL', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cargo_email = models.CharField(db_column='CARGO_EMAIL', max_length=60, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tel_email = models.CharField(db_column='TEL_EMAIL', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    finsite = models.BooleanField(db_column='FINSITE', blank=True, null=True)  # Field name made lowercase.
    lv_ativo = models.BooleanField(db_column='LV_ATIVO', blank=True, null=True)  # Field name made lowercase.
    atualizar = models.CharField(db_column='ATUALIZAR', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cobranca = models.BooleanField(db_column='COBRANCA', blank=True, null=True)  # Field name made lowercase.
    cred_receb = models.BooleanField(db_column='CRED_RECEB', blank=True, null=True)  # Field name made lowercase.
    inadimp = models.BooleanField(db_column='INADIMP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'US'


class Usctr(models.Model):
    nome = models.CharField(db_column='NOME', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fim = models.BooleanField(db_column='FIM', blank=True, null=True)  # Field name made lowercase.
    site = models.BooleanField(db_column='SITE', blank=True, null=True)  # Field name made lowercase.
    atend = models.BooleanField(db_column='ATEND', blank=True, null=True)  # Field name made lowercase.
    diario = models.BooleanField(db_column='DIARIO', blank=True, null=True)  # Field name made lowercase.
    analise = models.BooleanField(db_column='ANALISE', blank=True, null=True)  # Field name made lowercase.
    orc = models.BooleanField(db_column='ORC', blank=True, null=True)  # Field name made lowercase.
    planilha = models.BooleanField(db_column='PLANILHA', blank=True, null=True)  # Field name made lowercase.
    bxorc = models.BooleanField(db_column='BXORC', blank=True, null=True)  # Field name made lowercase.
    orcvend = models.BooleanField(db_column='ORCVEND', blank=True, null=True)  # Field name made lowercase.
    rankvend = models.BooleanField(db_column='RANKVEND', blank=True, null=True)  # Field name made lowercase.
    rankcli = models.BooleanField(db_column='RANKCLI', blank=True, null=True)  # Field name made lowercase.
    analdig = models.BooleanField(db_column='ANALDIG', blank=True, null=True)  # Field name made lowercase.
    margem = models.BooleanField(db_column='MARGEM', blank=True, null=True)  # Field name made lowercase.
    aud = models.BooleanField(db_column='AUD', blank=True, null=True)  # Field name made lowercase.
    loglivros = models.BooleanField(db_column='LOGLIVROS', blank=True, null=True)  # Field name made lowercase.
    logorc = models.BooleanField(db_column='LOGORC', blank=True, null=True)  # Field name made lowercase.
    loged = models.BooleanField(db_column='LOGED', blank=True, null=True)  # Field name made lowercase.
    logped = models.BooleanField(db_column='LOGPED', blank=True, null=True)  # Field name made lowercase.
    logfin = models.BooleanField(db_column='LOGFIN', blank=True, null=True)  # Field name made lowercase.
    util = models.BooleanField(db_column='UTIL', blank=True, null=True)  # Field name made lowercase.
    usuario = models.BooleanField(db_column='USUARIO', blank=True, null=True)  # Field name made lowercase.
    nsenha = models.BooleanField(db_column='NSENHA', blank=True, null=True)  # Field name made lowercase.
    rotsql = models.BooleanField(db_column='ROTSQL', blank=True, null=True)  # Field name made lowercase.
    sobre = models.BooleanField(db_column='SOBRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USCTR'


class Usfin(models.Model):
    nome = models.CharField(db_column='NOME', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    fim = models.BooleanField(db_column='FIM', blank=True, null=True)  # Field name made lowercase.
    mov = models.BooleanField(db_column='MOV', blank=True, null=True)  # Field name made lowercase.
    pgrec = models.BooleanField(db_column='PGREC', blank=True, null=True)  # Field name made lowercase.
    cheques = models.BooleanField(db_column='CHEQUES', blank=True, null=True)  # Field name made lowercase.
    bxmanual = models.BooleanField(db_column='BXMANUAL', blank=True, null=True)  # Field name made lowercase.
    realizados = models.BooleanField(db_column='REALIZADOS', blank=True, null=True)  # Field name made lowercase.
    concilia = models.BooleanField(db_column='CONCILIA', blank=True, null=True)  # Field name made lowercase.
    manreal = models.BooleanField(db_column='MANREAL', blank=True, null=True)  # Field name made lowercase.
    selemp = models.BooleanField(db_column='SELEMP', blank=True, null=True)  # Field name made lowercase.
    cad = models.BooleanField(db_column='CAD', blank=True, null=True)  # Field name made lowercase.
    cadcf = models.BooleanField(db_column='CADCF', blank=True, null=True)  # Field name made lowercase.
    proj = models.BooleanField(db_column='PROJ', blank=True, null=True)  # Field name made lowercase.
    ccusto = models.BooleanField(db_column='CCUSTO', blank=True, null=True)  # Field name made lowercase.
    conta = models.BooleanField(db_column='CONTA', blank=True, null=True)  # Field name made lowercase.
    bco = models.BooleanField(db_column='BCO', blank=True, null=True)  # Field name made lowercase.
    empresas = models.BooleanField(db_column='EMPRESAS', blank=True, null=True)  # Field name made lowercase.
    rel = models.BooleanField(db_column='REL', blank=True, null=True)  # Field name made lowercase.
    relpgrec = models.BooleanField(db_column='RELPGREC', blank=True, null=True)  # Field name made lowercase.
    relsaldo = models.BooleanField(db_column='RELSALDO', blank=True, null=True)  # Field name made lowercase.
    rellctos = models.BooleanField(db_column='RELLCTOS', blank=True, null=True)  # Field name made lowercase.
    reldfin = models.BooleanField(db_column='RELDFIN', blank=True, null=True)  # Field name made lowercase.
    rellvcx = models.BooleanField(db_column='RELLVCX', blank=True, null=True)  # Field name made lowercase.
    relextr = models.BooleanField(db_column='RELEXTR', blank=True, null=True)  # Field name made lowercase.
    relprevreal = models.BooleanField(db_column='RELPREVREAL', blank=True, null=True)  # Field name made lowercase.
    relcad = models.BooleanField(db_column='RELCAD', blank=True, null=True)  # Field name made lowercase.
    util = models.BooleanField(db_column='UTIL', blank=True, null=True)  # Field name made lowercase.
    usuario = models.BooleanField(db_column='USUARIO', blank=True, null=True)  # Field name made lowercase.
    nsenha = models.BooleanField(db_column='NSENHA', blank=True, null=True)  # Field name made lowercase.
    setch = models.BooleanField(db_column='SETCH', blank=True, null=True)  # Field name made lowercase.
    rsaldo = models.BooleanField(db_column='RSALDO', blank=True, null=True)  # Field name made lowercase.
    empr = models.BooleanField(db_column='EMPR', blank=True, null=True)  # Field name made lowercase.
    ctarec = models.BooleanField(db_column='CTAREC', blank=True, null=True)  # Field name made lowercase.
    bxcli = models.BooleanField(db_column='BXCLI', blank=True, null=True)  # Field name made lowercase.
    bxcart = models.BooleanField(db_column='BXCART', blank=True, null=True)  # Field name made lowercase.
    crec = models.BooleanField(db_column='CREC', blank=True, null=True)  # Field name made lowercase.
    rresproj = models.BooleanField(db_column='RRESPROJ', blank=True, null=True)  # Field name made lowercase.
    custch = models.BooleanField(db_column='CUSTCH', blank=True, null=True)  # Field name made lowercase.
    copiach = models.BooleanField(db_column='COPIACH', blank=True, null=True)  # Field name made lowercase.
    rotsql = models.BooleanField(db_column='ROTSQL', blank=True, null=True)  # Field name made lowercase.
    sdaconc = models.BooleanField(db_column='SDACONC', blank=True, null=True)  # Field name made lowercase.
    filiais = models.BooleanField(db_column='FILIAIS', blank=True, null=True)  # Field name made lowercase.
    agrupapg = models.BooleanField(db_column='AGRUPAPG', blank=True, null=True)  # Field name made lowercase.
    relctb = models.BooleanField(db_column='RELCTB', blank=True, null=True)  # Field name made lowercase.
    bxdir = models.BooleanField(db_column='BXDIR', blank=True, null=True)  # Field name made lowercase.
    trconta = models.BooleanField(db_column='TRCONTA', blank=True, null=True)  # Field name made lowercase.
    lcagr = models.BooleanField(db_column='LCAGR', blank=True, null=True)  # Field name made lowercase.
    bxbol = models.BooleanField(db_column='BXBOL', blank=True, null=True)  # Field name made lowercase.
    credff = models.BooleanField(db_column='CREDFF', blank=True, null=True)  # Field name made lowercase.
    atver = models.BooleanField(db_column='ATVER', blank=True, null=True)  # Field name made lowercase.
    bxmkt = models.BooleanField(db_column='BXMKT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USFIN'


class Usplace(models.Model):
    nome = models.CharField(db_column='NOME', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    senha = models.CharField(db_column='SENHA', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    mov = models.BooleanField(db_column='MOV', blank=True, null=True)  # Field name made lowercase.
    planilhas = models.BooleanField(db_column='PLANILHAS', blank=True, null=True)  # Field name made lowercase.
    sinc = models.BooleanField(db_column='SINC', blank=True, null=True)  # Field name made lowercase.
    cad = models.BooleanField(db_column='CAD', blank=True, null=True)  # Field name made lowercase.
    editoras = models.BooleanField(db_column='EDITORAS', blank=True, null=True)  # Field name made lowercase.
    cadlv = models.BooleanField(db_column='CADLV', blank=True, null=True)  # Field name made lowercase.
    impxls = models.BooleanField(db_column='IMPXLS', blank=True, null=True)  # Field name made lowercase.
    rel = models.BooleanField(db_column='REL', blank=True, null=True)  # Field name made lowercase.
    rel_ed = models.BooleanField(db_column='REL_ED', blank=True, null=True)  # Field name made lowercase.
    rel_lv = models.BooleanField(db_column='REL_LV', blank=True, null=True)  # Field name made lowercase.
    util = models.BooleanField(db_column='UTIL', blank=True, null=True)  # Field name made lowercase.
    usuario = models.BooleanField(db_column='USUARIO', blank=True, null=True)  # Field name made lowercase.
    rotsql = models.BooleanField(db_column='ROTSQL', blank=True, null=True)  # Field name made lowercase.
    lib = models.BooleanField(db_column='LIB', blank=True, null=True)  # Field name made lowercase.
    atver = models.BooleanField(db_column='ATVER', blank=True, null=True)  # Field name made lowercase.
    empr = models.BooleanField(db_column='EMPR', blank=True, null=True)  # Field name made lowercase.
    nsenha = models.BooleanField(db_column='NSENHA', blank=True, null=True)  # Field name made lowercase.
    configmp = models.BooleanField(db_column='CONFIGMP', blank=True, null=True)  # Field name made lowercase.
    impestff = models.BooleanField(db_column='IMPESTFF', blank=True, null=True)  # Field name made lowercase.
    etiquetas = models.BooleanField(db_column='ETIQUETAS', blank=True, null=True)  # Field name made lowercase.
    sincmkt = models.BooleanField(db_column='SINCMKT', blank=True, null=True)  # Field name made lowercase.
    atributos = models.BooleanField(db_column='ATRIBUTOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USPLACE'


class Vendedor(models.Model):
    codigo = models.CharField(db_column='CODIGO', primary_key=True, max_length=10, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=40, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    comissao = models.FloatField(db_column='COMISSAO', blank=True, null=True)  # Field name made lowercase.
    admissao = models.DateTimeField(db_column='ADMISSAO', blank=True, null=True)  # Field name made lowercase.
    cta_corrente = models.CharField(db_column='CTA_CORRENTE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    agencia = models.CharField(db_column='AGENCIA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    cod_cliente = models.CharField(db_column='COD_CLIENTE', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    tpcomissao = models.IntegerField(db_column='TPCOMISSAO', blank=True, null=True)  # Field name made lowercase.
    nr_maq = models.IntegerField(db_column='NR_MAQ', blank=True, null=True)  # Field name made lowercase.
    maquina = models.CharField(db_column='MAQUINA', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cod_mercos = models.IntegerField(db_column='COD_MERCOS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VENDEDOR'


class VerImpostos(models.Model):
    ver_ibpt = models.CharField(db_column='VER_IBPT', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtibpt = models.DateTimeField(db_column='DTIBPT', blank=True, null=True)  # Field name made lowercase.
    dtcest = models.DateTimeField(db_column='DTCEST', blank=True, null=True)  # Field name made lowercase.
    dticms = models.DateTimeField(db_column='DTICMS', blank=True, null=True)  # Field name made lowercase.
    dtfcp = models.DateTimeField(db_column='DTFCP', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VER_IMPOSTOS'


class Vlsat(models.Model):
    serie = models.IntegerField(db_column='SERIE')  # Field name made lowercase.
    equipamento = models.IntegerField(db_column='EQUIPAMENTO', primary_key=True)  # Field name made lowercase. The composite primary key (EQUIPAMENTO, SERIE) found, that is not supported. The first column is selected.
    fabricante = models.CharField(db_column='FABRICANTE', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    filial = models.CharField(db_column='FILIAL', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dll = models.CharField(db_column='DLL', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    codativacao = models.CharField(db_column='CODATIVACAO', max_length=32, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ambiente = models.IntegerField(db_column='AMBIENTE', blank=True, null=True)  # Field name made lowercase.
    layout = models.FloatField(db_column='LAYOUT', blank=True, null=True)  # Field name made lowercase.
    assinatura = models.TextField(db_column='ASSINATURA', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    modelo = models.IntegerField(db_column='MODELO', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'VLSAT'
        unique_together = (('equipamento', 'serie'),)


class Zfm(models.Model):
    codigo = models.IntegerField(db_column='CODIGO', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='NOME', max_length=25, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    uf = models.CharField(db_column='UF', max_length=2, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ZFM'


class Dtproperties(models.Model):
    objectid = models.IntegerField(blank=True, null=True)
    property = models.CharField(max_length=64, db_collation='Latin1_General_CI_AI')
    value = models.CharField(max_length=255, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    uvalue = models.CharField(max_length=255, db_collation='Latin1_General_CI_AI', blank=True, null=True)
    lvalue = models.BinaryField(blank=True, null=True)
    version = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dtproperties'
        unique_together = (('id', 'property'),)


class Livros(models.Model):
    nbook = models.CharField(db_column='NBOOK', primary_key=True, max_length=6, db_collation='Latin1_General_CI_AI')  # Field name made lowercase.
    publisher = models.CharField(db_column='PUBLISHER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    supplier = models.CharField(db_column='SUPPLIER', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    author = models.CharField(db_column='AUTHOR', max_length=20, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=75, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='EDITION', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    volume = models.CharField(db_column='VOLUME', max_length=6, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    binding = models.CharField(db_column='BINDING', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj1 = models.CharField(db_column='SUBJ1', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    statcd = models.CharField(db_column='STATCD', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    statdt = models.CharField(db_column='STATDT', max_length=8, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    list = models.FloatField(db_column='LIST', blank=True, null=True)  # Field name made lowercase.
    tpprod = models.CharField(db_column='TPPROD', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    di = models.CharField(db_column='DI', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    qtpag = models.IntegerField(db_column='QTPAG', blank=True, null=True)  # Field name made lowercase.
    nsuppl = models.CharField(db_column='NSUPPL', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    moeda = models.CharField(db_column='MOEDA', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    dtcad = models.DateTimeField(db_column='DTCAD', blank=True, null=True)  # Field name made lowercase.
    dtatual = models.DateTimeField(db_column='DTATUAL', blank=True, null=True)  # Field name made lowercase.
    dtlcto = models.DateTimeField(db_column='DTLCTO', blank=True, null=True)  # Field name made lowercase.
    autor = models.CharField(db_column='AUTOR', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj2 = models.CharField(db_column='SUBJ2', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    subj3 = models.CharField(db_column='SUBJ3', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    peso = models.FloatField(db_column='PESO', blank=True, null=True)  # Field name made lowercase.
    formato = models.CharField(db_column='FORMATO', max_length=10, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ano = models.CharField(db_column='ANO', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    colecao = models.CharField(db_column='COLECAO', max_length=100, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    isbn1 = models.CharField(db_column='ISBN1', max_length=13, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    sellpr = models.FloatField(db_column='SELLPR', blank=True, null=True)  # Field name made lowercase.
    disc = models.FloatField(db_column='DISC', blank=True, null=True)  # Field name made lowercase.
    flagpr = models.BooleanField(db_column='FLAGPR', blank=True, null=True)  # Field name made lowercase.
    prcusto = models.FloatField(db_column='PRCUSTO', blank=True, null=True)  # Field name made lowercase.
    marca = models.BooleanField(db_column='MARCA', blank=True, null=True)  # Field name made lowercase.
    cadlocal = models.CharField(db_column='CADLOCAL', max_length=1, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    cst = models.CharField(db_column='CST', max_length=3, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    desccli = models.FloatField(db_column='DESCCLI', blank=True, null=True)  # Field name made lowercase.
    unid = models.CharField(db_column='UNID', max_length=4, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    ativo = models.BooleanField(db_column='ATIVO', blank=True, null=True)  # Field name made lowercase.
    estmin = models.IntegerField(db_column='ESTMIN', blank=True, null=True)  # Field name made lowercase.
    flagdados = models.BooleanField(db_column='FLAGDADOS', blank=True, null=True)  # Field name made lowercase.
    descricao = models.CharField(db_column='DESCRICAO', max_length=140, db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase.
    mgatacado = models.FloatField(db_column='MGATACADO', blank=True, null=True)  # Field name made lowercase.
    mgvarejo = models.FloatField(db_column='MGVAREJO', blank=True, null=True)  # Field name made lowercase.
    conservacao = models.TextField(db_column='CONSERVACAO', db_collation='Latin1_General_CI_AI', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'livros'
