# Generated by Django 3.1.4 on 2020-12-12 15:17

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nutrition', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254)),
                ('is_customer', models.BooleanField(default=False)),
                ('is_fitnesscenter', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('Weight Loss', 'Weightloss'), ('Weight Gain', 'WeightGain'), ('Body Building', 'BodyBuilding'), ('Regular', 'Regular'), ('Dance', 'Dance'), ('Yoga', 'Yoga'), ('Physiotherapy', 'Physiotherapy'), ('Massage Therapy', 'MassageTherapy')], default='Regular', max_length=50)),
                ('number_of_sessions', models.IntegerField()),
                ('hours_per_session', models.FloatField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='program_pics')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='FitnessCenter',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fitbuddy.user')),
                ('fitnesscenter_name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=10)),
                ('email', models.EmailField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=5000)),
                ('rating', models.FloatField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitbuddy.program')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HiringRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('Gym Trainer', 'GymTrainer'), ('Gym Instructor', 'GymInstructor'), ('Personal Trainer', 'PersonalTrainer'), ('Front desk staff', 'FrontDeskStaff'), ('Sales Manager', 'SalesManager'), ('Fitness Nutritionist', 'Nutritionist'), ('Other', 'Other')], default='Other', max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('salary', models.FloatField()),
                ('qualifications', models.TextField()),
                ('responsibilities', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Any', 'Any')], default='Any', max_length=30)),
                ('contact_email', models.EmailField(default='', max_length=254)),
                ('slug', models.SlugField(unique=True)),
                ('fprogram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitbuddy.program')),
            ],
        ),
        migrations.CreateModel(
            name='EnrolledPrograms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitbuddy.program')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='program',
            name='fcenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitbuddy.fitnesscenter'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='fitbuddy.user')),
                ('nutrition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nutrition.nutritionofcustomer')),
            ],
        ),
    ]