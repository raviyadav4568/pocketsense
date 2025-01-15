from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Expense, Payment, Concern

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        ref_name = 'CustomUserSerializer'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'college', 'date_of_birth', 'phone_number']
        read_only_fields = ['user']

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['user'] = user
        return super().create(validated_data)

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'name', 'description', 'total_amount', 'split_details', 'pending_amount', 'paid_amount')
        read_only_fields = ['created_by', 'date_created']

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'expense', 'payer', 'amount', 'paid_on')
        read_only_fields = ['user', 'created_at']

    def validate(self, data):
        user = self.context['request'].user
        expense = data.get('expense')
        if not expense:
            raise serializers.ValidationError({"detail": "Expense must be provided."})

        if expense.created_by != user:
            raise serializers.ValidationError({"detail": "You cannot make a payment for an expense that you did not create."})

        return data

class ConcernSerializer(serializers.ModelSerializer):

    class Meta:
        model = Concern
        fields = ('id', 'expense', 'description')
        read_only_fields = ['user', 'date']
