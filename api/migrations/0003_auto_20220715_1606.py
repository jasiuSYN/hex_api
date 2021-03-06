# Generated by Django 4.0.6 on 2022-07-15 16:06

from django.db import migrations


def basic_tiers(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Tier = apps.get_model("api", "Tier")
    db_alias = schema_editor.connection.alias
    Tier.objects.using(db_alias).bulk_create(
        [
            Tier(tier_name="Premium", original_link=True, thumbnail_sizes="200, 400"),
            Tier(
                tier_name="Enterprise",
                original_link=True,
                thumbnail_sizes="200, 400",
                expiring_link=True,
            ),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_auto_20220715_1557"),
    ]

    operations = [
        migrations.RunPython(basic_tiers),
    ]
