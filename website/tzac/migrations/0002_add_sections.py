# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field sections on 'Page'
        db.create_table('tzac_page_sections', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('page', models.ForeignKey(orm['tzac.page'], null=False)),
            ('section', models.ForeignKey(orm['arm_sections.section'], null=False))
        ))
        db.create_unique('tzac_page_sections', ['page_id', 'section_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field sections on 'Page'
        db.delete_table('tzac_page_sections')


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
        'tzac.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'tzac_page_alternates'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['arm_sections.Section']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['tzac']
