# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'ListItem'
        db.create_table('tzac_listitem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
            ('list', self.gf('django.db.models.fields.related.ForeignKey')(related_name='items', to=orm['tzac.List'])),
        ))
        db.send_create_signal('tzac', ['ListItem'])

        # Adding model 'List'
        db.create_table('tzac_list', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=250)),
        ))
        db.send_create_signal('tzac', ['List'])


    def backwards(self, orm):
        
        # Deleting model 'ListItem'
        db.delete_table('tzac_listitem')

        # Deleting model 'List'
        db.delete_table('tzac_list')


    models = {
        'arm_sections.section': {
            'Meta': {'object_name': 'Section'},
            'full_slug': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'to': "orm['arm_sections.Section']", 'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'tzac.list': {
            'Meta': {'object_name': 'List'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'tzac.listitem': {
            'Meta': {'object_name': 'ListItem'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': "orm['tzac.List']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        },
        'tzac.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tzac_page_alternates'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['arm_sections.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250'})
        }
    }

    complete_apps = ['tzac']
