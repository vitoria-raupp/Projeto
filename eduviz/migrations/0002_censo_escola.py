# Generated by Django 5.0.4 on 2024-06-20 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduviz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='censo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_ano_censo', models.IntegerField(null=True)),
                ('in_energia_inexistente', models.BooleanField(null=True)),
                ('in_laboratorio_informatica', models.BooleanField(null=True)),
                ('in_computador', models.BooleanField(null=True)),
                ('qt_equip_lousa_digital', models.IntegerField(null=True)),
                ('in_equip_multimidia', models.BooleanField(null=True)),
                ('qt_equip_multimidia', models.IntegerField(null=True)),
                ('in_desktop_aluno', models.BooleanField(null=True)),
                ('qt_desktop_aluno', models.IntegerField(null=True)),
                ('in_comp_portatil_aluno', models.BooleanField(null=True)),
                ('qt_comp_portatil_aluno', models.IntegerField(null=True)),
                ('in_tablet_aluno', models.BooleanField(null=True)),
                ('qt_tablet_aluno', models.IntegerField(null=True)),
                ('in_internet', models.BooleanField(null=True)),
                ('in_internet_alunos', models.BooleanField(null=True)),
                ('in_internet_administrativo', models.BooleanField(null=True)),
                ('in_internet_aprendizagem', models.BooleanField(null=True)),
                ('in_acesso_internet_computador', models.BooleanField(null=True)),
                ('in_aces_internet_disp_pessoais', models.BooleanField(null=True)),
                ('tp_rede_local', models.IntegerField(null=True)),
                ('in_banda_larga', models.BooleanField(null=True)),
                ('co_entidade', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='escola',
            fields=[
                ('no_regiao', models.CharField(max_length=255, null=True)),
                ('no_uf', models.CharField(max_length=255, null=True)),
                ('sg_uf', models.CharField(max_length=2, null=True)),
                ('co_entidade', models.IntegerField(primary_key=True, serialize=False)),
                ('no_entidade', models.CharField(max_length=255, null=True)),
                ('tp_dependencia', models.IntegerField(null=True)),
                ('tp_categoria_escola_privada', models.IntegerField(null=True)),
                ('tp_localizacao', models.IntegerField(null=True)),
                ('tp_localizacao_diferenciada', models.IntegerField(null=True)),
            ],
        ),
    ]
