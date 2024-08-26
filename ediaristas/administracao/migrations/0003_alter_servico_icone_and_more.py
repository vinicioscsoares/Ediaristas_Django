# Generated by Django 5.1 on 2024-08-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracao', '0002_alter_servico_icone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('twf-cleaning-3', 'twf-cleaning-3'), ('twf-cleaning-1', 'twf-cleaning-1'), ('twf-cleaning-2', 'twf-cleaning-2')], max_length=14),
        ),
        migrations.AlterField(
            model_name='servico',
            name='porcentagem_comissao',
            field=models.FloatField(),
        ),
    ]
