# Generated by Django 4.0.5 on 2023-03-07 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('KartaTama', '0002_alter_kartatama_nu_karta_tama'),
        ('custom', '0002_alter_tinan_options_alter_tinan_tinan'),
    ]

    operations = [
        migrations.CreateModel(
            name='kartaTama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nu_karta_sai', models.CharField(max_length=20, unique=True, verbose_name='Numeru Karta Sai')),
                ('subject_karta_sai', models.CharField(max_length=100, verbose_name='Subject Karta sai')),
                ('deskrisaun_karta_sai', models.TextField(verbose_name='Deskrisaun Karta sai')),
                ('data_karta_sai', models.DateTimeField(auto_now_add=True)),
                ('orijen_karta_sai', models.CharField(max_length=100, verbose_name='Orijen Karta sai')),
                ('entrega_husi', models.CharField(max_length=100, verbose_name='Karta Entrega Husi')),
                ('klasifikasaun', models.CharField(choices=[('Urgente', 'Urgente'), ('Normal', 'Normal'), ('Konfidensial', 'Konfidensial')], max_length=32, null=True)),
                ('naran_folder', models.CharField(max_length=50, null=True, verbose_name='Naran Folder')),
                ('naran_file', models.FileField(max_length=200, null=True, upload_to='', verbose_name='Naran File')),
                ('hashed', models.CharField(max_length=32, null=True)),
                ('kategoria_karta_sai', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Kategoria_Karta_Sai', to='KartaTama.kategoriakarta')),
                ('tinan_karta_sai', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Karta_Sai', to='custom.tinan')),
            ],
            options={
                'verbose_name_plural': 'Karta Sai',
            },
        ),
    ]
