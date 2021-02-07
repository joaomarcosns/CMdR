# Generated by Django 3.1.5 on 2021-02-06 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20210206_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='breed',
            field=models.CharField(choices=[('Whites', 'Whites'), ('Dun', 'Dun'), ('Black', 'Black'), ('Yellow', 'Yellow'), ('Native', 'Native')], max_length=30, verbose_name='Raça'),
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=999, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='about',
            name='ethnicity',
            field=models.CharField(choices=[('Whites', 'Whites'), ('Black', 'Black'), ('Native', 'Native'), ('Dun', 'Dun'), ('Mulatto', 'Mulatto'), ('Caboclos', 'Caboclos'), ('Cafuzos', 'Cafuzos')], max_length=30, verbose_name='Etnia'),
        ),
        migrations.AlterField(
            model_name='about',
            name='history',
            field=models.TextField(max_length=999, verbose_name='História'),
        ),
        migrations.AlterField(
            model_name='about',
            name='school_level',
            field=models.CharField(choices=[('Complete primary education', 'Complete primary education'), ('Incomplete elementary school', 'Incomplete elementary school'), ('Complete high school', 'Complete high school'), ('Incomplete high school', 'Incomplete high school'), ('Complete higher education', 'Complete higher education'), ('Incomplete higher education', 'Incomplete higher education'), ('Higher education more', 'Higher education more')], max_length=40, verbose_name='Níveis de escolaridade'),
        ),
        migrations.AlterField(
            model_name='about',
            name='sexual_orientation',
            field=models.CharField(max_length=30, verbose_name='Orientação sexual'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='homeless',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.homeless', verbose_name='Sem-teto'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='name_disease',
            field=models.CharField(max_length=90, verbose_name='Nome da doença'),
        ),
        migrations.AlterField(
            model_name='disease',
            name='type_disease',
            field=models.CharField(max_length=90, verbose_name='Tipo da doença'),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='city',
            field=models.CharField(max_length=35, verbose_name='Cidade'),
        ),
        migrations.AlterField(
            model_name='nationality',
            name='state',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins'), ('DF', 'Distrito Federal')], max_length=2, verbose_name='Estado'),
        ),
    ]