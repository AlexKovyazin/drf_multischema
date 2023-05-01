from rest_framework import serializers

from base_models.models import Article, Balance, Shop


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        fields = ['id', 'code', 'name', 'address', 'type']


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'code', 'name', 'price']


class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Balance
        fields = ['id', 'shop', 'article', 'quantity']
