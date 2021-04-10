# Generated by Django 3.2 on 2021-04-09 09:38

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('stu_id', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='学号')),
                ('nickname', models.CharField(max_length=24, verbose_name='昵称')),
                ('description', models.TextField(blank=True, default='--', verbose_name='自我介绍')),
                ('avatar_key', models.CharField(default='avatar/default_customer', max_length=48, verbose_name='头像key')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='账号创建日期')),
                ('is_active', models.BooleanField(default=True, help_text='不选相当于删除用户', verbose_name='激活状态')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]