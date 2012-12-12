# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UniqueID'
        db.create_table('OnCredit_uniqueid', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unique_id', self.gf('django.db.models.fields.CharField')(default='08124450295', max_length=11)),
        ))
        db.send_create_signal('OnCredit', ['UniqueID'])

        # Adding model 'CreditUser'
        db.create_table('OnCredit_credituser', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accountName', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('email_addr', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone_number', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OnCredit.UniqueID'])),
            ('total_amount_borrowed', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=9, decimal_places=2)),
            ('present_Rating', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('OnCredit', ['CreditUser'])

        # Adding field 'Postpaid.phone_number'
        db.add_column('OnCredit_postpaid', 'phone_number',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='07035209976', to=orm['OnCredit.UniqueID']),
                      keep_default=False)

        # Adding field 'Postpaid.time'
        db.add_column('OnCredit_postpaid', 'time',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'UniqueID'
        db.delete_table('OnCredit_uniqueid')

        # Deleting model 'CreditUser'
        db.delete_table('OnCredit_credituser')

        # Deleting field 'Postpaid.phone_number'
        db.delete_column('OnCredit_postpaid', 'phone_number_id')

        # Deleting field 'Postpaid.time'
        db.delete_column('OnCredit_postpaid', 'time')


    models = {
        'OnCredit.cabletv': {
            'Meta': {'object_name': 'CableTV'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'subscription_plan': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OnCredit.SubscriptionPlan']"})
        },
        'OnCredit.cabletvsubscription': {
            'Meta': {'object_name': 'CableTVSubscription', '_ormbases': ['OnCredit.Subscription']},
            'subscription': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OnCredit.CableTV']"}),
            'subscription_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['OnCredit.Subscription']", 'unique': 'True', 'primary_key': 'True'})
        },
        'OnCredit.credituser': {
            'Meta': {'object_name': 'CreditUser'},
            'accountName': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'email_addr': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone_number': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OnCredit.UniqueID']"}),
            'present_Rating': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'total_amount_borrowed': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '9', 'decimal_places': '2'})
        },
        'OnCredit.dataplan': {
            'Meta': {'object_name': 'DataPlan'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'data_plan': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'OnCredit.postpaid': {
            'Meta': {'object_name': 'Postpaid', '_ormbases': ['OnCredit.Recharge']},
            'duration': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone_number': ('django.db.models.fields.related.ForeignKey', [], {'default': "'07035209976'", 'to': "orm['OnCredit.UniqueID']"}),
            'recharge_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['OnCredit.Recharge']", 'unique': 'True', 'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        },
        'OnCredit.prepaid': {
            'Meta': {'object_name': 'Prepaid', '_ormbases': ['OnCredit.Recharge']},
            'recharge_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['OnCredit.Recharge']", 'unique': 'True', 'primary_key': 'True'})
        },
        'OnCredit.recharge': {
            'Meta': {'object_name': 'Recharge'},
            'amount_charged': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'network_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'pincode': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'used': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'OnCredit.subscription': {
            'Meta': {'object_name': 'Subscription'},
            'amount_charged': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'card_num': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subscriber_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'OnCredit.subscriptionplan': {
            'Meta': {'object_name': 'SubscriptionPlan'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'plan_amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'plan_name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'OnCredit.transportbills': {
            'Meta': {'object_name': 'TransportBills', '_ormbases': ['OnCredit.Subscription']},
            'subscription_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['OnCredit.Subscription']", 'unique': 'True', 'primary_key': 'True'})
        },
        'OnCredit.uniqueid': {
            'Meta': {'object_name': 'UniqueID'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'unique_id': ('django.db.models.fields.CharField', [], {'default': "'08124450295'", 'max_length': '11'})
        },
        'OnCredit.utilitybills': {
            'Meta': {'object_name': 'UtilityBills', '_ormbases': ['OnCredit.Subscription']},
            'subscription_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['OnCredit.Subscription']", 'unique': 'True', 'primary_key': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['OnCredit']