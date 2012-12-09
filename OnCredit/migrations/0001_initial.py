# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Recharge'
        db.create_table('OnCredit_recharge', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('network_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('amount_charged', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('pincode', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('used', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('OnCredit', ['Recharge'])

        # Adding model 'Prepaid'
        db.create_table('OnCredit_prepaid', (
            ('recharge_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['OnCredit.Recharge'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('OnCredit', ['Prepaid'])

        # Adding model 'Postpaid'
        db.create_table('OnCredit_postpaid', (
            ('recharge_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['OnCredit.Recharge'], unique=True, primary_key=True)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('OnCredit', ['Postpaid'])

        # Adding model 'Subscription'
        db.create_table('OnCredit_subscription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('subscriber_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('card_num', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('amount_charged', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('OnCredit', ['Subscription'])

        # Adding model 'UtilityBills'
        db.create_table('OnCredit_utilitybills', (
            ('subscription_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['OnCredit.Subscription'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('OnCredit', ['UtilityBills'])

        # Adding model 'TransportBills'
        db.create_table('OnCredit_transportbills', (
            ('subscription_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['OnCredit.Subscription'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('OnCredit', ['TransportBills'])

        # Adding model 'SubscriptionPlan'
        db.create_table('OnCredit_subscriptionplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('plan_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('plan_amount', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('OnCredit', ['SubscriptionPlan'])

        # Adding model 'CableTV'
        db.create_table('OnCredit_cabletv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('subscription_plan', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OnCredit.SubscriptionPlan'])),
        ))
        db.send_create_signal('OnCredit', ['CableTV'])

        # Adding model 'CableTVSubscription'
        db.create_table('OnCredit_cabletvsubscription', (
            ('subscription_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['OnCredit.Subscription'], unique=True, primary_key=True)),
            ('subscription', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OnCredit.CableTV'])),
        ))
        db.send_create_signal('OnCredit', ['CableTVSubscription'])

        # Adding model 'DataPlan'
        db.create_table('OnCredit_dataplan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('network', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('data_plan', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('duration', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('amount', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('OnCredit', ['DataPlan'])


    def backwards(self, orm):
        # Deleting model 'Recharge'
        db.delete_table('OnCredit_recharge')

        # Deleting model 'Prepaid'
        db.delete_table('OnCredit_prepaid')

        # Deleting model 'Postpaid'
        db.delete_table('OnCredit_postpaid')

        # Deleting model 'Subscription'
        db.delete_table('OnCredit_subscription')

        # Deleting model 'UtilityBills'
        db.delete_table('OnCredit_utilitybills')

        # Deleting model 'TransportBills'
        db.delete_table('OnCredit_transportbills')

        # Deleting model 'SubscriptionPlan'
        db.delete_table('OnCredit_subscriptionplan')

        # Deleting model 'CableTV'
        db.delete_table('OnCredit_cabletv')

        # Deleting model 'CableTVSubscription'
        db.delete_table('OnCredit_cabletvsubscription')

        # Deleting model 'DataPlan'
        db.delete_table('OnCredit_dataplan')


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
            'recharge_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['OnCredit.Recharge']", 'unique': 'True', 'primary_key': 'True'})
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