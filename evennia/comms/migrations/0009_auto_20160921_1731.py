# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-21 17:31


from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("comms", "0008_auto_20160905_0902")]

    operations = [
        migrations.AlterField(
            model_name="msg",
            name="db_hide_from_channels",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="hide_from_channels_set",
                to="comms.ChannelDB",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_hide_from_objects",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="hide_from_objects_set",
                to="objects.ObjectDB",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_hide_from_accounts",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="hide_from_accounts_set",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_receivers_channels",
            field=models.ManyToManyField(
                blank=True,
                help_text="channel recievers",
                null=True,
                related_name="channel_set",
                to="comms.ChannelDB",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_receivers_objects",
            field=models.ManyToManyField(
                blank=True,
                help_text="object receivers",
                null=True,
                related_name="receiver_object_set",
                to="objects.ObjectDB",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_receivers_accounts",
            field=models.ManyToManyField(
                blank=True,
                help_text="account receivers",
                null=True,
                related_name="receiver_account_set",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_sender_external",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="identifier for external sender, for example a sender over an IRC connection (i.e. someone who doesn't have an exixtence in-game).",
                max_length=255,
                null=True,
                verbose_name="external sender",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_sender_objects",
            field=models.ManyToManyField(
                blank=True,
                db_index=True,
                null=True,
                related_name="sender_object_set",
                to="objects.ObjectDB",
                verbose_name="sender(object)",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_sender_accounts",
            field=models.ManyToManyField(
                blank=True,
                db_index=True,
                null=True,
                related_name="sender_account_set",
                to=settings.AUTH_USER_MODEL,
                verbose_name="sender(account)",
            ),
        ),
        migrations.AlterField(
            model_name="msg",
            name="db_tags",
            field=models.ManyToManyField(
                blank=True,
                help_text="tags on this message. Tags are simple string markers to identify, group and alias messages.",
                null=True,
                to="typeclasses.Tag",
            ),
        ),
    ]
