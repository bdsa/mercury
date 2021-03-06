# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'nexus_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.Group'])),
            ('startdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('enddate', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'nexus', ['Event'])

        # Adding model 'Booking'
        db.create_table(u'nexus_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('role', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['nexus.Role'], unique=True)),
            ('contact', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['nexus.Contact'], unique=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['nexus.Event'])),
        ))
        db.send_create_signal(u'nexus', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'nexus_event')

        # Deleting model 'Booking'
        db.delete_table(u'nexus_booking')


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
        u'nexus.booking': {
            'Meta': {'object_name': 'Booking'},
            'contact': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['nexus.Contact']", 'unique': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['nexus.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'role': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['nexus.Role']", 'unique': 'True'})
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
        u'nexus.event': {
            'Meta': {'object_name': 'Event'},
            'enddate': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            'startdate': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'nexus.role': {
            'Meta': {'unique_together': "(('role', 'owner'),)", 'object_name': 'Role'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.Group']"}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['nexus']