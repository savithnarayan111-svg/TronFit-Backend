from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_enquiry_branch'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='biometricemployeemapping',
            name='biometric_mapping_one_person',
        ),
        migrations.AddConstraint(
            model_name='biometricemployeemapping',
            constraint=models.CheckConstraint(
                condition=(
                    models.Q(member__isnull=True)
                    | models.Q(staff__isnull=True)
                ),
                name='biometric_mapping_one_person',
            ),
        ),
    ]