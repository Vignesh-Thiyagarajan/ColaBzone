from django.db import migrations


def AddUserType(apps, schema_editor):
    UserType = apps.get_model('ColabUsers', 'UserType')
    UserType.objects.bulk_create([
        UserType(user_type='SuperAdmin'),
        UserType(user_type='ColabUser')
    ])


def AddUser(apps, schema_editor):
    ColabUser = apps.get_model('ColabUsers', 'ColabUser')
    password_superadmin = "pbkdf2_sha256$390000$CGX31lpuoKQNlJu8lV9wSV$HLCU7/7lMbgmGetoby7NifW6x3sb2clqn+0fDEPiBg0="
    ColabUser.objects.bulk_create([
        ColabUser(email="superadmin@colabzone.com", password=password_superadmin, is_staff=1,
                  is_superuser=1, first_name="Super", last_name="Admin", user_type_id=1,
                  phone_number="1234567890")
    ])


class Migration(migrations.Migration):
    dependencies = [
        ('ColabUsers', '0001_S_initial'),
    ]

    operations = [
        migrations.RunPython(AddUserType),
        migrations.RunPython(AddUser),
    ]
