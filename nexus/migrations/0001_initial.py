# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'nexus_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('forename', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('surname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('telephone_mobile', self.gf('django.db.models.fields.CharField')(max_length=14)),
        ))
        db.send_create_signal(u'nexus', ['Contact'])

        # Adding model 'Role'
        db.create_table(u'nexus_role', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'nexus', ['Role'])

        # Adding M2M table for field contacts on 'Role'
        m2m_table_name = db.shorten_name(u'nexus_role_contacts')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('role', models.ForeignKey(orm[u'nexus.role'], null=False)),
            ('contact', models.ForeignKey(orm[u'nexus.contact'], null=False))
        ))
        db.create_unique(m2m_table_name, ['role_id', 'contact_id'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'nexus_contact')

        # Deleting model 'Role'
        db.delete_table(u'nexus_role')

        # Removing M2M table for field contacts on 'Role'
        db.delete_table(db.shorten_name(u'nexus_role_contacts'))


    models = {
        u'nexus.contact': {
            'Meta': {'object_name': 'Contact'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'forename': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'telephone_mobile': ('django.db.models.fields.CharField', [], {'max_length': '14'})
        },
        u'nexus.role': {
            'Meta': {'object_name': 'Role'},
            'contacts': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['nexus.Contact']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['nexus']