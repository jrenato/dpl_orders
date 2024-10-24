# Generated by Django 5.0.9 on 2024-10-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliforn",
            fields=[
                (
                    "tipo",
                    models.CharField(
                        db_collation="Latin1_General_CI_AI",
                        db_column="TIPO",
                        max_length=1,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "codigo",
                    models.CharField(
                        db_collation="Latin1_General_CI_AI",
                        db_column="CODIGO",
                        max_length=8,
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="NOME",
                        max_length=70,
                        null=True,
                    ),
                ),
                (
                    "cgc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CGC",
                        max_length=18,
                        null=True,
                    ),
                ),
                (
                    "ativo",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ATIVO",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "fj",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="FJ",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "razsocial",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="RAZSOCIAL",
                        max_length=70,
                        null=True,
                    ),
                ),
                (
                    "endereco",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ENDERECO",
                        max_length=70,
                        null=True,
                    ),
                ),
                (
                    "bairro",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="BAIRRO",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "cidade",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CIDADE",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "estado",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ESTADO",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "cep",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CEP",
                        max_length=9,
                        null=True,
                    ),
                ),
                (
                    "telres",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TELRES",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "telcom",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TELCOM",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "tel2",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TEL2",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "fax",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="FAX",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "ramal",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="RAMAL",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "inscr",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="INSCR",
                        max_length=18,
                        null=True,
                    ),
                ),
                (
                    "contato",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CONTATO",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "email",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="EMAIL",
                        max_length=70,
                        null=True,
                    ),
                ),
                (
                    "subj1",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUBJ1",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "subj2",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUBJ2",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "celular",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CELULAR",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "endc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ENDC",
                        max_length=70,
                        null=True,
                    ),
                ),
                (
                    "bairroc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="BAIRROC",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "cidc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CIDC",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "cepc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CEPC",
                        max_length=9,
                        null=True,
                    ),
                ),
                (
                    "ufc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="UFC",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "telc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TELC",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "contatoc",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CONTATOC",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "transp",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TRANSP",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "fretecta",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="FRETECTA",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "vendedor",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="VENDEDOR",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "cargo",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CARGO",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "filiacao",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="FILIACAO",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "fpg",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="FPG",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "condpg",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CONDPG",
                        max_length=14,
                        null=True,
                    ),
                ),
                ("descn", models.FloatField(blank=True, db_column="DESCN", null=True)),
                ("desci", models.FloatField(blank=True, db_column="DESCI", null=True)),
                (
                    "desccli",
                    models.FloatField(blank=True, db_column="DESCCLI", null=True),
                ),
                (
                    "limite",
                    models.FloatField(blank=True, db_column="LIMITE", null=True),
                ),
                ("spc", models.BooleanField(blank=True, db_column="SPC", null=True)),
                (
                    "setbol",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SETBOL",
                        max_length=7,
                        null=True,
                    ),
                ),
                (
                    "tipo_cli",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TIPO_CLI",
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "cadlocal",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CADLOCAL",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="STATUS",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "dtcad",
                    models.DateTimeField(blank=True, db_column="DTCAD", null=True),
                ),
                (
                    "dtatual",
                    models.DateTimeField(blank=True, db_column="DTATUAL", null=True),
                ),
                (
                    "dtnasc",
                    models.DateTimeField(blank=True, db_column="DTNASC", null=True),
                ),
                (
                    "obs",
                    models.TextField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="OBS",
                        null=True,
                    ),
                ),
                (
                    "shortn",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SHORTN",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "distrib",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="DISTRIB",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "ddd",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="DDD",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "compradir",
                    models.BooleanField(blank=True, db_column="COMPRADIR", null=True),
                ),
                (
                    "fatmin",
                    models.FloatField(blank=True, db_column="FATMIN", null=True),
                ),
                ("pais", models.IntegerField(blank=True, db_column="PAIS", null=True)),
                (
                    "paisc",
                    models.IntegerField(blank=True, db_column="PAISC", null=True),
                ),
                (
                    "num",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="NUM",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "complemento",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="COMPLEMENTO",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "codmun",
                    models.IntegerField(blank=True, db_column="CODMUN", null=True),
                ),
                (
                    "emailnfe",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="EMAILNFE",
                        max_length=60,
                        null=True,
                    ),
                ),
                (
                    "im",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="IM",
                        max_length=14,
                        null=True,
                    ),
                ),
                (
                    "suframa",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUFRAMA",
                        max_length=9,
                        null=True,
                    ),
                ),
                ("ipi", models.BooleanField(blank=True, db_column="IPI", null=True)),
                (
                    "simples",
                    models.BooleanField(blank=True, db_column="SIMPLES", null=True),
                ),
                (
                    "instituicao",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="INSTITUICAO",
                        max_length=8,
                        null=True,
                    ),
                ),
                (
                    "sbscard",
                    models.IntegerField(blank=True, db_column="SBSCARD", null=True),
                ),
                (
                    "contribuinte",
                    models.BooleanField(
                        blank=True, db_column="CONTRIBUINTE", null=True
                    ),
                ),
                (
                    "estrangeiro",
                    models.BooleanField(blank=True, db_column="ESTRANGEIRO", null=True),
                ),
                (
                    "arred",
                    models.IntegerField(blank=True, db_column="ARRED", null=True),
                ),
                (
                    "emailbol",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="EMAILBOL",
                        max_length=60,
                        null=True,
                    ),
                ),
                (
                    "nome_ev",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="NOME_EV",
                        max_length=30,
                        null=True,
                    ),
                ),
                (
                    "tp_cobranca",
                    models.IntegerField(blank=True, db_column="TP_COBRANCA", null=True),
                ),
                (
                    "at_cobranca",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="AT_COBRANCA",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "cod_mercos",
                    models.IntegerField(blank=True, db_column="COD_MERCOS", null=True),
                ),
            ],
            options={
                "db_table": "CLIFORN",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Espec",
            fields=[
                (
                    "codigo",
                    models.CharField(
                        db_collation="Latin1_General_CI_AI",
                        db_column="CODIGO",
                        max_length=3,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "nome",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="NOME",
                        max_length=45,
                        null=True,
                    ),
                ),
                (
                    "estante",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ESTANTE",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "wpress",
                    models.IntegerField(blank=True, db_column="WPRESS", null=True),
                ),
                (
                    "catavento",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CATAVENTO",
                        max_length=50,
                        null=True,
                    ),
                ),
                ("li", models.IntegerField(blank=True, db_column="LI", null=True)),
            ],
            options={
                "db_table": "ESPEC",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Estoque",
            fields=[
                (
                    "nbook",
                    models.CharField(
                        db_collation="Latin1_General_CI_AI",
                        db_column="NBOOK",
                        max_length=6,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("disp", models.IntegerField(blank=True, db_column="DISP", null=True)),
                (
                    "reserva",
                    models.IntegerField(blank=True, db_column="RESERVA", null=True),
                ),
                (
                    "qtped",
                    models.IntegerField(blank=True, db_column="QTPED", null=True),
                ),
                (
                    "exame",
                    models.IntegerField(blank=True, db_column="EXAME", null=True),
                ),
                (
                    "consig",
                    models.IntegerField(blank=True, db_column="CONSIG", null=True),
                ),
                (
                    "dtatu",
                    models.DateTimeField(blank=True, db_column="DTATU", null=True),
                ),
                (
                    "di",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="DI",
                        max_length=1,
                        null=True,
                    ),
                ),
                ("dp", models.IntegerField(blank=True, db_column="DP", null=True)),
                ("ev", models.IntegerField(blank=True, db_column="EV", null=True)),
                (
                    "filial",
                    models.CharField(
                        db_collation="Latin1_General_CI_AI",
                        db_column="FILIAL",
                        max_length=3,
                    ),
                ),
                (
                    "locest",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="LOCEST",
                        max_length=40,
                        null=True,
                    ),
                ),
                (
                    "qtsep",
                    models.IntegerField(blank=True, db_column="QTSEP", null=True),
                ),
                (
                    "atualizar",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="Atualizar",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "cod_ff",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="COD_FF",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "disp_ff",
                    models.IntegerField(blank=True, db_column="DISP_FF", null=True),
                ),
                ("li", models.BooleanField(blank=True, db_column="LI", null=True)),
                (
                    "cad_ok",
                    models.BooleanField(blank=True, db_column="CAD_OK", null=True),
                ),
                (
                    "codprod_ff",
                    models.IntegerField(blank=True, db_column="CODPROD_FF", null=True),
                ),
            ],
            options={
                "db_table": "ESTOQUE",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Livros",
            fields=[
                (
                    "nbook",
                    models.CharField(
                        db_collation="Latin1_General_CI_AI",
                        db_column="NBOOK",
                        max_length=6,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "publisher",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="PUBLISHER",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "supplier",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUPPLIER",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "author",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="AUTHOR",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TITLE",
                        max_length=75,
                        null=True,
                    ),
                ),
                (
                    "edition",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="EDITION",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "volume",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="VOLUME",
                        max_length=6,
                        null=True,
                    ),
                ),
                (
                    "binding",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="BINDING",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "subj1",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUBJ1",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "statcd",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="STATCD",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "statdt",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="STATDT",
                        max_length=8,
                        null=True,
                    ),
                ),
                ("list", models.FloatField(blank=True, db_column="LIST", null=True)),
                (
                    "tpprod",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="TPPROD",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "di",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="DI",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "qtpag",
                    models.IntegerField(blank=True, db_column="QTPAG", null=True),
                ),
                (
                    "nsuppl",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="NSUPPL",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "moeda",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="MOEDA",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "dtcad",
                    models.DateTimeField(blank=True, db_column="DTCAD", null=True),
                ),
                (
                    "dtatual",
                    models.DateTimeField(blank=True, db_column="DTATUAL", null=True),
                ),
                (
                    "dtlcto",
                    models.DateTimeField(blank=True, db_column="DTLCTO", null=True),
                ),
                (
                    "autor",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="AUTOR",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "subj2",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUBJ2",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "subj3",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="SUBJ3",
                        max_length=3,
                        null=True,
                    ),
                ),
                ("peso", models.FloatField(blank=True, db_column="PESO", null=True)),
                (
                    "formato",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="FORMATO",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "ano",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ANO",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "colecao",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="COLECAO",
                        max_length=100,
                        null=True,
                    ),
                ),
                (
                    "isbn1",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="ISBN1",
                        max_length=13,
                        null=True,
                    ),
                ),
                (
                    "sellpr",
                    models.FloatField(blank=True, db_column="SELLPR", null=True),
                ),
                ("disc", models.FloatField(blank=True, db_column="DISC", null=True)),
                (
                    "flagpr",
                    models.BooleanField(blank=True, db_column="FLAGPR", null=True),
                ),
                (
                    "prcusto",
                    models.FloatField(blank=True, db_column="PRCUSTO", null=True),
                ),
                (
                    "marca",
                    models.BooleanField(blank=True, db_column="MARCA", null=True),
                ),
                (
                    "cadlocal",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CADLOCAL",
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "cst",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CST",
                        max_length=3,
                        null=True,
                    ),
                ),
                (
                    "desccli",
                    models.FloatField(blank=True, db_column="DESCCLI", null=True),
                ),
                (
                    "unid",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="UNID",
                        max_length=4,
                        null=True,
                    ),
                ),
                (
                    "ativo",
                    models.BooleanField(blank=True, db_column="ATIVO", null=True),
                ),
                (
                    "estmin",
                    models.IntegerField(blank=True, db_column="ESTMIN", null=True),
                ),
                (
                    "flagdados",
                    models.BooleanField(blank=True, db_column="FLAGDADOS", null=True),
                ),
                (
                    "descricao",
                    models.CharField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="DESCRICAO",
                        max_length=140,
                        null=True,
                    ),
                ),
                (
                    "mgatacado",
                    models.FloatField(blank=True, db_column="MGATACADO", null=True),
                ),
                (
                    "mgvarejo",
                    models.FloatField(blank=True, db_column="MGVAREJO", null=True),
                ),
                (
                    "conservacao",
                    models.TextField(
                        blank=True,
                        db_collation="Latin1_General_CI_AI",
                        db_column="CONSERVACAO",
                        null=True,
                    ),
                ),
            ],
            options={
                "db_table": "livros",
                "managed": False,
            },
        ),
    ]
