# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Type'
        db.create_table('tzac_contacts_type', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
        ))
        db.send_create_signal('tzac_contacts', ['Type'])

        # Adding model 'City'
        db.create_table('tzac_contacts_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
        ))
        db.send_create_signal('tzac_contacts', ['City'])

        # Adding model 'Contact'
        db.create_table('tzac_contacts_contact', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tzac_contacts.City'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['tzac_contacts.Type'])),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('tzac_contacts', ['Contact'])


    def backwards(self, orm):
        
        # Deleting model 'Type'
        db.delete_table('tzac_contacts_type')

        # Deleting model 'City'
        db.delete_table('tzac_contacts_city')

        # Deleting model 'Contact'
        db.delete_table('tzac_contacts_contact')


    models = {
        'tzac_contacts.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'tzac_contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tzac_contacts.City']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['tzac_contacts.Type']"})
        },
        'tzac_contacts.type': {
            'Meta': {'object_name': 'Type'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        }
    }

    complete_apps = ['tzac_contacts']
