# Generated by Django 3.2.6 on 2021-09-15 13:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0122_alter_multiplecollaboratorsfield_notify_user_when_added"),
    ]

    operations = [
        migrations.RunSQL(
            (
                """
create or replace function try_encode_uri(text) returns text as $$
    select string_agg(
        case
            when bytes > 1 or c !~ '[0-9a-zA-Z_.!~*''();,/?:@&=+$#-]+' then
                regexp_replace(encode(convert_to(c, 'utf-8')::bytea, 'hex'), '(..)', E'%\\\\1', 'g')
            else
                c
        end,
        ''
    )
    from (
        select c, octet_length(c) bytes
        from regexp_split_to_table($1, '') c
    ) q;
$$ language sql immutable strict;

"""
            ),
            ("DROP FUNCTION IF EXISTS try_encode_uri(text);"),
        )
    ]
