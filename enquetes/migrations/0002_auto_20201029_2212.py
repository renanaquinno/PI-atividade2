# Generated by Django 3.1.2 on 2020-10-30 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enquetes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=200)),
                ('dt_publicacao', models.DateField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postagens', to='enquetes.perfil')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('senha', models.CharField(max_length=255)),
                ('dt_nascimento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Reacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Gostar', 'gostar'), ('Amor', 'amor'), ('Engraçado', 'engracado'), ('Raiva', 'raiva')], default='gostar', max_length=10)),
                ('data', models.DateField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacoes', to='enquetes.perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reacoes', to='enquetes.postagem')),
            ],
        ),
        migrations.AddField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquetes.usuario'),
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(max_length=20)),
                ('dt_publicacao', models.DateField()),
                ('perfil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='enquetes.perfil')),
                ('postagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='enquetes.postagem')),
                ('respostas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enquetes.comentario')),
            ],
        ),
    ]
