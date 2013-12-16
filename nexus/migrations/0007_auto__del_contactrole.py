# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ContactRole'
        db.delete_table(u'nexus_contactrole')

        # Adding M2M table for field roles on 'Contact'
        m2m_table_name = db.shorten_name(u'nexus_contact_roles')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contact', models.ForeignKey(orm[u'nexus.contact'], null=False)),
            ('role', models.ForeignKey(orm[u'nexus.role'], null=False))
        ))
        db.create_unique(m2m_table_name, ['contact_id', 'role_id'])

        # Adding M2M table for field contacts on 'Role'
        m2m_table_name = db.shorten_name(u'nexus_role_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('role', models.ForeignKey(orm[u'nexus.role'], null=False)),
            ('contact', models.ForeignKey(orm[u'nexus.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['role_id', 'contact_id'])


    def backwards(self, orm):
        # Adding model 'ContactRole'
        db.create_table(u'nexus_contactrole', (
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nexus.Role'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contact', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nexus.Contact'])),
        ))
        db.send_create_signal(u'nexus', ['ContactRole'])

        # Removing M2M table for field roles on 'Contact'
        db.delete_table(db.shorten_name(u'nexus_contact_roles'))

        # Removing M2M table for field contacts on 'Role'
        db.delete_table(db.shorten_name(u'nexus_role_contacts'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'nexus.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            'roles': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nexus.Role']", 'symmetrical': 'False'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'nexus.role': {
            'Meta': {'object_name': 'Role'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nexus.Contact']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['nexus']