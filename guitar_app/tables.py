import django_tables2 as tables
from guitar_app import models
from django_tables2.utils import A

class GuitarTable(tables.Table):
    name = tables.LinkColumn('guitar_detail', args=[A('pk')])
    producer_name = tables.Column(verbose_name='Producer')
    body_material = tables.Column(verbose_name='Body')
    bridge_name = tables.Column(verbose_name='Bridge')
    pickup_set_type = tables.Column(verbose_name='Pickups')
    selection = tables.CheckBoxColumn(accessor='pk', attrs={"th__input": {"onclick": "toggle(this)"}}, orderable=False)
    class Meta:
        model = models.Guitars
        attrs = {"class": "paleblue"}
        fields = ('id', 'name', 'string_amount', 'price', 'neck_material', 'fretboard_material', 'pick_guard',
                  'type', 'producer_name', 'body_material', 'bridge_name', 'pickup_set_type', 'selection')
        sequence = ('id', 'name', 'string_amount', 'price', 'neck_material', 'fretboard_material', 'pick_guard',
                  'type', 'producer_name', 'body_material', 'bridge_name', 'pickup_set_type', 'selection')
        #exclude = ['id']

class StatisticsTable(tables.Table):
    #id = tables.Column()
    type = tables.Column()
    count = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}

class PriceTable(tables.Table):
    #id = tables.Column()
    producer = tables.Column()
    low_price = tables.Column()
    middle_price = tables.Column()
    high_price = tables.Column()
    class Meta:
        attrs = {"class": "paleblue"}
